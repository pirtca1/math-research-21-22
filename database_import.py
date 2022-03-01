from pandas.core.arrays import string_
import pyodbc
import datetime
import plotly.express as px
import pandas as pd

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\AMR\Desktop\math_research\OAMDatabase11.12.21.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT UserUid, MAX(EET) FROM EventRegistration1112 GROUP BY UserUid')
#Currently 4950 rows grabbed
i = 1
v_date = []
for row in cursor.fetchall():
    row_to_list = [elem for elem in row]
    #datee = datetime.datetime.strptime(row,"%Y-%m-%d")
    # v_date = row[1]
    month_date = (row_to_list[1].month)
    v_date.append(month_date)
    i += 1
    
#print(i)
df = pd.DataFrame(v_date, columns= ["Month"])
fig = px.histogram(df, [v_date])
fig.show()
#print(v_date)