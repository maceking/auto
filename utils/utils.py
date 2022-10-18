#连接数据库查询code码
import psycopg2

def search_code(action,email):
    # 连接数据库，查询发送的验证码
    # 建立连接
    conn = psycopg2.connect(
            "dbname=dev-common-user-center user=ulandmaster password=k2G9!Qpr host=youland-test-db-instance-1.cjurcg0zx8s1.us-west-1.rds.amazonaws.com port=5432")
    # 获取游标
    cur = conn.cursor()
    # 查询数据库获取tenant_id
    sql1 = "SELECT tenant_id FROM public.yl_oss_institution_app where appkey = 'jcDlAFZpmslrRYwUzfpP'"
    try:
        cur.execute(sql1)
        tenant_ids = cur.fetchone()
        #数据库查询code
        sql = f"SELECT code FROM public.yl_oss_verify_code where inbox_email = '{email}' and tenant_id = '{tenant_ids[0]}' and biz_type = '{action}' and validate = '1' ORDER BY expired_time DESC"
        cur.execute(sql)
        rows2 = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return rows2[0][0]