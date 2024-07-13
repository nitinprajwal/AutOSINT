from flask import Flask, render_template, request, session, send_file,url_for,redirect
import requests
import re
import json
from bs4 import BeautifulSoup
from fpdf import FPDF

app = Flask(__name__)

default_email_api_key = "015b6138b5ba4072a2e2aef6b8d08af2"
default_phone_api_key = "282c43000dbc482ca089d26f7466cb4e"
default_ip_api_key = "634da9cfe64743fe8978d94f8d8d4ba9"

# Replace these keys with your actual API keys
email_api_key = "015b6138b5ba4072a2e2aef6b8d08af2"
phone_api_key = "282c43000dbc482ca089d26f7466cb4e"
ip_api_key = "634da9cfe64743fe8978d94f8d8d4ba9"

@app.route('/')
def index():
    return render_template('index.html')

def index():
    return render_template('index.html')

@app.route('/settings', methods=['GET', 'POST'])  # Allow both GET and POST requests
def settings():
    if request.method == 'POST':
        session['eapi'] = request.form.get('eapi', default_email_api_key)
        session['papi'] = request.form.get('papi', default_phone_api_key)
        session['iapi'] = request.form.get('iapi', default_ip_api_key)
    return redirect(url_for('index'))

    return render_template('settings.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    result = None
    email_api_key = session.get('eapi', default_email_api_key)
    phone_api_key = session.get('papi', default_phone_api_key)
    ip_api_key = session.get('iapi', default_ip_api_key)

    if request.method == 'POST':
        input_value = request.form['query']

        if re.match(r"[^@]+@[^@]+\.[^@]+", input_value):
            result = email_validation(input_value, email_api_key)
        elif re.match(r"^\+?\d+$", input_value):
            result = phone_validation(input_value, phone_api_key)
        elif re.match(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                  r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                  r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                  r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$", input_value):    
            result = ip_geolocation(input_value, ip_api_key)
        elif re.match(r"^(?:[-A-Za-z0-9]+\.)+[A-Za-z]{2,6}$", input_value):
            result = whois(input_value)
            

    return render_template('search.html', result=result)

def email_validation(email, api_key):
    url = f'https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}'
    response = requests.get(url)
    return response.json()

def phone_validation(phone, api_key):
    url = f'https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone}'
    response = requests.get(url)
    return response.json()

def ip_geolocation(ip, api_key):
    url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip}'
    response = requests.get(url)
    return response.json()

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

def whois(domain):
    raw_data = scrape_whois(domain)
    whois_info = parse_whois(raw_data)
    if whois_info:
        return whois_info
    else:
        return {}  # Return an empty dictionary if WHOIS information is not available


@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        data = {}
        for key in request.form:
            if key != 'csrf_token':  # Exclude CSRF token
                data[key] = request.form[key]
        
        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        for key, value in data.items():
            pdf.cell(200, 10, txt = f"{key}: {value}", ln=True)
        pdf_output = "search_results.pdf"
        pdf.output(pdf_output)
        
        # Return the PDF file as a download
        return send_file(pdf_output, as_attachment=True)
    

if __name__ == "__main__":
    app.run(debug=True)