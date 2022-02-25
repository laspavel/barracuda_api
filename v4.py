#!/usr/bin/env python3

# Синхронизация данных CMDB and Zabbix

import json
import requests
import traceback

class BarracudaAPI(object):
    def __init__(self, api_user=None,api_password=None):
        self.token=False
        self.api_timeout=60
        self.api_host='https://api.waas.barracudanetworks.com/v4//waasapi/'
        login_data={"email": api_user,"password": api_password}
        rapi=requests.post(self.api_host+'api_login', data=login_data,headers={'Content-Type': 'application/x-www-form-urlencoded'},timeout=self.api_timeout)
        rapi.raise_for_status()
        result = json.loads(rapi.text)
        self.token=result['key']

    def do_request(self, smethod='',request_type='get', sdata=""):

        if request_type=='post':
            rapi=requests.post(self.api_host + smethod, data=sdata, headers={'Content-Type': 'application/json','auth-api': self.token },timeout=self.api_timeout)
        elif request_type=='patch':
            rapi=requests.patch(self.api_host + smethod, data=sdata, headers={'Content-Type': 'application/json','auth-api': self.token },timeout=self.api_timeout)
        elif request_type=='put':
            rapi=requests.put(self.api_host + smethod, data=sdata, headers={'Content-Type': 'application/json','auth-api': self.token },timeout=self.api_timeout)
        elif request_type=='delete':
            rapi=requests.delete(self.api_host + smethod, data=sdata, headers={'Content-Type': 'application/json','auth-api': self.token },timeout=self.api_timeout)
        else:
            rapi=requests.get(self.api_host + smethod, data=sdata, headers={'Content-Type': 'application/json','auth-api': self.token },timeout=self.api_timeout)
        rapi.raise_for_status()
        result = json.loads(rapi.text)
        return result

if __name__ == "__main__": 
    try:
        api_user='xxxxx@xxxxxx'
        api_pass='xxxxxxx'
      
        b=BarracudaAPI(api_user,api_pass)
        r=b.do_request('applications/xxxxxxx/endpoints')
        r=b.do_request('applications/xxxxxxx/servers')
        print(r)

    except Exception as ee:
        print(str(ee)+ '\n'+traceback.format_exc())
    finally:
        print('Bye !!!')
        exit(0)   