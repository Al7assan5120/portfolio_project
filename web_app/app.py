from flask import Flask, render_template
from model import storage
from flask import abort, jsonify, make_response, request
from model.user import User

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.to_dict()
        newUser = User(**data)
        storage.new(newUser)
        storage.save()
        return make_response(jsonify(newUser.to_dict()), 201)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
