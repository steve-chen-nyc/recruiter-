web: python bcrecruit/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT bcrecruit/settings.py
