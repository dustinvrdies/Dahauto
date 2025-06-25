import random
import string

def claim_from_faucets(faucets, credentials):
    results = []
    for faucet in faucets:
        results.append({
            "site": faucet['name'],
            "url": faucet['url'],
            "status": "Claimed",
            "amount": "random"
        })
    return results

def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"

def sign_up_to_faucet(site):
    new_email = generate_random_email()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return {
        "email": new_email,
        "password": password,
        "status": "Signed up"
    }

def sign_up_to_all(faucets):
    credentials = {}
    for site in faucets:
        credentials[site['name']] = sign_up_to_faucet(site)
    return credentials
