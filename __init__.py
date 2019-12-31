import requests
import smtplib
from bs4 import BeautifulSoup


class AirQuality:

    def scraper(self):

        result = requests.get('https://airnow.gov/index.cfm?action=airnow.local_city&cityid=327')
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        find_quality = soup.find(background="/images/aqi_mod_lg.gif").get_text()
        self.air_quality = int(find_quality)

    def email(self):

        if self.air_quality >= 101:
            e_alert = 'Air Quality is USG or above!', self.air_quality

        else:
            e_alert = 'All clear'

        gmail_user = '@gmail.com'
        gmail_pass = 'password'

        sent_from = '@gmail.com'
        to = ['@gmail.com']
        subject = 'Air Quality Alert!'
        body = e_alert


        email_text = '''
                From: %s
                To: %s
                Subject: %s

                %s
                 ''' % (sent_from, ', '.join(to), subject, body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_pass)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('sent!')


aq = AirQuality()
aq.scraper()
aq.email()
