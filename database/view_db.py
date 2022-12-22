import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  #could have port here to identify correct server
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("USE test")
mycursor.execute("SELECT * FROM person")

for row in mycursor:
  print(row)