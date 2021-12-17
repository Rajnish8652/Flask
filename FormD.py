from email.headerregistry import Address
from tkinter.messagebox import NO
from flask import Flask,request,render_template,session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField,PasswordField,SelectField,RadioField
from wtforms.validators import DataRequired

app=Flask(__name__) # create a Flask instance

# Sceret key
app.config['SECRET_KEY'] = 'my name is Rajnish'

# Create a Flask Instance
class NamerForm(FlaskForm):
    Email = EmailField(validators = [DataRequired()])
    Password = PasswordField(validators = [DataRequired()])
    Address = StringField(validators = [DataRequired()])
    Address2 = StringField(validators = [DataRequired()])
    City = StringField(validators = [DataRequired()])
    State = SelectField(choices=['Choose','UP','Delhi','MP','Bihar'],validators=[DataRequired()])
    Zip = StringField(validators = [DataRequired()])
    ChekMeOut = RadioField(choices=[('Check me Out')],validators = [DataRequired()])

    submit = SubmitField('Sign in')


@app.route('/', methods = ['GET','POST'])  
def name():
    Email = None
    Password = None
    Address = None
    Address2= None
    City = None
    State = None
    Zip = None
    ChekMeOut = None
  
    form = NamerForm()
    # validate form
    if form.validate_on_submit():
        Email = form.Email.data
        form.Email.data = ''
        Password = form.Password.data
        form.Password.data = ''
        Address = form.Address.data
        form.Address.data = ''
        Address2 = form.Address2.data
        form.Address2.data = ''
        City = form.City.data
        form.City.data = ''
        State = form.State.data
        form.State.data = ''
        Zip = form.Zip.data
        form.Zip.data = ''
        Zip = form.ChekMeOut.data
        form.ChekMeOut.data = ''
    return render_template('FormD.html',Email=Email, form=form,Password = Password,Address = Address,
    Address2=Address2,City = City, State = State, Zip = Zip, ChekMeOut = ChekMeOut)

if __name__ == "__main__":
    app.run(debug=True,port=5006)    

    