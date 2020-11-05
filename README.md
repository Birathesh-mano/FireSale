# SaleMyCart

Sends notifcation when the price of desired amazon product reduces

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar, requests, bs4 (BeautifulSoup), pyscopg2, and smtplib.

```bash
pip install foobar
```
```bash
pip install requests
```
```bash
pip install bs4
```
```bash
pip install smtplib
```
```bash
pip install pscopg2
```
## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```
```python
import requests
headers = {'User-Agent':'info about the browsers'} # A dictionary which holds the user agent and the browser info
url = 'url' # holds the url targetted
requests.get(url, headers=headers) # does a HTTP request
```
```python
from bs4 import BeautifulSoup

headers = {'User-Agent':'info about the browsers'} # A dictionary which holds the user agent and the browser info
BeautifulSoup(responseFromRequest.content,'htm.parser') # returns the html format of the url page requested
```
```python
import smtplib
smtplib.SMTP('email server address',portNumber) #returns the server information
server.ehlo() # command sent by a server email to connect to another email
server.startls() # command to make a connection
server.ehlo()
server.login(email,password) # logs into the server for a sender
server.sendmail(senderEmail,recieverEmail,message) # method to send the email with the content from the sender to reciever
server.quit() # closes the connection

```
```python
import psycopg2
conn=psycopg2.connect(host='HostIPAddress', port = 'Port number', database='database name', user='username', password='password') # starts a connections with the database
cur= conn.cursor() # cursor object
cur.execute("command") # executes command in the database
conn.commit() # commits the command in the database
cur.close() # closes the cursor object
conn.close() # closes the connection
```
## Contributors
- [Kian Salehi](https://github.com/KianSalehi)
- [Kish Dubey](https://github.com/kishdubey)
