#!/usr/bin/env python3.5

'''
========================
Service_API module
========================
Created on Dec.27, 2018
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of service API that used for demo_app.
'''
import time
import requests
import datetime
import json

import sys
from utilities import DatetimeUtil, TypesUtil, FileUtil

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")
    
class SrvAPI(object):
	'''
	Get BC_account given node_name
	@node_name: ip_address:port_num
	@datafile: node account datafile path
	'''
	@staticmethod
	def getAddress(node_name, datafile):
		address_json = json.load(open(datafile))
		return address_json[node_name]

	'''
	Get IndexAuth_Token
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def getIndexToken(host_addr, index_id, data_args={}):
		#construct api_url
		api_url = "http://" + host_addr + "/indexauth/api/v1.0/getIndexToken"
		params={}
		params['index_id']=index_id
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url,params=params, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Get authorized nodes
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def getAuthorizedNodes(host_addr, data_args={}):
		#construct api_url
		api_url = "http://" + host_addr + "/indexauth/api/v1.0/getAuthorizedNodes"
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url,data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Verify hashed index value
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def verify_indexToken(host_addr, index_id, index_data, data_args={}):
		#construct api_url
		api_url = "http://" + host_addr + "/indexauth/api/v1.0/verify_indexToken"
		params={}
		params['index_id']=index_id
		params['index_data']=index_data
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url,params=params, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Get CapAC_Token
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def getCapToken(data_args={}):
		#construct api_url
		host_addr = data_args['host_ip']
		api_url = "http://" + host_addr + "/BlendCAC/api/v1.0/getCapToken"
		params={}
		params['client_addr']=data_args['host_address']
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url,params=params, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Verify Access
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def isValidAccess(data_args={}):
		#construct api_url
		host_addr = data_args['host_ip']
		api_url = "http://" + host_addr + "/BlendCAC/api/v1.0/isValidAccess"
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Get Vnode information
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def getVNodeInfo(data_args={}):
		#construct api_url
		host_addr = data_args['host_ip']
		api_url = "http://" + host_addr + "/AuthID/api/v1.0/getVNodeInfo"
		params={}
		params['client_addr']=data_args['host_address']
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url,params=params, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

	'''
	Verify identity
	@host_addr: ip_address:port_num
	'''
	@staticmethod
	def isValidID(data_args={}):
		#construct api_url
		host_addr = data_args['host_ip']
		api_url = "http://" + host_addr + "/AuthID/api/v1.0/isValidID"
		headers = {'Content-Type' : 'application/json'}
		response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

		#get response json
		json_response = response.json()

		return json_response

def test_func(host_str, param_str):
	filepath = './features/0_2_person1/13.2.52.txt'
	filepath0 = './features/0_2_person1/13.4.53.txt'

	addr_list = './addr_list.json'
	param_args=param_str.split(',')
	host_args = host_str.split(',')
	host_ip = host_args[0]
	index_id = param_args[0]
	node_name = param_args[1]
	node_address = SrvAPI.getAddress(node_name, addr_list)

	# construct data argument
	data_args = {}
	data_args ['host_ip'] = host_args[1]
	data_args ['host_address'] = node_address
	data_args ['url_rule'] = '/BlendCAC/api/v1.0/getCapToken'

	start_time=time.time()

	print(SrvAPI.getIndexToken(host_ip, index_id))
	print(SrvAPI.getAuthorizedNodes(host_ip))	
	print(SrvAPI.verify_indexToken(host_ip, index_id, filepath))

	print(SrvAPI.getCapToken(data_args))
	print(SrvAPI.isValidAccess(data_args))

	end_time=time.time()

	    #calculate exec time
	exec_time=end_time-start_time

	time_exec=format(exec_time*1000, '.3f')
	print("Execution time is:%2.6f" %(exec_time))

	FileUtil.AddLine('exec_time_client.log', time_exec)
  

	
if __name__ == "__main__":
    if(len(sys.argv)<2):
        print("Usage: %s host_list param_list" %(sys.argv[0]))
        exit()
    host_ip = sys.argv[1]
    param_str = sys.argv[2]
    test_func(host_ip, param_str)
