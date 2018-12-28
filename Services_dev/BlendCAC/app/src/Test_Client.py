#!/usr/bin/env python3.5

'''
========================
Test_Client module
========================
Created on Dec.27, 2018
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of client API that access to Web service.
'''
import time
import requests
import datetime
import json

from CapACToken import CapACToken

import sys
from utilities import DatetimeUtil, TypesUtil, FileUtil

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")
    
class WSClient(object):
    '''
    Get IndexAuth_Token
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
    Get IndexAuth_Token
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

def test_func():
	addr_list = '../../node_data/addr_list.json'
	node_address = CapACToken.getAddress('PI_Node_1', addr_list)
	host_addr = '128.226.77.237:8080'
	# construct data argument
	data_args = {}
	data_args ['host_ip'] = host_addr
	data_args ['host_address'] = node_address
	data_args ['url_rule'] = '/BlendCAC/api/v1.0/getCapToken'

	start_time=time.time()

	print(WSClient.getCapToken(data_args))
	print(WSClient.isValidAccess(data_args))
	
	end_time=time.time()

        #calculate exec time
	exec_time=end_time-start_time
	
	time_exec=format(exec_time*1000, '.3f')
	print("Execution time is:%2.6f" %(exec_time))
	
	FileUtil.AddLine('exec_time_client.log', time_exec)
  

	
if __name__ == "__main__":
	test_func()
	pass
