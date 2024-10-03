# Import required libraries
# mysql-connector-python is a MySQL driver for Python
# pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name=None):
    """Establish a connection to the MySQL database."""
    connection = None
    try:
        # If a database name is provided, connect to that specific database
        if db_name:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=db_name
            )
        # If no database name is provided, connect to the MySQL server without selecting a database
        else:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password
            )
        print("Connection to MySQL DB successful")
    except Error as e:
        # If an error occurs during connection, print the error message
        print(f"The error '{e}' occurred")

    return connection

def create_table(connection):
    """Create a new table in the MySQL database."""
    # SQL query to create a 'users' table if it doesn't already exist
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT, 
        name TEXT NOT NULL, 
        age INT,
        PRIMARY KEY (id)
    ); 
    """
    cursor = connection.cursor()
    try:
        # Execute the SQL query to create the table
        cursor.execute(create_users_table)
        print("Users table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_user(connection, name, age):
    """Insert a new user into the users table."""
    # SQL query to insert a new user, using placeholders for values
    insert_user_query = """
    INSERT INTO users (name, age) VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        # Execute the SQL query with the provided name and age
        cursor.execute(insert_user_query, (name, age))
        # Commit the changes to the database to make them permanent
        connection.commit()
        print("User inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def read_users(connection):
    """Read all users from the users table."""
    cursor = connection.cursor()
    # SQL query to select all users from the table
    read_users_query = "SELECT * FROM users;"
    
    try:
        # Execute the SQL query
        cursor.execute(read_users_query)
        # Fetch all records returned by the query
        users = cursor.fetchall()
        # Print each user record
        for user in users:
            print(user)
    except Error as e:
        print(f"The error '{e}' occurred")

# Database connection parameters
host = "localhost"         # The server hosting the MySQL database
user = "your_username"     # Your MySQL username
password = "your_password" # Your MySQL password
database = "test_db"       # The name of the database you want to connect to

# Establish a connection to the database
connection = create_connection(host, user, password, database)

# Create the users table in the database
create_table(connection)

# Insert sample users into the table
insert_user(connection, "Alice", 30)
insert_user(connection, "Bob", 25)

# Retrieve and display all users from the table
read_users(connection)

# Close the database connection
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed")