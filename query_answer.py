import json
import urllib

api_key = open("api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
query = [{'author': None, 'name': 'Hobbit', 'type': '/book/author'}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for planet in response['result']:
  print planet['author']