from config.celery import app

from .services import send_order_confirmed

@app.task
def celery_send_order_confirmed(email, order_number):
    send_order_confirmed(email, order_number)
