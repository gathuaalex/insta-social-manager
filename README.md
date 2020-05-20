# insta-social-manager
## HOW TO RUN THE APP

NB: This guildlines are for a windows environment, prefer using windows powershell

After cloning cloning the app:

Make sure you have python3 and pip3 installed in your machine 

ensure virtualenv is installed on your machine 

Create a virtual environment  by running virtualenv on your machine. Checkout on how to create  virtual environments environments if there's trouble.

In the windows powershell, navigate into the app directory. Make sure the virtual environment is activated ...try use this command "Scripts\activate.ps1".

Run pip install -r requirements.txt

Run python manage.py makemigrations

Run python manage.py migrate

Add an admin by running python manage.py createsuperuser.

Visit the admin site and add some dummy data.

Assuming everything is okay, run python manage.py runserver and you should see a link to the app.
