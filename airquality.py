import requests
import smtplib
import emailconfig
from bs4 import BeautifulSoup


def scraper():

    result = requests.get('https://airnow.gov/index.cfm?action=airnow.local_city&cityid=327')
    soup = BeautifulSoup(result.content, 'lxml')

    find_quality = soup.find(background="/images/aqi_mod_lg.gif").get_text()
    air_quality = int(find_quality)
    
    return air_quality
   

def email():

    air_quality = scraper()
    if air_quality >= 101:
        e_alert = 'Air Quality is USG or above! Air Quality:', air_quality

    else:
        e_alert = 'Good or Moderate, Air Quality:', air_quality

    sent_from = '@gmail.com'
    to = ['@gmail.com']
    subject = 'Air Quality Alert!'
    body = e_alert

    email_text = f'''
                From: {sent_from}
                To: {to}
                Subject: {subject}

                {body}
                 '''

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(emailconfig.gmail_user,emailconfig.gmail_pass)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('sent!')


if __name__ == '__main__':
    scraper()
    email()
