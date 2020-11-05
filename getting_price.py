import smtplib
import re
import gettingPriceDB # Custom database script to get prices from the database
from bs4 import BeautifulSoup
import requests

# Libraries requests and BeautifulSoup are used to gather information for the app

# The server credentials
SERVEREMAIL='SERVEREMAIL'
SERVERPASS='SERVERPASSWORD'

# In headers user-agent is used to get information about the browser used.
# User-Agent can be found by searching in google "My user-agent"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

# url inputting in the function when called
def priceCheck(url):
#pageInfo stores all the information regarding the items
    pageInfo = requests.get(url, headers=headers)
#soup stores the information in html parser format
    soup = BeautifulSoup(pageInfo.content, 'html.parser')
#title stores the title of the product
    title = soup.find(id="productTitle").get_text()
#price stores the price of the items
    price = soup.find(id="priceblock_ourprice").get_text()
#converted price stores the first
    re.sub("\D", "", price)
    print(price)
    convertedPrice = float(price)

#checks if the new price is less than the old price of the item
#checks if the item is on sale
    oldPrice,userEmail=gettingPriceDB.gettingPAE(url)
    if (convertedPrice<oldPrice):
        sendEmail(title,price,url,userEmail)

    print(title.strip())
    print(price.strip())

#Establishes connection between the app and the user email.
def sendEmail(title, price, url, userEmail):
    # gmails smtp server address and smtp port number(TLS)
    server = smtplib.SMTP('smtp.gmail.com',587)
    # command sent by a server email to connect to another email
    server.ehlo()
    # command for connection
    server.starttls()
    server.ehlo()
    # login into the server
    email = SERVEREMAIL
    password = SERVERPASS
    server.login(email,password)

    #Messages to be sent to the user's email
    subject = 'Your item is on sale!'
    body = "Your item: "+title+" price dropped to "+price+". Make sure to not miss the sale!" \
                                                          "link: "+url
    messagetbs = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        #server email
        email,
        #user email
        userEmail,
        #Message to be sent
        messagetbs
    )
    print('Email has been successfully sent!')
    server.quit()
