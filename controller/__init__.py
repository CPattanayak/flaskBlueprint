from flask import Flask
from controller.main.controllers import main
from controller.admin.controllers import admin
from controller.view.viewcontroller import view

app = Flask(__name__,static_folder = './view/static',template_folder='./view/templates')


app.register_blueprint(view, url_prefix='/')
app.register_blueprint(main, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/api/admin')