import whois


def whois_lookup(query):
    try:
        result = whois.whois(query)
        return result
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    user_input = input("Enter an IP address or host address: ")
    print(whois_lookup(user_input))
