import json
import urllib

entity_dic = {'/people/person':'Person', '/book/author':'Author', '/film/actor':'Actor', '/tv/tv_actor':'Actor', '/organization/organization_founder':'BusinessPerson', '/business/board_member':'BusinessPerson', '/sports/sports_league':'League', '/sports/sports_team':'SportsTeam', '/sports/professional_sports_team':'SportsTeam'}

# utilize search API to get 'mid'
mid = []
api_key = open("api_key").read()
query = 'Bill Gates'
search_url = 'https://www.googleapis.com/freebase/v1/search'
params = {
        'query': query,
        'key': api_key
}
url = search_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for result in response['result']:
	mid.append(str(result['mid']))

# pass 'mid' to topic API
topic_url = 'https://www.googleapis.com/freebase/v1/topic'
found = False
count = 0
type_set = set()
topic_id = mid[0]
# print topic_id
# params = {
#   'key': api_key,
#   'filter': 'all'
# }
# url = topic_url + topic_id + '?' + urllib.urlencode(params)
# topic = json.loads(urllib.urlopen(url).read())
# with open('json','w') as fout:
# 	print >> fout, urllib.urlopen(url).read()

while (found == False) & (count < len(mid)):
	topic_id = mid[count]
	print mid[count]
	params = {
	  'key': api_key,
	  'filter': 'all'
	}
	url = topic_url + topic_id + '?' + urllib.urlencode(params)
	topic = json.loads(urllib.urlopen(url).read())

	# get 'id' in '/type/object/type'
	for property in topic['property']:
		# top level of '/type/object/type' property
		if property == '/type/object/type':
			for value in topic['property'][property]['values']:
				if entity_dic.has_key(str(value['id'])):
					found = True
					type_set.add(entity_dic.get(str(value['id'])))
				else:
					count = count + 1
			break

print type_set
