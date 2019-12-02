from flask import Flask,jsonify,request,render_template,redirect,url_for
from flask_restful import Resource, Api
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from users import UserRegister,findUser
from forms import LoginForm
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
api = Api(app)
app.debug = True
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kandra5moneR@localhost/Recommendations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

api.add_resource(UserRegister,'/registerUser')
api.add_resource(findUser,'/findUser')

@app.route('/register',methods=['GET','POST'])
def register():
    form = LoginForm()
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        return ok
    else:
        return render_template('login.html',title='Sign in',form = form)

if __name__ == "__main__":
    app.run(port=5000)
