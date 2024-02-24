import requests


def get_country_ip(ip_address):
    api_url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        country = data.get("country", "Unknown")
        return country
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None


def get_public_ip():
    try:
        response = requests.get(r"http://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip", "Unknown")
        else:
            print(f"Error: Unable to fetch public IP. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


user_input = input("Enter an IP address (press Enter to use your public IP): ").strip()

if not user_input:
    ip_address = get_public_ip()
    print(f"Your public IP address: {ip_address}")
else:
    ip_address = user_input

country = get_country_ip(ip_address)
if country:
    print(f"The IP address {ip_address} is registered in {country}")
else:
    print("Country information not available")
