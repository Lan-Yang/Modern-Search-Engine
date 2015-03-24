import json
import urllib

api_key = open("api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
search_term = "Microsoft"
query = [{
  "/book/author/works_written": [{
    "a:name": None,
    "name~=": search_term
  }],
  "id":   None,
  "name": None,
  "type": "/book/author"
}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
print '+ author:'
for author in response['result']:
  print author['name']


query = [{
  "/organization/organization_founder/organizations_founded": [{
    "a:name": None,
    "name~=": search_term
  }],
  "id": None,
  "name": None,
  "type": "/organization/organization_founder"
}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
print '+ founder:'
for founder in response['result']:
  print founder['name']