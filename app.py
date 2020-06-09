from flask import Flask
import sqlite3
app = Flask(__name__)

sqliteConnection = sqlite3.connect('d:/html_pro/heart_disease_prediction.db')

from flask import render_template
 
@app.route('/m')
def signUp():
    return render_template('m_page.html')
def connectDb():
    try:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        return cursor
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

@app.route('/login')
def login(username, password):
    try:
        cursor = connectDb()
        sqlite_select_query = """SELECT * from users where username = ? and password = ?"""
        cursor.execute(sqlite_select_query, (username,password))
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row)
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

login("tanzeela", "10zilla")