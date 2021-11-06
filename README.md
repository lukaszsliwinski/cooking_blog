# Cooking blog

## About
This is a blog application based on Django framework that contains a database with recipes. After create an account in administration panel you can add recipes including description, photo, ingrediends, country of origin and category. On the main site, you can sort recipes by country or category and select to view details. This is my first web app made for learning Django and gain experience in web development.

## Used technologies
Python 3.8<br>
Django 3.1.7<br>
SQLite3<br>
HTML5<br>
CSS3<br>
Javascript

## Setup and run (Windows)
1 Install Python 3.8 from website:<br>
&emsp;https://www.python.org/downloads/release/python-380/<br>
&emsp;Important - remember to mark "Add Python 3.8 to PATH"!<br>
&emsp;![alt text](https://github.com/lukaszsliwinski/cooking_blog/blob/master/add-python-to-path.png?raw=true)<br><br>
2 Download repository
```bash
git clone https://github.com/lukaszsliwinski/cooking_blog
```
3 Go into main directory
```bash
cd cooking_blog
```
4 Create virtual environment with Python 3.8 (you can use any name)
```bash
py -3.8 -m venv name
```
&emsp;This may take a while<br><br>
5 Run virtual environment
```bash
name\scripts\activate
```
&emsp;Important! Keep virtual environment running always when you use app. To deactivate venv use:
```bash
deactivate
```
6 With venv kept running install required packages from requirements.txt file
```bash
pip install -r requirements.txt
```
&emsp;This may take a while<br><br>
7 Create database
```bash
python manage.py migrate
```
8 Create account
```bash
python manage.py createsuperuser
```
&emsp;Enter username, email adress and password that will be used later to log in administration panel <br><br>
9 Run application on localhost
```bash
python manage.py runserver
```
&emsp;Enter https://127.0.0.1:8000 in browser to run main page of an app<br><br>
10 In the top right corner press login to log in administration panel and add dishes