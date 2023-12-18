from flask import Flask, jsonify, request
import pymysql.cursors

app = Flask(__name__)

def insert_course_data(major_name, course_name, course_id, category, credit, modules):
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
        host='your_database_host',
        user='your_database_user',
        password='your_database_password',
        db='your_database_name',
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
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
