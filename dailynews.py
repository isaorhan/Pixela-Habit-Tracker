import requests
from bs4 import BeautifulSoup
headers = {
"Accept-Language" : "en-US,en;q=0.5",
"User-Agent": "Defined",
}
webpage = requests.get("https://news.ycombinator.com/", headers=headers)
webpage.raise_for_status()
ycwebpage = webpage.text
soup = BeautifulSoup(ycwebpage, "html.parser")
ac = soup.find_all(name="span", class_="titleline")
message = """"""

for a in ac:
    message += f"\n{a.text} * Check the details:{a.findNext('a').get('href')}\n\n"

EMAIL = str('YOUR GMAIL')
PASSWORD = str('YOUR APP PASSWORD')
RECEIVER = str('RECEIVER MAIL ADDRESS')

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    msge = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, msge.encode("utf-8"))
    server.close()

send_email(EMAIL, PASSWORD, RECEIVER, "Daily News", message)
