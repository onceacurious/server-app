web: python manage.py runserver && python manage.py makemigrations && python manage.py migrate && channels -b 0.0.0.0 -p &PORT core.asgi:application
worker: python manage.py runworker channels --settings=core.settings