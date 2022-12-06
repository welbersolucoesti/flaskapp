from flask import Flask
from app.controllers import routers

app = Flask(
    __name__,
    static_url_path='/assets',
    static_folder='../www',
    template_folder='views'
)

routers(app)