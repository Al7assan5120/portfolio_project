from flask import Flask, render_template
from model import storage
from flask import abort, jsonify, make_response, request
from model.user import User

app = Flask(__name__)



@app.route("/")
def route():
    return render_template('newapp.html')

@app.route("/submit", methods=['POST'], strict_slashes=False)
def new_user():
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    newUser = User(**data)
    storage.new(newUser)
    storage.save()
    return make_response(jsonify(newUser.to_dict()), 201)

if __name__ == "__main__":
    app.run(debug=True)

