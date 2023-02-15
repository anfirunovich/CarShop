from celery import app

from customer.services import customer_buy_cars


@app.task
def customer_task():
    customer_buy_cars.delay()
