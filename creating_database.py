import psycopg2

# Credentials for the database
hostIP='localhost'
portNumber='5432'
databaseName='postgres'
username='postgres'
pas='password'

# Establishes connection to the database
try:
    print("Creating the database...")
    conn=psycopg2.connect(host=hostIP, port=portNumber, database=databaseName, user=username, password=pas)
    #Creates a cursor object
    cur=conn.cursor()
    print("Database is connected successfully!")
except:
    print("There was an error in connecting to the database.\ Please check the credentials")

# Makes a table in the database
try:
    print("Creating tables in the database...")
    cur.execute("CREATE TABLE Items("
                "item_id INT PRIMARY KEY,"
                "link VARCHAR,"
                "email VARCHAR,"
                "price VARCHAR);")
    conn.commit()
    print("Tables have been made successfully")
except:
    print("There was a problem in creating the tables")

# Closing the connection to the database
cur.close()
conn.close()
