import bcrypt
from flask import Blueprint, request, redirect, render_template, session

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

#login '/sessions/create

#logout '/sessions/destroy'