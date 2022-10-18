import requests,json,psycopg2


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
            "appkey": "jjHggHfNVaGvkabpQXfs",
            "loginType": "YLACCOUNT_LOGIN",
            "emailParam": {
            "account": f"{account}",
            "password": f"{password}",
                                                             },
                    }
        resp = requests.post(login_url, headers=header,json=payload)
        dic= resp.json()
        token = "Bearer "+ dic["accessToken"]
        return token

class Verifycode():
    def sendcode(self,action,email):
        '''
        发送验证码
        :param action: 接收操作，注册/重置密码/更换邮箱
        :return: 返回验证码
        '''
        login_url= 'http://dev-pos-api.youland.com/usercenter/api/user/sendCode'
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
        "email": f"{email}",
        "appkey": "jjHggHfNVaGvkabpQXfs",
        "bizType": f"{action}",
                                        }
        resp = requests.post(login_url, headers=header, json=payload)
        dic = resp.json()#发送验证码，获取结果
        if dic == True:
        # 连接数据库，查询发送的验证码
            #建立连接
            conn= psycopg2.connect("dbname=common_user_center user=ulandmaster password=k2G9!Qpr host=testdb-pos-1.cluster-cjurcg0zx8s1.us-west-1.rds.amazonaws.com port=5432")
            #获取游标
            cur = conn.cursor()
            #查询数据库获取tenant_id
            sql1 = "SELECT tenant_id FROM public.yl_oss_institution where appkey = 'jjHggHfNVaGvkabpQXfs'"
            try:
                cur.execute(sql1)
                rows = cur.fetchone()
                # 获取到tenant_id
                tenant_id=rows[0]
                sql = f"SELECT code FROM public.yl_oss_verify_code where inbox_email = '{email}' and tenant_id = '{tenant_id}' and biz_type = '{action}' and validate = '1' ORDER BY expired_time DESC"
                cur.execute(sql)
                rows2 = cur.fetchall()
            finally:
                cur.close()
                conn.close()
            return rows2[0][0]
        print('-----------获取验证码失败-----------')


    def verifycode(self, action, *email):
        if action == 'CHANGE_EMAIL' :
            conn = psycopg2.connect(
                "dbname=common_user_center user=ulandmaster password=k2G9!Qpr host=testdb-pos-1.cluster-cjurcg0zx8s1.us-west-1.rds.amazonaws.com port=5432")
            cur = conn.cursor()
            sql1 = "SELECT tenant_id FROM public.yl_oss_institution where appkey = 'jjHggHfNVaGvkabpQXfs'"
            try:
                cur.execute(sql1)
                rows = cur.fetchone()
                # 获取到tenant_id
                tenant_id=rows[0]
                sql = f"SELECT code FROM public.yl_oss_verify_code where inbox_email = '{email[0][1]}' and tenant_id = '{tenant_id}' and biz_type = '{action}' and validate = '1' ORDER BY expired_time DESC"
                cur.execute(sql)
                rows2 = cur.fetchall()
            finally:
                cur.close()
                conn.close()
            code = rows2[0][0]
        else:
            code = self.sendcode(action=action,email=email[0][0])

        login_url = 'http://dev-pos-api.youland.com/usercenter/api/user/verifyCode'
        header = {
            'accept': 'application/json,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "code": f"{code}",
            "appkey": "jjHggHfNVaGvkabpQXfs",
            "email": f"{email[0][0]}",
            "bizType": f"{action}"
                                                }
        resp = requests.post(login_url, headers=header, json=payload)
        dic = resp.json()  # 发送验证码，获取结果


