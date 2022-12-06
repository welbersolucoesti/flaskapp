from flask import render_template, jsonify
from app.models import associates as associates_model
from app.models import users as users_model

def controller(app):

    @app.route("/")
    def home():
        return render_template('home.html')
    
    @app.route("/homedata")
    def homedata():
        return jsonify(
            total_associados=associates_model.count()[0],
            total_usuarios=users_model.count()[0]
        )