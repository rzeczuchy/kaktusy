# Daruma
Daruma is a lightweight CMS and blogging app on Django.

## Starting app using Pipenv
To start the app you'll need [Pipenv](https://pypi.org/project/pipenv/).

To run the app, clone the repository. In the root folder (where `Pipfile` is located) install packages using Pipenv:
```
$ pipenv install
```

Activate the Pipenv shell:
```
$ pipenv shell
```

Once the Pipenv shell is activated, go from the root to the `daruma` folder, where the `manage.py` file is located.

From there you will need to run the migrations:
```
python manage.py migrate
```

Once the migrations are completed, start the app using:
```
python manage.py runserver
```

The development server should by default start at port 8000. You can specify a different port like so:
```
python manage.py runserver [port]
```

To access the admin area, create the superuser with:
```
python manage.py createsuperuser
```

## Notices
This app makes use of the Django framework for Python:\
https://github.com/django/django

For rich-text editing, the Django CKEditor integration has been used:\
https://github.com/django-ckeditor/django-ckeditor

For storing environment variables, python-dotenv has been used:\
https://github.com/theskumar/python-dotenv

Placeholder hero photo by verneho on Unsplash:\
https://unsplash.com/@verneho