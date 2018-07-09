# mastermind
###This is an API for the mastermind game


##To install:

After clone the repository, in your virtual enviroment run

pip install -r requirements.txt

run migrations

create a file named settings_dev.py in the same level of settings.py
add ALLOWED_HOST['your_host'] to settings_dev.py

##TODO

Since we are not handling sessions we disabled the authentication and authorization policies 
in the view classes. We must add User support in order to allow only autheticated users
perssions to use the POST endpoints 

