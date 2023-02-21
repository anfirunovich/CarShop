from datetime import datetime
from decimal import Decimal

from django.db.models import Q

from celery import app

from customer.models import Customer, Offer

from showroom.models import CarOfShowroom, ShowroomSale


@app.task
def customer_buy_cars():
    for customer in Customer.objects.all():

        find_suppliers_q = (
                Q(car__manufacturer__startswith=customer.get('manufacturer')) &
                Q(car__brand__startswith=customer.get('brand')) &
                Q(car__color__startswith=customer.get('color')) &
                Q(car__type__startswith=customer.get('type')) &
                Q(car__price__lte=customer.get('price'))
        )

        showroom_cars = CarOfShowroom.objects.filter(find_suppliers_q)

        showroom_discounts = ShowroomSale.objects.filter(
            date_end__lte=datetime.utcnow(),
            car_id__in=[
                showroom_car.car_id
                for showroom_car in showroom_cars
            ],
            showroom_id__in=[
                showroom_car.showroom_id
                for showroom_car in showroom_cars
            ],
        ).order_by('-discount')

        showroom_discounts_map = {
            (
                showroom_discount.showroom_id,
                showroom_discount.car_id,
            ): showroom_discount.discount
            for showroom_discount in showroom_discounts
        }

        car_prices_with_discount = []

        for showroom_car in showroom_cars:

            showroom_car_discount = showroom_discounts_map.get(
                (showroom_car.showroom_id, showroom_car.car_id),
                Decimal(0.0),
            )
            price = (showroom_car.price - showroom_car_discount)

            car_prices_with_discount.append(price)

        min_price_with_discount = min(car_prices_with_discount)

        if min_price_with_discount > customer.balance:
            continue

        customer.balance -= min_price_with_discount

        Offer.objects.create(
            customer=customer,
            car=showroom_car.car,
            price=showroom_car.price,
            showroom=showroom_car.showroom,
        )

        customer.save()