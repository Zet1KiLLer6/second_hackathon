from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Melorm API',
        f'Привет! Ссылка для активации аккаунта: \n\n http://localhost:8000/api/v1/account/activate/{code}',
        'py29.hakaton@gmail.com',
        [email]
    )

