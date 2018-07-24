#!/usr/bin/python
#testscript.py
#a python script to talk to db
import MySQLdb
db = MySQLdb.connect(host="172.17.0.2” , user="root", passwd="Hashmap@1", db="testdb")
#create a cursor
cursor = db.cursor()
#execute query
cursor.execute("SELECT FirstName,LastName from testdb.NameList")
#iteration
for row in cursor.fetchall() :
 #data from rows
   FirstName = str(row[0])
   LastName = str(row[1])
#print
   print " The Person Name is "+FirstName + " " +LastName
#close
cursor.close()
#close dbconnection
db.close()

