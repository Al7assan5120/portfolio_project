from flask import Flask, render_template, flash
from model import storage, secret_key
from flask import abort, jsonify, make_response, request
from model.user import User
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = secret_key
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "amr96.adel@gmail.com"
app.config["MAIL_PASSWORD"] = "gswntjlzalbihyjg"
mail = Mail(app)

@app.route("/", methods=["GET"])
def idnex():
    return render_template('index.html')


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

    return render_template('index.html')





@app.route("/tracking", methods=["GET", "POST"])
def tracking():
    if request.method == "POST":
        userId = request.form.get('ID')
        user = storage.get(userId)
        print(userId, user)
        if (user == "None"):
            print("amr")
            flash ("Invalid ID", "faild")
        else:
            flash (f"{user.first_name}, Your Application current status is : {user.status}", "success")

    return render_template('tracking.html')


if __name__ == "__main__":
    app.run(debug=True)
