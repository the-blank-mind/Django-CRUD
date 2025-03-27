# Django-CRUD


# Django Employee CRUD Project

A simple Employee CRUD (Create, Read, Update, Delete) application built using Django for the backend and HTML/CSS with Django Forms for the frontend. This project allows users to add, view, update, and delete employee records.


# Features
    1. Add new employees
    2. View employee list
    3. Update employee details
    4. Delete employee records

# Prerequisites
Make sure you have the following installed on your system:

    * Python (>= 3.7)
    * pip (Python package installer)
    * Django (>= 4.0)

# Installation and Setup

Follow these steps to set up and run the project:
1. Clone the Repository

    git clone https://github.com/the-blank-mind/Django-CRUD
   
    cd Django-CRUD

   
3. Open Terminal in the above directory.
  
4. Apply Migrations

   python manage.py makemigrations
   
   python manage.py migrate


6. Run the Development Server

   python manage.py runserver
   

Open your browser and navigate to http://127.0.0.1:8000/ to use the app.




# Project Structure


    CrudOperation/crud/urls.py: Contains URL routes for the application.


    CrudOperation/crud/forms.py: Handles form input using Django Forms.


    CrudOperation/crud/models.py: Defines the Employee model.


    CrudOperation/templates/: HTML templates for CRUD operations.


    CrudOperation/crud/views.py: Contains logic for CRUD functionalities.


Feel free to modify this according to your actual project structure and requirements. Let me know if you'd like to refine specific sections or add more details! 🚀
