import mysql.connector
from datetime import datetime,date
from flask import Flask, session, redirect, url_for, escape, request, render_template

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
todaydate=date.today()

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="prathamesh",
  database="hospital"
)

mycur = mydb.cursor()
''' 
query="INSERT INTO patients (SSN,patientid,patient_name,age,doa,bedtype,address,city,state,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
vals=("350587741","prath29","Prathamesh More",21,todaydate,"single","115/a-14 Gorai","Mumbai","Maharashtra","Active")
mycur.execute(query,vals)
mydb.commit()
query="INSERT INTO medicines (medicineid,quantityissued,patientid) VALUES (%s,%s,%s)"
vals=("cro12",5,"prath29")
mycur.execute(query,vals)
mydb.commit()
print("Done")'''



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        un=request.form['username']
        up=request.form['password']
        param_dict = { "val": un,"val2":up }

        query=("SELECT * FROM userstore WHERE username= %(val)s AND password= %(val2)s")

        mycur.execute(query,param_dict)
        a=mycur.fetchall()
        if len(a)>0:
            print("Sucessfull Login")
        if len(a)==0:
            print("Invalid Credentials")
        
    return render_template('login.html', error=error)


@app.route('/create-patient', methods=['GET', 'POST'])
def createpatient():
    if request.method=='POST':
        patname=str(request.form['patientname'])
        patname=patname[0:7]
        patid=str(patname)+str(request.form['age'])
        status="Active"

   
        
        #pat_dict={"ssnid":request.form['ssnid'],"patid":patid,"name":request.form['patientname'],"age":request.form['age'],"doa":request.form['doa'],"bedtype":request.form['bedtype'],"address":request.form['address'],"state":request.form['state'],"city":request.form['city'],"status":status}
        
        query="INSERT INTO patients (SSN,patientid,patient_name,age,doa,bedtype,address,city,state,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vals=(request.form['ssnid'],patid,request.form['patientname'],request.form['age'],todaydate,request.form.get('bedtype'),request.form['address'],request.form['city'],request.form['state'],status)
        
        mycur.execute(query,vals)
        mydb.commit()

        
    return render_template('create-patient.html')

if __name__ == '__main__':
    app.run(debug=True)    

