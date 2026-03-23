import requests #requests library is used to make http requests to get data from APIs

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "Error"
    urls = input("Enter URLs (comma separated): ").split(",")

print("\nResults:\n")

for url in urls:
    url = url.strip()
    status = check_url(url)
    print(f"{url} → {status}")