'''import mysql.connector
from datetime import datetime,date
from flask import Flask, session, redirect, url_for, escape, request, render_template

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
todaydate=date.today()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="prathamesh",
  database="hospital"
)

mycur = mydb.cursor()
val="3"
valp="pass124"
param_dict = { "val": val,"val2":valp }

query=("SELECT * FROM userstore WHERE username= %(val)s AND password= %(val2)s")

mycur.execute(query,param_dict)
a=mycur.fetchall()
for i in a:
    print(a)'''
'''
query="INSERT INTO patients (SSN,patientid,patient_name,age,doa,bedtype,address,city,state,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
vals=("350587741","prath2020","Prathamesh More",21,todaydate,"single","115/a-14 Gorai","Mumbai","Maharashtra","Active")
mycur.execute(query,vals)
mydb.commit()'''

a="1234567890"
print(a[0:7])
