from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = '8c083218c63f3a2b0f6b095295dddba0'  # 设置一个安全密钥
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'litera'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test_mysql:test2023MYSQL@rm-cn-9lb3i9qvj001pbjo.rwlb.rds.aliyuncs.com/test_mysql'
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
    return db.session.get(User,int(user_id))


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
    # semesters 是一个布尔值列表，表示每个学期是否开课
    semesters = [bool(int(bit)) for bit in format(semester_binary, '08b')]
    semester_string = ""
    for i, offer in enumerate(semesters):
        if offer:
            semester_string += str(i + 1) + ','
    return semester_string[:-1]


class Major(db.Model):
    __tablename__ = 'Major'
    Mid = db.Column('Mid', db.String(4), primary_key=True, doc='专业ID')
    Mname = db.Column('Mname', db.String(40), doc='专业名')
    Mcollege = db.Column('Mcollege', db.String(20), doc='所属学院')
    follows = db.relationship('MC', primaryjoin='Major.Mid==foreign(MC.Mid)')


class Course(db.Model):
    __tablename__ = 'Course'
    Cname = db.Column('Cname', db.String(40), doc='课程名')
    Cid = db.Column('Cid', db.String(15), primary_key=True, doc='课程ID')
    Ccredit = db.Column('Ccredit', db.SmallInteger, doc='课程学分')
    Csemester = db.Column('Csemester', db.BINARY, doc='开课学期')
    follows = db.relationship('MC', primaryjoin='Course.Cid==foreign(MC.Cid)')


class MC(db.Model):
    __tablename__ = 'MC'
    Mid = db.Column('Mid', db.String(4), db.ForeignKey('Major.Mid'), primary_key=True, index=True, doc='专业ID')
    Cid = db.Column('Cid', db.String(15), db.ForeignKey('Course.Cid'), primary_key=True, index=True, doc='课程ID')
    MCcategory = db.Column('Mccategory', db.String(20), doc='课程类别')
    MCmodules = db.Column('MCmodules', db.String(20), doc='课程模块', nullable=True)


ALLMODULES = [
    {'name': '通识模块',
     'categories': [
         {'name': '思想政治理论课', 'modules': ['必修模块', '选修模块']},
         {'name': '公共外语', 'modules': ['普通班A级', '普通班B级', '实验班', '拓展类课程', '实验班第二外语']},
         {'name': '公共体育', 'modules': ['核心基础课', '专项基础课']},
         {'name': '通识课程群', 'modules': ['新生研讨课', '公共艺术教育', '心理健康教育必修', '心理健康教育选修']}
     ]
     },
    {'name': '专业模块',
     'categories': [
         {'name': '思想政治理论课', 'modules': ['必修模块', '选修模块']},
         {'name': '公共外语', 'modules': ['普通班A级', '普通班B级', '实验班', '拓展类课程', '实验班第二外语']},
         {'name': '公共体育', 'modules': ['核心基础课', '专项基础课']},
         {'name': '通识课程群', 'modules': ['新生研讨课', '公共艺术教育', '心理健康教育必修', '心理健康教育选修']}
     ]
     }
]

MAJORS = ["计算机科学与技术", "信息管理与信息系统", "信息安全", "软件工程", "数据科学与大数据技术（工学）"]

app.course_list = []


@app.route('/')
@login_required
def index():
    return render_template('general.html', majors=MAJORS, allmodules=ALLMODULES, data=app.course_list)


@app.route('/process-selection', methods=['POST'])
@login_required
def process_selection():
    data = request.get_json()
    major = data['major']
    supercategory = data['supercategory']
    category = data['category']
    module = data['module']
    base_query = (db.session.query(Course.Cname, Course.Cid, Course.Ccredit, Course.Csemester, MC.MCmodules)
                  .join(MC, Course.Cid == MC.Cid)
                  .join(Major, MC.Mid == Major.Mid)
                  .filter(MC.MCcategory == category)
                  )
    # 动态添加过滤条件
    if major:
        base_query = base_query.filter(Major.Mname == major)
    if module:
        base_query = base_query.filter(MC.MCmodules == module)
    # 执行查询
    app.course_list = base_query.all()
    return "success"


@app.route('/change_theme')
def bootswatch():
    theme_list = ['cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'litera', 'lumen', 'lux', 'materia',
                  'minty', 'morph', 'pulse', 'quartz', 'sandstone', 'simplex', 'sketchy', 'slate', 'solar', 'spacelab',
                  'superhero', 'united', 'vapor', 'yeti', 'zephyr']
    theme_now = app.config['BOOTSTRAP_BOOTSWATCH_THEME']
    try:
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme_list[theme_list.index(theme_now) + 1]
    except IndexError:
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'cerulean'
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
