from flask import Blueprint, request, redirect, render_template, session
import bcrypt

user_controller = Blueprint("user_controller", __name__, template_folder="../templates/user")

#signup /signup