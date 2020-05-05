import mysql.connector

a = mysql.connector.connect(host="localhost:1407",user="root",password="psycho")
mycursor = a.cursor()
mycursor.execute('show databases')

for x in mycursor:
	print(x)