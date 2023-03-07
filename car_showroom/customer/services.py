from datetime import datetime
from decimal import Decimal

from django.db.models import Q

from celery import app

from customer.models import Offer, PurchaseHistory

from showroom.models import CarOfShowroom, ShowroomSale


@app.task
def customer_buy_cars():
    for active_offer in Offer.objects.filter(is_active=True).all():

        customer_car_query = Q()

        if active_offer.requested_car_manufacturer:
            customer_car_query &= Q(
                car__manufacturer__name__startswith=active_offer.requested_car_manufacturer,
            )

        if active_offer.requested_car_brand:
            customer_car_query &= Q(car__brand__startswith=active_offer.requested_car_brand)

        if active_offer.requested_car_color:
            customer_car_query &= Q(car__color__startswith=active_offer.requested_car_color)

        if active_offer.requested_car_type:
            customer_car_query &= Q(car__type__startswith=active_offer.requested_car_type)

        showroom_cars = CarOfShowroom.objects.filter(customer_car_query)

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

        min_price_with_discount = Decimal(float("inf"))
        min_price_showroom = None
        min_price_car = None

        for showroom_car in showroom_cars:

            showroom_car_discount = showroom_discounts_map.get(
                (showroom_car.showroom_id, showroom_car.car_id),
                Decimal(0.0),

            )
            price = showroom_car.price - (showroom_car.price * (showroom_car_discount / 100))

            if price < min_price_with_discount:
                min_price_with_discount = price
                min_price_car = showroom_car.car
                min_price_showroom = showroom_car.showroom

        if (
                (min_price_with_discount > active_offer.customer.balance)
                and (min_price_with_discount > active_offer.max_price)
        ):
            return

        active_offer.customer.balance -= min_price_with_discount

        active_offer.is_active = True

        PurchaseHistory.objects.create(
            customer=active_offer.customer,
            offer=active_offer,
            car=min_price_car,
            showroom=min_price_showroom,
            total_price=min_price_with_discount,
        )

        active_offer.save()
        active_offer.customer.save()
