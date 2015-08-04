import requests
payload = {"cardID":"750047FB76BF"}
print payload
r = requests.post("http://127.0.0.1:5000/index", data=payload)
