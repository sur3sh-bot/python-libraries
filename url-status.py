import requests #requests library is used to make http requests to get data from APIs

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "Error"