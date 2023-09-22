from config.celery import app

from.services import send_activation_code

@app.task
def celery_send_activation_code(email, code):
    send_activation_code(email, code)