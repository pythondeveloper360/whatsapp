from flask import Flask, render_template,redirect,session,request,abort
import sql

app = Flask(__name__)
app.secret_key = "hanzala"

@app.route("/")
def index():
    if "login" in session:
        print(session['login'])
        return render_template('index.html',chats = sql.getChats(session['login']))
    else:
        return render_template("login.html")

@app.route('/login',methods= ["POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")
        if sql.authenticateUser(user_id=user_id,password=password):
            session['login'] = user_id
            return redirect("/")
        else:
            print(user_id,password)
            return ''
app.run(debug=True)