__author__ = "John Rocha"
__date__ = "2024/09/15"

#: Import Section
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_mail import Message, Mail

#: Instantiate application
app = Flask(__name__)

#: Set the environment.  Options are 
#:  1.- ConfigProdNoDbNoMail ==> For Production applications NOT using a database or email
#:  2.- ConfigProdWithDBWithMail ==> For Production applications USING database and email
#:  3.- ConfigDevNoDbNoMail ==> For Development applications NOT using a database or email
#:  4.- ConfigDevWithDBWithMail ==> For Development applications USING database and email
app.config['ENV'] = 'ConfigDevWithDBWithMail'

match app.config['ENV']:
    case 'ConfigProdNoDbNoMail':
        app.config.from_object('config.ConfigProdNoDbNoMail')
    case 'ConfigProdWithDBWithMail':
        app.config.from_object('config.ConfigProdWithDBWithMail')
    case 'ConfigDevNoDbNoMail':
        app.config.from_object('config.ConfigDevNoDbNoMail')
    case 'ConfigDevWithDBWithMail':
        app.config.from_object('config.ConfigDevWithDBWithMail')


@app.route('/')
@app.route('/index')
def index():
    """
        Function name: index

        Arguments:

        Preconditions:

        Returns:
            Some long string
    """
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route: ('/')                                                                              │
    #+│ Function: FuncName                                                                        │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Methods:  Supports GET and POST                                                           │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│                                                                                           │
    #:│                                                                                           │
    #:│                                                                                           │
    #:│                                                                                           │
    #:│                                                                                           │
    #:│                                                                                           │
    #:│                                                                                           │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘
    return render_template('index.html',admin=session.get('is_admin'))
    return 'TODO Main Route'


if __name__ == '__main__':
    if app.config['ENV'] == 'development':
        app.run(debug=True)
    else:
        app.run(debug=False)
