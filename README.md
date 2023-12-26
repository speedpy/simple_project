# SpeedPy Simple Project

This is a simple project to start your Django based webapps.

## How to use

1. Clone this repository
1.1. Remove the `.git` directory
1.2. Initialize a new git repository 
2. Create a virtualenv
3. Install the requirements
4. Run the migrations
5. Run the `makesuperuser` command to create a superuser
6. Run the server

```bash
git clone git@github.com:speedpy/simple_project.git
cd simple_project
rm -rf .git
git init
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py makesuperuser
python manage.py runserver
```

### Tailwind

There is Tailwind configuration in the root of the project.

To install standalone Tailwind run one of the following commands depending on your platform:

```bash
wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.3.6/tailwindcss-macos-x64 -o tailwindcss
wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.3.6/tailwindcss-macos-arm64 -o tailwindcss
wget https://github.com/tailwindlabs/tailwindcss/releases/download/v3.3.6/tailwindcss-linux-x64 -o tailwindcss
```

See also: [Tailwind Standalone CLI 3.3.6 Release](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.3.6)

If you want to use 3rd party addons for Tailwind, then you need to install Node.js and npm. See [Tailwind Installation](https://tailwindcss.com/docs/installation).

To compile CSS run:

```bash
./tailwindcss -i mainapp/static/mainapp/input.css -o mainapp/static/mainapp/styles.css
```

## Project Structure

Project structure is based on the idea of Single App Django Project
Layout. [Watch the video](https://youtu.be/R7y1MkzOk7o?si=bzxWTvF7Wtyl2yW7) for the reasoning and detailed explanation.

Actually two apps are present: `mainapp` and `usermodel`. But the majority of changes you'll be making in the `mainapp`
app.

### mainapp

The main app is where you will be putting your code.

Instead of typical files, like `views.py` or `models.py`, you'll find directories with similar names. These are Python
packages. The reason for this is that it's easier to split your code into multiple files this way.

Since we have only one app, we don't really need to create a separate `urls.py` file, so the whole URL configuration is
in `project/urls.py`. If you choose to have it separate, you can create a `urls.py` file in the `mainapp` directory and
import it in the `project/urls.py`
file. [Including other URLconfs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#including-other-urlconfs)

### usermodel

This app holds the custom user model. It's a good idea to keep it separate from the main app, since it will be pretty
static and you won't be changing it often.

Custom User model has email as a login field.

The `email` field is case-insensitive. Also, the initial migration for this field is created with collation set to `db_collation=settings.CI_COLLATION` and `CI_COLLATION` is it `project/settings.py` depending on the database you are using.

## How to work on the project
Add your models in new files under `mainapp/models/` directory. Then add the model to `mainapp/models/__init__.py` file. This way you can split your models into multiple files.

Add your views in new files under `mainapp/views/` directory. Then add the view to `mainapp/views/__init__.py` file. 

Add your forms in new files under `mainapp/forms/` directory. Then add the form to `mainapp/forms/__init__.py` file. 

Templates for the app go into the root `templates` directory under `mainapp` subdirectory. For example, if you have a view `mainapp.views.home`, then the template should be at `templates/mainapp/home.html`.

The root template directory is great because you can override templates from other apps.


