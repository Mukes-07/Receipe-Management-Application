Date:-28/07/2025

Django -> 

- Djnago is a backend server side web framework. 
- Django is free, Open source & written in python. 
- Django makes easier to build web pages using python. 

How Does django work -> 

- Django follows the MVT design pattern (Model-View-Template)

1. Model -> the data you want to present, usually the data from a database.
2. View -> in view , we can write the functional logics part. so that it makes request & responce to the frontend.
3. Template -> A text file (like HTML) containing the layout of the web pages. 


How to setup the django Project ->>> 

- when we set up a django project , we need to create one environment where we start our project. 
- Creating an environment the command is -> python -m venv myenv
- Then after creating an environment, you need to activate the environment by the command 
    -> .\myenv\Scripts\activate

- Then we need to install django by the command 
    -> pip install django 

- After that we can create a project , by provide any type of name like 
    -> djnago-admin startproject core  ( where, core is my project name )

- After creating one project , if the project have 3 module so you need create 3 usable app for our project. Now we can create a app , to demonostrate our project 
    -> python manage.py startapp home  (where home is my app name)
    -> python manage.py runserver
    
Views & URL :-
 - views basically store the logical part in our project.
 - But in URL we need to map the logical part on our rootes so URL's play a imp. role in Django.

 CRUD -> Create, read, update, delete

Create -> this involves adding new record to a database table. 
Read -> This involves retriving data from the database. 
Update -> This involves modifying existing record in the database. 
Delete -> This involves removing record from the database.

Data redirect -> 

- when we are transfer the data from backend to frontend we can use -> context
- when we are transfer the data from frontend to backend we can use -> method="post"

