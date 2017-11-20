import requests
from bs4 import BeautifulSoup
import time
import smtplib
import email.utils
from email.mime.text import MIMEText

def send_email():
    subject = 'Delayed Metrolink'
    text = 'Please visit the metrolink app.'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    fromaddr = 'delayed.metrolink@gmail.com'
    toaddrs  = ['khadija.alselini@gmail.com']
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server.starttls()
    server.login('delayed.metrolink@gmail.com', '1029384756Dm!')
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()

while True:
    url = "http://www.metrolink.co.uk/Pages/default.aspx"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    if str(soup).find('Minor Delays'):
        send_email()
        break

