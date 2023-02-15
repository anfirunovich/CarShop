from django.db.models import Q, F

from celery import app

from showroom.models import Showroom

from supplier.models import SupplierSale, CarOfSupplier


@app.task
def showroom_buy_cars():
    for showroom in Showroom.objects.all():
        sample = showroom.sortquery

        find_suppliers_q = (
                Q(car__manufacturer__startswith=sample[0].get('manufacturer')) &
                Q(car__brand__startswith=sample[1].get('brand')) &
                Q(car__color__startswith=sample[2].get('color')) &
                Q(car__type__startswith=sample[3].get('type')) &
                Q(car__price__lte=sample[4].get('price'))
        )

        supplier_cars = SupplierSale.objects.filter(find_suppliers_q).order_by('-discount').first()
        showroom_cars = CarOfSupplier.objects.filter(find_suppliers_q).order_by('manufacturer')

        for supplier_car in supplier_cars:

            price = supplier_car.price

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



