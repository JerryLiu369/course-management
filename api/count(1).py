@app.route('/calculate-credits', methods=['POST'])
@login_required
def calculate_credits():
    data = request.get_json()
     # 读入专业，所选模块，以及选中模块内的课程
    major = data['major']
    module = data['module']
    selected_categories = data['categories']  # 类别列表，可能有多个列表
    selected_courses = data['courses']  # 课程列表，可能有多个课程


    base_query = (db.session.query(Course.Cname, Course.Ccredit)
                  .join(MC, Course.Cname == MC.Cname)
                  .join(Major, MC.Mname == Major.Mname)
                  .filter(MC.MCcategory.in_(selected_categories))
                  .filter(Major.Mname == major)
                  .filter(MC.MCmodules == module)
                  )

    # 过滤出选择的课程
    base_query = base_query.filter(Course.Cname.in_(selected_courses))

    # 执行查询，获取课程和对应的学分
    course_credits = base_query.all()

    # 计算学分总和
    total_credits = sum(credit for _, credit in course_credits)

    return total_credits
