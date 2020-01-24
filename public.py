from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def index():
	if 'submit' in request.form:
		u_name=request.form['c_name']
		u_collegename=request.form['c_school']
		u_number=request.form['c_mobile']
		u_email=request.form['c_email']

		q="insert into reg values(null,'%s','%s','%s','%s',curdate())"%(u_name,u_collegename,u_number,u_email)
		insert(q)

	return render_template('index.html')
@public.route('/login_form',methods=['get','post'])
def login_form():
	data={}

	if 'submit' in request.form:
		username=request.form['user_name']
		password=request.form['pass_word']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			if res[0]['l_type']=="admin":
				return redirect(url_for('admin.admin_home'))

	return render_template('login_form.html',data=data)