# Virtual environment

```shell
linku@deadalus:~$ cd ~/Desktop/Stuy/SoftDev/Flask/
linku@deadalus:~/Desktop/Stuy/SoftDev/Flask$ virtualenv venv
New python executable in /home/linku/Desktop/Stuy/SoftDev/Flask/venv/bin/python
Installing setuptools, pip, wheel...done.
linku@deadalus:~/Desktop/Stuy/SoftDev/Flask$ ls venv/
bin/                lib/                pip-selfcheck.json
include/            local/              
linku@deadalus:~/Desktop/Stuy/SoftDev/Flask$ ls venv/bin/
activate       activate_this.py  pip     python     python-config
activate.csh   easy_install      pip2    python2    wheel
activate.fish  easy_install-2.7  pip2.7  python2.7
linku@deadalus:~/Desktop/Stuy/SoftDev/Flask$ . venv/bin/activate
(venv) linku@deadalus:~/Desktop/Stuy/SoftDev/Flask$ 
```

# Flask

`127.0.0.1` is the 'loopback' address because it is your computer requesting itself.        
It is also known as the localhost.

Network ports allow your computer to respond to different internet requests.

The default webserver port is port 80 but flask does not want to interfere with webservers.     
That's why flask uses the port 5000.

By default, flask does not allow 'outside world' access by default.       
This prevents external 'forces' from interfering with your virtual environment.



```py
from flask import Flask 
# Imports the 'Flask' class from the 'flask' module
# Means you are not importing the entire flask module
# This makes it so you don't have to do flask.Flash().

my_app = Flask(__name__)
# This is the constructor.
# It makes a new Flask object and returns it.
# The Flask object only takes one argument
# Always format it in the format '__name__' with the underscores.

# __name__ will be the name of the file if it is imported as a module
# __name__ will be __main__ if it is run as a program

# my_app is now a Flask instance.
# To make it do stuff, interact with my_app

@my_app.route('/')
def root():
    print 'PRINTING!!!!!!!!!'
    return 'Hi Everybody!'

# Allows the Flask app to respond to different page requests
# Allows you to create different 'routes' or 'targets' for your website
# Makes creating a multi-page website really easy with Flask.
# You can attach different functions to different routes.
# '@' is a 'decorator' in python.
# Decorators HAVE to be right on top of the declaration of the function to attach it.
# You can attach multiple routes to one function.
# You cannot have a route attached to multiple functions.

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
# If this isn't being imported from elsewhere then do this.
# AKA if 'this' is the currently running program then do this.
# my_app.run() is the code to run the Flask app.

# Page not found means your web server is running but the route isn't defined.
# This site can't be reached means that your server isn't running.

# Generall if you want to change your program, you have to restart the app.
# `my_app.debug = True`
# In debug mode, whenever the file changes then the app will restart with changes.

```