from flask import Flask, render_template, redirect
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
# DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")

SECRET_KEY = os.environ.get("SECRET_KEY", "password")

from controllers.cheerup_controller import cheerup_controller
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return redirect('home')


app.register_blueprint(cheerup_controller)
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
