import requests, allure, sys,pprint
sys.path.append('.')
from Lib.login import Signin, Verifycode
from utils.util import del_user


class Test_usercenter():
    def teardown_class(self):
        del_user(deluser)
    @allure.story('注册')
    def test_signup(self):
        signup_url = 'http://test-pos-api.youland.com/usercenter/api/user/sign_up'
        header = {
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "appkey": "jcDlAFZpmslrRYwUzfpP",
            "emailParam": {
                "email": "294991281@qq.com",
                "name": "macewf",
                "password": "qaz123456",
                "userType": "CUSTOMER"
            }
        }
        resp = requests.post(signup_url, headers=header, json=payload)
        code_result=Verifycode().verifycode('REGISTER', (payload['emailParam']['email'],))
        assert resp.status_code == 200 and code_result==True

    @allure.story('修改密码')
    def test_changepassword(self):

        chagepass_url = 'http://test-pos-api.youland.com/usercenter/api/user/changePass'
        header = {
            'authorization': Signin().signin(account='294991281@qq.com', password='qaz123456'),
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
        resetpass_url = 'http://test-pos-api.youland.com/usercenter/api/user/resetPass'
        header = {
            'authorization': Signin().signin(account='294991281@qq.com', password='aa123456'),
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "newPass": "qaz123456",
            "appkey": "jcDlAFZpmslrRYwUzfpP",
            "verifyCode": Verifycode().sendcode(action='RESET_PASS',email='294991281@qq.com'),
            "email": "294991281@qq.com",
        }
        resp = requests.post(resetpass_url, headers=header, json=payload)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200

    @allure.story('修改邮箱')
    def test_changeemail(self):
        chagepass_url = 'http://test-pos-api.youland.com/usercenter/api/user/changeEmail'
        header = {
            'authorization':Signin().signin(account='294991281@qq.com',password='qaz123456'),
            'accept':'application/json',
            'user-agen':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                        }
        payload = {
            "oldEmail": "294991281@qq.com",
            "newEmail": "294991280@qq.com",
                                            }
        resp = requests.post(chagepass_url,headers=header,json=payload)
        coderesult=Verifycode().verifycode('CHANGE_EMAIL',(payload["oldEmail"],payload['newEmail']))
        global deluser
        deluser = payload['newEmail']
        # 比对响应码
        assert resp.status_code == 200 and coderesult== True
