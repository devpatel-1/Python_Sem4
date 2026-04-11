# Write a python code to establish connection with MySQL and create database demo_data. Also display list of all the available database.

import mysql.connector

# Step 1: Create connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"   # use your MySQL password
)

print("Connected successfully!")

# Step 2: Create cursor
mycursor = mydb.cursor()

# Step 3: Create database
mycursor.execute("CREATE DATABASE demo_data")
print("Database 'demo_data' created")

# Step 4: Show all databases
mycursor.execute("SHOW DATABASES")

print("\nList of Databases:")
for db in mycursor:
    print(db)