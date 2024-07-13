import json
import requests

TARGET_COUNT = "60"

def lookup_username(username):
    url = "https://social-scanner.p.rapidapi.com/social-scan/"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "d21463b5a4msh3b5315baac058b3p192d0ajsnd8593706082c",
        "X-RapidAPI-Host": "social-scanner.p.rapidapi.com"
    }
    payload = {
        "username": username,
        "target_count": TARGET_COUNT
    }
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.text)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def format_output(results):
    formatted_results = []
    for item in results['detected']:
        formatted_item = {
            'type': item['type'],
            'country': item['country'],
            'language': item['language'],
            'link': item['link']
        }
        formatted_results.append(formatted_item)
    return json.dumps(formatted_results, indent=4)

def main():
    username = input("Enter the username to lookup: ")
    result = lookup_username(username)
    if result:
        formatted_result = format_output(result)
        print(formatted_result)
    else:
        print("No results found or an error occurred.")

if __name__ == "__main__":
    main()
