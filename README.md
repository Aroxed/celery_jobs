# Django Celery/Redis example

## Setup

Install: python, redis

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Aroxed/celery_jobs.git
$ cd celery_jobs
```

Modify settings.py:
CELERY_BROKER_URL='redis://192.168.0.102:6379', where 192.168.0.102 is the address of redis server

Create a virtual environment to install dependencies in and activate it:

```sh
$ sudo apt install python3-virtualenv
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ celery -A celery_jobs  worker --loglevel=INFO
```

In another terminal window
```sh
$ source env/bin/activate
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/run_task/`.