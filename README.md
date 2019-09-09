# [Awwwards Application](https://Instaclone-application.herokuapp.com/)
#### Web clone of the awwwards.com
#### August 5th, 2019
#### By **[Denis Githinji](https://github.com/dmwaigithinji)**

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
`git clone https://github.com/Dmgithinji/awwwards.git && cd awwwards`

### Activate virtual environment
Activate virtual environment using python3.7 as default handler
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
    - Python 3.7
    - HTML
    - Bootstrap 4
    - JavaScript
    - Django
    - Heroku
    - Postgresql

## Support and contact details
Contact me on dmwaigithinji@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Dmgithinji**