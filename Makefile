run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
user:
	python manage.py createsuperuser
