from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/admin_home',methods=['get','post'])
def admin_home():
	data={}
	q="select * from reg"
	res=select(q)
	data['register']=res
	
	return render_template('admin_home.html',data=data)