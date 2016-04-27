### Description

This project is so far just Django boilerplate code set up with `django-dotenv` for configuration, `django-compressor` for static asset compilation, MySQL as the database and Jinja2 as the primary template engine. Has `videos` and `sites` apps that don't really have much yet, but will eventually integrate with Microsoft Azure's Media Services and CDN.

### Setup

Create a virtual environment with Python 3 and `pip` and run `pip install -R requirements.txt` to install package dependencies. Next, prepare the development environment by filling in fields in provided `.env.example` file. Assign a randomly generated string of fifty characters to the `SECRET KEY` and the location of your MySQL configuration file to `MYSQL_CONFIG`. The MySQL configuration file should be in the format:

```
[client]
database = {database_name}
host = localhost
user = {username}
password = {password}
default-character-set = utf8
```

Keep `DEBUG = True` for development. Rename the `.env.example` file to `.env` for the app to read its configuration values. Run `python manage.py runserver`, which starts the web application at `http://localhost:8000`.

### Project Structure

The project is divided up by logical components into apps, and each app contains its own models, controllers, routing, templates, and static assets. The important parts of the project are shown below.

```
azurecasts/
    jinja2.py
    settings.py
    urls.py
build/
    CACHE/
        css/
        js/
common/
    jinja2/
    static/
    scss/
    js/
sites/
videos/
    jinja2/
    static/
        videos/
            scss/
            js/
    urls.py
    views.py
.env
manage.py
requirements.txt
```

`azurecasts/` contains global settings and project configuration in `settings.py`. Additional Jinja2 environment configuration, which is required for `django-compressor` to work, is done in `jinja2.py`. `azurecasts/urls.py` has project-wide root level routing.

`build/` is *not* part of the repository, but is created automatically by `django-compressor` when running the local development server or by running `python manage.py compress`. This directory contains the SCSS files compiled into CSS, and minified CSS/JS.

`common/` contains templates and stylesheets that don't really belong to a particular app, For example, the template and styles for the home page or navigation bar go into the `common/` assets.

`sites/` and `videos/` are mostly empty apps. Static file organization is done as the Django documentation recommends. Directories originally named `templates` are named `jinja2` in order for the Jinja2 template engine to find them. The `scss` and `js` directories containing the actual static assets are doubly nested within the app with `app_name/static/app_name/scss` so that each app's static assets are namespaced, which prevents accidentally overwriting other files that are named the same. This structure will be the same for every app.

`.env` file contains per-environment configuration and `requirements.txt` contains the necessary package dependencies.
