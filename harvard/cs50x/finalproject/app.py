__author__ = 'John Rocha'
__date__ = '2024/11/23'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'


import re
import string
import random

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous.exc import BadSignature as BadSignature
from itsdangerous.exc import BadTimeSignature as BadTimeSignature
from itsdangerous.exc import SignatureExpired as SignatureExpired

#: Configure application
app = Flask(__name__)
app.secret_key = 'K5QwCWsJ8qkypg2R3rifHnI0O7'

#: Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


#: email Configuration
app.config['MAIL_SERVER'] = 'mail.smartshots.org'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noreply@smartshots.org'
app.config['MAIL_PASSWORD'] = '#Pfd7*x8kp3H&B'
mail = Mail(app)



#: Configure CS50 Library to use SQLite database
db = SQL('sqlite:///surveys.db')

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = 0
    response.headers['Pragma'] = 'no-cache'
    return response


#: Routes
@app.route('/', methods=['GET','POST'])
@login_required
def index():
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/'                                                                           │
    #+│ Function:   index                                                                         │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  This is the default route.  The main purpose is to show what surveys the user     │
    #:│         has requested hash values for.  Supports only GET methods                         │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Requires that the user is logged in                                                  │
    #:│  2.- Presents the user with a 4 column table denoting:                                    │
    #:│    2.1.- Survey name                                                                      │
    #:│    2.2.- Status where "Pending" is not requested and "Taken" if already taken             │
    #:│    2.3.- Taken date where blank if not taken or date of when taken                        │
    #:│    2.4.- Link Survey where it is just a link that if clicked on                           │
    #:│      2.4.1.- Store in session, the hash value for the survey                              │
    #:│      2.4.2.- Save information in database                                                 │
    #:│      2.4.3.- Routes to the survey site                                                    │
    #:│  3.- Present the user with a message that tell the users which surveys are pending and    │
    #:│      if all the surveys are taken, a message that tells the user their tasks are          │
    #:│      complete.                                                                            │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    if request.method != 'GET':
        return 'Inappropriate page access'

    return render_template('index.html',admin=session.get('is_admin'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a user"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/register'                                                                   │
    #+│ Function:   register                                                                      │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST methods.  After registration completes it redirects to '/'  │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Presents the user with three required fields.  Userid, Password and Password         │
    #:│      Confirmation                                                                         │
    #:│  2.- User ID must be oneMedical email address using expressions and is required           │
    #:│  3.- Password is masked and required                                                      │
    #:│  4.- Password Confirmation is masked and required and must match Password                 │
    #:│  5.- Userid is saved in the database hashed                                               │
    #:│  5.- Password is saved in the database hashed                                             │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Forget any user_id
    session.clear()
    email_pattern="^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@onemedical.com$"

    if request.method == 'GET':
        return render_template('register.html')

    #: User reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':
        #: Ensure username was submitted
        username = request.form.get('username').upper()
        matches = re.search(email_pattern, username, re.IGNORECASE)
        if matches or username == 'JOHN.ROCHA@OUTLOOK.COM':
            pass
        else:
            flash('User names must be a valid email address', 'danger')
            return render_template('register.html')

        #: Ensure password was submitted
        user_password = request.form.get('password')
        if len(user_password) < 8:
            flash('Password field must contain at least 8 characters', 'danger')
            return render_template('register.html')

        #: Ensure confirmation password was submitted
        user_password_confirmation = request.form.get('confirmation')
        if user_password != user_password_confirmation:
            flash('Passwords do not match.  Please re-enter passwords', 'danger')
            return render_template('register.html')

        #: Hash userid and password
        hashed_username = ''
        hashed_password = ''
        hashed_username = generate_password_hash(username, method='scrypt', salt_length=16)
        hashed_password = generate_password_hash(user_password, method='scrypt', salt_length=16)

        #: Check to see if the user is already defined and the password entered is the same
        rows = db.execute('SELECT id, user_name, password, is_admin, url_key FROM users')

        #: Seed event for the very first account created in the system
        if len(rows) == 0:
            #: There are no users in the database so we need to insert the very first row
            try:
                url_key = "".join(random.choice(string.ascii_letters) for i in range(16))
                identity = db.execute(
                    '''INSERT INTO users (user_name, password, is_admin, url_key)
                            VALUES (?,?,?,?)''', hashed_username, hashed_password, 'N', url_key)
                session['user_id'] = identity
                session['is_admin'] = 'N'
                session['url_key'] = url_key
                flash(f'User account for {username} was successfully created', 'success')
                return redirect('/')
            except:
                messageTitle = 'Internal Error'
                messageDescription = 'Unable to insert a new user'
                return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)

        #: If we are here, there is at least one account in the system
        #: Need to find out if there is already a user with the same email address.
        for row in rows:

            #: Check to see if the stored username is the same as the forms username
            if check_password_hash(row['user_name'], username):

                #: Now check if the user's password is the same
                if check_password_hash(row['password'],user_password):
                    session['user_id'] = row['id']
                    session['is_admin'] = row['is_admin']
                    session['url_key'] = row['url_key']
                    flash('Successfully logged in','success')
                    return redirect('/')
                else:
                    flash('The password you entered is invalid', 'danger')
                    return render_template('register.html')


        #: If we are here, there is no user in the system with the same account
        print('Did not find the user in the users table')
        try:
            url_key = "".join(random.choice(string.ascii_letters) for i in range(16))
            identity = db.execute('INSERT INTO users (user_name, password, is_admin, url_key) VALUES (?,?,?,?)',
                                   hashed_username, hashed_password, 'N', url_key)
            session['user_id'] = identity
            session['is_admin'] = 'N'
            session['url_key'] = url_key
            flash(f'Account for {username} was successfully created', 'success')
            return redirect('/')
        except:
            messageTitle = 'Internal Error'
            messageDescription = 'Unable to insert a new user'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)
    else:
         #: User reached route via GET (as by clicking a link or via redirect)
         messageTitle = 'Internal Error'
         messageDescription = 'Method not allowed for registration'
         return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)



@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/login'                                                                      │
    #+│ Function:   login                                                                         │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST methods.  After login completes it redirects to '/'         │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Presents the user with two required fields.  Userid and Password                     │
    #:│  2.- User ID must be oneMedical email address using expressions and is required           │
    #:│  3.- Password is masked and required                                                      │
    #:│  4.- The hashed userid must have a matched hashed password                                │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Forget any user_id
    session.clear()
    email_pattern="^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@onemedical.com$"

    if request.method == 'GET':
        return render_template('login.html')


    #: User reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':
        #: Ensure username was submitted
        username = request.form.get('username').upper()
        matches = re.search(email_pattern, username, re.IGNORECASE)
        if matches or username == 'JOHN.ROCHA@OUTLOOK.COM':
            pass
        else:
            flash('User names must be a valid email address', 'danger')
            return render_template('login.html')

        #: Ensure password was submitted
        user_password = request.form.get('password')
        if len(user_password) < 8:
            flash('Password is invalid', 'danger')
            return render_template('login.html')

        rows = db.execute('SELECT id, user_name, password, is_admin, url_key FROM users')
        if len(rows) == 0:
            return redirect('/register')

        #: Find the user
        for row in rows:
            #: Check to see if the stored username is the same as the forms username
            if check_password_hash(row['user_name'], username):
                #: Now check if the user's password is the same
                if check_password_hash(row['password'],user_password):
                    session['user_id'] = row['id']
                    session['is_admin'] = row['is_admin']
                    session['url_key'] = row['url_key']
                    flash('Successfully logged in','success')
                    return redirect('/')
                else:
                    flash('Your password is invalid', 'danger')
                    return render_template('login.html')

        #: If we are here, we did not find a user with that username
        flash('User id is not valid.  Consider registering if you would like to create an accunt.','danger')
        return render_template('login.html')

    #: Not GET or POST
    else:
        messageTitle = 'Internal Error'
        messageDescription = 'Login method not allowed'
        return render_template('error.html',messageTitle=messageTitle,
                                            messageDescription=messageDescription)



@app.route('/logout')
def logout():
    """Log user out"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/logout'                                                                     │
    #+│ Function:   logout                                                                        │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET only and routes to '/'                                               │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Destroys the session elements and routes to '/'                                      │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Forget any user_id
    session.clear()

    #: Redirect user to login form
    flash('Successfully logged out', 'success')
    return render_template('login.html')


@app.route('/surveys')
@login_required
def surveys():
    """Log user out"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/surveys'                                                                    │
    #+│ Function:   surveys                                                                       │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET                                                                      │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Depicts the surveys that the user has taken so far                                   │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘
    if request.method == 'GET':
        rows = db.execute(
                    '''SELECT usrv.survey_id as surveyId,
                              srvy.name as surveyName,
                              srvy.longname as surveyLongName,
                              srvy.url as survey_Url,
                              usr.url_key as userUrlPrefix
                         FROM user_surveys usrv
                            inner join surveys srvy on srvy.id = usrv.survey_id
                            inner join users usr on usr.id = usrv.user_id
                        WHERE usrv.user_id = ?''',session.get('user_id'))
        for row in rows:
            row['survey_Url'] = row['survey_Url'] + '/?sguid=' + session['url_key']
        return render_template('surveys.html',admin=session.get('is_admin'), surveys=rows)

    return 'TODO - Surveys'


@app.route('/addSurveys', methods=['GET','POST'])
@login_required
def addSurveys():
    """Add surveys"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/addSurveys'                                                                 │
    #+│ Function:   addSurveys                                                                    │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST                                                             │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Allows admins to add surveys                                                         │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Get the survey's from the table
    rows = db.execute('SELECT id, name, longname, url, active from surveys')
    if request.method == 'GET':
        return render_template('addSurveys.html',admin=session.get('is_admin'), surveys=rows)

    if request.method == 'POST':
        #: Need to determine if we are inactivating a survey
        if 'buttonAdd' in request.form:
            survey_name = request.form.get('surveyname')
            survey_longname = request.form.get('longname')
            survey_url = request.form.get('surveyurl')
            if len(survey_name) < 1 or len(survey_longname) < 1 or len(survey_url) < 1:
                flash(f'Survey fields must all contain data', 'danger')
                return render_template('addSurveys.html',admin=session.get('is_admin'), surveys=rows)

            #: Now let's insert the survey
            try:
                db.execute(
                    '''INSERT INTO surveys (name, longname, url, active)
                                    VALUES (?,?,?,?)''', survey_name,
                                                         survey_longname,
                                                         survey_url,
                                                         'Y')
            except:
                messageTitle = 'Internal Error'
                messageDescription = 'Unable to insert into survey table'
                return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)

            #: Reload surveys
            rows = db.execute('SELECT id, name, longname, url, active from surveys')
            flash('Successfully added survey','success')
            return render_template('addSurveys.html',admin=session.get('is_admin'), surveys=rows)
        else:
            #: We are inactivating
            inactivate_survey = request.form.get('inactivateSurvey')

            #: Now inactivating a survey
            try:
                db.execute('UPDATE surveys set active = "N" where id = ?',inactivate_survey)
            except:
                messageTitle = 'Internal Error'
                messageDescription = 'Unable to inactivate a survey'
                return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)

            #: Now load the surveys again
            rows = db.execute('SELECT id, name, longname, url, active from surveys')
            flash(f'Survey "{rows[0]['name']}" has been inactivated', 'success')
            return render_template('addSurveys.html',admin=session.get('is_admin'), surveys=rows)
    else:
        #: Not GET or POST
        messageTitle = 'Internal Error'
        messageDescription = 'Add survey method not allowed'
        return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)


@app.route('/takeSurvey', methods=['GET','POST'])
@login_required
def takeSurvey():
    """Take surveys"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/takeSurvey'                                                                 │
    #+│ Function:   takeSurvey                                                                    │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST                                                             │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- Allows users to register to surveys                                                  │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    rows = db.execute(
                '''SELECT usrv.survey_id as surveyId,
                          srvy.name as surveyName,
                          srvy.longname as surveyLongName,
                          srvy.url as surveyUrl,
                          usr.url_key as userUrlPrefix
                     FROM user_surveys usrv
                        inner join surveys srvy on srvy.id = usrv.survey_id
                        inner join users usr on usr.id = usrv.user_id
                    WHERE usrv.user_id = ?''',session.get('user_id'))

    survey_list = db.execute(
        '''SELECT srv.id as id,
                  srv.name as name,
                  srv.longname as longname,
                  srv.url as url
             FROM surveys srv
            WHERE srv.active = "Y"
              AND srv.id NOT IN (SELECT usrv.survey_id
                                   FROM user_surveys usrv
                                  WHERE usrv.survey_id = srv.id
                                    AND usrv.user_id = ?)''', session.get('user_id'))

    if request.method == 'GET':
        return render_template('takeSurvey.html',admin=session.get('is_admin'), surveys=rows, surveyList=survey_list)

    if request.method == 'POST':
        #: Now let's add the selected survey
        survey_id = request.form.get('surveyid')
        try:
            int(survey_id)
        except:
            messageTitle = 'My Surveys'
            messageDescription = 'No survey selected.'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)

        #: Insert the selected survey into the userSurveys table
        try:
            db.execute('INSERT INTO user_surveys (user_id, survey_id) VALUES (?,?)',
                            int(session['user_id']),
                            int(survey_id) )
        except:
            messageTitle = 'Internal Error'
            messageDescription = 'Unable to take a survey'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)
        #: Build survey link
        selected_survey = db.execute('SELECT url FROM surveys WHERE id = ?', survey_id)
        survey_link = selected_survey[0]['url'] + '/?sguid=' + session['url_key']
        return redirect(survey_link)

    else:
        messageTitle = 'Internal Error'
        messageDescription = 'Take survey method not allowed.  Only accept GET and POST'
        return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)


@app.route('/request_reset', methods=['GET','POST'])
def request_reset():
    """password reset request"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/request_reset'                                                              │
    #+│ Function:   request_reset                                                                 │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST                                                             │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- This route will present a page where the user can enter an email address             │
    #:│  2.- The page will react the same way even if the user enters a bad address               │
    #:│  3.- If the email address is an existing account, the app will create a secure token and  │
    #:│      send the user an email with that token.                                              │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘
    session.clear()
    email_pattern="^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@onemedical.com$"

    if request.method == 'GET':
        return render_template('request_reset.html')

    if request.method == 'POST':
        #: Check the email address field is a valid email address
        username = request.form.get('username').upper()
        matches = re.search(email_pattern, username, re.IGNORECASE)
        #: When asking for account resets, we don't let them know if they entered the wrong email
        #: address.  This will confuse non OneMedical users from trying to create a new account
        if matches or username == 'JOHN.ROCHA@OUTLOOK.COM':
            pass
        else:
            flash('User names must be a valid email address', 'danger')
            return render_template('login.html')

        #: Now scan all the users to see if there is an user with that email address
        rows = db.execute('SELECT id, user_name, password, is_admin, url_key FROM users')
        if len(rows) == 0:
            msg = 'Your request has been submitted. Please follow your instructions included in the'
            msg = msg + ' body of the email.  Please note that you have 15 minutes to complete this'
            msg = msg + ' request.'
            flash(msg, 'info')
            return render_template('login.html')

        #: Find the user
        for row in rows:
            #: Check to see if the stored username is the same as the forms username
            if check_password_hash(row['user_name'], username):

                #: email address exists so let's build the token
                out_srlzr = Serializer(app.config['SECRET_KEY'])
                out_token = out_srlzr.dumps({'user_id': int(row['id'])},salt='7KCIkoovLq4gdC5r')

                #: Now we can send the email
                link = url_for('pass_reset', in_token=out_token, _external=True)
                msg = Message('Password Reset', sender=app.config['MAIL_USERNAME'], recipients=[username])
                msg.html = '<b>To reset your password, visit the following link:</b>'
                msg.html = msg.html + f' {link}'
                msg.html = msg.html + '<br><br>If you did not make this request, the simply ignore this email and no '
                msg.html = msg.html + 'changes will be made.<br><br>'
                msg.html = msg.html + 'If you have problems with the link, in this email, copy the url and paste it in '
                msg.html = msg.html + 'your browser.'
                try:
                    mail.send(msg)
                except Exception as e:
                    messageTitle = 'Internal Error'
                    messageDescription = f'Unable to send email {e}'
                    return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)

                flash('Thank you for submitting your password reset request.  Please follow email instructions', 'info')
                return render_template('login.html')

        #: There is no local account with that email address
        return render_template('login.html')
    else:
        messageTitle = 'Internal Error'
        messageDescription = 'Reset password method not allowed.  Only accept GET and POST'
        return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)



@app.route('/pass_reset/<in_token>', methods=['GET','POST'])
def pass_reset(in_token):
    """password reset request"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Route:      '/pass_reset'                                                                 │
    #+│ Function:   pass_reset                                                                    │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Route:  Supports GET and POST                                                             │
    #:│ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . │
    #:│ Function:                                                                                 │
    #:│  1.- A insdangerous token is received in this route and will have an expiration of 5      │
    #:│      minutes.  If within the 5 minutes, provide the means to change the password.  If     │
    #:│      past the 5 minutes, send them back to the request page                               │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Testing unpacking
    if request.method == 'GET':
        return render_template('reset_password.html')

    if request.method == 'POST':
        #: Ensure confirmation password was submitted
        user_password = request.form.get('password')
        if len(user_password) < 8:
            flash('Password field must contain at least 8 characters', 'danger')
            return render_template('reset_password.html')

        #: Ensure confirmation password was submitted
        user_password_confirmation = request.form.get('confirmation')
        if user_password != user_password_confirmation:
            flash('Passwords do not match.  Please re-enter passwords', 'danger')
            return render_template('reset_password.html')

        #: Hash userid and password
        hashed_password = ''
        hashed_password = generate_password_hash(user_password, method='scrypt', salt_length=16)

        #: Save the new user password
        try:
            in_srlzr = Serializer(app.config['SECRET_KEY'])
            token = in_srlzr.loads(in_token, salt="7KCIkoovLq4gdC5r", max_age=300)

        except BadTimeSignature as error_expired:
            flash('Your email has expired.  Please submit another request', 'danger')
            return render_template('request_reset.html')

        except BadSignature as error_bad_token:
            messageTitle = 'Internal Error'
            messageDescription = f'Exception error_bad_token: {error_bad_token}'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)
        except SignatureExpired as error_expire2:
            messageTitle = 'Internal Error'
            messageDescription = f'Exception signature_expired: {error_expire2}'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)


        #: If we are here, we know who the user is
        try:
            db.execute('UPDATE users SET password = ? WHERE id = ?', hashed_password,
                                                                     token['user_id'])
            flash('Passwords has been reset.  Please login now', 'info')
            return render_template('login.html')
        except:
            messageTitle = 'Internal Error'
            messageDescription = 'Unable to set the new password'
            return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)
    else:
        messageTitle = 'Internal Error'
        messageDescription = 'Pass_reset method not allowed.  Only accept GET and POST'
        return render_template('error.html',messageTitle=messageTitle, messageDescription=messageDescription)


