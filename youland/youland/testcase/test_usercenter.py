import requests, allure, sys,pprint

sys.path.append('.')
from Lib.login import Signin, Verifycode


class Test_usercenter():
    @allure.story('注册')
    def test_signup(self):
        verify_url = 'http://dev-pos-api.youland.com/usercenter/api/user/sign_up'
        header = {
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "appkey": "jjHggHfNVaGvkabpQXfs",
            "emailParam": {
                "email": "294991281@qq.com",
                "name": "macewf",
                "password": "qaz123456",
                "userType": "CUSTOMER"
            }
        }
        resp = requests.post(verify_url, headers=header, json=payload)
        Verifycode().verifycode('REGISTER', (payload['emailParam']['email'],))
        # 比对响应码
        # print(resp.text)
        assert resp.status_code == 200

    @allure.story('修改密码')
    def test_changepassword(self):
        token = Signin().signin(account='294991281@qq.com', password='qaz123456')
        chagepass_url = 'http://dev-pos-api.youland.com/usercenter/api/user/changePass'
        header = {
            'authorization': token,
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "newPass": "aa123456",
            "oldPass": "qaz123456",
        }
        resp = requests.post(chagepass_url, headers=header, json=payload)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200

    @allure.story('重置密码')
    def test_resetpassword(self):
        token = Signin().signin(account='294991281@qq.com', password='aa123456')
        code = Verifycode().sendcode(action='RESET_PASS',email='294991281@qq.com')
        resetpass_url = 'http://dev-pos-api.youland.com/usercenter/api/user/resetPass'
        header = {
            'authorization': token,
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "newPass": "qaz123456",
            "appkey": "jjHggHfNVaGvkabpQXfs",
            "verifyCode": f"{code}",
            "email": "294991281@qq.com",
        }
        resp = requests.post(resetpass_url, headers=header, json=payload)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200

    @allure.story('修改邮箱')
    def test_changeemail(self):
        token=Signin().signin(account='294991281@qq.com',password='qaz123456')

        chagepass_url = 'http://dev-pos-api.youland.com/usercenter/api/user/changeEmail'
        header = {
            'authorization':token,
            'accept':'application/json',
            'user-agen':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                        }
        payload = {
            "oldEmail": "294991281@qq.com",
            "newEmail": "294991280@qq.com",
                                            }
        resp = requests.post(chagepass_url,headers=header,json=payload)
        Verifycode().verifycode('CHANGE_EMAIL',(payload["oldEmail"],payload['newEmail']))
        pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200
