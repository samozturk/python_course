# pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name=None):
    """Establish a connection to the MySQL database."""
    connection = None
    try:
        if db_name:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=db_name
            )
        else:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password
            )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_table(connection):
    """Create a new table in the MySQL database."""
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
        cursor.execute(create_users_table)
        print("Users table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_user(connection, name, age):
    """Insert a new user into the users table."""
    insert_user_query = """
    INSERT INTO users (name, age) VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(insert_user_query, (name, age))
        connection.commit()  # Commit the changes to the database
        print("User inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def read_users(connection):
    """Read all users from the users table."""
    cursor = connection.cursor()
    read_users_query = "SELECT * FROM users;"
    
    try:
        cursor.execute(read_users_query)
        users = cursor.fetchall()  # Fetch all records from the executed query
        for user in users:
            print(user)
    except Error as e:
        print(f"The error '{e}' occurred")

# Set up connection parameters
host = "localhost"         # Change this to your host
user = "your_username"     # Change this to your MySQL username
password = "your_password" # Change this to your MySQL password
database = "test_db"       # Change this to your database name

# Connect to the database
connection = create_connection(host, user, password, database)

# Create the users table
create_table(connection)

# Insert users
insert_user(connection, "Alice", 30)
insert_user(connection, "Bob", 25)

# Read users
read_users(connection)

# Close the connection
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed")
