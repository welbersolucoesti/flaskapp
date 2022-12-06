from app.controllers.home import controller as home
from app.controllers.associates import controller as associates
from app.controllers.users import controller as users

def routers(app):
    home(app)
    associates(app)
    users(app)