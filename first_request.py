import requests

# url = "http://www.google.com"
# response = requests.get(url)

# print(f"Your request to {url} came back w/ status code {response.status_code}")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
  url,
  headers={"Accept": "application/json"},
  params={'term': "cat", "limit": 1}
 )
# print(type(res.text))
data = res.json()
print(data['results'])
# print(type(data))
# print(data["joke"])
# print(f"status: {data['status']}")
