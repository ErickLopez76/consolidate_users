from os import getenv
import pymssql


server = "10.21.32.12\SQLEXPRESS"
user = "sa"
password = "Ab123456"

cnn = pymssql.connect(server, user, password,"WCity")

cursor = cnn.cursor()
cursor.execute('select top 10 * from persona order by IDPerson')
row = cursor.fetchone()

while row:
    print(row[2])
    row = cursor.fetchone()

cnn.close()
