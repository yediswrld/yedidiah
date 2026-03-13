pip install -r ../requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Also create a file called `Procfile` (no extension) in the `yedidiah` folder with this:
```
web: cd backend && gunicorn config.wsgi:application
