import psycopg2
cnn = psycopg2.connect("dbname=SIS host=10.21.37.19 user=postgres password=postgresql")

cur = cnn.cursor()


cur.execute("select name from res_partner")
print(cur.rowcount )
row = cur.fetchone()
while row:
    print(row[0])
    row = cur.fetchone()
    

cnn.close()