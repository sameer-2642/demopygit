# pymysql is a library in Python that allows you to connect to a MySQL database and perform various operations such as executing SQL queries,
# retrieving data, and managing the database. In this code snippet, we are connecting to a MySQL database using pymysql, 
# executing a query to show all databases, and printing the results.

import pymysql

# Connect to the MySQL database using the provided host, user, and password.
mydb = pymysql.connect(host = "localhost",user = "root",password = "root",database = "company")

# Create a cursor object which allows us to execute SQL queries and fetch results from the database.
mycursor = mydb.cursor()

# Execute the SQL query "show databases" to retrieve a list of all databases available in the MySQL server.
mycursor.execute("select * from department")

# Fetch all the results returned by the executed query and store them in the variable 'results'.
results = mycursor.fetchall()

# Iterate through the results returned by the query and print each database name. 
# The results are returned as a list of tuples, where each tuple contains the name of a database.
for i in results:
    print(i)
