# SpeedPy Simple Project

This is a simple project to start your Django based webapps.

## How to use

1. Clone this repository
2. Create a virtualenv
3. Install the requirements
4. Run the migrations
5. Run the `makesuperuser` command to create a superuser
6. Run the server

```bash
git clone
cd speedpy-simple-project
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

