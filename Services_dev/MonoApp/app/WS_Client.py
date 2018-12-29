#!/usr/bin/env python3.5

'''
========================
WS_Client module
========================
Created on Sep.15, 2018
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
from Service_API import SrvAPI

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")

 
class WSClient(object):
    
    '''
    Get all dataset
    '''
    @staticmethod
    def Get_Datasets(api_url, data_args={}):          
        headers = {'Content-Type' : 'application/json'}
        response = requests.get(api_url, data=json.dumps(data_args), headers=headers)
        
        #get response json
        json_response = response.json()      

        return json_response
    
    '''
    Get record by id
    '''
    @staticmethod
    def Get_DataByID(api_url, params, data_args={} ):          
        headers = {'Content-Type' : 'application/json'}
        response = requests.get(api_url,params=params, data=json.dumps(data_args), headers=headers)
        
        #get response json
        json_response = response.json()      

        return json_response
    
    '''
    Post data to add record
    '''
    @staticmethod
    def Create_Data(api_url, data):          
        headers = {'Content-Type' : 'application/json'}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        
        #get response json
        json_response = response.json()      

        return json_response
    
    '''
    Put updated data
    '''
    @staticmethod
    def Update_Data(api_url, data):          
        headers = {'Content-Type' : 'application/json'}
        response = requests.put(api_url, data=json.dumps(data), headers=headers)
        
        #get response json
        json_response = response.json()      

        return json_response
    
    '''
    Put id to delete data
    '''
    @staticmethod
    def Delete_Data(api_url, data):          
        headers = {'Content-Type' : 'application/json'}
        response = requests.delete(api_url, data=json.dumps(data), headers=headers)
        
        #get response json
        json_response = response.json()      

        return json_response

def test_search(data_args={}):
	params={}
	if('project_id' in data_args):
		params['project_id']=data_args['project_id']
	else:
		params['project_id']=0

	SP_ipaddress = data_args['host_ip']
	#print(WSClient.Get_Datasets('http://' + SP_ipaddress + '/test/api/v1.0/dt', data_args))
	print(WSClient.Get_DataByID('http://' + SP_ipaddress + '/test/api/v1.0/dt/project', params, data_args))
    

	
def test_CapAC(host_ip):
	# set host id address
	filepath = './features/0_2_person1/13.2.52.txt'
	filepath0 = './features/6_10_person/14.52.38.txt'

	addr_list = './addr_list.json'
	
	project_id = 1
	index_id = 1
	node_name = 'PI_Node_1'
	node_address = SrvAPI.getAddress(node_name, addr_list)

	# construct data argument
	data_args = {}
	data_args ['project_id'] = project_id
	data_args ['host_ip'] = host_ip
	data_args ['index_id'] = index_id
	data_args ['filepath'] = filepath
	data_args ['host_address'] = node_address
	data_args ['url_rule'] = '/BlendCAC/api/v1.0/getCapToken'
	# set project id
	project_id = 3

	
	start_time=time.time()
	
	#------------------ test data access service API ------------------	
	test_search(data_args)
	
	end_time=time.time()
	exec_time=end_time-start_time
	
	time_exec=format(exec_time*1000, '.3f')
	print("Execution time is:%2.6f" %(exec_time))

	FileUtil.AddLine('exec_time_client.log', time_exec)

if __name__ == "__main__":
    if(len(sys.argv)<2):
        print("Usage: %s host_list" %(sys.argv[0]))
        exit()
    host_ip = sys.argv[1]
    test_run = 10
    wait_interval = 1
    for x in range(test_run):
        test_CapAC(host_ip)
        time.sleep(wait_interval)
    pass
