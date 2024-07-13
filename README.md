# Automated OSINT Tool

## Installation Guide

Follow these steps to install and run the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/SmartyDroidBot/AutOSINT.git
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the web application:
   ```bash
   python3 app.py
   ```

Feel free to explore, contribute, and stay tuned for exciting updates!

## Abstract

This project is an evolving Open Source Intelligence (OSINT) tool designed to automate data collection, enrichment, analysis, and visualization. Currently, the tool focuses on domain, phone number, email, IP, and geolocation lookups through a combination of Abstract API, WHOIS lookup, and web scraping. The future roadmap includes a comprehensive set of features for investigators and analysts. The tool is built on Flask, providing a professional and user-friendly web application experience.

## Implemented Features

### 1. Current Functionality

- **Domain Lookup**: Obtain detailed information about a domain using Abstract API, WHOIS lookup, and web scraping techniques.
- **Phone Number Lookup**: Gather information related to a phone number through various online sources.
- **Email Lookup**: Retrieve details associated with an email address using Abstract API and web scraping.
- **IP and Geo Location Lookup**: Collect data about an IP address and its geographical location using Abstract API, WHOIS lookup, and web scraping.

### 2. Report Generation

- **PDF Report Download**: Generate and download detailed reports in PDF format for the information obtained.

## Future Upgradation Plans

### 1. Automated Data Collection

- Develop modules for automated data collection from various online sources, including social media, websites, forums, and public databases.

### 2. Data Enrichment and Correlation

- Implement algorithms to automatically enrich collected data and correlate information from different sources.

### 3. Scheduled Scans

- Enable users to schedule regular scans for continual monitoring based on predefined queries.

### 4. Alerts and Notifications

- Implement an alerting system for notifying users when new relevant information is found.

### 5. Geolocation and Mapping

- Integrate geolocation features for visualizing and mapping collected data.

### 6. Natural Language Processing (NLP)

- Incorporate NLP capabilities to analyze and extract insights from unstructured text data.

### 7. Anonymity and Privacy Measures

- Implement features to ensure user privacy and anonymity during data collection.

### 8. Custom Plugins and Extensibility

- Allow users to develop custom plugins or scripts to extend the tool's functionality.

### 9. API Integrations

- Provide API integrations with popular OSINT data sources for a wider range of information.

### 10. Credential Monitoring

- Include features for monitoring and alerting users about compromised credentials.

### 11. Dark Web Monitoring

- Integrate capabilities to monitor the dark web for relevant information.

### 12. Case Automation Workflows

- Allow users to create and automate workflows for specific investigation scenarios.

### 13. Reporting and Evidence Packaging

- Generate detailed reports and package evidence for legal or law enforcement purposes.

### 14. Historical Data Archiving

- Implement a system for archiving historical data to track changes and patterns over time.

### 15. Cross-Platform Compatibility

- Ensure compatibility with various operating systems for flexibility in deployment.

### 16. Resource Usage Optimization

- Optimize resource usage, especially during large-scale data collection processes.

### 17. Intuitive Command-Line Interface (CLI)

- Provide a user-friendly command-line interface for scripting and automation.

### 18. Community and Documentation

- Foster a community around the tool with forums, documentation, and tutorials for user support and collaboration.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
