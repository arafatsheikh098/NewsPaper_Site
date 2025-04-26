## **Step 1: Set Up the Django Project**

### **1.1 Install Python and Virtual Environment**

Navigate into the project folder:

cd blog-site

Ensure you have Python installed (preferably Python 3.9+). Then, set up a virtual environment.

\# Install virtualenv if not installed

pip install virtualenv

\# Create a virtual environment

python \-m venv venv

\# Activate the virtual environment

\# On Windows:

venv\\Scripts\\activate

\# On macOS/Linux:

source venv/bin/activate

Set-ExecutionPolicy Unrestricted \-Scope Process

### **1.2 Install Django**

Once the virtual environment is activated, install Django.

pip install django

### **1.3 Start a New Django Project**

Run the following command to create a Django project named `Newspaper`:

django-admin startproject newspaper_site .

Run the development server to check if Django is set up correctly:

python3 manage.py runserver

You should see the Django welcome page at `http://127.0.0.1:8000/`.

---
check requirement.txt to see all dependency 

install all dependency by 
pip install -r requirements.txt
