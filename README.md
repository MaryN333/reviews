## Table of Contents
1. [Visitors Functionality](#visitors-functionality)
2. [Installation](#installation)
3. [Admin](#admin)
4. [API](#api)

## Visitors Functionality
* Sign Up
* Log In
*	Create an review (you need to Sign Up or Log In)
*	Change own review
*	Delete own review
*	Log out
## Installation
*	Download This Project Zip Folder and Extract it
*	Move to the project folder in Terminal
*	Create a .venv folder in the root folder.
*	Install Python(3.11.2)
*	Execute Following Commands In Terminal:
```bash
pipenv install django==3.2.20
pipenv install pillow==10.2.0
pipenv install django-tastypie==0.14.6
pipenv install djangorestframework==3.14.0
```
```bash
python manage.py migrate
python manage.py runserver
```
*	Now enter following URL in Your Browser Installed On Your Pc:
http://127.0.0.1:8000/
## Admin
*	First admin will login ( for username/password run following command in Terminal )
python manage.py createsuperuser
*	Give username, email, password and your admin account will be created.
Admin can add/delete/view/edit the restaurants, types and reviews (navbar link Admin).

## API
*	Create a key in Admin panel.
*	Install Postman.
*	Key owner can add (POST)/ delete (DELETE)/ view (GET)/ edit (PATCH) the restaurants with key in Headers.
*	You can view (GET) the types and reviews without any key.

