from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL
import pandas as pd

app = Flask(__name__,template_folder="template")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Diyakarat05!!'
app.config['MYSQL_DB'] = 'dcc4'

mysql = MySQL(app)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/user1', methods = ["POST"])
def user1():
    date=request.form["date"]
    cursor = mysql.connection.cursor()
    date=str(date)
    cursor.execute(f"select * from purchase where Journal_date='{date}'")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()

@app.route('/user2', methods = ["POST"])
def user2():
    name=request.form["name"]
    print(name)
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Name_of_the_Political_Party='{str(name)}'")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()

@app.route('/user3', methods = ["POST"])
def user3():
    prefix=request.form["prefix"]
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Prefix='{prefix}'")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()
    
@app.route('/user4', methods = ["POST"])
def user4():
    bnumber=request.form["bondnumber"]
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Bond_Number={bnumber}")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()
    

@app.route('/user5', methods = ["POST"])
def user5():
    denom=request.form["denom"]
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Denominations={denom}")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()

@app.route('/user6', methods = ["POST"])
def user6():
    pcode=request.form["branchcode"]
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Issue_Branch_Code={pcode}")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()

@app.route('/user7', methods = ["POST"])
def user7():
    pteller=request.form["payteller"]
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from purchase where Pay_Teller={pteller}")
    userdetails=cursor.fetchall()
    data={}
    L=["Sr_No","Reference_No","Journal_date","Date_of_Purchase","Date_of_Expiry","Name_of_the_purchaser","Prefix","Bond_Number","Denominations","Issue_branch_code","Issue_Teller","Status"]
    for i in L:
        data[i]=[]
    for i in userdetails:
        for j in range(len(i)):
            data[L[j]].append(i[j])
    data=pd.DataFrame(data)
    data=data.set_index("Sr_No")
    return data.to_html()

if __name__ == '__main__':
    app.run(debug = True)