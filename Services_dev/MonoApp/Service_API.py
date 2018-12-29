#!/usr/bin/env python3.5

'''
========================
Service_API module
========================
Created on Dec.27, 2018
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of service API that used for MonoApp.
'''
import time
#import requests
import datetime
import json

import sys
from utilities import DatetimeUtil, TypesUtil, FileUtil

from IndexAuth_Policy import IndexPolicy
from BlendCapAC_Policy import CapPolicy

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
    def getIndexToken(index_id):
        json_token = IndexPolicy.get_indexToken(str(index_id))
        return json_token

    '''
    Get IndexAuth_Token
    @host_addr: ip_address:port_num
    '''
    @staticmethod
    def getAuthorizedNodes():
        json_token = IndexPolicy.get_AuthorizedNodes()
        return json_token

    '''
    Get IndexAuth_Token
    @host_addr: ip_address:port_num
    '''
    @staticmethod
    def verify_indexToken(index_id, filepath):
        json_data = IndexPolicy.verify_indexToken(str(index_id),filepath)
        return json_data

    '''
    Get Cap_Token
    @host_addr: ip_address:port_num
    '''
    @staticmethod
    def getCapToken(node_addr):
        json_data=CapPolicy.get_token(node_addr)
        return json_data

    '''
    Verify_CapAC
    @req_args: request argument
    '''
    @staticmethod
    def isValidAccess(req_args):
        return CapPolicy.is_valid_access_request(req_args)


def test_func(param_str):
	filepath = './features/0_2_person1/13.2.52.txt'
	filepath0 = './features/0_2_person1/13.4.53.txt'

	addr_list = './addr_list.json'
	param_args=param_str.split(',')

	index_id = param_args[0]
	node_name = param_args[1]
	node_address = SrvAPI.getAddress(node_name, addr_list)

	# construct data argument
	#data_args = {}
	#data_args ['host_address'] = node_address
	#data_args ['url_rule'] = '/BlendCAC/api/v1.0/getCapToken'
	
	start_time=time.time()
	
	print(SrvAPI.getIndexToken(index_id))
	print(SrvAPI.getAuthorizedNodes())	
	print(SrvAPI.verify_indexToken(index_id, filepath))

	print(SrvAPI.getCapToken(node_address))
	#print(SrvAPI.isValidAccess(req_args))
	
	end_time=time.time()

        #calculate exec time
	exec_time=end_time-start_time
	
	time_exec=format(exec_time*1000, '.3f')
	print("Execution time is:%2.6f" %(exec_time))
	
	FileUtil.AddLine('exec_time_client.log', time_exec)
  

	
if __name__ == "__main__":
    if(len(sys.argv)<2):
        print("Usage: %s param_list" %(sys.argv[0]))
        exit()
    param_str = sys.argv[1]
    test_func(param_str)
