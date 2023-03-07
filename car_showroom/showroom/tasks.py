from celery import app

from showroom.services import showroom_buy_cars


@app.task
def showroom_task():
    showroom_buy_cars.delay()
