import json
import urllib

def cal_whitespace(a, b):
	whitespace = ''

	for i in range(len(a) - len(b)):
		whitespace += ' '

	return whitespace

def extract_person():
	for property in topic['property']:
		try:
			if property == '/type/object/name':
				print temp
				name = topic['property'][property]['values'][0]['text']
				name = '\t' + '| Name:           '  + name 
				whitespace = cal_whitespace(temp, name)[:-2]
				print name + whitespace + '|' + '\t'

			if property == '/people/person/date_of_birth':
				print temp
				birth_date = topic['property'][property]['values'][0]['text']
				birth_date = '\t' + '| Birthday:       ' + birth_date
				whitespace = cal_whitespace(temp, birth_date)[:-2]
				print birth_date + whitespace + '|' + '\t'

			if property == '/people/person/place_of_birth':
				print temp
				birth_place = topic['property'][property]['values'][0]['text']
				birth_place = '\t' + '| Place of birth: ' + birth_place
				whitespace = cal_whitespace(temp, birth_place)[:-2]
				print birth_place + whitespace + '|' + '\t'

			if property == '/common/topic/description':
				print temp
				descriptions = topic['property'][property]['values'][0]['value']
				descriptions = ' Descriptions:   ' + descriptions
				descriptions = descriptions.replace("\n", " ")
				if len(descriptions)<len(temp):
					whitespace = cal_whitespace(temp, descriptions)[:-4]
					print '\t' + '|' + descriptions + whitespace + '|'
				else:
					print '\t' + '|' + descriptions[:len(temp)-4] + '|'
					descriptions = descriptions[-(len(descriptions)-(len(temp)-4)):]

					while len(descriptions) > len(temp):
						print '\t' + '|                 ' + descriptions[:len(temp)-21] + '|'
						descriptions = descriptions[-(len(descriptions)-(len(temp)-21)):]

					if len(descriptions)>0 and len(descriptions)<len(temp):
						descriptions = '\t' + '|                 ' + descriptions
						whitespace = cal_whitespace(temp, descriptions)[:-2]
						print descriptions + whitespace + '|'

			if property == '/people/person/sibling_s':
				print temp
				for i in range(int(topic['property'][property]['count'])):
					sibling = topic['property'][property]['values'][i]['property']['/people/sibling_relationship/sibling']['values'][0]['text']
					if i == 0:
						sibling = '\t' + '| Siblings:       ' + sibling
					else:
						sibling = '\t' + '|                 ' + sibling
					whitespace = cal_whitespace(temp, sibling)[:-2]
					print sibling + whitespace + '|' + '\t'

		except KeyError:
			pass

def extract_author():
	for property in topic['property']:
		try:
			if property == '/book/author/works_written':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					book = item['text']
					if count == 1:
						book = '\t' + '| Books:          ' + book
					else:
						book = '\t' + '|                 ' + book  
					if len(book)>91:
						about = about[0:91] + "..."
					whitespace = cal_whitespace(temp, book)[:-2]
					print book + whitespace + '|' + '\t'

			if property == '/book/book_subject/works':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					about = item['text']
					if count == 1:
						about = '\t' + '| Books about:    ' + about
					else:
						about = '\t' + '|                 ' + about  
					if len(about)>91:
						about = about[0:91] + "..."
					whitespace = cal_whitespace(temp, about)[:-2]
					print about + whitespace + '|' + '\t'
			

		except KeyError:
			pass

def extract_actor():
	print temp
	print '\t' + "| Films:         |Character                              | Film Name                               |"
	print '\t' + "|                ----------------------------------------------------------------------------------"

	for property in topic['property']:
		try:
			if property == '/film/actor/film':
				for item in topic['property'][property]['values']:
					character = item['property']['/film/performance/character']['values'][0]['text']
					film = item['property']['/film/performance/film']['values'][0]['text']
					whitespace1 = ''
					for i in range(39 - len(character)):
						whitespace1 += ' '
					whitespace2 = ''
					for i in range(40 - len(film)):
						whitespace2 += ' '
					print '\t' + "|                |" + character + whitespace1 + "| " + film + whitespace2 + '|' + '\t'

		except KeyError:
			pass


def extract_businessperson():
	pass

def extract_league():
	pass

def extract_sportsteam():
	pass


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

while found == False and count < len(mid):
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

			if not found:
				count += 1

temp = '\t' + " -------------------------------------------------------------------------------------------------- " + '\t'
print temp

line = query + '('

for item in type_set:
	line += item + ", "

line = line[:-2]

line += ')'

whitespace = ''

for i in range((len(temp) - len(line) -4)/2):
	whitespace += ' ' 

line = '\t' + '|' + whitespace + line + whitespace + '|' + '\t'

print line

for item in type_set:
	if item == 'Person':
		extract_person()
	if item == 'Actor':
		extract_actor()
	if item == 'Author':
		extract_author()
	if item == 'BusinessPerson':
		extract_businessperson()
	if item == 'League':
		extract_league()
	if item == 'SportsTeam':
		extract_sportsteam()





	
