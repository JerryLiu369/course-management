
class Major(db.Model):
    Mid = db.Column(db.Integer, primary_key=True)
    Mname = db.Column(db.String(255))
    Mcollege = db.Column(db.String(255))

# 假设你的 Course 表结构如下：
class Course(db.Model):
    Cid = db.Column(db.Integer, primary_key=True)
    Cname = db.Column(db.String(255))
    Ccredit = db.Column(db.Integer)
    Csemester = db.Column(db.String(255))

# 假设你的 MC 表结构如下：
class MC(db.Model):
    Mname = db.Column(db.String(255), primary_key=True)
    Cname = db.Column(db.String(255), primary_key=True)
    MCcategory = db.Column(db.String(255))
    MCmodules = db.Column(db.String(255))


# 新增数据的函数
@login_required
@app.route('/insert-data', methods=['POST'])
def insert_data():
    data = request.get_json()
    table_name = data['table_name']
    new_data = data['new_data']

    # 根据表名动态选择模型类
    model_class = None
    if table_name == 'Major':
        model_class = Major
    elif table_name == 'Course':
        model_class = Course
    elif table_name == 'MC':
        model_class = MC

    if model_class:
        # 创建新数据并添加到数据库
        new_record = model_class(**new_data)
        db.session.add(new_record)
        db.session.commit()
        return "success"
    else:
        return "Invalid table name"
    

def delete_data():
    data = request.get_json()
    table_name = data['table_name']
    # 根据表名动态选择模型类
    model_class = None
    if table_name == 'Major':
        model_class = Major
    elif table_name == 'Course':
        model_class = Course
    elif table_name == 'MC':
        model_class = MC

    if model_class:
        # 获取要删除的记录的主键值
        primary_key_values = data['primary_key_values']

        # 查询要删除的记录
        record_to_delete = model_class.query.filter_by(**primary_key_values).first()

        if record_to_delete:
            # 删除记录并提交事务
            db.session.delete(record_to_delete)
            db.session.commit()
            return "success"
        else:
            return "Record not found"
    else:
        return "Invalid table name"    