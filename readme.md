## Project setup
``` shell
pip install -r requirements.txt
```


## Run the web API (Web server)
``` shell
python manage.py runserver
```
Output
``` console
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 05, 2024 - 14:41:34
Django version 4.2.7, using settings 'articon_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Migrations
These two commands are mandatory at application startup for the first time <br>
This should prepare the migrations, and create database tables
``` shell
python manage.py makemigrations
python manage.py migrate
```

## Create admin account
Create (add) new superuser "Admin"
``` bash
python manage.py createsuperuser
```
You will be prompted to enter the following information: Username, Email, and a Password <br>
These credentials will be used later to access the django administration panel