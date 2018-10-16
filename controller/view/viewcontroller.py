from flask import Blueprint,render_template,request
view = Blueprint('view', __name__)
routers = {'Home': '/?viewid=index.html', 'Admin': '/?viewid=admin.html'}
@view.route('/')
def home():
  viewid = request.args.get('viewid', 'index.html', type=str)
  return render_template(viewid,result = routers)

