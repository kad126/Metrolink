#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from urlparse import urlparse
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

host, port = urlparse(os.environ["http_proxy"]).netloc.split(":")
Connection.set_proxy_info(
    host,
    int(port),
    proxy_type=PROXY_TYPE_HTTP,
)

from twilio.rest import TwilioRestClient

def send_text():
     login = 'ACe21a93021e1c8696a5bb2ac549b476e0'
     password = '646dd7f5cc71abf725c28b5e4378a71e'
     client = TwilioRestClient(login, password )
     client.messages.create(from_='+441543624730', to='+447741521172', body ='Please visit the metrolink app.')
    

while True:
    url = "http://www.metrolink.co.uk/Pages/default.aspx"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    if str(soup).find('Minor Delays'):
        print('No delays')

    else:
        send_text()
    break
