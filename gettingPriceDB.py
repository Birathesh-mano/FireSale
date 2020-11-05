import psycopg2
## ASSUMPTION URL AND EMAIL CORRELATION IS 1-1
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

#Function to return the old price
def gettingPAE(url):
    cur.execute("SELECT price FROM items WHERE link="+"'"+url+"'")
    oldPriceD=cur.fetchone()
    oldPrice=float(oldPriceD[0])
    cur.execute("SELECT email FROM items WHERE link="+"'"+url+"'")
    emailD=cur.fetchone()
    email=str(emailD[0])
    cur.close()
    conn.close()
    return oldPrice,email
