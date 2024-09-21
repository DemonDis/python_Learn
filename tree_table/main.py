import json

PUT_JSON = [
    {
        'key': '0',
        'data': {
            'name': 'name_1',
            'id': '000',
            "status": "pass"
        },
        'children': [
            {
                "key": '0-0',
                "data": {
                    'name': 'child_1',
                    'id': '111',
                    "status": "pass"
                },
                'children': [
                        {
                            'key': '0-0-0',
                            'data': {
                                'name': 'child_2',
                                'id': '222',
                                "status": "pass"
                            },
                            'children': [
                                {
                                    'key': '0-0-0-0',
                                    'data': {
                                        'name': 'child_3',
                                        'id': '333',
                                        "status": "pass"
                                    },
                                    'children': [
                                        {
                                            'key': '0-0-0-0-0',
                                            'data': {
                                                'name': 'child_4',
                                                'id': '444',
                                                "status": "pass"
                                            },
                                            'children': [
                                                {
                                                    'key': '0-0-0-0-0-0',
                                                    'data': {
                                                        'name': 'child_5',
                                                        'id': '555',
                                                        "status": "pass"
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
]

TREE_DATA = []

with open('./static/out/db.json') as f:
    tree_data = json.load(f)
    print(tree_data)

with open('./static/put/data_tree.json', 'w') as f:
    f.write(json.dumps(PUT_JSON, indent=4))