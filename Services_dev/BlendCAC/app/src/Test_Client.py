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
    
    '''
    Get BC_account given node_name
    @node_name: ip_address:port_num
    @datafile: node account datafile path
    '''
    @staticmethod
    def getAddress(node_name, datafile):
        address_json = json.load(open(datafile))
        return address_json[node_name]

def test_func(host_ip, node_name):
	addr_list = '../../node_data/addr_list.json'
	node_address = WSClient.getAddress(node_name, addr_list)
	
	# construct data argument
	data_args = {}
	data_args ['host_ip'] = host_ip
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
    if(len(sys.argv)<2):
        print("Usage: %s host_ip node_name" %(sys.argv[0]))
        exit()
    host_ip = sys.argv[1]
    node_name = sys.argv[2]
    test_func(host_ip, node_name)
	
