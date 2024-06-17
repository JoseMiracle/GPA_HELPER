#!/bin/bash

# Run database migrations
python3 manage.py migrate

# Run collectstatic 
python manage.py collectstatic --noinput


# Set default port if not provided
PORT=${PORT:-80}

# Start the Gunicorn server
gunicorn --bind :$PORT --workers 2 config.wsgi:application
