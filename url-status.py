import requests #pip install requests
#this library is used to make HTTP requests in Python. It allows you to send HTTP requests and handle responses easily.
def check_url(url):
    try:
        response = requests.get(url, timeout=5) #sends a GET request to the specified URL with a timeout of 5 seconds. If the server does not respond within this time, it will raise an exception.
        return response.status_code
    except:
        return "Error"

urls = input("Enter URLs (comma separated): ").split(",")

print("\nResults:\n")

for url in urls:
    url = url.strip()
    status = check_url(url)
    print(f"{url} → {status}")