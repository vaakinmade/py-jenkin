### 1 Install Python 2.7/3.5 and Django Framework > 1.10

Python 2.7.x/3.5.x https://www.python.org/downloads/

Django 1.11.x https://docs.djangoproject.com/en/1.11/intro/install/

### 2 Clone the repository

Via https

    git clone https://github.com/vaakinmade/infostore.git

or via ssh

    git clone git@github.com:vaakinmade/infostore.git

### 3 Install dependencies
At the project root there is a requirements file

    pip install -r requirements.txt

### 4 Syncdb
 
    python manage.py migrate

### 5 Run

    python manage.py runserver
