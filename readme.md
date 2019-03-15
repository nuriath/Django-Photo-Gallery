# PHOTOS GALLERY

This is a gallery application that have different categories of photos

## Prerequisites

To run locally, it is assumed that you have python installed on your system.

## Installing

 -Create a virtual environment. virtualenv venv
 -Activate venv. venv\scripts\activate.bat
 -Install the requirements. pip install -r requirements.txt
 -Set DEBUG = True in settings.py
 -Run the server. python manage.py runserver

## Deployment
 -When you deploy on heroku the dependencies you specify in your requirements.txt file are automatically installed before app startup.

 $ heroku create <app-name>
 $ git push heroku master
 $ heroku open

## Authors

 -Mwangaza Nuriath




