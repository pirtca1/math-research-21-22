import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\AMR\Desktop\math_research\OAMDatabase11.12.21.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT UserUid, MAX(EET) FROM EventRegistration1112 GROUP BY UserUid')

for row in cursor.fetchall():
    print (row)