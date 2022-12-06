from flask import render_template
from app.models import associates as model

def controller(app):

    @app.route("/associados")
    def associates_list():
        return render_template('associates/list.html', data=model.get_all())

    @app.route("/associado/<cnpj>")
    def associates_item(cnpj):
        return render_template('associates/item.html', data=model.get(cnpj))