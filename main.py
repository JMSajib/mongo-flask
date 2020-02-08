from app import app, mongo
from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId


@app.route('/add', methods=['POST'])
def add_user():
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_password = _json['pwd']

	if _name and _email and _password and request.method == 'POST':
		id = mongo.db.user.insert({'name': _name, 'email': _email, 'pwd': _password})
		resp = jsonify('User added successfully!')
		resp.status_code = 200
		return resp
	else:
		return not_found()
		
@app.route('/users')
def users():
	users = mongo.db.user.find()
	resp = dumps(users)
	return resp
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()