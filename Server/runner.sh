python manage.py runserver &
celery -A Server worker -l info &
celery -A Server beat -l info &
