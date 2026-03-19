import requests #pip install requests
#requests library is used to make http requests to get data from APIs

def convert_currency():
    # We use a public API to get live rates
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extracting the conversion rates dictionary
        rates = data['rates']
        
        print("--- Real-Time Currency Converter ---")
        amount = float(input("Enter amount in USD: "))
        target_curr = input("Enter target currency (e.g., EUR, GBP, INR): ").upper()

        if target_curr in rates:
            # The calculation: v = a * r
            converted_amount = amount * rates[target_curr]
            print(f"\n{amount} USD is equal to {converted_amount:.2f} {target_curr}")
            print(f"Current Rate: 1 USD = {rates[target_curr]} {target_curr}")
        else:
            print("Currency not found!")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

convert_currency()
#currently this code converts usd to other currency. will modify it to convert from any currency in future