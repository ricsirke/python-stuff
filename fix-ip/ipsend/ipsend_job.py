import ipgetter, requests

myip = ipgetter.myip()

url = "0.0.0.0"
payload = {'ip': myip}

resp = requests.post(url, data=payload)

print myip
print resp.status, resp.text