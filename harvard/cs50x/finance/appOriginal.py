__author__ = 'John Rocha'
__date__ = '2024/11/17'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'

#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Understanding app.py:                                                                         │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Open up app.py. Atop the file are a bunch of imports, among them CS50’s SQL module and a few  │
#:│ helper functions. More on those soon.                                                         │
#:│                                                                                               │
#:│ After configuring Flask, notice how this file disables caching of responses (provided you’re  │
#:│ in debugging mode, which you are by default in your code50 codespace), lest you make a change │
#:│ to some file but your browser not notice. Notice next how it configures Jinja with a custom   │
#:│ “filter,” usd, a function (defined in helpers.py) that will make it easier to format values as│
#:│ US dollars (USD). It then further configures Flask to store sessions on the local filesystem  │
#:│ (i.e., disk) as opposed to storing them inside of (digitally signed) cookies, which is Flask’s│
#:│ default. The file then configures CS50’s SQL module to use finance.db.                        │
#:│                                                                                               │
#:│ Thereafter are a whole bunch of routes, only two of which are fully implemented: login and    │
#:│ logout. Read through the implementation of login first. Notice how it uses db.execute (from   │
#:│ CS50’s library) to query finance.db. And notice how it uses check_password_hash to compare    │
#:│ hashes of users’ passwords. Also notice how login “remembers” that a user is logged in by     │
#:│ storing his or her user_id, an INTEGER, in session. That way, any of this file’s routes can   │
#:│ check which user, if any, is logged in. Finally, notice how once the user has successfully    │
#:│ logged in, login will redirect to "/", taking the user to their home page. Meanwhile, notice  │
#:│ how logout simply clears session, effectively logging a user out.                             │
#:│                                                                                               │
#:│ Notice how most routes are “decorated” with @login_required (a function defined in helpers.py │
#:│ too). That decorator ensures that, if a user tries to visit any of those routes, he or she    │
#:│ will first be redirected to login so as to log in.                                            │
#:│                                                                                               │
#:│ Notice too how most routes support GET and POST. Even so, most of them (for now!) simply      │
#:│ return an “apology,” since they’re not yet implemented.                                       │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ helpers.py:                                                                                   │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Next take a look at helpers.py. Ah, there’s the implementation of apology. Notice how it      │
#:│ ultimately renders a template, apology.html. It also happens to define within itself another  │
#:│ function, escape, that it simply uses to replace special characters in apologies. By defining │
#:│ escape inside of apology, we’ve scoped the former to the latter alone; no other functions     │
#:│ will be able (or need) to call it.                                                            │
#:│                                                                                               │
#:│ Next in the file is login_required. No worries if this one’s a bit cryptic, but if you’ve     │
#:│ ever wondered how a function can return another function, here’s an example!                  │
#:│ Thereafter is lookup, a function that, given a symbol (e.g., NFLX), returns a stock quote for │
#:│ a company in the form of a dict with three keys: name, whose value is a str; price, whose     │
#:│ value isa float; and symbol, whose value is a str, a canonicalized (uppercase) version of a   │
#:│ stock’s symbol, irrespective of how that symbol was capitalized when passed into lookup. Note │
#:│ that these are not “real-time” prices but do change over time, just like in the real world!   │
#:│                                                                                               │
#:│ Last in the file is usd, a short function that simply formats a float as USD (e.g., 1234.56   │
#:│ is formatted as $1,234.56).                                                                   │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ requirements.txt:                                                                             │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Next take a quick look at requirements.txt. That file simply prescribes the packages on which │
#:│ this app will depend.                                                                         │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ static/:                                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Glance too at static/, inside of which is styles.css. That’s where some initial CSS lives.    │
#:│ You’re welcome to alter it as you see fit.                                                    │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘



#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ templates/:                                                                                   │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Now look in templates/. In login.html is, essentially, just an HTML form, stylized with       │
#:│ Bootstrap. In apology.html, meanwhile, is a template for an apology. Recall that apology in   │
#:│ helpers.py took two arguments: message, which was passed to render_template as the value of   │
#:│ bottom, and, optionally, code, which was passed to render_template as the value of top.       │
#:│                                                                                               │
#:│ Notice in apology.html how those values are ultimately used! And here’s why 0:-)              │
#:│                                                                                               │
#:│ Last up is layout.html. It’s a bit bigger than usual, but that’s mostly because it comes with │
#:│ a fancy, mobile-friendly “navbar” (navigation bar), also based on Bootstrap. Notice how it    │
#:│ defines a block, main, inside of which templates (including apology.html and login.html)      │
#:│ shall go. It also includes support for Flask’s message flashing so that you can relay         │
#:│ messages from one route to another for the user to see.                                       │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification - register:                                                                     │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Complete the implementation of register in such a way that it allows a user to register for   │
#:│ an account via a form.                                                                        │
#:│                                                                                               │
#:│ 1.- Require that a user input a username, implemented as a text field whose name is username  │
#:│     Render an apology if the user’s input is blank or the username already exists.            │
#:│                                                                                               │
#:│   1.1.- Note that cs50.SQL.execute will raise a ValueError exception if you try to INSERT a   │
#:│         duplicate username because we have created a UNIQUE INDEX on users.username. Be sure, │
#:│         then, to use try and except to determine if the username already exists.              │
#:│                                                                                               │
#:│ 2.- Require that a user input a password, implemented as a text field whose name is password, │
#:│     and then that same password again, implemented as a text field whose name is confirmation.│
#:│     Render an apology if either input is blank or the passwords do not match.                 │
#:│                                                                                               │
#:│ 3.- Submit the user’s input via POST to /register.                                            │
#:│                                                                                               │
#:│ 4.- INSERT the new user into users, storing a hash of the user’s password, not the password   │
#:│     itself. Hash the user’s password with generate_password_hash Odds are you’ll want to      │
#:│     create a new template (e.g., register.html) that’s quite similar to login.html.           │
#:│                                                                                               │
#:│ Once you’ve implemented register correctly, you should be able to register for an account and │
#:│ log in (since login and logout already work)! And you should be able to see your rows via     │
#:│ phpLiteAdmin or sqlite3.                                                                      │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification - quote:                                                                        │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Complete the implementation of quote in such a way that it allows a user to look up a stock’s │
#:│ current price.                                                                                │
#:│                                                                                               │
#:│ 1.- Require that a user input a stock’s symbol, implemented as a text field whose name is     │
#:│     symbol.                                                                                   │
#:│                                                                                               │
#:│ 2.- Submit the user’s input via POST to /quote.                                               │
#:│                                                                                               │
#:│ 3.- Odds are you’ll want to create two new templates (e.g., quote.html and quoted.html). When │
#:│     a user visits /quote via GET, render one of those templates, inside of which should be an │
#:│     HTML form that submits to /quote via POST. In response to a POST, quote can render that   │
#:│     second template, embedding within it one or more values from lookup.                      │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification - buy:                                                                          │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Complete the implementation of buy in such a way that it enables a user to buy stocks.        │
#:│                                                                                               │
#:│ 1.- Require that a user input a stock’s symbol, implemented as a text field whose name is     │
#:│     symbol. Render an apology if the input is blank or the symbol does not exist (as per the  │
#:│     return value of lookup).                                                                  │
#:│                                                                                               │
#:│ 2.- Require that a user input a number of shares, implemented as a text field whose name is   │
#:│     shares. Render an apology if the input is not a positive integer.                         │
#:│                                                                                               │
#:│ 3.- Submit the user’s input via POST to /buy.                                                 │
#:│                                                                                               │
#:│ 4.- Upon completion, redirect the user to the home page.                                      │
#:│                                                                                               │
#:│ 5.- Odds are you’ll want to call lookup to look up a stock’s current price.                   │
#:│                                                                                               │
#:│ 6.- Odds are you’ll want to SELECT how much cash the user currently has in users.             │
#:│                                                                                               │
#:│ 7.- Add one or more new tables to finance.db via which to keep track of the purchase. Store   │
#:│     enough information so that you know who bought what at what price and when.               │
#:│                                                                                               │
#:│   7.1.- Use appropriate SQLite types.                                                         │
#:│                                                                                               │
#:│   7.2.- Define UNIQUE indexes on any fields that should be unique.                            │
#:│                                                                                               │
#:│   7.3.- Define (non-UNIQUE) indexes on any fields via which you will search (as via SELECT    │
#:│         with WHERE).                                                                          │
#:│                                                                                               │
#:│ 8.- Render an apology, without completing a purchase, if the user cannot afford the number    │
#:│     of shares at the current price.                                                           │
#:│                                                                                               │
#:│ 9.- You don’t need to worry about race conditions (or use transactions).                      │
#:│                                                                                               │
#:│ Once you’ve implemented buy correctly, you should be able to see users’ purchases in your new │
#:│ table(s) via phpLiteAdmin or sqlite3.                                                         │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification - index:                                                                        │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Complete the implementation of index in such a way that it displays an HTML table summarizing,│
#:│ for the user currently logged in, which stocks the user owns, the numbers of shares owned,    │
#:│ the current price of each stock, and the total value of each holding (i.e., shares times      │
#:│ price).                                                                                       │
#:│                                                                                               │
#:│ Also display the user’s current cash balance along with a grand total (i.e., stocks’ total    │
#:│ value plus cash).                                                                             │
#:│                                                                                               │
#:│ 1.- Odds are you’ll want to execute multiple SELECTs. Depending on how you implement your     │
#:│     table(s), you might find GROUP BY HAVING SUM and/or WHERE of interest.                    │
#:│                                                                                               │
#:│ 2.- Odds are you’ll want to call lookup for each stock.                                       │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification -  history:                                                                     │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Complete the implementation of history in such a way that it displays an HTML table           │
#:│ summarizing all of a user’s transactions ever, listing row by row each and every buy and      │
#:│ every sell.                                                                                   │
#:│                                                                                               │
#:│ 1.- Complete the implementation of history in such a way that it displays an HTML table       │
#:│     summarizing all of a user’s transactions ever, listing row by row each and every buy and  │
#:│     every sell.                                                                               │
#:│                                                                                               │
#:│ 2.- You might need to alter the table you created for buy or supplement it with an additional │
#:│     table. Try to minimize redundancies.                                                      │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Specification - personal touch:                                                               │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ Implement at least one personal touch of your choice:                                         │
#:│                                                                                               │
#:│ 1.- Allow users to change their passwords.                                                    │
#:│                                                                                               │
#:│ 2.- Allow users to add additional cash to their account.                                      │
#:│                                                                                               │
#:│ 3.- Allow users to buy more shares or sell shares of stocks they already own via index        │
#:│     itself, without having to type stocks’ symbols manually.                                  │
#:│ 4.- Implement some other feature of comparable scope.                                         │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Things to know:                                                                               │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ 1.- Downloading a new "helpers.py" file as instructed by the problem instructions:            │
#:│                                                                                               │
#:│   1.1.- While the instructions mentioned to download a new helpers.py file, the command       │
#:│         provided did not download any file                                                    │
#:│                                                                                               │
#:│   1.2.- I went directly to the site and opened the file in the browser.  Compared that file   │
#:│         with the originally downloaded file and there were no differences.                    │
#:│                                                                                               │
#:│ 2.- There are no users defined in the database                                                │
#:│                                                                                               │
#:│ 3.- Initial execution of flask resulted in a site that ran and prompted for a user to log in  │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Walkthrough:                                                                                  │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ 1.- Looks like the register and signin routines are already implemented.                      │
#:│                                                                                               │
#:│ 2.- We will need to create tables                                                             │
#:│                                                                                               │
#:│ 3.- I am going to implement one part of the walkthrough at a time                             │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Implementation:                                                                               │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│ 1.- Register users                                                                            │
#:│                                                                                               │
#:│   1.1.- Need to accept access modes "GET" and "POST".  If using "GET", display the            │
#:│         registration form                                                                     │
#:│                                                                                               │
#:│   1.2.- When the user submits using post, check for possible errors in the form.  Such as     │
#:│         missing user ids                                                                      │
#:│                                                                                               │
#:│   1.3.- Create a new template borrowing from login.html                                       │
#:│                                                                                               │
#:│     1.3.1.- Make sure user has fields to enter ID and password and that they can reenter the  │
#:│             password.                                                                         │
#:│                                                                                               │
#:│ 2.- Quote                                                                                     │
#:│                                                                                               │
#:│   2.1.- When using get, present an input field so that the user can enter a symbol            │
#:│                                                                                               │
#:│   2.2.- If post, use the lookup function to get the value of the stock                        │
#:│                                                                                               │
#:│   2.3.- The lookup function, if successful, returns back a dictionary containing values for   │
#:│         the stock.  If not successful, it returns none                                        │
#:│                                                                                               │
#:│ 3.- Buy                                                                                       │
#:│                                                                                               │
#:│   3.1.- Get is used to get the stock that the user wants to buy and post is used to display   │
#:│         the purchased stock if there was enough funds.  If not enough funds display an        │
#:│         apology to the user.  The GET method also needs to check if the symbol is valid       │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters['usd'] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL('sqlite:///finance.db')


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = 0
    response.headers['Pragma'] = 'no-cache'
    return response


@app.route('/', methods=['GET'])
@login_required
def index():
    """Show portfolio of stocks"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Name: "index"                                                                             │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Purpose:  There is only GET method                                                        │
    #:│   1.- Build an HTML table.  Using Jinja loops                                             │
    #:│     1.1.- Headers are "Symbol", "Shares", "Price", "TOTAL"                                │
    #:│     1.2.- Under "Symbol" display all the stocks owned by the user                         │
    #:│     1.3.- Under "Shares" display the number of shares for each stock                      │
    #:│     1.4.- Under "Price" display the "current" value of each stock.  Not the purchase price│
    #:│   2.- After the table, and new line that will contain                                     │
    #:│     2.1.- Right justified, render the total cash available in dollars                     │
    #:│     2.2.- Right justified a label called "Cash" that sits before bullet  2.1              │
    #:│   3.- After bullet 2, add a new line and place two elements                               │
    #:│     3.1.- Right justified, render the total funds available which includes the cash on    │
    #:│           amount plus the current value of all the stock                                  │
    #:│     3.2.- Right justified a label called "TOTAL" right before bullet 3.1                  │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    if request.method != 'GET':
        return apology('Inappropriate page access', 450)

    #: Get the user's cash balance
    cashOnHand = db.execute('SELECT cash FROM users WHERE id = ?',session['user_id'])
    print(type(cashOnHand))
    #: The result from the database is a list of dictionaries.  We need to send a dictionary
    #: to Jinja and not a list.  If we send a list, then Jinja would want to iterate therefore
    #: I am assigning availableFunds the first row of availableFunds returned by the database
    cashOnHand = cashOnHand[0]

    #: Now let's get all the stocks owned by the user
    stocks = db.execute(
        ''' SELECT symbol, sum(numberOfShares) as numberOfShares
              FROM transactions
             WHERE userid = ?
             GROUP BY symbol
            HAVING sum(numberOfShares) > 0''',session['user_id'])
    currentStockValue = 0.0;
    for stock in stocks:
        #< print(f'The current symbol [{stock['symbol']}]')
        currentStockInfo = lookup(stock['symbol'])
        #< print(f'Has a current price of [{currentStockInfo['price']}]')
        currentStockValue = currentStockValue + (currentStockInfo['price'] * stock['numberOfShares'])
        stock['currentValue'] = currentStockInfo['price']
    #<print(f'The total of all stocks current value is [{currentStockValue}]')

    #: Total funds is the sum of cashOnHand plus the current value of stocks
    totalFunds = cashOnHand['cash'] + currentStockValue

    return render_template('portfolio.html',cashOnHand=cashOnHand, stockValue=totalFunds, stocks=stocks)



@app.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
    """Buy shares of stock"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Name: "buy"                                                                               │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Purpose:                                                                                  │
    #:│   1.- GET - HTML                                                                          │
    #:│     1.1.- Page should be buy.html                                                         │
    #:│     1.2.- Contains one field called "symbol" which is a text field.                       │
    #:│     1.3.- Contains one field called "shares" which is a text field                        │
    #:│     1.4.- Submit via post to /buy                                                         │
    #:│   2.- GET - Python                                                                        │
    #:│     2.1.- Confirm that symbol is a real symbol                                            │
    #:│     2.2.- Confirm that shares is a positive integer                                       │
    #:│     2.3.- Confirm that the user has enough funds to purchased the said amount             │
    #:│     2.4.- Create a new table called Purchases                                             │
    #:│     2.5.- If the user selected a good stock and the number is positive and there are      │
    #:│           enough funds, store the transaction in the database and deduct the money spent  │
    #:│           from the available funds                                                        │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘
    if request.method == 'GET':
        return render_template('buy.html')
    else:
        symbol = request.form.get('symbol')

        #: Check to see that the symbol is a valid stock symbol
        price = lookup(symbol)
        if not price:
            return apology(f'Stock symbol {symbol} does not exists',410)
        quantity = request.form.get('shares')

        #: Check to ensure that the shares amount is an integer and that it is greater than zero
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return apology('Negative amount is invalid',410)
        except:
            return apology('Amount is invalid',410)
        pass

    #: Check to see that there are enough funds
    availableFunds = db.execute('SELECT cash FROM users WHERE id = ?',session['user_id'])
    print(availableFunds)
    print(f'Attempting to purchase [{quantity}] shares of [{symbol}] at a price of [{price['price']}]')
    print(f'Available funds is [{availableFunds[0]['cash']}]')
    if availableFunds[0]['cash'] < (quantity * price['price']):
        return apology('Not enough funds', 420)

    #: Now add the purchase to the database
    try:
        db.execute(
            '''INSERT INTO transactions (userid, symbol, numberOfShares, unitPrice, transactionAmount)
                              VALUES (?,?,?,?,?)''',
            session['user_id'],
            symbol,
            quantity,
            price['price'],
            quantity * price['price'])

        db.execute('UPDATE users SET cash = ? WHERE id = ?', availableFunds[0]['cash'] - (quantity * price['price']),
                                                             session['user_id'])
    except:
        return apology('Unable to save in purchase', 430)

    #: Redirect to index page
    return redirect('/')



@app.route('/history', methods=['GET','POST'])
@login_required
def history():
    """Show history of transactions"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Name: "history"                                                                           │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Purpose:                                                                                  │
    #:│   1.- GET Method will show the history                                                    │
    #:│     1.1.- Use HTML table.  Columns "Symbol", "Shares", "Price", "Transacted"              │
    #:│       1.1.1.- "Symbol" is the stock symbol                                                │
    #:│       1.1.2.- "Shares" is the number of shares in the transaction                         │
    #:│       1.1.3.- "Price" is the price paid, or received, for the shares, at the time of the  │
    #:│               and not the current price of the transaction                                │
    #:│       1.1.4.- "Transacted" is the date that the transaction took place.  Format can be    │
    #:│               "YYYY-MM-DD MHH:MM:SS"                                                      │
    #:│     1.2.- Add a div and a button:                                                         │
    #:│       1.2.1.- Label should be "Add additional funds"                                      │
    #:│       1.2.2.- Thin height                                                                 │
    #:│       1.1.1.- Type should be submit                                                       │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    if request.method != 'GET':
        return apology('Inappropriate page access', 450)

    history = db.execute(
        '''SELECT symbol,
                  numberOfShares,
                  transactionAmount,
                  transactionDate
             FROM transactions
            WHERE userid = ?
         ORDER BY transactionDate ASC''', session['user_id'])
    return render_template('history.html',history=history)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':
        # Ensure username was submitted
        if not request.form.get('username'):
            return apology('must provide username', 403)

        # Ensure password was submitted
        elif not request.form.get('password'):
            return apology('must provide password', 403)

        # Query database for username
        rows = db.execute(
            'SELECT * FROM users WHERE username = ?', request.form.get('username')
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]['hash'], request.form.get('password')
        ):
            return apology('invalid username and/or password', 403)

        # Remember which user has logged in
        session['user_id'] = rows[0]['id']

        # Redirect user to home page
        return redirect('/')

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect('/')


@app.route('/quote', methods=['GET', 'POST'])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'GET':
        return render_template('quote.html')
    else:
        symbol = request.form.get('symbol')
        price = lookup(symbol)
        if not price:
            return apology(f'Stock symbol {symbol} does not exists',410)
        return render_template('quoted.html', price=price)



@app.route('/register', methods=['GET', 'POST'])
def register():
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Name: "register"                                                                          │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Purpose:                                                                                  │
    #:│   1.- Allows users to register to the application                                         │
    #:│   2.- Confirms that the user does not already exist in the database                       │
    #:│   3.- Confirms that the user enters two matching passwords                                │
    #:│   4.- If the user enters all required data elements, it will hash                         │
    #:│       the password and create the new user in the database.                               │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #; If the method is "GET" display the registration page
    if request.method == 'GET':
        return render_template('register.html')

    #; Want to check if it is POST and if it is then check the fields
    #; Ensure that the user entered an ID
    username = request.form.get('username')
    if not username:
        return apology('must provide username', 403)

    #; Ensure password was submitted
    password = request.form.get('password')
    if not password:
        return apology('must enter password', 403)

    #; Ensure password was confirmed
    confirmation = request.form.get('confirmation')
    if not confirmation:
        return apology('must enter password twice', 403)

    #; Check if passwords match
    if password != confirmation:
        return apology('passwords must match', 403)

    #; Now check if the user already exists.
    rows = db.execute(
            'SELECT * FROM users WHERE username = ?', request.form.get('username')
        )
    if len(rows) != 0:
        return apology('User already exists', 403)

    #;Save the userid and password
    phrase = generate_password_hash(password, method='scrypt', salt_length=16)

    try:
        result = db.execute('INSERT INTO users (username, hash) VALUES (?,?)',username,
                                                                              phrase)
        print(f'db.execute - insert new user returned [{result}]')
        rows = db.execute('SELECT * FROM users WHERE username = ?', username)
        if len(rows) == 0:
            return apology('Unable to get the new row from the database', 403)
        session['user_id'] = rows[0]['id']
        print('Session stated and now redirecting to "/"')
        return redirect('/')
    except:
        return apology('Unable to insert into the database', 403)



@app.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    """Sell shares of stock"""
    #+┌───────────────────────────────────────────────────────────────────────────────────────────┐
    #+│ Name: "sell"                                                                              │
    #+├───────────────────────────────────────────────────────────────────────────────────────────┤
    #:│ Purpose:                                                                                  │
    #:│   1.- GET                                                                                 │
    #:│     1.1.- Present the user with the ability to select what stock they want to sell        │
    #:│       1.1.1.- Use dropdown to list all the different stocks the user owns                 │
    #:│     1.2.- Present the user with a field, numeric, where they enter the number of shares   │
    #:│           they want to sell                                                               │
    #:│   2.- POST                                                                                │
    #:│     2.1.- Confirm that that the number of shares entered is less or equal to the number   │
    #:│           of shares the user actually has                                                 │
    #:│     2.2.- If the user has enough shares                                                   │
    #:│       2.2.1.- Get the current price                                                       │
    #:│       2.2.2.- Insert the sell row in the purchases table                                  │
    #:│       2.2.3.- Update the available cash on hand                                           │
    #:│       2.2.4.- Redirect to home                                                            │
    #:│     2.3.- If the user does not have enough shares                                         │
    #:│       2.3.1.- Present an apology to the user                                              │
    #:│                                                                                           │
    #:│ There is an issue with purchases table.  When it was initially set up, I did not account  │
    #:│ for sales when naming the columns.  I am not going to fix that now and will just enter a  │
    #:│ negative number of shares when it is a sale.                                              │
    #:└───────────────────────────────────────────────────────────────────────────────────────────┘

    #: Get the current list of stocks the user has
    if request.method == 'GET':
        symbols = db.execute(
            '''SELECT symbol, sum(numberOfShares) as totalShares
                 FROM transactions
                WHERE userid = ?
             GROUP BY symbol
             HAVING totalShares > 0
             ORDER BY 1 ASC''', session['user_id'])
        return render_template('sell.html', symbols=symbols)

    if request.method == 'POST':
        stockToSell = request.form.get('symbol')
        howMany = request.form.get('numberOfShares')
        if not stockToSell or not howMany:
            return apology('No symbol or number or shares', 450)

        print(f'Attempting to sell [{howMany}] shares for stock[{stockToSell}]')

        #: Do we have enough shares
        canSell = db.execute(
            '''SELECT sum(numberOfShares) as totalShares
                 FROM transactions
                WHERE userid = ?
                  AND symbol = ?
             GROUP BY symbol
             HAVING totalShares > 0
             ORDER BY 1 ASC''', session['user_id'], stockToSell)
        print(f'Can sell [{canSell[0]['totalShares']}] shares for stock[{stockToSell}]')
        if int(howMany) > int(canSell[0]['totalShares']):
            return apology('Selling more shares than in stock', 450)

        #: Get the current value of the symbol being sold
        valuePerShare = lookup(stockToSell)
        totalSale = valuePerShare['price'] * int(howMany)
        print(f'Selling for a total of [{howMany}] [{stockToSell}] shares for a total of [{totalSale}]')

        #: Now update database
        try:
            db.execute(
                '''UPDATE users
                      SET cash = cash + ?
                    WHERE id = ?''',session['user_id'], totalSale
            )
            db.execute(
                '''INSERT INTO transactions (userid, symbol, numberOfShares, unitPrice, transactionAmount)
                              VALUES (?,?,?,?,?)''',
            session['user_id'],
            stockToSell,
            int(howMany) * -1,
            valuePerShare['price'],
            int(howMany) * valuePerShare['price'])
            return redirect('/')
        except:
            return apology('Unable to sell stock', 460)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def addFunds():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        amount = request.form.get('addAmount')
        if not amount:
            return apology('Bad number', 470)
        try:
            amount = float(amount)
            db.execute('UPDATE users SET cash = cash + ? WHERE id = ?',amount, session['user_id'])
            return redirect('/')
        except:
            return apology('Unable to add funds', 470)


