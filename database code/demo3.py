import cx_Oracle
try:
    con=cx_Oracle.connect("SYSTEM/Sandi1928@localhost")
    cursor=con.cursor()
    cursor.execute("select * from employees")
    data=cursor.fetchmany(3)
    for row in data:
        print('employee number:',row[0])
        print('employee name:',row[1])
        print('employee salary:',row[2])
        print('employee address:',row[3])
        print()
        print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('prbm with database',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
