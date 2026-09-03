import whois

domain = input("Enter domain name: ")

try:
    information = whois.whois(domain)

    print("\nWHOIS Information")
    print("--------------------------------")

    print("Domain Name :", information.domain_name)
    print("Registrar   :", information.registrar)
    print("Creation Date :", information.creation_date)
    print("Expiration Date :", information.expiration_date)
    print("Name Servers :", information.name_servers)
    print("Status :", information.status)

except Exception as e:
    print("Unable to retrieve WHOIS information.")
    print("Error:", e)
