import pymysql
try:
    con=pymysql.connect(host='localhost', user='root', password='root', database='sandidb')
    cursor = con.cursor()
    cursor.execute("create table employees2(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
    print('table created')
    sql="insert into employees2(eno,ename,esal,eaddr) VALUES(%s,%s,%s,%s)"
    record=[(11,'sachin',1111,'mumbai'),
            (22,'dhoni',2222,'pune'),
            (33,'kohli',3333,'nashik'),
            (44,'virat',4444,'nagpur')]
    cursor.executemany(sql,record)
    con.commit()
    print('record saved successfully')
    cursor.execute('select * from employees1')
    data=cursor.fetchall()
    for row in data:
        print('employee number',row[0])
        print('employee ename',row[1])
        print('employee number',row[2])
        print('employee number',row[3])

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('there is prbm with sql:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
