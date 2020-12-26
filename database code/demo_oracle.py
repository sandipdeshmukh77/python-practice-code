import cx_Oracle
try:
    con=cx_Oracle.connect('SYSTEM/Sandi1928@localhost')
    cursor=con.cursor()
    # cursor.execute('create table employees(eno number(10),ename varchar2(10),esal number(10,2),eaddr varchar(10))')
    # print('table created successfully')
    cursor.execute("insert into employees values(100,'sandi',1111,'puneri')")
    con.commit()
    print('record inserted successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is problem with Oracle',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
