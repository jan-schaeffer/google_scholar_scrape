import requests 

def verify(emails):
    for email in emails:
        api_key = ""
        response = requests.get("https://isitarealemail.com/api/email/validate",
                                params={'email': email},
                                headers={'Authorization': "Bearer " + api_key})

        status = response.json()['status']
        if status == "valid":
            print("Mail found")
            return email
        else:
            continue