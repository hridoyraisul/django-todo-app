1. Set up virtual environment for specific project:
python3 -m venv venv

2. Activate virtual environment: (in linux)
source venv/bin/activate

3. INstall django:
pip install django

4. Environment Requiremtns file add:
pip freeze >requirements.txt 

5. Create django-admin project in same directory:
django-admin startproject todo .

6. Create an app inside django project:
python3 manage.py startapp todoapp

7. run server
python3 manage.py runserver

8. Make migration:
python3 manage.py makemigrations
python3 manage.py migrate

9. create super user for django admin:
python3 manage.py createsuperuser
