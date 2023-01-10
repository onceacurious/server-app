web: python manage.py runserver && channels -b 0.0.0.0 -p &PORT core.asgi:application
worker: python manage.py runworker channels --settings=core.settings