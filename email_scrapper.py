import requests
from bs4 import BeautifulSoup
import re

def scrape_emails_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)
        unique_emails = set(emails)
        return unique_emails
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return None


#  usage
url = input("Enter the website URL: ")
emails = scrape_emails_from_website(url)

if emails:
    print(f"Email addresses found: {emails}")
    print(emails)
else:
    print("No email addresses found.")