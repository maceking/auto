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
    print('--------开始申请-------')
    return processInsId,taskid
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
    print('--------贷款用途-------')

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
    print('--------房产地址相关-------')

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
    print('-----提交所有信息-----')

#保存开始申请资料
def starting_save():
    login_url = f'{host}tasks/{taskid}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action":"complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
    data = resp.json()
    global taskid2
    taskid2 = data[0]['extra']['id']
    print('-----保存所有信息-----')

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
    print('-----即将开始征信查询-----')

#
def varibles_creditscore():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": f"{processInsId}",
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "selfInfo"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "creditScore"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('---确认查询---')

def varibles_myself():
    login_url = f'{host}tasks/{taskid2}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "overwrite": True,
    "taskId": f"{taskid2}",
    "variables": [
        {
            "type": "json",
            "value": {
                "firstName": "12",
                "lastName": "21",
                "phoneNumber": "3312312312",
                "dateOfBirth": "1111-11-11 GMT+8:05",
                "propAddr": {
                    "address": "250 Vesey Street",
                    "aptNumber": "",
                    "city": "New York",
                    "state": "NY",
                    "postcode": "10281"
                },
                "ssn": "666795322",
                "authorizedCreditCheck": True
            },
            "name": "aboutUSelf"
        }
    ]
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----更新征信查询变量------')

def credit_check():
    login_url = f'{host}tasks/{taskid2}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action":"complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
    data = resp.json()
    global taskid3
    taskid3 = data[0]['extra']['id']
    print('-----查询征信-----')

def varibles_cedit():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": "20221104011747717007",
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "creditScore"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "creditScore"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('----征信查询成功----')

def varibles_selfincome():
    login_url = f'{host}{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": processInsId,
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "selfIncome"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "creditScore"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----即将开始填写收入-----')

def varibles_incomeconfirm():
    login_url = f'{host}tasks/{taskid3}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "overwrite": True,
    "taskId": f"{taskid3}",
    "variables": [
        {
            "name": "salaryIncome",
            "type": "json",
            "value": {
                "timeunit": "months",
                "salary": 100000
            }
        },
        {
            "name": "selfEmployIncome",
            "type": "json",
            "value": {
                "timeunit": "years"
            }
        },
        {
            "name": "otherIncome",
            "type": "json",
            "value": {
                "timeunit": "months"
            }
        }
    ]
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----即将确认收入-----')

def selfincome_confirm():
    login_url = f'{host}tasks/{taskid3}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action": "complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
    data = resp.json()
    global taskid4
    taskid4 = data[0]['extra']['id']
    print('-----保存收入信息-----')

def varibles_startprd():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": f"{processInsId}",
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "coBorrower"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "creditScore"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----确认收入,开始下一阶段-----')

def varibles_isOnTheTitle():
    login_url = f'{host}tasks/{taskid4}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "overwrite": True,
    "taskId": "20221104031213816255",
    "variables": [
        {
            "name": "aboutOtherRelation",
            "type": "json",
            "value": {
                "isOnTheTitle": False,
                "relationshipOpt": ""
            }
        }
    ]
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----notitle提交-----')

def notitle_confirm():
    login_url = f'{host}tasks/{taskid4}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action": "complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
    data = resp.json()
    global taskid5
    taskid5 = data[0]['extra']['id']
    print('-----保存notitle信息-----')

def other_confirm():
    login_url = f'{host}tasks/{taskid5}'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {"action": "complete"}
    resp = requests.post(login_url, headers=header, json=paylod)
    data = resp.json()
    global taskid6
    taskid6 = data[0]['extra']['id']
    print('-----保存other信息-----')

def varibles_assets():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": processInsId,
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "coBorrower"
                },
                "assets": {
                    "state": "currentEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "assets"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----即将开始下阶段-----')

def varibles_ownCurrentEstate():
    login_url = f'{host}tasks/{taskid6}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "overwrite": True,
    "taskId": "20221104031218418159",
    "variables": [
        {
            "name": "propertyOwn",
            "type": "json",
            "value": {
                "assets": {},
                "ownCurrentEstate": False,
                "ownOtherEstate": False
            }
        }
    ]
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('-----提交ownCurrentEstate-----')

def varibles_processtag():
    login_url = f'{host}processes/{processInsId}/variables'
    header = {
        'authorization': token,
        'accept': 'application/json,text/plain,',
        'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    paylod = {
    "processInsId": f"{processInsId}",
    "variables": [
        {
            "name": "clientAppProgress",
            "type": "json",
            "value": {
                "applicationType": "purchase",
                "productCategory": "mortgage",
                "starting": {
                    "state": "property"
                },
                "creditScore": {
                    "state": "coBorrower"
                },
                "assets": {
                    "state": "everOwnedEstate"
                },
                "DTI": {
                    "state": "notice"
                },
                "state": "assets"
            }
        }
    ],
    "overwrite": True
}
    resp = requests.put(login_url, headers=header, json=paylod)
    print('---流程确认assert---')

start_application()
varibles_purposre()
varibles_property()
varibles_staring()
starting_save()
varibles_cri()
varibles_creditscore()
varibles_myself()
credit_check()
varibles_cedit()
varibles_selfincome()
varibles_incomeconfirm()
selfincome_confirm()
varibles_startprd()
varibles_isOnTheTitle()
notitle_confirm()
other_confirm()
varibles_assets()
varibles_ownCurrentEstate()
varibles_processtag()