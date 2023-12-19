import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='fhyega', password='005635', database='train_system')
cur = conn.cursor()


def is_empty3(username, password1, password2):
    if username == '' or password1 == '' or password2 == '':
        return True
    else:
        return False


def is_different(password1, password2):
    if password1 == password2:
        return False
    else:
        return True


def is_existed(username):
    sql = "SELECT * FROM mysite_userinfo WHERE username ='%s'" % username
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True

def add_user(username, password):
    sql = "INSERT INTO mysite_userinfo(username, password) VALUES ('%s','%s')" % (username, password)
    cur.execute(sql)
    conn.commit()
    conn.close()