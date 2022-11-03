import json
import pprint
import requests,sys
from config.config import host
from utils.logger import logger
sys.path.append('.')
from Lib.login import Signin

# 开始
def start_application():
    global token
    token = Signin().signin('mace@126.com','QWExMjM0NTY=')
    login_url = f'{host}processes/mortgage'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {}
    resp = requests.post(login_url, headers=header, json=paylod)
    logger.info(resp)
    data = resp.json()
    global processInsId,taskid
    processInsId=data['extra']['id']
    taskid = data['currentTasks'][0]['extra']['id']
#标的房
def varibles_purposre():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod={
        "processInsId": processInsId,
        "variables": [{
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "purpose"
                },
                "creditScore": {
                    "state": "notice"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "starting"
            }
        }],
        "overwrite": True
    }
    resp = requests.put(login_url, headers=header, json=paylod)

# 产权相关
def varibles_property():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
        "processInsId": processInsId,
        "variables": [{
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "notice"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "starting"
            }
        }],
        "overwrite": True
    }
    resp = requests.put(login_url, headers=header, json=paylod)

# 更新开始变量
def varibles_staring():
    login_url = f'{host}tasks/{taskid}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "overwrite": True,
    "taskId": f"{taskid}",
    "variables": [
        {
            "name": "starting",
            "type": "json",
            "value": {
                "stageOpt": "researching",
                "offerOpt": "pre_approval",
                "purchaseTimeOpt": "quarter",
                "propAddr": {
                    "address": "261 5th Avenue",
                    "aptNumber": "",
                    "city": "New York",
                    "state": "NY",
                    "postcode": "10016"
                },
                "occupancyOpt": "primary_residence",
                "propertyOpt": "single_family",
                "numberOfUnits": 0
            }
        }
    ]
}
    resp = requests.put(login_url, headers=header, json=paylod)

def starting_save():
    login_url = f'{host}tasks/{taskid}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action":"complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
#更新开始变量后，预开启下一阶段
def varibles_cri():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
        "overwrite": True,
        "taskId": f"{taskid}",
        "variables": [
            {
                "name": "starting",
                "type": "json",
                "value": {
                    "stageOpt": "researching",
                    "offerOpt": "pre_approval",
                    "purchaseTimeOpt": "quarter",
                    "propAddr": {
                        "address": "261 5th Avenue",
                        "aptNumber": "",
                        "city": "New York",
                        "state": "NY",
                        "postcode": "10016"
                    },
                    "occupancyOpt": "primary_residence",
                    "propertyOpt": "single_family",
                    "numberOfUnits": 0
                }
            }
        ]
    }
    resp = requests.put(login_url, headers=header, json=paylod)
    print(resp.text)




start_application()
varibles_purposre()
varibles_property()
varibles_staring()
starting_save()
varibles_cri()