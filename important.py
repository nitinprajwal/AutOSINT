import requests
from bs4 import BeautifulSoup
import json

def scrape_whois(domain):
    url = f"https://www.whois.com/whois/{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    raw_data_div = soup.find('div', class_='df-block-raw')
    if raw_data_div:
        raw_data = raw_data_div.find('pre', class_='df-raw')
        if raw_data:
            return raw_data.text.strip()

    return None

def parse_whois(raw_data):
    if raw_data:
        lines = raw_data.split('\n')
        whois_info = {}
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if value != "REDACTED FOR PRIVACY":
                    whois_info[key] = value
        return whois_info

    return None

def main():
    domain = input("Enter domain name: ")
    raw_data = scrape_whois(domain)
    whois_info = parse_whois(raw_data)
    if whois_info:
        print(json.dumps(whois_info, indent=4))
    else:
        print("Failed to retrieve WHOIS information.")

if __name__ == "__main__":
    main()
