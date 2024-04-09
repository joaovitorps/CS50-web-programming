# Project airline in Django

- To run the project: `docker compose -f ./infra/compose.yaml up -d`
- Open `http://localhost:8000/` to see the app running

### Apps inside this project

- flight

To add an app, run: `docker compose -f ./infra/compose.yaml run web ./manage.py test app_name`

To run tests: `docker compose -f -f ./infra/compose.yaml run web ./manage.py test app_name`
