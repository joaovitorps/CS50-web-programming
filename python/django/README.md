## Apps inside this project

To add an app, run: `docker compose -f ./python/django/compose.yaml run web python manage.py startapp app_name`

- hello
- christmas
  - run tests tests: `docker compose -f ./python/django/compose.yaml run web ./manage.py test christmas`
- newyear
