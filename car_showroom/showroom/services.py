from datetime import datetime
from decimal import Decimal

from django.db.models import Q, F

from celery import app

from showroom.models import Showroom, CarOfShowroom

from supplier.models import SupplierSale, CarOfSupplier


@app.task
def showroom_buy_cars():
    for showroom in Showroom.objects.all():
        car = showroom.query

        find_suppliers_q = (
                Q(car__manufacturer__startswith=car.get('manufacturer')) &
                Q(car__brand__startswith=car.get('brand')) &
                Q(car__color__startswith=car.get('color')) &
                Q(car__type__startswith=car.get('type')) &
                Q(car__price__lte=car.get('price'))
        )

        supplier_cars = CarOfSupplier.objects.filter(find_suppliers_q)
        showroom_cars = CarOfShowroom.objects.filter(showroom__name__iexact=showroom.name)

        supplier_discounts = SupplierSale.objects.filter(
            date_end__lte=datetime.utcnow(),
            car_id__in=[
                supplier_car.car_id
                for supplier_car in supplier_cars
            ],
            showroom_id__in=[
                supplier_car.supplier_id
                for supplier_car in supplier_cars
            ],
        ).order_by('-discount')

        showroom_discounts_map = {
            (
                supplier_discount.supplier_id,
                supplier_discount.car_id,
            ): supplier_discount.discount
            for supplier_discount in supplier_discounts
        }

        for supplier_car in supplier_cars:

            supplier_car_discount = showroom_discounts_map.get(
                (supplier_car.showroom_id, supplier_car.car_id),
                Decimal(0.0),
            )

            price = (supplier_car.price - supplier_car_discount / 100)

            if price > showroom.balance:
                continue

            showroom.balance -= price

            showroom_cars.update_or_create(
                car=supplier_car.car,
                showroom=showroom,
                supplier=supplier_car.supplier,
                defaults={
                    'count': F('count') + 1
                }
            )

        showroom.save()



