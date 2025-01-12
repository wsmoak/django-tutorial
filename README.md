# Django Tutorial

This repo contains the 'polls' app with questions and choices from the tutorial in the official Django project documentation:

https://docs.djangoproject.com/en/5.0/intro/tutorial01/#

It assumes you have completed the setup described on previous pages in the docs.

### Notes

The directory structure differs slightly from the tutorial instructions.  There is a `config` directory instead of `mysite`.

Here is some info about how I prefer to structure projects: https://github.com/wsmoak/wiki/wiki/Starting-a-Django-project-with-uv

Be sure to activate the virtual environment, for example:

`source .venv/bin/activate`

The project is configured to use Postgres.  See config/settings.py for details.

Start the app with

`uv run python manage.py runserver`

There is an alternate settings file for the tests.  Run the the tests with

`DJANGO_SETTINGS_MODULE=config.test_settings python manage.py test`
