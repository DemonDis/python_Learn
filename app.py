import json

with open('./static/status_arr.json', 'r', encoding='utf-8') as file:
    templates = json.load(file)
with open('./static/result_.json', 'r', encoding='utf-8') as file:
    templates_2 = json.load(file)

post = [s['status'] for s in templates]
for index, post_i in enumerate(post):
    for id in set(post_i):
        print(f'{id}: {post_i.count(id)}')
        templates_2[index]['status'].append({'status': id, 'sum': post_i.count(id)})

with open('sw_.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(templates_2, indent=4, ensure_ascii=False,))