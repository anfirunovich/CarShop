from django.db.models import Q, F

from celery import app

from customer.models import Customer, Offer

from showroom.models import CarOfShowroom, ShowroomSale


@app.task
def customer_buy_cars():
    for customer in Customer.objects.all():
        sample = customer.sortquery

        find_suppliers_q = (
                Q(car__manufacturer__startswith=sample[0].get('manufacturer')) &
                Q(car__brand__startswith=sample[1].get('brand')) &
                Q(car__color__startswith=sample[2].get('color')) &
                Q(car__type__startswith=sample[3].get('type')) &
                Q(car__price__lte=sample[4].get('price'))
        )

        showroom_discount = ShowroomSale.objects.filter(find_suppliers_q).order_by('-discount').first()
        showroom_cars = CarOfShowroom.objects.filter(find_suppliers_q).order_by('manufacturer')

        for showroom_car in showroom_cars:

            price = showroom_car.price

            if price > customer.balance:
                continue

            customer.balance -= price

            Offer(
                customer=customer,
                car=showroom_car.car,
                price=price,
                showroom=showroom_car.showroom,
            ).save()

        customer.save()