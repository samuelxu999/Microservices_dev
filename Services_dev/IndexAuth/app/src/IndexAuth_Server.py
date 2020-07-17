#!/usr/bin/env python3.5

'''
========================
IndexAuth_Server module
========================
Created on Dec.27, 2018
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of Hashed Index Authentication Microservices API that handle and response client's request.
'''

import datetime
import json
from flask import Flask, jsonify
from flask import abort,make_response,request
from IndexAuth_Policy import IndexPolicy

app = Flask(__name__)

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")

#========================================== Error handler ===============================================
#Error handler for abort(404) 
@app.errorhandler(404)
def not_found(error):
    #return make_response(jsonify({'error': 'Not found'}), 404)
	response = jsonify({'result': 'Failed', 'message':  error.description['message']})
	response.status_code = 404
	return response

#Error handler for abort(400) 
@app.errorhandler(400)
def type_error(error):
    #return make_response(jsonify({'error': 'type error'}), 400)
    response = jsonify({'result': 'Failed', 'message':  error.description['message']})
    response.status_code = 400
    return response
	
#Error handler for abort(401) 
@app.errorhandler(401)
def access_deny(error):
    response = jsonify({'result': 'Failed', 'message':  error.description['message']})
    response.status_code = 401
    return response

	
#========================================== Request handler ===============================================	
#GET query indexToken for specific index_id
@app.route('/indexauth/api/v1.0/getIndexToken', methods=['GET'])
def getIndexToken():
	#print request.data
	index_id = request.args.get('index_id', type = str)
	json_data = IndexPolicy.get_indexToken(index_id)
	return jsonify({'result': 'Succeed', 'data': json_data}), 201

#GET query authorized nodes
@app.route('/indexauth/api/v1.0/getAuthorizedNodes', methods=['GET'])
def getAuthorizedNodes():
	#print request.data
	json_data = IndexPolicy.get_AuthorizedNodes()
	return jsonify({'result': 'Succeed', 'data': json_data}), 201

#GET apply for verify_indexToken service for specific index_id
@app.route('/indexauth/api/v1.0/verify_indexToken', methods=['GET'])
def verify_indexToken():
	#print request.data
	index_id = request.args.get('index_id', type = str)
	filepath = request.args.get('index_data', type = str)
	json_data = IndexPolicy.verify_indexToken(index_id,filepath)
	return jsonify({'result': 'Succeed', 'data': json_data}), 201

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)




