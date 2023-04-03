from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
# from flask_sqlalchemy import SQLAlchemy #<-- this is an easier/safer way to do SQL back-end
# from sqlalchemy import exc


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3a'



# bcrypt = Bcrypt(app)

# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 10)

#we need to point flask to our SQLAlchemy database and
#then instantiate it
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)


# connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()

# Creating the User table
# sql_query = """
#     CREATE TABLE IF NOT EXISTS User 
#     (
#         username TEXT PRIMARY KEY, 
#         password TEXT, 
#         role TEXT
#     )
# """

#Creating prompts table
sql_query = """
    CREATE TABLE IF NOT EXISTS Prompts
    (
        title TEXT PRIMARY KEY,
        category TEXT,
        explanation TEXT
    )
"""

# class Prompts(db.Model):
#     __tablename__ = 'Prompts'
#     title = db.Column(db.String(50), primary_key=True)
#     text = db.Column(db.String(100), primary_key=True)

# with app.app_context():
#     db.create_all()

cur.execute(sql_query)
# sql_query = """INSERT INTO Prompts VALUES
#     ('Spot', 'mind', 'Look outside and try to spot an object of every colour of the rainbow'),
#     ('Jump', 'move', 'Do 15 jumping jacks'),
#     ('Calm', 'mind', 'Take 10 deep breaths'),
#     ('Reflect', 'mind', 'What is something you are grateful for today?');
    
# """
# cur.execute(sql_query)
# con.commit()
# cur.close()


@app.route('/query', methods=['POST'])
def handle_query():
    query = request.json['query'] # extract the SQL query from the AJAX request
    print("here" + query)
    con = sqlite3.connect('database.db') # connect to the SQLite database
    cursor = con.cursor()
    cursor.execute(query) # execute the SQL query
    results = cursor.fetchall() # retrieve the query results
    con.close()
    return jsonify(results)


@app.route("/", methods=['POST', 'GET'])
def home():
    
    # if(request.method == 'GET'):
    #     try:
    #         sql_query="""
    #             SELECT * FROM table_name
    #             ORDER BY RAND()
    #             LIMIT 1;
    #         """
    #         con = sqlite3.connect("database.db")
    #         cur = con.cursor()
    #         cur.execute(sql_query)
    #         con.commit()
    #         cur.close()
    #     except sqlite3.IntegrityError:
    #         #if we're in here, then not able to select a random query
    #         return render_template("home.html")

   
    return render_template("home.html")


# @app.route("/signup", methods=['GET', 'POST'])
# def register():
#     if(request.method == "POST"):
#         print("testing")

#         username = request.form['username']
#         password = request.form['password']
#         role = request.form['role']

#         try:
#             sql_query = "INSERT INTO User VALUES ('"
#             sql_query += username + "', '" + password + "', '" + role + "')"
#             con = sqlite3.connect("database.db")
#             cur = con.cursor()
#             cur.execute(sql_query)
#             con.commit()  # commit the results
#             print("sql query:" + sql_query)
#             flash("User successfully created")
#             cur.close()
#             return redirect(url_for('login'))
#         except sqlite3.IntegrityError:
#             flash("User already exists, please enter a different username")
#             return render_template("signup.html")
#     else:
#         return render_template('signup.html')


@app.route("/add.html", methods=['POST', 'GET'])
def add():
    return render_template('add.html');
# @app.route("/", methods=['GET', 'POST'])
# def login():
#     if(request.method == "POST"):
#         username = request.form['username']
#         password = request.form['password']
#         # role = request.form['role']

#         sql_query = "SELECT username, password, role FROM User WHERE "
#         sql_query += "username = '" + username + "' "
#         con = sqlite3.connect("database.db")
#         cur = con.cursor()
#         rows = cur.execute(sql_query).fetchall()
#         cur.close()
#         print("sql query:" + str(rows))
#         if(len(rows) == 0):
#             flash("This username is not recognized. Please try again.")
#             return render_template('login.html')
#         elif(password != rows[0][1]):
#             flash("Wrong password, please try again")
#             return render_template('login.html')
#         else:
#             print("here")
#             if(rows[0][0] == "admin"):
#                 return render_template('admin.html')
#             else:
#                 return render_template('user.html')
#     else:
#         return render_template('login.html')


app.run(host='0.0.0.1', port=81, debug=True)