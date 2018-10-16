from flask import Blueprint,render_template,jsonify,request
from db import customerCollection

main = Blueprint('main', __name__)
@main.route("/order")
def evaluateorder():
    name = request.args.get('name', '', type=str)
    phone = request.args.get('phone', 0, type=int)
    quantity = request.args.get('quantity', 0, type=int)
    customerCollection.insert_one({'name':name,'phone':phone,'quantity':quantity})
    return jsonify ({'result':'Success'})