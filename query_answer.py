import json
import urllib

question = raw_input('Input your question like "Who created [X]?", X is a book name or a company name: ')
question = question.split()
length = len(question)
if (question[0].lower() != 'who' or question[1].lower() != 'created' or question[-1][-1] != '?'):
	print 'Wrong input format!'
	exit(1)

search_term = ' '.join(question[2:])
search_term = search_term[:-1]
print 'search_term: ' + search_term
api_key = open("api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
# search_term = "Microsoft"
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