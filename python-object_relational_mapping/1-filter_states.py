#!/usr/bin/python3
"""
Lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query with case-sensitive
    # search for 'N%'
    cursor.execute
    ("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows and print them
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
