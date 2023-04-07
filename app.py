from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3a'


# connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()

#Creating prompts table
sql_query = """
    CREATE TABLE IF NOT EXISTS Prompts
    (
        title TEXT PRIMARY KEY,
        category TEXT,
        explanation TEXT
    )
"""
cur.execute(sql_query)

############
# Execute this when creating a new database 
############

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
    #print("here" + query)
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

@app.route("/add.html", methods=['POST', 'GET'])
def add():
    if(request.method == "POST"):
        print("testing")

        title = request.form['title']
        category = request.form['category']
        explanation = request.form['explanation']

        try:
            sql_query = "INSERT INTO Prompts VALUES ('"
            sql_query += title + "', '" + category + "', '" + explanation + "')"
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute(sql_query)
            con.commit()  # commit the results
            print("sql query:" + sql_query)
            cur.close()
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            flash("Prompt already exists, please enter a different prompt")
            return render_template(url_for("add"))

    return render_template(url_for('add'))


app.run(host='0.0.0.1', port=81, debug=True)