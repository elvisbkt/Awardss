# [Awwwards Application](https://Instaclone-application.herokuapp.com/)
#### Web clone of the awwwards.com
#### September 8th, 2019
#### By **[Elvis Biketi](https://github.com/elvisbkt)**

## Description
This is a simple web clone of the awwwards website where users can share their web projects
and review other users web projects.


## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6 or Python3.7
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/elvisbkt/awwwards.git && cd awwwards`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE awwwards;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'awwwards'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

```
### Run initial Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the app
```bash
python manage.py runserver
```
Open terminal on `localhost:8000`


## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Django
    - Heroku
    - Postgresql

## Support and contact details
Contact me on elvisbkt@gmail.com for any comments, reviews or advice.
Alternate https://elvis-awards.herokuapp.com/ ## License
Copyright (c) **Elvisbkt**
