from flask import Flask,render_template,request,redirect,url_for,flash,session,send_from_directory,jsonify
import pyodbc
from datetime import datetime
from werkzeug.utils import secure_filename 
import os


app=Flask(__name__)

# Database configuration
server = 'LAPTOP-97QATREI'
database = 'employee'
username = 'your_username'  # Replace with your SQL Server username
password = 'your_password'  # Replace with your SQL Server password
driver = '{ODBC Driver 17 for SQL Server}'

# Create the connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes'

con = pyodbc.connect(conn_str)
con.close()







#view of the accesories details having some fields
# @app.route('/')
@app.route("/index")
def index():
    con=pyodbc.connect(conn_str)
    cur=con.cursor()

    cur.execute("SELECT DISTINCT AssetType FROM category ORDER BY AssetType ASC")
    employee = cur.fetchall()


    # cur.execute("SELECT AssetType, AssetModel, AssetSerialNumber, SapAssetNo, AssetOwner,Department,AssetLocation FROM category")
    # data=cur.fetchall()


    cur.close()
    con.close()


    return render_template("index.html", employee=employee)

#fetchrecords by using a dropdown list 

@app.route("/fetchrecords", methods=["GET", "POST"])
def fetchrecords():
    con = pyodbc.connect(conn_str)
    cur = con.cursor()
    
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cur.execute("SELECT AssetType, AssetModel, AssetSerialNumber, SapAssetNo, AssetOwner, Department, AssetLocation FROM category")
        else:
            cur.execute("SELECT AssetType, AssetModel, AssetSerialNumber, SapAssetNo, AssetOwner, Department, AssetLocation FROM category WHERE AssetType = ?", (query,))
        data = cur.fetchall()
        return jsonify(htmlresponse=render_template('response.html', datas=data))

    # Fetch data for initial load (GET request)
    cur.execute("SELECT DISTINCT AssetType FROM category ORDER BY AssetType ASC")
    employee = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(employee=employee)



@app.route('/')
@app.route("/index1")
def index1():
    con=pyodbc.connect(conn_str)
    cur=con.cursor()

    cur.execute("SELECT DISTINCT AssetType FROM category ORDER BY AssetType ASC")
    employee = cur.fetchall()


    # cur.execute("SELECT AssetType, AssetModel, AssetSerialNumber, SapAssetNo, AssetOwner,Department,AssetLocation FROM category")
    # data=cur.fetchall()


    cur.close()
    con.close()


    return render_template("index1.html", employee=employee)

#fetchrecords 1 by using a dropdown list 

@app.route("/fetchrecords1", methods=["GET", "POST"])
def fetchrecords1():
    con = pyodbc.connect(conn_str)
    cur = con.cursor()
    
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cur.execute("SELECT  AssetType, AllocationDate, AllocationType, ValidTill FROM category")
        else:
            cur.execute("SELECT  AssetType, AllocationDate, AllocationType, ValidTill FROM category WHERE AssetType = ?", (query,))
        data = cur.fetchall()
        return jsonify(htmlresponse=render_template('response1.html', datas=data))

    # Fetch data for initial load (GET request)
    cur.execute("SELECT DISTINCT AssetType FROM category ORDER BY AssetType ASC")
    employee = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(employee=employee)









#adding accesories values to the table 

@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == 'POST':
        assettype = request.form['asset_type']
        assetmodel = request.form['asset_model']
        assetserialnumber = request.form['asset_number']
        sapassetno = request.form['sap_number']
        assetowner = request.form['asset_owner']
        department = request.form['department']  
        assetlocation = request.form['asset_location']       
        
        
        con=pyodbc.connect(conn_str)
        cur=con.cursor()



        cur.execute("INSERT INTO category (AssetType,  AssetModel,  AssetSerialNumber, SapAssetNo, AssetOwner,Department,AssetLocation) VALUES (?, ?, ?, ?, ?,?,?)",
                    (assettype, assetmodel, assetserialnumber, sapassetno, assetowner,department,assetlocation))
        con.commit()


        flash('ASSET REGISTRATION SUCCESSFUL','success')
        return redirect(url_for("index"))
    return render_template("add.html")






#adding 1  accesories values to the table 

@app.route("/add1",methods=['POST','GET'])
def add1():
    if request.method == 'POST':
        assettype = request.form['asset_type']
        allocationDate = request.form['allocationDate']
        allocationType = request.form['allocationType']
        validTill = request.form['validTill']
        
        
        con=pyodbc.connect(conn_str)
        cur=con.cursor()



        cur.execute("INSERT INTO category (AssetType, AllocationDate,  AllocationType, ValidTill) VALUES (?, ?, ?, ?)",
                    (assettype, allocationDate,  allocationType, validTill))
        con.commit()


        flash('ASSET REGISTRATION SUCCESSFUL','success')
        return redirect(url_for("index1"))
    return render_template("add1.html")










#edit the ASSET DETAILS


@app.route("/edit/<assetserialnumber>",methods=['POST','GET'])
def edit(assetserialnumber):
    if request.method=='POST':
        assettype = request.form['asset_type']
        assetmodel = request.form['asset_model']
        assetserialnumber = request.form['asset_number']
        sapassetno = request.form['sap_number']
        assetowner = request.form['asset_owner']
        department = request.form['department']  
        assetlocation = request.form['asset_location']       


        
        con=pyodbc.connect(conn_str)
        cur=con.cursor()
        cur.execute("UPDATE category SET AssetType=?, AssetModel=?,SapAssetNo=?, AssetOwner=?, Department=?,AssetLocation=?  WHERE AssetSerialNumber=?",
                             ( assettype, assetmodel, sapassetno, assetowner, department, assetlocation,assetserialnumber))
        con.commit()



        flash('Employee Details Updated','success')
        return redirect(url_for("index"))
    con = pyodbc.connect(conn_str)
    cur=con.cursor()

    cur.execute("select * from category where AssetSerialNumber=?",(assetserialnumber,))
    data=cur.fetchone()
    return render_template("edit.html",datas=data)



#edit 1 the ASSET DETAILS


@app.route("/edit1/<assetserialnumber>",methods=['POST','GET'])
def edit1(assetserialnumber):
    if request.method=='POST':
        assettype = request.form['asset_type']
        
        
        allocationDate = request.form['allocationDate']
        allocationType = request.form['allocationType']
        validTill = request.form['validTill']
               


        
        con=pyodbc.connect(conn_str)
        cur=con.cursor()
        cur.execute("UPDATE category SET AssetType=?, AllocationDate=?, AllocationType=?, ValidTill=?, Department=?,AssetLocation=?  WHERE AssetSerialNumber=?",
                             ( assettype,  allocationDate, allocationType,validTill,assetserialnumber))
        con.commit()



        flash('Employee Details Updated','success')
        return redirect(url_for("index1"))
    con = pyodbc.connect(conn_str)
    cur=con.cursor()

    cur.execute("select * from category where AssetSerialNumber=?",(assetserialnumber,))
    data=cur.fetchone()
    return render_template("edit1.html",datas=data)



#deleting  assets

@app.route("/delete/<string:assetserialnumber>",methods=['GET'])
def delete(assetserialnumber):
 

        con = pyodbc.connect(conn_str)
        cur=con.cursor()
        cur.execute("delete from category where AssetSerialNumber=?",(assetserialnumber,))
        con.commit()
        # return redirect('/')
        # return render_template('delete.html')
        flash('Asset Details Deleted','warning')
        return redirect(url_for("index"))  




#the function for running the app


if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)
