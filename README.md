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
https://www.python.org/downloads/release/python-380/<br>
Important - remember to mark "Add Python 3.8 to PATH"!<br>
![alt text](https://github.com/lukaszsliwinski/cooking_blog/blob/master/add-python-to-path.png?raw=true)<br><br>
2 Download repository
```bash
git clone https://github.com/lukaszsliwinski/cooking_blog
```
3 Go into main directory
```bash
cd cooking_blog
```
4 Install required packages from requirements.txt file
```bash
pip install -r requirements.txt
```
5 Create database
```bash
python manage.py migrate
```
6 Create account
```bash
python manage.py createsuperuser
```
Enter username, email adress and password<br><br>
7 Run application on localhost
```bash
python manage.py runserver
```
Enter https://127.0.0.1:8000 in browser<br><br>
8 Enter https://127.0.0.1:8000/admin and log in adminitration panel to add recipies