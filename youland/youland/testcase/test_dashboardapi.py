'''
from config.config import host,authorization
from utils.logger import logger
import requests,allure
import pprint,pytest

#deshboard,查询application列表
@allure.feature('Dashboard')
class Test_Dashboard:

    @allure.story('申请列表')
    def test_listapplication(self):
        login_url = f'{host}processes/user'
        header = {
            'authorization':authorization,
            'accept':'application/json,text/plain,',
            'user-agen':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url,headers=header)
        logger.info(resp)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200

    @allure.story('单独申请记录')
    def test_processesinfo(self):
        login_url = f'{host}processes/20220810063034967073'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        # pprint.pprint(resp.text)
        #比对响应码
        assert resp.status_code == 200

    @allure.story('个人设置信息')
    def test_sttingsinfo(self):
        login_url = f'{host}dashboard/user/settings/info'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200

    @allure.story('预批准信')
    def test_letter(self):
        login_url = f'{host}dashboard/letter/20220810063034967073'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('申请summary')
    def test_summary(self):
        login_url = f'{host}dashboard/overview/summary/20220810063034967073'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('申请状态')
    def test_taskstatus(self):
        login_url = f'{host}dashboard/user/tasks/status/20220810063034967073'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('查看所有产品信息')
    def test_rateall(self):
        login_url = f'{host}dashboard/rate/20220810063034967073/all'
        header = {
            'authorization': authorization,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

'''