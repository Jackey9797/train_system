import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='fhyega', password='005635', database='train_system')
cur = conn.cursor()


def is_empty2(username, password):
    if username == '' or password == '':
        return True
    else:
        return False


def is_correct(username, password):
    sql = "SELECT * FROM mysite_userinfo WHERE username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True
    
