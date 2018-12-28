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
from wrapper_pyca import Crypto_DSA

now = datetime.datetime.now()
datestr=now.strftime("%Y-%m-%d")
timestr=now.strftime("%H:%M:%S")
    
class WSClient(object):
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
    Get IndexAuth_Token
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
    Get IndexAuth_Token
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

def test_func(host_ip, index_id):
	filepath = './features/0_2_person1/13.2.52.txt'
	filepath0 = './features/0_2_person1/13.4.53.txt'
	
	start_time=time.time()
	
	print(WSClient.getIndexToken(host_ip, index_id))
	print(WSClient.getAuthorizedNodes(host_ip))	
	print(WSClient.verify_indexToken(host_ip, index_id, filepath))
	
	end_time=time.time()

        #calculate exec time
	exec_time=end_time-start_time
	
	time_exec=format(exec_time*1000, '.3f')
	print("Execution time is:%2.6f" %(exec_time))
	
	FileUtil.AddLine('exec_time_client.log', time_exec)
  

	
if __name__ == "__main__":
    if(len(sys.argv)<2):
        print("Usage: %s host_ip index_id" %(sys.argv[0]))
        exit()
    host_ip = sys.argv[1]
    index_id = sys.argv[2]
    test_func(host_ip, index_id)
