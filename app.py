from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3a'


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

# cur.execute(sql_query)
# # sql_query = "INSERT INTO User Values('admin', 'admin','Admin')"
# # cur.execute(sql_query)
# print("hello" + sql_query)
# cur.close()


@app.route("/")
def home():
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