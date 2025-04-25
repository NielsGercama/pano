import requests

url = 'https://nielsgercama.github.io/pano/myEndpoint'
query = {'hello': "something"}
res = requests.post(url, data=query)
print(res.text)
