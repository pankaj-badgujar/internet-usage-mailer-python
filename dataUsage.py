from lxml import html
import requests
import smtplib
from email.message import EmailMessage

page = requests.get('https://center.vodafone.de/vfcenter/index.html')
tree = html.fromstring(page.content)
volumeList = tree.xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div[2]/div/div/div/strong/text()')
print(volumeList)
# volume = volumeList[0]

# contacts = ['badgujarpankaj24@gmail.com']
#
# msg = EmailMessage()
# msg['Subject'] = 'Internet Usage'
# msg['From'] = 'Server'
# msg['To'] = contacts
# msg.set_content(volume)
#
# with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
#     smtp.login('badgujarpankaj24@gmail.com','Usa@2019')
#     smtp.send_message(msg)
