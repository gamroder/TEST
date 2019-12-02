from flask_restful import Resource, reqparse
import psycopg2
from flask import Flask,jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    @classmethod
    def find_user(self,username):
        connection = psycopg2.connect(user = "postgres",password = "Kandra5moneR",host="localhost",port="5432",database = "Recommendations")
        cursor = connection.cursor()
        find_user = '''SELECT * FROM users where lower(USERNAME) = lower(%s) '''
        cursor.execute(find_user,(username,))
        row = cursor.fetchone()
        if row :
            user = User(*row)
        else:
            user = None
        connection.close()
        return user
    def authentication(self,password):
        result = check_password_hash(self.password,password)
        return result

class findUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str,required=True,help='This field cannot be blank')
    parser.add_argument('password',type = str,required=False)
    def get(self):
        data =  findUser.parser.parse_args()
        user_f = User.find_user(data['username'])
        if user_f and user_f.authentication(data['password']):
            return {"message":"User was found"}, 201
        elif user_f and user_f.authentication(data['password'])==False:
            return {"message":"User was found but password is wrong"},201
        else:
            return {"message":"User wasn't found"},201

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str,required=True,help='This field cannot be blank')
    parser.add_argument('password',type = str,required=True,help='This field cannot be blank')
    def post(self):
        data =  UserRegister.parser.parse_args()
        password_hash = generate_password_hash(data['password'])
        connection = psycopg2.connect(user = "postgres",password = "Kandra5moneR",host="localhost",port="5432",database = "Recommendations")
        cursor = connection.cursor()
        create_user = '''INSERT INTO  users(username,password) VALUES (%s,%s)  '''
        cursor.execute(create_user,(data['username'],password_hash))
        connection.commit()
        connection.close()
        return {"message": "User was created successfully"},201
