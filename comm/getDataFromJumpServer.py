import pymysql
from sshtunnel import SSHTunnelForwarder

def mysqlconn(sql):

    with SSHTunnelForwarder(
        ('192.168.20.233', 8066),  # 跳板机地址
        ssh_username='k_dep',
        ssh_password='Q2wtjmuz',
        remote_bind_address=('192.168.20.76')) as tunnel:

        db = pymysql.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            uesr='alpha',
            password='sqrj@alpha#16888',
            charset='utf8',
            db='lesson'
        )