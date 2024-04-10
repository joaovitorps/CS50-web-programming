# Project airline in Django

All commandos should be run from `CS50-web-programming/python/django-airline-project`

- To create this project was run: `docker compose run web django-admin startproject airline .`

- To run the project: `docker compose up -d`
- Open `http://localhost:8000/` to see the app running

### Apps inside this project

- flight
- users

To add an app, run: `docker compose run web ./manage.py startapp app_name`

To run tests: `docker compose run web ./manage.py test app_name`

To run migrations: `docker compose run web ./manage.py migrate`

To create a migration run: `docker compose run web ./manage.py makemigrations`

To manipulate sqlite run: `docker compose run web python ./manage.py shell`

To create a superuser run: `docker compose run web python ./manage.py createsuperuser`
