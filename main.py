from flask import Flask, render_template, request, redirect, url_for
from comms.ldap_login import LDAP
from comms.sql_login import SQL
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os
if os.path.exists(".env"):
    load_dotenv()
from ldap3 import Server, Connection, SAFE_SYNC




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secKey'
Bootstrap(app)
ldap = LDAP()
sql = SQL()
use_ldap = True if os.environ.get("USE_LDAP") == "1" else False


@app.route('/login', methods=["POST"])
def login():
    
    
    logged_in_user = ldap.log_in(request.form["username"], request.form["password"]) if use_ldap else sql.login(request.form["username"], request.form["password"])
    if logged_in_user is None:
        return render_template("index.html", bad_login=True), 401
    return render_template("user_page.html", username=logged_in_user)


@app.route('/', methods=["GET", "POST"])
def landing_page():
    return render_template("index.html")

app.run()