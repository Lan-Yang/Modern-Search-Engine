import json
import urllib

# User input question in the format "Who created [X]?"
question = raw_input('Input your question like "Who created [X]?", X is a book name or a company name: ')
question = question.split()
length = len(question)
result_list = []

# Check input question's format
if (question[0].lower() != 'who' or question[1].lower() != 'created' or question[-1][-1] != '?'):
	print 'Wrong input format!'
	exit(1)

# Get [X]
search_term = ' '.join(question[2:])
search_term = search_term[:-1]
api_key = open("api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

# Treat X as substring of a book name, search its author's name
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

# Format output result in the format "A (as XXX) created <X1>, <X2>, ... and <Xn>."
for author in response['result']:
  tmp_list = []
  tmp_str = ''
  tmp_length = 0
  name = author['name']
  for book in author["/book/author/works_written"]:
    tmp_list.append(book['a:name'])
  tmp_length = len(tmp_list)
  tmp_str = '%s (as Author) created <%s>' % (name, tmp_list[0])
  tmp_length = tmp_length - 1
  while (tmp_length > 1):
    tmp_str = tmp_str + ', <%s>' % tmp_list[len(tmp_list) - tmp_length]
    tmp_length = tmp_length - 1
  if (tmp_length > 0):
    tmp_str = tmp_str + ' and <%s>.' % tmp_list[len(tmp_list) - tmp_length]
  result_list.append(tmp_str)

# Treat X as substring of a company name, search its businessperson's name
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

# Format output result in the format "A (as XXX) created <X1>, <X2>, ... and <Xn>."
for businessperson in response['result']:
  tmp_list = []
  tmp_str = ''
  tmp_length = 0
  name = businessperson['name']
  for company in businessperson["/organization/organization_founder/organizations_founded"]:
    tmp_list.append(company['a:name'])
  tmp_length = len(tmp_list)
  tmp_str = '%s (as BusinessPerson) created <%s>' % (name, tmp_list[0])
  tmp_length = tmp_length - 1
  while (tmp_length > 1):
    tmp_str = tmp_str + ', <%s>' % tmp_list[len(tmp_list) - tmp_length]
    tmp_length = tmp_length - 1
  if (tmp_length > 0):
    tmp_str = tmp_str + ' and <%s>.' % tmp_list[len(tmp_list) - tmp_length]
  result_list.append(tmp_str)

# Sort lines alphabetically by <Name>
result_list.sort()

# Display result
for each_result in result_list:
  print each_result