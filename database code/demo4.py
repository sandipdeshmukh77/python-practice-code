import cx_Oracle
import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='root',database='sandidb')
    cursor=con.cursor()
    cursor.execute("select * from employees1")
    data=cursor.fetchall()
    print(list(data))
    list=list(data)
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('prbm with mysql',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
try:
    con=cx_Oracle.connect("SYSTEM/Sandi1928@localhost")
    cursor=con.cursor()
    sql="insert into employees values(:eno,:ename,:esal,:eaddr)"
    cursor.executemany(sql,list)
    con.commit()
    print('data copied from mysql to oracle')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('prbm with oracle',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
