from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Nana welcomes you!'


@app.route('/<username>')
def get_user_profile(username):
    if username == 'Nana':
        return 'Username: \'{name}\' is me :('.format(name=username), 500

    response = {
        'username': username,
        'friends': ['Nana'],
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
