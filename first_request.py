import requests

# url = "http://www.google.com"
# response = requests.get(url)

# print(f"Your request to {url} came back w/ status code {response.status_code}")
url = "https://icanhazdadjoke.com/"

res = requests.get(url, headers={"Accept": "application/json"})
print(type(res.text))
data = res.json()
print(type(data))
print(data["joke"])
