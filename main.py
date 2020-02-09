from app import app, mongo
from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId


@app.route('/add', methods=['POST'])
def add_user():
	data = request.json
	name = data['name']
	email = data['email']
	password = data['pwd']
	credit_card = data['credit_card']
	subscriber_id = data['subscriber_id']
	subscribe_date = data['subscribe_date']

	if name and email and password and request.method == 'POST':
		id = mongo.db.user.insert({
			'name': name, 
			'email': email, 
			'pwd': password,
			'credit_card': credit_card,
			'subscriber_id': subscriber_id,
			'subscriber_date': subscribe_date
			})
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