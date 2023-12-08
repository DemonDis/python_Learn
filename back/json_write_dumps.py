import json

test_1 =  [
    {"name": "aaa", "value": "rise"},
    {"name": "sss", "value": "ddd"}
]

test_2 = 'ss'

to_json = {
    'test_1': test_1, 
    'test_2': test_2
}

with open('sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json, indent=4))

with open('sw_templates.json') as f:
    print(f.read())