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

