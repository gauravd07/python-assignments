import mysql.connector
from flask import Flask, render_template, json, request,redirect,session

app = Flask(__name__)

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'fr3sca'
#app.config['MYSQL_DATABASE_DB'] = 'my_doublehorn'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'


@app.route('/getUser')
def getuser():
    try:
            con = mysql.connector.connect(host='localhost',
                                       database='my_doublehorn',
                                       user='root',
                                       password='fr3sca')
            cursor = con.cursor()
            cursor.callproc("sp_GetAllUsers")
            users = cursor.fetchall()

            users_dict = []
            for user in users:
                user_dict = {
                        'Id': user[0],
                        'Name': user[1]}
                users_dict.append(user_dict)

            return "success"

    except Exception as e:
        return e.message


@app.route('/addUser',methods=['POST'])
def adduser():
    try:
        request_json_data = request.get_json()
        print(request_json_data)

        user_id = request_json_data.__getitem__('user_id')
        user_name = request_json_data.__getitem__('user_name')

        conn = mysql.connector.connect(host='localhost',
                                      database='my_doublehorn',
                                      user='root',
                                      password='fr3sca')
        cursor = conn.cursor()
        cursor.callproc('sp_addUser',(user_name,user_id))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return redirect('/')
        else:
            return "success"

    except Exception as e:
        return e.message
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(port=5003)
