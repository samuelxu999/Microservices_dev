#!/usr/bin/env python3.5

'''
========================
WS_Server module
========================
Created on Sep.16, 2018
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of server API that handle and response client's request.
'''

import datetime
import json
from flask import Flask, jsonify
from flask import abort,make_response,request
from Service_API import SrvAPI

app = Flask(__name__)

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")

#global variable
srv_list = './srv_list.json'
Secirity_ENABLE = 0

#Defining dictionary dataset model
projects = [
    {
        'id': 1,
		'title':u'test record',
		'description':u'This is test record to demonstrate access control mechanism!',
		'date':u'08-28-2018',
        'time': u'Morning'
    },
    {
        'id': 2,
        'title':u'data record sample',
        'description':u'You can read the record if you have access right!',
		'date':u'8-29-2018',
		'time': u'12:00 am'
    }
]

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
#GET req
@app.route('/test/api/v1.0/dt', methods=['GET'])
def get_projects():
	if(Secirity_ENABLE!=0):
		#Token missing, deny access
		if(request.data=='{}'):
			abort(401, {'message': 'Token missing, deny access'})
		#----------------------Authentication process--------------------
		if(Secirity_ENABLE==1):
			service_address = SrvAPI.getAddress('indexauth-service', srv_list)
			indexAuth_ret = SrvAPI.verify_indexToken(service_address, request.json['index_id'], request.json['filepath'])	
			#Authentication process
			if(not indexAuth_ret['data']):
				abort(401, {'message': 'Hashed Index Authentication fail, deny access'})
		#------------------------Access control process	-------------------
		if(Secirity_ENABLE==2):
			# construct data argument
			data_args = {}
			data_args ['host_ip'] = SrvAPI.getAddress('blendcac-service', srv_list)
			data_args ['host_address'] = request.json['host_address']
			data_args ['url_rule'] = request.json['url_rule']

			CapAC_ret = SrvAPI.isValidAccess(data_args)
			if(not CapAC_ret['data']):
				abort(401, {'message': 'Access right validation fail, deny projects querying'})
		#------------------------Identity authentication process	-------------------
		if(Secirity_ENABLE==3):
			# construct data argument
			data_args = {}
			data_args ['host_ip'] = SrvAPI.getAddress('authid-service', srv_list)
			data_args ['host_address'] = request.json['host_address']

			AuthID_ret = SrvAPI.isValidID(data_args)
			if(not AuthID_ret['data']):
				abort(401, {'message': 'Identity authentication fail, deny projects querying'})

	return jsonify({'result': 'Succeed', 'data': projects}), 201
	
#GET req for specific ID
@app.route('/test/api/v1.0/dt/project', methods=['GET'])
def get_project():
	if(Secirity_ENABLE!=0):
		#Token missing, deny access
		if(request.data=='{}'):
			abort(401, {'message': 'Token missing, deny access'})
		#----------------------Authentication process--------------------
		if(Secirity_ENABLE==1):
			service_address = SrvAPI.getAddress('indexauth-service', srv_list)
			indexAuth_ret = SrvAPI.verify_indexToken(service_address, request.json['index_id'], request.json['filepath'])	
			#Authentication process
			if(not indexAuth_ret['data']):
				abort(401, {'message': 'Hashed Index Authentication fail, deny access'})
		#------------------------Access control process	-------------------
		if(Secirity_ENABLE==2):
			# construct data argument
			data_args = {}
			data_args ['host_ip'] = SrvAPI.getAddress('blendcac-service', srv_list)
			data_args ['host_address'] = request.json['host_address']
			data_args ['url_rule'] = request.json['url_rule']

			CapAC_ret = SrvAPI.isValidAccess(data_args)
			if(not CapAC_ret['data']):
				abort(401, {'message': 'Access right validation fail, deny projects querying'})
		#------------------------Identity authentication process	-------------------
		if(Secirity_ENABLE==3):
			# construct data argument
			data_args = {}
			data_args ['host_ip'] = SrvAPI.getAddress('authid-service', srv_list)
			data_args ['host_address'] = request.json['host_address']
			#print(SrvAPI.getVNodeInfo(data_args))
			AuthID_ret = SrvAPI.isValidID(data_args)
			if(not AuthID_ret['data']):
				abort(401, {'message': 'Identity authentication fail, deny projects querying'})

	#print request.data
	project_id = request.args.get('project_id', default = 1, type = int)
	#project_id = int(request.args['project_id'])
	
	project = [project for project in projects if project['id'] == project_id]
	if len(project) == 0:
		abort(404, {'message': 'No data found'})
	return jsonify({'result': 'Succeed', 'data': project[0]}), 201
	
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
