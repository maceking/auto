import requests,json,psycopg2
from utils.utils import search_code


class Signin():
    '''
    登录获取token
    '''
    def signin(self,account,password):
        login_url = 'http://dev-pos-api.youland.com/usercenter/api/user/sign_in' #登录url
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                }
        payload = {
            "appkey": "jcDlAFZpmslrRYwUzfpP",
            "loginType": "YLACCOUNT_LOGIN",
            "emailParam": {
            "account": f"{account}",
            "password": f"{password}",
                                                             },
                    }
        resp = requests.post(login_url, headers=header,json=payload)
        token = "Bearer "+ resp.json()["accessToken"]
        return token

class Verifycode():

    def sendcode(self,action,email):
        '''
        发送验证码
        :param action: 接收操作，注册/重置密码/更换邮箱
        :return: 返回验证码
        '''
        sendcode_url= 'http://dev-pos-api.youland.com/usercenter/api/user/sendCode'
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
        "email": f"{email}",
        "appkey": "jcDlAFZpmslrRYwUzfpP",
        "bizType": f"{action}",
                                        }
        resp = requests.post(sendcode_url, headers=header, json=payload)
        dic = resp.json()#发送验证码，获取结果
        if dic == True :
            code = search_code(action,email)
            return code

    def verifycode(self, action, *email):
        if action == 'CHANGE_EMAIL' :
            code = search_code(action,email[0][1])
        else:
            code = self.sendcode(action=action,email=email[0][0])
        verifycode_url = 'http://dev-pos-api.youland.com/usercenter/api/user/verifyCode'
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "code": f"{code}",
            "appkey": "jcDlAFZpmslrRYwUzfpP",
            "email": f"{email[0][0]}",
            "bizType": f"{action}"
                                                }
        resp = requests.post(verifycode_url, headers=header, json=payload)
        return resp.json()  # 返回验证码验证结果
