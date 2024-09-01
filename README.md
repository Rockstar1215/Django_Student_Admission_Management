# Student Management System

This is a web-based student management system developed using **Django 4**, **HTML5**, **CSS3**, and **Bootstrap 5**, enhanced with a **Bootswatch** theme.

## Contents
- [Requirements](#requirements)
- [Setup Guide](#setup-guide)
- [Starting the Application](#starting-the-application)
- [Running Tests](#running-tests)
- [Accessing the Application](#accessing-the-application)

### Requirements

Before getting started, make sure you have the following installed:

1. [Python 3.8-3.11](https://www.python.org/downloads/):  
   This project relies on **Django v4.2.4**. To ensure compatibility, you'll need the correct version of Python. For further details, visit the [Django installation guide](https://django.readthedocs.io/en/stable/faq/install.html).

2. [Visual Studio Code](https://code.visualstudio.com/download):  
   This is the recommended IDE for development.

### Setup Guide

#### 1. Set Up a Virtual Environment

Navigate to the project’s **root** directory and create a virtual environment:

```bash
python -m venv venv
```

#### 2. Activate the Virtual Environment

To activate the virtual environment, run the following commands from the **root** directory:

- On macOS:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\scripts\activate
```

#### 3. Install Dependencies

Install the necessary packages by running:

```bash
pip install -r requirements.txt
```

#### 4. Apply Database Migrations

Execute the following commands to set up the database:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

#### 5. Create an Admin Account

To manage the system through the Django Admin interface, create a superuser account:

```bash
python manage.py createsuperuser
```

You will be prompted to provide a username, email address, and password.

### Starting the Application

To launch the application, use the following command from the **root** directory:

```bash
python manage.py runserver
```

### Running Tests

You can run the tests by executing:

```bash
python manage.py test --pattern="tests.py"
```

### Accessing the Application

Once the server is running, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the application.
