# Neuromat's Podcast Website

This repository contains the source for Neuromat's podcast blog.


The steps recommended for deploying this project are:

``` bash
virtualenv --python=python3 podcast_env
cd podcast_env
source bin/activate
git clone https://github.com/neuromat/podcast
cd podcast
pip install -r requirements.txt

# SETUP YOUR WSGI AND LOCAL SETTINGS FILES

python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
