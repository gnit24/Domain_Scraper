import sys
import requests
from urllib.parse import urlparse

def check_domain(domain):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            print(f"{domain} returned status code 200")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {domain}")

def add_scheme(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme:
        return url
    else:
        return "https://" + url

def replace_or_append_tld(url, tld):
    parsed_url = urlparse(url)
    if parsed_url.netloc:
        return f"{parsed_url.scheme}://{parsed_url.netloc}{tld}"
    else:
        return url + tld

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    base_url = add_scheme(sys.argv[1])
  
  # Read TLDs from file
    with open("Domains.txt", "r") as file:
        tlds = file.read().splitlines()

    for tld in tlds:
        domain = replace_or_append_tld(base_url, tld)
        check_domain(domain)
