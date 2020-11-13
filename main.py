import requests
import sys

args = sys.argv
url = args[1]

headers={"accept":"application/activity+json"}

response = requests.get(url,headers=headers)
print(response.text)
