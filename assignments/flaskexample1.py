#!/usr/bin/python2.7 -tt

import mysql.connector
from flask import Flask, render_template, json, request, redirect, session
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'fr3sca'
# app.config['MYSQL_DATABASE_DB'] = 'my_doublehorn'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'


class CreateUser(Resource):
    @property
    def get(self):
        try:
            con = mysql.connector.connect(host='localhost',
                                          database='my_doublehorn',
                                          user='root',
                                          password='fr3sca')
            cursor = con.cursor()
            cursor.callproc('sp_GetAllUsers')
            users = cursor.fetchmany(5)

            users_dict = []
            for user in users:
                user_dict = {
                    'Id': user[0],
                    'Name': user[1]}
                users_dict.append(user_dict)

            return "success"

        except Exception as e:
            return e.message
        finally:
         cursor.close()
        conn.close()

    @property
    def post(self):
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
            cursor.callproc('sp_addUser', (user_name, user_id))
            data = cursor.fetchmany(5)

            if len(data) is 0:
                conn.commit()
                return "no data found."
            else:
                return "success"

        except Exception as e:
            return e.message
        finally:
            cursor.close()
            conn.close()


api.add_resource(CreateUser, '/CreateUser')

if __name__ == "__main__":
    app.run(port=5003)
