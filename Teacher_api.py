import requests
import MySQLdb
import time


class Login:
    def login_api(self):
        url = "http://localhost/api/mgr/loginReq"
        payload = {
             "username": "auto",
            "password": "sdfsdfsdf"
        }
        response = requests.post(url, data=payload)
        assert response.json()['retcode'] == 0
        self.dic = {'sessionid':response.cookies['sessionid']}
        return self.dic


class Teacher(Login):
    def add_teacher(self, username, password, realname, desc):
        url = "http://localhost/api/mgr/sq_mgr/"
        payload = {
            'action': 'add_teacher',
            'data': '''{
    "username":"%s",
    "password":"%s",
    "realname":"%s",
    "desc":"%s",
    "courses":[],
    "display_idx":1
}''' % (username,password,realname,desc)
        }
        response = requests.post(url, data=payload, cookies=self.dic)
        return response.json()

    def search_sql_add(self, id):
        connection = MySQLdb.connect(host='172.16.0.163',
                                     user='songqin',
                                     passwd='songqin',
                                     db='plesson',
                                     charset="utf8")
        c = connection.cursor()
        sql = f'select * from sq_teacher where id ={id} '
        c.execute(sql)
        res = c.fetchone()
        c.close()
        return res

    def search_username(self, id):
        connection = MySQLdb.connect(host='172.16.0.163',
                                     user='songqin',
                                     passwd='songqin',
                                     db='plesson',
                                     charset="utf8")
        c = connection.cursor()
        sql = f'select username from common_user where id ={id} '
        c.execute(sql)
        res = c.fetchone()
        c.close()
        return res



username = '363554'
password = 'password'
realname = '真实姓名'
desc = '细节描述'
t = Teacher()
t.login_api()
print(t.add_teacher(username, password, realname, desc))
