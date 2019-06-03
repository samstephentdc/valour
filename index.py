from flask import Flask,render_template, flash,redirect,request,url_for
from forms import ContactForm #including file formms.py
from flask_mail import Mail,Message


app=Flask(__name__)
app.secret_key = '******'
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '******',
    MAIL_PASSWORD = '********',
))

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact',methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == True:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            
            msg = Message(request.form["subject"], sender = '****linudummy@gmail.com', recipients = ['*****'])
            data = [request.form["name"] , request.form["email"] ,request.form["message"]]
            s="\n"
            s = s.join(data)
            msg.body = s
            mail.send(msg)
            flash('.')
            return redirect(url_for('contact'))
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
    


if __name__ == "__main__":
    
    app.run(debug=False)
    

