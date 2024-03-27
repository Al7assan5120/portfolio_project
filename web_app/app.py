from flask import Flask, render_template, flash
from model import storage, secret_key
from flask import abort, jsonify, make_response, request
from model.user import User

app = Flask(__name__)
app.secret_key = secret_key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.to_dict()
        newUser = User(**data)
        storage.new(newUser)
        storage.save()
        flash(f"{newUser.first_name}, Your form was subitted successfully, We've sent a confirmation E-mail to {newUser.email}!", "success")

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
