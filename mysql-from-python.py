import os
import pymysql

username = os.getenv("C9_USER")

connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")

try:
    with connection.cursor() as cursor:
        list_of_names = ["Jim", "Bob"]
        format_strings = ",".join(["%s"]*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});"
                       .format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()
