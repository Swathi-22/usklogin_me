import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic YXBpOllPVVJfQVBJX0tFWQ=="


resp = requests.get(url, headers=headers)

print(resp.status_code)
