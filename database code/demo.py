import cx_Oracle
try:
    con=cx_Oracle.connect("SYSTEM/Sandi1928@localhost")
    cursor=con.cursor()
    sql="insert into employees values(:eno,:ename,:esal,:eaddr)"
    record=[(222,'sunny',2222,'mumbai'),
            (333,'bunny',3333,'banglore'),
            (444,'chinny',4444,'aurangabad'),
            (555,'tinnny',5555,'sillod')]
    cursor.executemany(sql,record)
    con.commit()
    print('record inserted successfully')

except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('prbm with oracle',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
