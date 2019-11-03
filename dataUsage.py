from lxml import html
import requests
import smtplib
from email.message import EmailMessage

page = requests.get('https://center.vodafone.de/vfcenter/index.html')
tree = html.fromstring(page.content)
volumeList = tree.xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div[2]/div/div/div/strong/text()')
volumeAvailable = volumeList[0]
volumeAvailable = float((volumeAvailable[:-3]).replace(',','.'))
volumeConsumed = 200 - volumeAvailable
mailContent = "Data consumed until today: " + str(round(volumeConsumed,1)) + " GB\n\nData remaining for this month: " + str(volumeAvailable) + " GB"

contacts = [<emailID>]

msg = EmailMessage()
msg['Subject'] = 'Internet Status'
msg['From'] = 'Server'
msg['To'] = contacts
msg.set_content(mailContent)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(<emailID>,<password>)
    smtp.send_message(msg)
