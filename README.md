# mastermind

### This is an API for the mastermind game

Done in Python 3 and Django 1.10

## To install:

After clone the repository, in your virtual enviroment run:

- pip install -r requirements.txt

- migrations

- create a file named settings_dev.py at the same level of the settings.py file

- add ALLOWED_HOST = ['your_host'] to settings_dev.py

Once the app is running you can check the APOI documentation in http://<your_host>:<your_port>/docs

## TODO

Since we are not handling sessions we've disabled the authentication and authorization policies 
in the view classes. We must add User support in order to allow only authenticated users to use the POST endpoints 

