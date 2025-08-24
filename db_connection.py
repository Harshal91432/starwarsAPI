"""
user : root
password : root password
host : 127.0.0.1
port : 3306
database : starwarsDB
"""


import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='harsh_root',
                             database='starwarsDB',
                             cursorclass=pymysql.cursors.DictCursor)

breakpoint()
cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
results = cursor.fetchall()
for result in results:
    print(result)



