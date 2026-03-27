# Django Sticky Notes App

A personal Sticky Notes web application built with Django. This app allows users to register, log in, and manage their own private collection of notes (create, read, update, and delete) with a color-coded sticky note interface.

## Features
- **User Authentication:** Sign up, log in, and log out functionality using Django's built-in system.
- **Private Notes:** Users can only view and manage their own notes (@login_required enforced).
- **CRUD Operations:** Create, read, update, and delete sticky notes.
- **Custom Colors:** Notes have custom background colors to simulate real sticky notes.
- **Admin Panel:** Built-in Django admin interface to manage backend data.

## Prerequisites
Make sure you have Python installed on your system.

## Setup and Installation Instructions

Follow these step-by-step instructions to run the project on your local machine:

**1. Open the Project Folder**
Extract the `Name_RollNumber.zip` file and open the extracted folder in your terminal or command prompt.

**2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```

**3. Activate the Virtual Environment**
- For Windows:
  ```bash
  venv\Scripts\activate
  ```
- For macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

**4. Install Django**
```bash
pip install django
```

**5. Apply Database Migrations**
Run the following commands to create the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create a Superuser (Optional - for Admin Panel access)**
```bash
python manage.py createsuperuser
```

**7. Run the Development Server**
```bash
python manage.py runserver
```

## Usage
- Open your web browser and navigate to: `http://127.0.0.1:8000/notes/`
- Register a new account or log in with an existing one.
- Start creating and managing your sticky notes!

## Author
**Name:** Muhammad Subhan Tariq
**Roll Number:** 22p-9067
```
