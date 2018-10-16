from flask import Blueprint,jsonify,request
from db import customerCollection
admin = Blueprint('admin', __name__)
@admin.route("/orders", methods=['POST'])
def orderlist():
    returnList = []
    page_size=request.form.get('rowCount', 10, type=int)
    page_num=request.form.get('current', 1, type=int)
    skips = page_size * (page_num - 1)
    totalcount=customerCollection.count()
    for customer in customerCollection.find().skip(skips).limit(page_size):
        returnList.append({'name':customer['name'],'phone':customer['phone'],'quantity':customer['quantity']})
    return jsonify ({'current':page_num,
                     'rowCount': page_size,
                     'rows':returnList,'total':totalcount})


@admin.route("/deleteorder", methods=['DELETE'])
def deleteOrder():
    phone=request.form.get('phone',0,type=int)
    deletemap = {'phone': phone}
    x=customerCollection.delete_many(deletemap)
    print(x.deleted_count, " documents deleted.")
    return jsonify({'result': 'Success'})