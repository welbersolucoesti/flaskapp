from flask import render_template
from app.models import users as model

def controller(app):

    @app.route("/usuarios")
    def users_list():
        return render_template('users/list.html', data=model.get_all())

    @app.route("/usuario/<id>")
    def users_item(id):
        return render_template('users/item.html', data=model.get(id))