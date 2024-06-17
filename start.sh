python3 manage.py migrate
python3 manage.py runserver

PORT=${PORT:-80}

gunicorn --bind :$PORT --workers 2 config.wsgi:application