from ipwhois import IPWhois


def whois_lookup(query):
    try:
        ipwhois = IPWhois(query)
        result = ipwhois.lookup_rdap()
        return result
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    user_input = input("Enter an IP address or host address: ")
    result = whois_lookup(user_input)
    if isinstance(result, dict):
        print("WHOIS Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)