release: python manage.py makemigrations user --no-input
release: python manage.py migrate user --no-input
release: python manage.py makemigrations artist --no-input
release: python manage.py migrate artist --no-input
release: python manage.py makemigrations sharing --no-input
release: python manage.py migrate sharing --no-input
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn imgapiv1.wsgi
