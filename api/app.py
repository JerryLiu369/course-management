import os
import secrets
import string


def generate_secure_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(letters) for _ in range(length))


from flask import Flask, render_template, flash, redirect, url_for, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = generate_secure_string(30)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'litera'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'SQLALCHEMY_DATABASE_URI',
    'sqlite:///db.db'
)
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


ALLMODULES = [
    {'name': '通识模块',
     'categories': [
         {'name': '专业实习', 'modules': []},
         {'name': '专业核心课', 'modules': []},
         {'name': '公共体育', 'modules': ['专项基础课', '核心基础课']},
         {'name': '公共外语',
          'modules': ['实验班', '实验班第二外语', '拓展类课程', '普通班A级', '普通班B级', '英语演讲']},
         {'name': '军事课', 'modules': []},
         {'name': '劳动教育', 'modules': []},
         {'name': '志愿服务', 'modules': []},
         {'name': '思想政治理论课', 'modules': ['必修模块', '选修模块']},
         {'name': '毕业论文（设计）', 'modules': []},
         {'name': '研究训练', 'modules': []},
         {'name': '职业生涯规划', 'modules': []},
         {'name': '通识课程群', 'modules': ['公共艺术教育', '心理健康教育选修', '新生研讨课']},
     ]
     },
    {'name': '专业模块',
     'categories': [
         {'name': '部类核心课', 'modules': ['部类共同课', '部类基础课']},
         {'name': '个性化选修',
          'modules': ['人工智能', '信息安全应用', '信息安全技术', '信息管理理论基础', '信息系统技术基础',
                      '复杂工程实践', '多媒体技术', '大数据技术', '电子商务创新应用', '系统与网络', '计算机理论基础',
                      '计算机类专业实践', '软件工程与系统开发', '金融科技创新应用']}
     ]
     }
]

MAJORS = ["计算机科学与技术", "信息管理与信息系统", "信息安全", "软件工程", "数据科学与大数据技术（工学）"]

app.course_list = []


@app.route('/')
@login_required
def index():
    return redirect(url_for('general'))


@app.route('/general')
@login_required
def general():
    return render_template('general.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)

@app.route('/major')
@login_required
def major():
    return render_template('major.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)

@app.route('/calculate')
@login_required
def calculate():
    return render_template('calculate.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)
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
    result=base_query.all()
    app.course_list = result
    return jsonify(result)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host="0.0.0.0")
