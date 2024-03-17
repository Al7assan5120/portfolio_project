from flask import Flask, render_template
from model import storage
from flask import abort, jsonify, make_response, request

app = Flask(__name__)



@app.route("/")
def route():
    return render_template('index.html')

@app.route("/user/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    user = storage.get(user_id)
    return jsonify(user.to_dict())

if __name__ == "__main__":
    app.run(debug=True)

