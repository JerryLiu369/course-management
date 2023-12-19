import os
import secrets
import string
from excel_gen import gen_excel

from flask import Flask, render_template, flash, redirect, url_for, request, jsonify,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required
import pymysql
import os


def generate_secure_string(length):
	letters = string.ascii_letters + string.digits
	return ''.join(secrets.choice(letters) for _ in range(length))


app = Flask(__name__)
app.secret_key = generate_secure_string(30)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'litera'
with open(f"{os.path.dirname(os.path.abspath(__file__))}/.env", "r") as f:
	app.config['SQLALCHEMY_DATABASE_URI'], HOST, USER, PASSWORD, DB = f.read().strip("\n").split("\n")
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)


@login_manager.user_loader
def load_user(user_id):
	return db.session.get(User, int(user_id))


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])
	submit = SubmitField('Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			return redirect(url_for("index"))
		else:
			flash("用户名或密码错误！")
			return redirect(url_for("login"))
	return render_template('login.html', form=form)


@app.template_filter()
def process_semester(semester_binary):
	# 将字节类型转换为二进制字符串
	bin_str = ''.join(f'{byte:08b}' for byte in semester_binary)
	# semesters 是一个布尔值列表，表示每个学期是否开课
	semesters = [bool(int(bit)) for bit in bin_str]
	semester_string = ""
	for i, offer in enumerate(semesters):
		if offer:
			semester_string += str(i + 1) + ','
	return semester_string[:-1]


class Major(db.Model):
	__tablename__ = 'Major'
	Mid = db.Column('Mid', db.String(4), doc='专业ID')
	Mname = db.Column('Mname', db.String(40), primary_key=True, doc='专业名')
	Mcollege = db.Column('Mcollege', db.String(20), doc='所属学院')
	follows = db.relationship('MC', primaryjoin='Major.Mname==foreign(MC.Mname)')


class Course(db.Model):
	__tablename__ = 'Course'
	Cname = db.Column('Cname', db.String(40), primary_key=True, doc='课程名')
	Cid = db.Column('Cid', db.String(15), doc='课程ID')
	Ccredit = db.Column('Ccredit', db.SmallInteger, doc='课程学分')
	Csemester = db.Column('Csemester', db.BINARY(1), doc='开课学期')
	follows = db.relationship('MC', primaryjoin='Course.Cname==foreign(MC.Cname)')


class MC(db.Model):
	__tablename__ = 'MC'
	Mname = db.Column('Mname', db.String(40), db.ForeignKey('Major.Mname'), primary_key=True, index=True, doc='专业名')
	Cname = db.Column('Cname', db.String(40), db.ForeignKey('Course.Cname'), primary_key=True, index=True, doc='课程名')
	MCcategory = db.Column('Mccategory', db.String(20), doc='课程类别')
	MCmodules = db.Column('MCmodules', db.String(20), doc='课程模块', nullable=True)


ALLMODULES = []

MAJORS = ["计算机科学与技术", "信息管理与信息系统", "信息安全", "软件工程", "数据科学与大数据技术（工学）"]

app.course_list = []


def update_all_modules():
	mysql_config = {
		'host': HOST,
		'user': USER,
		'password': PASSWORD,
		'db': DB,
		'cursorclass': pymysql.cursors.DictCursor
	}


	try:
		# 创建 MySQL 连接
		conn = pymysql.connect(**mysql_config)
		cursor = conn.cursor()

		# 查询 MC 表数据
		query = """
				SELECT MCcategory, GROUP_CONCAT(DISTINCT MCmodules) AS MCmodules
				FROM MC
				GROUP BY MCcategory;
			"""

		cursor.execute(query)
		result = cursor.fetchall()

		# 将结果转换为字典格式
		data = [{'name': '通识模块', 'categories': []}, {'name': '专业模块', 'categories': []}]

		# 将特定的 MCcategory 值映射到专业模块或通识模块中
		for item in result:
			module = {'name': item['MCcategory'], 'modules': item['MCmodules'].split(',') if item['MCmodules'] else []}

			if item['MCcategory'] in ['部类核心课', '专业核心课', '个性化选修']:
				data[1]['categories'].append(module)
			else:
				data[0]['categories'].append(module)

		return data

	except Exception as e:
		print(f"Error: {e}")
		return None

	finally:
		# 关闭连接
		cursor.close()
		conn.close()



@app.route('/')
@login_required
def index():
	global ALLMODULES
	ALLMODULES=update_all_modules()
	return redirect(url_for('general'))


@app.route('/general')
@login_required
def general():
	global ALLMODULES
	ALLMODULES=update_all_modules()
	return render_template('general.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)


@app.route('/major')
@login_required
def major():
	return render_template('major.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)


@app.route('/calculate')
@login_required
def calculate():
	return render_template('calculate.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)


@app.route('/add')
@login_required
def add():
	return render_template('add.html')


@app.route('/minus')
@login_required
def minus():
	return render_template('minus.html')


@app.route('/download')
@login_required
def download():
	return render_template('download.html',majors=MAJORS)

@app.route('/download/<major>')
@login_required
def download_major():
	filepath=gen_excel(major)
	return send_file(filepath, as_attachment=True)

@app.route('/process-selection', methods=['POST'])
@login_required
def process_selection():
	data = request.get_json()
	major_input = data['major']
	category = data['category']
	module = data['module']
	base_query = (db.session.query(Course.Cname, Course.Cid, Course.Ccredit, Course.Csemester, MC.MCmodules)
	              .join(MC, Course.Cname == MC.Cname)
	              .join(Major, MC.Mname == Major.Mname)
	              .filter(MC.MCcategory == category)
	              .distinct()
	              )
	# 动态添加过滤条件
	if major_input:
		base_query = base_query.filter(Major.Mname == major_input)
	if module:
		base_query = base_query.filter(MC.MCmodules == module)
	# 执行查询
	app.course_list = base_query.all()
	return "success"


@app.route('/calculate-credits', methods=['POST'])
@login_required
def calculate_credits():
	data = request.get_json()
	# 读入专业，所选模块，以及选中模块内的课程
	major = data['major']
	module = data['module']
	category = data['category']  # 类别列表，可能有多个列表
	selected_courses = data['courses']  # 课程列表，可能有多个课程

	base_query = (db.session.query(Course.Cname, Course.Ccredit)
	              .join(MC, Course.Cname == MC.Cname)
	              .join(Major, MC.Mname == Major.Mname)
	              .filter(MC.MCcategory == category)
	              .filter(Major.Mname == major)
	              .filter(MC.MCmodules == module)
	              .distinct()
	              )

	# 过滤出选择的课程
	base_query = base_query.filter(Course.Cname.in_(selected_courses))

	# 执行查询，获取课程和对应的学分
	course_credits = base_query.all()

	# 计算学分总和
	total_credits = sum(credit for _, credit in course_credits)

	return str(total_credits)


def insert_course_data(major_name, course_name, course_id, category, credit, modules):
	connection = pymysql.connect(
		host=HOST,
		user=USER,
		password=PASSWORD,
		db=DB,
		charset='utf8mb4',
		cursorclass=pymysql.cursors.DictCursor
	)

	try:
		with connection.cursor() as cursor:
			# 尝试插入 Course 表
			course_sql = "INSERT INTO Course (Cname, Cid, Ccredit) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE Cid=Cid;"
			cursor.execute(course_sql, (course_name, course_id, credit))

			# 尝试插入 MC 表
			if major_name:
				# 如果专业名称不为空，只插入一条记录
				mc_sql = "INSERT INTO MC (Mname, Cname, MCcategory, MCmodules) VALUES (%s, %s, %s, %s);"
				cursor.execute(mc_sql, (major_name, course_name, category, modules))
			else:
				# 如果专业名称为空，为每个专业插入相同的记录
				get_majors_sql = "SELECT Mname FROM Major;"
				cursor.execute(get_majors_sql)
				majors = cursor.fetchall()

				mc_sql = "INSERT INTO MC (Mname, Cname, MCcategory, MCmodules) VALUES (%s, %s, %s, %s);"
				for major in majors:
					cursor.execute(mc_sql, (major['Mname'], course_name, category, modules))

			connection.commit()
	except pymysql.Error as e:
		error_message = f"Error: {e}"
		return jsonify({'status': 'error', 'message': error_message})
	finally:
		connection.close()

	flash("增加已完成")

	return jsonify({'status': 'success', 'message': 'Data inserted successfully'})


@app.route('/insert_data', methods=['POST'])
def insert_data():
	data = request.get_json()
	major_name = data.get('Mname', None)
	course_name = data.get('Cname', None)
	course_id = data.get('Cid', None)
	category = data.get('MCcategory', None)
	credit = data.get('Ccredit', None)
	modules = data.get('MCmodules', None)

	if not (course_name and course_id and category and credit and modules):
		return jsonify({'status': 'error', 'message': 'Missing required data'})

	return insert_course_data(major_name, course_name, course_id, category, credit, modules)


def delete_course_data(major_name, course_name, course_id, category, credit, modules):
	connection = pymysql.connect(
		host=HOST,
		user=USER,
		password=PASSWORD,
		db=DB,
		charset='utf8mb4',
		cursorclass=pymysql.cursors.DictCursor
	)

	try:
		with connection.cursor() as cursor:
			# 删除 MC 表中的记录
			if major_name:
				mc_sql = "DELETE FROM MC WHERE Mname=%s AND Cname=%s AND MCcategory=%s AND MCmodules=%s;"
				cursor.execute(mc_sql, (major_name, course_name, category, modules))
			else:
				get_majors_sql = "SELECT Mname FROM Major;"
				cursor.execute(get_majors_sql)
				majors = cursor.fetchall()

				mc_sql = "DELETE FROM MC WHERE Mname=%s AND Cname=%s AND MCcategory=%s AND MCmodules=%s;"
				for major in majors:
					cursor.execute(mc_sql, (major['Mname'], course_name, category, modules))

			# 删除 Course 表中的记录
			course_sql = "DELETE FROM Course WHERE Cname=%s AND Cid=%s AND Ccredit=%s;"
			cursor.execute(course_sql, (course_name, course_id, credit))

			connection.commit()
	except pymysql.Error as e:
		error_message = f"Error: {e}"
		return jsonify({'status': 'error', 'message': error_message})
	finally:
		connection.close()

	flash("删除已完成")

	return jsonify({'status': 'success', 'message': 'Data deleted successfully'})


@app.route('/delete_data', methods=['POST'])
def delete_data():
	data = request.get_json()
	major_name = data.get('Mname', None)
	course_name = data.get('Cname', None)
	course_id = data.get('Cid', None)
	category = data.get('MCcategory', None)
	credit = data.get('Ccredit', None)
	modules = data.get('MCmodules', None)

	if not (course_name and course_id and category and credit and modules):
		return jsonify({'status': 'error', 'message': 'Missing required data'})

	return delete_course_data(major_name, course_name, course_id, category, credit, modules)


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True, host="0.0.0.0")
