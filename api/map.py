from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)

def get_zhuan_courses(major_name):
    connection = pymysql.connect(
        host='your_database_host',
        user='your_database_user',
        password='your_database_password',
        db='your_database_name',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 查询专业核心课
            sql = f"SELECT Course.Cname, Course.Csemester FROM Course " \
                  f"JOIN MC ON Course.Cname = MC.Cname " \
                  f"JOIN Major ON MC.Mname = Major.Mname " \
                  f"WHERE Major.Mname = '{major_name}' AND MC.MCcategory = '专业核心课';"
            cursor.execute(sql, (major_name,))
            result = cursor.fetchall()

            return result
    finally:
        connection.close()

def map_zhuan(major_name):
    core_courses = get_zhuan_courses(major_name)

    semester_courses = {i: [] for i in range(1, 9)}  # 初始化一个字典，表示八个学期的课程
    max2 = 0

    for course in core_courses:
        cname = course['Cname']
        for i in range(1, 9):
            if((course['Csemester'] >> 8-i) & 1 == 1):    # 获取课程开设的学期
                semester = i #第i学期
                semester_courses[semester].append(cname)
                break

        # 更新最大专业核心课数
        max2 = max(max2, len(semester_courses[semester]))

    # 构建二维列表
    table1 = []
    for i in range(1, 9):
        semester_courses[i] = semester_courses[i][:max2]  # 只保留每学期最靠前的专业核心课
        table1.append(semester_courses[i])

    return max2,table1

def get_bulei_courses(major_name):
    connection = pymysql.connect(
        host='your_database_host',
        user='your_database_user',
        password='your_database_password',
        db='your_database_name',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 查询专业核心课
            sql = f"SELECT Course.Cname, Course.Csemester FROM Course " \
                  f"JOIN MC ON Course.Cid = MC.Cname " \
                  f"JOIN Major ON MC.Mname = Major.Mname " \
                  f"WHERE Major.Mname = '{major_name}' AND MC.MCcategory = '部类核心课';"
            cursor.execute(sql, (major_name,))
            result = cursor.fetchall()

            return result
    finally:
        connection.close()

def map_bulei(major_name):
    core_courses = get_bulei_courses(major_name)

    semester_courses = {i: [] for i in range(1, 9)}  # 初始化一个字典，表示八个学期的课程
    max1 = 0

    for course in core_courses:
        cname = course['Cname']
        for i in range(1, 9):
            if((course['Csemester'] >> 8-i) & 1 == 1):    # 获取课程开设的学期
                semester = i #第i学期
                semester_courses[semester].append(cname)
                break

        # 更新最大专业核心课数
        max1 = max(max1, len(semester_courses[semester]))

    # 构建二维列表
    table2 = []
    for i in range(1, 9):
        table2.append(semester_courses[i])

    return max1,table2

if __name__ == '__main__':
    app.run(debug=True)
