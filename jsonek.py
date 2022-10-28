import json

person = '{"name": "Bob", "languages": ["English", "French", ["Python", "Java"]]}'
person_dict = json.loads(person)

# print(person_dict)
# print(person_dict['languages'])
# print(person_dict['languages'][0])
# print(person_dict['languages'][1])
# print(person_dict['languages'][2][0])

# with open('person.json', 'r') as f:
#     data = json.load(f)
# print(data)








