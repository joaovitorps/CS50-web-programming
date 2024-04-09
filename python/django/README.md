## Apps inside this project

- hello
- christmas
- newyear
- tasks

To add an app, run: `docker compose -f ./python/django/compose.yaml run web python manage.py startapp app_name`

To run tests: `docker compose -f ./python/django/compose.yaml run web ./manage.py test app_name`
