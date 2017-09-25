from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    print "Route Uno"
    return 'First Route'

@my_app.route('/route')
def route():
    print "You have reached the 2nd route"
    return 'Second Route'

@my_app.route('/altroute')
def altroute():
    print "You have reached the route of no return"
    return "Final Route"

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()