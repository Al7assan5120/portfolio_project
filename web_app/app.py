from flask import Flask, render_template, flash, url_for, redirect, request
from model import storage, secret_key
from model.user import User
from model.admin import Admin
from flask_mail import Mail, Message
from hashlib import md5
from flask_login import LoginManager, login_user, login_required, logout_user


app = Flask(__name__)
app.debug = True
app.secret_key = secret_key
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "amr96.adel@gmail.com"
app.config["MAIL_PASSWORD"] = "gswntjlzalbihyjg"
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return storage.get(Admin, user_id)


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/newapp", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.to_dict()
        newUser = User(**data)
        storage.new(newUser)
        storage.save()

        # Sending Email
        message_body = f"Thanks {newUser.first_name} for submission, Please find your id to be able to track the status of your form.\n" \
            f"id = {newUser.id}"

        message = Message(subject="New Form Submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[newUser.email],
                          body=message_body)
        mail.send(message)

        # Submission Success Message!
        flash(f"{newUser.first_name}, Your form was submitted successfully, For tracking purposes we've sent id of your form to {newUser.email}!", "success")

    return render_template('newapp.html')


@app.route("/tracking", methods=["GET", "POST"])
def tracking():
    if request.method == "POST":
        userId = request.form.get('ID')
        user = storage.get(User, userId)
        if (user == None):
            flash ("Invalid ID", "faild")
        else:
            flash (f"{user.first_name}, Your Application current status is : {user.status}", "success")

    return render_template('tracking.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        passWord = request.form.get('password')
        HpassWord = md5(passWord.encode()).hexdigest()
        admin = storage.all(Admin)

        for admins in admin.values():
            print(admins)
            if admins.email == email:
                if admins.password == HpassWord:
                    login_user(admins)
                    return redirect(url_for('dashboard'))
                else:
                    return("Password is Wrong")
        else:
            return("Email Not Found")

    return render_template('login.html')


@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()
