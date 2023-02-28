from datetime import datetime
from decimal import Decimal

from django.db.models import Q, F

from celery import app

from showroom.models import CarOfShowroom, ShowroomOffer, ShowroomPurchaseHistory

from supplier.models import SupplierSale, CarOfSupplier


@app.task
def showroom_buy_cars():
    for active_offer in ShowroomOffer.objects.filter(is_active=True).all():

        showroom_car_query = Q()

        if active_offer.requested_car_manufacturer:
            showroom_car_query &= Q(
                car__manufacturer__name__startswith=active_offer.requested_car_manufacturer,
            )

        if active_offer.requested_car_brand:
            showroom_car_query &= Q(car__brand__startswith=active_offer.requested_car_brand)

        if active_offer.requested_car_color:
            showroom_car_query &= Q(car__color__startswith=active_offer.requested_car_color)

        if active_offer.requested_car_type:
            showroom_car_query &= Q(car__type__startswith=active_offer.requested_car_type)

        supplier_cars = CarOfSupplier.objects.filter(showroom_car_query)

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

        min_price_with_discount = Decimal(float("inf"))
        min_price_supplier = None
        min_price_car = None

        for supplier_car in supplier_cars:

            supplier_car_discount = showroom_discounts_map.get(
                (supplier_car.showroom_id, supplier_car.car_id),
                Decimal(0.0),
            )

            price = (supplier_car.price - supplier_car_discount / 100)

            if price < min_price_with_discount:
                min_price_with_discount = price
                min_price_car = supplier_car.car
                min_price_supplier = supplier_car.supplier

            if price > active_offer.showroom.balance:
                continue

            active_offer.showroom.balance -= price

            ShowroomPurchaseHistory.objects.create(
                showroom=active_offer.showroom,
                offer=active_offer,
                car=min_price_car,
                supplier=min_price_supplier,
                total_price=min_price_with_discount,
            )

        active_offer.save()
        active_offer.showroom.save()



