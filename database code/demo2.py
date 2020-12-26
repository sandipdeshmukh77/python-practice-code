import cx_Oracle
try:
    con=cx_Oracle.connect("SYSTEM/Sandi1928@localhost")
    cursor=con.cursor()
    salary=int(input('enter salary to increse:'))
    salrange=int(input('enter salary range for which salary want to increse:'))
    sql="update employees set esal=esal+%f where esal<%f"
    cursor.execute(sql %(salary,salrange))
    con.commit()
    print('updated successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
