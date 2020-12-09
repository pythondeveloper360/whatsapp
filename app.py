from flask import Flask, render_template,redirect,session   
import sql

app = Flask(__name__)

@app.route("/")
def index():
    if "login" in session:
        return render_template('index.html',chats = sql.getChats(session['login']))
    else:
        return render_template("login.html")
app.run(debug=True)