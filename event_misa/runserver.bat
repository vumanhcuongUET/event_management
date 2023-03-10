@echo off
start \env\Scripts\activate.bat
cd event_misa
start python manage.py runserver