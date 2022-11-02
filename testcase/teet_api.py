from utils.excel_handle import get_excel_data
import pytest,sys,requests
from config.config import host
sys.path.append('.')



class Test_Signin():
    '''
    登录获取token
    '''

    @pytest.mark.parametrize('url,user', get_excel_data('登录模块', 'Login', *['URL', '请求参数'], selectCase=['all']))
    def test_signin(self,url,user):
        login_url = f'{host}{url}' #登录url
        print(login_url)
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                }
        payload = {
            "appkey": "jcDlAFZpmslrRYwUzfpP",
            "loginType": "YLACCOUNT_LOGIN",
            "emailParam": {
            "account": user['username'],
            "password": user['password'],
                                                             },
                    }
        resp = requests.post(login_url, headers=header,json=payload)
