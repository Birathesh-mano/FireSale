import psycopg2
import re
from bs4 import BeautifulSoup
import requests
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

def addItem(url,email):
    # In headers user-agent is used to get information about the browser used.
    # User-Agent can be found by searching in google "My user-agent"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    # url inputting in the function when called
    # pageInfo stores all the information regarding the items
    pageInfo = requests.get(url, headers=headers)
    # soup stores the information in html parser format
    soup = BeautifulSoup(pageInfo.content, 'html.parser')
    # title stores the title of the product
    title = soup.find(id="productTitle").get_text( )
    # price stores the price of the items
    price = soup.find(id="priceblock_ourprice").get_text( )
    # converted price stores the first
    re.sub("\D", "", price)
    print(price)
    convertedPrice = float(price)
    cur.execute("INSERT INTO items(link, email,price) VALUES("+"'"+url+"'"+","+"'"+email+"'"+","+"'"+convertedPrice+"')")
    cur.close()
    conn.close()