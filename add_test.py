from  Teacher_api import *
import time


def test_add():
    username = str(time.time())
    password = 'password'
    realname = 'realname'
    desc = 'desc'
    t = Teacher()
    t.login_api()
    res = t.add_teacher(username,password,realname,desc)
    assert res['retcode'] == 0
    id = res['id']
    res = t.search_sql_add(id)
    res1 = t.search_username(res[4])
    assert res[0] == id
    assert res[1] == realname
    assert res[2] == desc
    assert res1[0] == username


