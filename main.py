import datetime
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, make_response, render_template, request, flash, get_flashed_messages, session, redirect, abort, url_for
from datetime import timedelta, datetime
import random
from smtp import send_email
from tg import send_message_to_admins
from config import secret, admins_emails, admins_ids

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = secret
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['PORT'] = 5000


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/roadmap')
def roadmap():
    return render_template('index1.html')

@app.route('/makeoffer' , methods=['POST', 'GET'])
def makeoffer():

    if request.method == 'POST':
        
        name = request.form.get('name')
        tel = request.form.get('tel')
        email = request.form.get('email')
        service = request.form.get('service')
        message = request.form.get('message')


        for admin_email in admins_emails:
            send_email('bolgrakov@gmail.com', admin_email, 'Новий юзер!', f'користувач з імям {name} та поштою {email} хоче заказати у вас послугу {service}. його прохання - {message}')
      

        for admin_id in admins_ids:

            send_message_to_admins(adress=admin_id,text= f'користувач з імям {name} та поштою {email} хоче заказати у вас послугу {service}. його прохання - {message}')
        return 'спасибі за заявку'
    return render_template('form.html')

if __name__ =='__main__':
    app.run(debug=True)