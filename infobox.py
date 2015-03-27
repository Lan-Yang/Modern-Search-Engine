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

			if property == '/people/deceased_person/date_of_death':
				print temp
				date_of_death = topic['property'][property]['values'][0]['text']
				date_of_death = '\t' + '| Date of Death:  '  + date_of_death 
				whitespace = cal_whitespace(temp, date_of_death)[:-2]
				print date_of_death + whitespace + '|' + '\t'

			if property == '/people/deceased_person/place_of_death':
				print temp
				place_of_death = topic['property'][property]['values'][0]['text']
				place_of_death = '\t' + '| Place of Death: '  + place_of_death 
				whitespace = cal_whitespace(temp, place_of_death)[:-2]
				print place_of_death + whitespace + '|' + '\t'

			if property == '/people/deceased_person/cause_of_death':
				print temp
				cause_of_death = topic['property'][property]['values'][0]['text']
				cause_of_death = '\t' + '| Cause of Death: '  + cause_of_death 
				whitespace = cal_whitespace(temp, cause_of_death)[:-2]
				print cause_of_death + whitespace + '|' + '\t'

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

			if property == '/people/person/spouse_s':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					name = item['property']['/people/marriage/spouse']['values'][0]['text']

					try:
						location = item['property']['/people/marriage/location_of_ceremony']['values'][0]['text']
					except (KeyError, IndexError):
						location = ''

					from_year = item['property']['/people/marriage/from']['values'][0]['text']
					try:
						to_year = item['property']['/people/marriage/to']['values'][0]['text']
					except (KeyError, IndexError):
						to_year = 'now'
					from_to = ' (' + from_year + ' - ' + to_year + ') '

					if count == 1:
						line = '\t' + '| Spouses:        ' + name + from_to
						if location is not '':
							line += '@ ' + location
					else:
						line = '\t' + '|                 ' + name + from_to
						if location is not '':
							line += '@ ' + location

					whitespace = cal_whitespace(temp, line)[:-2]

					print line + whitespace + '|' + '\t'

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
						book = book[0:91] + "..."
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

			if property == '/influence/influence_node/influenced':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					influenced = item['text']
					if count == 1:
						influenced = '\t' + '| Influenced:     ' + influenced
					else:
						influenced = '\t' + '|                 ' + influenced  
					if len(influenced)>91:
						influenced = influenced[0:91] + "..."
					whitespace = cal_whitespace(temp, influenced)[:-2]
					print influenced + whitespace + '|' + '\t'
			
			if property == '/influence/influence_node/influenced_by':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					influenced_by = item['text']
					if count == 1:
						influenced_by = '\t' + '| Influenced By:  ' + influenced_by
					else:
						influenced_by = '\t' + '|                 ' + influenced_by  
					if len(influenced_by)>91:
						influenced_by = influenced_by[0:91] + "..."
					whitespace = cal_whitespace(temp, influenced_by)[:-2]
					print influenced_by + whitespace + '|' + '\t'

		except KeyError:
			pass

def extract_actor():
	for property in topic['property']:
		try:
			if property == '/film/actor/film':
				print temp
				print '\t' + "| Films:         |Character                              | Film Name                               |"
				print '\t' + "|                ----------------------------------------------------------------------------------"

				for item in topic['property'][property]['values']:
					try:
						character = item['property']['/film/performance/character']['values'][0]['text']
					except KeyError:
						character = item['property']['/film/performance/special_performance_type']['values'][0]['text']
					film = item['property']['/film/performance/film']['values'][0]['text']

					if len(character)>38:
						character = character[0:35] + "..."

					if len(film)>39:
						film = film[0:36] + "..."

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
	for property in topic['property']:
		try:
			if property == '/organization/organization_founder/organizations_founded':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					founded = item['text']
					if count == 1:
						founded = '\t' + '| Founded:        ' + founded
					else:
						founded = '\t' + '|                 ' + founded  
					if len(founded)>91:
						founded = founded[0:91] + "..."
					whitespace = cal_whitespace(temp, founded)[:-2]
					print founded + whitespace + '|' + '\t'


			if property == '/business/board_member/leader_of':
				print temp
				print '\t' + "| Leadership:    |Organization            | Role            | Title            | From-To           |"
				print '\t' + "|                ----------------------------------------------------------------------------------"
				for item in topic['property'][property]['values']:
					organization = item['property']['/organization/leadership/organization']['values'][0]['text']
					try:
						role = item['property']['/organization/leadership/role']['values'][0]['text']
					except KeyError:
						role = ''

					try:
						title = item['property']['/organization/leadership/title']['values'][0]['text']
					except KeyError:
						title = ''

					from_year = item['property']['/organization/leadership/from']['values'][0]['text']
					try:
						to_year = item['property']['/organization/leadership/to']['values'][0]['text']
					except (KeyError, IndexError):
						to_year = 'now'
					from_to = from_year + ' / ' + to_year

					if len(organization)>23:
						organization = organization[0:20] + "..."

					if len(role)>15:
						role = role[0:12] + "..."

					if len(title)>16:
						title = title[0:13] + "..."

					if len(from_to)>17:
						from_to = from_to[0:14] + "..."

					whitespace1 = ''
					for i in range(24 - len(organization)):
						whitespace1 += ' '
					whitespace2 = ''
					for i in range(16 - len(role)):
						whitespace2 += ' '
					whitespace3 = ''
					for i in range(17 - len(title)):
						whitespace3 += ' '
					whitespace4 = ''
					for i in range(18 - len(from_to)):
						whitespace4 += ' '

					print '\t' + "|                |" + organization + whitespace1 + '| ' + role + whitespace2 + '| ' + title + whitespace3 + '| ' + from_to + whitespace4 + '|' + '\t'

			if property == '/business/board_member/organization_board_memberships':
				print temp
				print '\t' + "| Board Member:  |Organization            | Role            | Title            | From-To           |"
				print '\t' + "|                ----------------------------------------------------------------------------------"
				for item in topic['property'][property]['values']:
					organization = item['property']['/organization/organization_board_membership/organization']['values'][0]['text']
					try:
						role = item['property']['/organization/organization_board_membership/role']['values'][0]['text']
					except KeyError:
						role = ''

					try:
						title = item['property']['/organization/organization_board_membership/title']['values'][0]['text']
					except KeyError:
						title = ''

					from_year = item['property']['/organization/organization_board_membership/from']['values'][0]['text']
					try:
						to_year = item['property']['/organization/organization_board_membership/to']['values'][0]['text']
					except (KeyError, IndexError):
						to_year = 'now'
					from_to = from_year + ' / ' + to_year

					if len(organization)>23:
						organization = organization[0:20] + "..."

					if len(role)>15:
						role = role[0:12] + "..."

					if len(title)>16:
						title = title[0:13] + "..."

					if len(from_to)>17:
						from_to = from_to[0:14] + "..."

					whitespace1 = ''
					for i in range(24 - len(organization)):
						whitespace1 += ' '
					whitespace2 = ''
					for i in range(16 - len(role)):
						whitespace2 += ' '
					whitespace3 = ''
					for i in range(17 - len(title)):
						whitespace3 += ' '
					whitespace4 = ''
					for i in range(18 - len(from_to)):
						whitespace4 += ' '

					print '\t' + "|                |" + organization + whitespace1 + '| ' + role + whitespace2 + '| ' + title + whitespace3 + '| ' + from_to + whitespace4 + '|' + '\t'


		except KeyError:
			pass
	

def extract_league():
	for property in topic['property']:
		try:
			if property == '/type/object/name':
				print temp
				name = topic['property'][property]['values'][0]['text']
				name = '\t' + '| Name:           '  + name 
				whitespace = cal_whitespace(temp, name)[:-2]
				print name + whitespace + '|' + '\t'

			if property == '/sports/sports_league/sport':
				print temp
				sport = topic['property'][property]['values'][0]['text']
				sport = '\t' + '| Sport:          ' + sport
				whitespace = cal_whitespace(temp, sport)[:-2]
				print sport + whitespace + '|' + '\t'

			if property == '/organization/organization/slogan':
				print temp
				slogan = topic['property'][property]['values'][0]['text']
				slogan = '\t' + '| Slogan:           ' + slogan
				whitespace = cal_whitespace(temp, slogan)[:-2]
				print slogan + whitespace + '|' + '\t'

			if property == '/common/topic/official_website':
				print temp
				website = topic['property'][property]['values'][0]['text']
				website = '\t' + '| Official Website: ' + website
				whitespace = cal_whitespace(temp, website)[:-2]
				print website + whitespace + '|' + '\t'

			if property == '/sports/sports_league/championship':
				print temp
				championship = topic['property'][property]['values'][0]['text']
				championship = '\t' + '| Championship:     ' + championship
				whitespace = cal_whitespace(temp, championship)[:-2]
				print championship + whitespace + '|' + '\t'

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

			if property == '/sports/sports_league/teams':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					team = item['property']['/sports/sports_league_participation/team']['values'][0]['text']
					if count == 1:
						team = '\t' + '| Teams:            ' + team
					else:
						team = '\t' + '|                   ' + team 
					whitespace = cal_whitespace(temp, team)[:-2]
					print team + whitespace + '|' + '\t'

		except KeyError:
			pass	

def extract_sportsteam():
	for property in topic['property']:
		try:
			if property == '/type/object/name':
				print temp
				name = topic['property'][property]['values'][0]['text']
				name = '\t' + '| Name:             '  + name 
				whitespace = cal_whitespace(temp, name)[:-2]
				print name + whitespace + '|' + '\t'

			if property == '/sports/sports_team/sport':
				print temp
				sport = topic['property'][property]['values'][0]['text']
				sport = '\t' + '| Sport:            ' + sport
				whitespace = cal_whitespace(temp, sport)[:-2]
				print sport + whitespace + '|' + '\t'

			if property == '/sports/sports_team/arena_stadium':
				print temp
				arena = topic['property'][property]['values'][0]['text']
				arena = '\t' + '| Arena:          ' + arena
				whitespace = cal_whitespace(temp, arena)[:-2]
				print arena + whitespace + '|' + '\t'

			if property == '/common/topic/description':
				print temp
				descriptions = topic['property'][property]['values'][0]['value']
				descriptions = ' Descriptions:     ' + descriptions
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

			if property == '/sports/sports_team/league':
				print temp
				league = topic['property'][property]['values'][0]['property']['/sports/sports_league_participation/league']['values'][0]['text']
				league = '\t' + '| Leagues:        ' + league
				whitespace = cal_whitespace(temp, league)[:-2]
				print league + whitespace + '|' + '\t'

			if property == '/sports/sports_team/location':
				print temp
				location = topic['property'][property]['values'][0]['text']
				location = '\t' + '| Locations:      ' + location
				whitespace = cal_whitespace(temp, location)[:-2]
				print location + whitespace + '|' + '\t'

			if property == '/sports/sports_team/founded':
				print temp
				founded = topic['property'][property]['values'][0]['text']
				founded = '\t' + '| Founded:        ' + founded
				whitespace = cal_whitespace(temp, founded)[:-2]
				print founded + whitespace + '|' + '\t'

			if property == '/sports/sports_team/championships':
				print temp
				count = 0
				for item in topic['property'][property]['values']:
					count += 1
					championships = item['text']
					if count == 1:
						championships = '\t' + '| Championships:  ' + championships
					else:
						championships = '\t' + '|                 ' + championships 
					whitespace = cal_whitespace(temp, championships)[:-2]
					print championships + whitespace + '|' + '\t'

			if property == '/sports/sports_team/coaches':
				print temp
				print '\t' + "| Coaches:      |Name                    | Position                    | From/To                   |"
				print '\t' + "|               -----------------------------------------------------------------------------------"
				for item in topic['property'][property]['values']:
					name = item['property']['/sports/sports_team_coach_tenure/coach']['values'][0]['text']
					try:
						position = item['property']['/sports/sports_team_coach_tenure/position']['values'][0]['text']
					except KeyError:
						position = ''

					from_year = item['property']['/sports/sports_team_coach_tenure/from']['values'][0]['text']
					try:
						to_year = item['property']['/sports/sports_team_coach_tenure/to']['values'][0]['text']
					except (KeyError, IndexError):
						to_year = 'now'
					from_to = from_year + ' / ' + to_year

					if len(name)>23:
						name = name[0:20] + "..."

					if len(position)>27:
						position = position[0:24] + "..."

					if len(from_to)>25:
						from_to = from_to[0:22] + "..."

					whitespace1 = ''
					for i in range(24 - len(name)):
						whitespace1 += ' '
					whitespace2 = ''
					for i in range(28 - len(position)):
						whitespace2 += ' '
					whitespace3 = ''
					for i in range(26 - len(from_to)):
						whitespace3 += ' '

					print '\t' + "|               |" + name + whitespace1 + '| ' + position + whitespace2 + '| ' + from_to + whitespace3 + '|' + '\t'

			if property == '/sports/sports_team/roster':
				print temp
				print '\t' + "| PlayersRoster:|Name             | Position             | Number             | From/To            |"
				print '\t' + "|               -----------------------------------------------------------------------------------"
				for item in topic['property'][property]['values']:
					name = item['property']['/sports/sports_team_roster/player']['values'][0]['text']
					try:
						number = item['property']['/sports/sports_team_roster/number']['values'][0]['text']
					except KeyError:
						number = ''

					try:
						position = ''
						for i in item['property']['/sports/sports_team_roster/position']['values']:
							position += i['text'] + ', '
						position = position[:-2]
					except KeyError:
						position = ''

					from_year = item['property']['/sports/sports_team_roster/from']['values'][0]['text']
					try:
						to_year = item['property']['/sports/sports_team_roster/to']['values'][0]['text']
					except (KeyError, IndexError):
						to_year = 'now'
					from_to = from_year + ' / ' + to_year

					if len(name)>16:
						name = name[0:13] + "..."

					if len(position)>19:
						position = position[0:17] + "..."

					if len(from_to)>17:
						from_to = from_to[0:15] + "..."

					whitespace1 = ''
					for i in range(17 - len(name)):
						whitespace1 += ' '
					whitespace2 = ''
					for i in range(21 - len(position)):
						whitespace2 += ' '
					whitespace3 = ''
					for i in range(19 - len(number)):
						whitespace3 += ' '
					whitespace4 = ''
					for i in range(19 - len(from_to)):
						whitespace4 += ' '

					print '\t' + "|               |" + name + whitespace1 + '| ' + position + whitespace2 + '| ' + number + whitespace3 + '| ' + from_to + whitespace4 + '|' + '\t'

		except KeyError:
			pass


entity_dic = {'/people/person':'Person', '/book/author':'Author', '/film/actor':'Actor', '/tv/tv_actor':'Actor', '/organization/organization_founder':'BusinessPerson', '/business/board_member':'BusinessPerson', '/sports/sports_league':'League', '/sports/sports_team':'SportsTeam', '/sports/professional_sports_team':'SportsTeam'}

# utilize search API to get 'mid'
mid = []
api_key = open("api_key").read()
query = 'New York Knicks'
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

print '\t' + " --------------------------------------------------------------------------------------------------"
