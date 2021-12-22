from flask import Flask, abort, flash,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import re


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __inint__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        # return  f"{self.username},{self.email}"
        return  f"{self.username},{self.email}"

@app.route('/',methods =['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/register',methods =['GET','POST'])
def register():
    if request.method == 'GET':
        return 'here is not using get method'
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email'] 
        password = request.form['password'] 
        user = Register(username = username, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        return redirect("/users")
@app.route('/users')
def users():
    users = Register.query.all()
    return render_template('users.html',users= users) 

@app.route('/update/<int:id>',methods = ['GET','POST'])
def update(id):
    user = Register.query.get(id)
    if request.method == 'POST':
        user.username= request.form['username']
        user.email= request.form['email']
        user.password= request.form['password']
        try:
            db.session.commit()
            return redirect('/users')
        except:
            return "there was a problem in update"
    else:
        return render_template('update.html',user = user )

@app.route('/delete/<int:id>',methods=['POST','GET'])
def delete(id):
    user = Register.query.get(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/users')
    except:
        return 'there was a problem in delete'


if __name__ == '__main__':
    app.run(debug=True)
