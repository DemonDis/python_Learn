import json
# https://ru.stackoverflow.com/questions/1056998/%D0%9F%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C-%D0%B2-%D0%B2%D0%B8%D0%B4%D0%B5-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B3%D0%BE-%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%B0

data = [
    {"id": "000", "name": "name_1", "status": "pass", "parent_id": None},
    {"id": "111", "name": "child_1", "status": "pass", "parent_id": "000"},
    {"id": "222", "name": "child_2", "status": "pass", "parent_id": "111"},
    {"id": "333", "name": "child_3", "status": "pass", "parent_id": "222"},
    {"id": "444", "name": "child_4", "status": "pass", "parent_id": "333"},
    {"id": "555", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "555", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "3", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "5455", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "5", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "6", "name": "child_5", "status": "pass", "parent_id": "444"},
    {"id": "001", "name": "name_2", "status": "pass", "parent_id": None},
     {"id": "002", "name": "name_2", "status": "pass", "parent_id": None},
     {"id": "003", "name": "name_2", "status": "pass", "parent_id": None},
     {"id": "004", "name": "name_2", "status": "pass", "parent_id": None},
    {"id": "33", "name": "child_1", "status": "pass", "parent_id": "004"},
    {"id": "3443", "name": "child_1", "status": "pass", "parent_id": "004"},
    {"id": "666", "name": "child_1", "status": "pass", "parent_id": "004"},
]

def make_tree2(tests):
    # Сюда кладутся элементы без родителей
    tree = []

    # А здесь элементы с родителями будут искать своего родителя по id
    children_by_id = {}

    for item_data in tests:
        # Для корректной работы кода у элементов должны быть уникальные id
        item_id = item_data["id"]

        parent_id = item_data["parent_id"]
        if parent_id is not None:
            # Если родитель есть — создаём список children для него
            try:
                parent_list = children_by_id[parent_id]
            except KeyError:
                parent_list = []
                children_by_id[parent_id] = parent_list
        else:
            # Если родителя нет — положим новый элемент в tree
            parent_list = tree

        # Формируем новый элемент в почти нужном виде
        # Список children мог быть создан в предыдущих итерациях цикла
        try:
            children = children_by_id[item_id]
        except KeyError:
            children = []
            children_by_id[item_id] = children

        item = {
            "key": "",  # Придётся сформировать позже
            "data": item_data.copy(),
            "children": children,
        }
        item["data"].pop("parent_id")

        # Кладём его родителю (а если родителя нет, то parent_list это tree)
        parent_list.append(item)

    # Теперь формируем key во втором цикле, используя очередь
    queue = [(str(item_idx), item) for item_idx, item in enumerate(tree)]
    while queue:
        key, item = queue.pop()
        item["key"] = key
        for child_idx, child_item in enumerate(item["children"]):
            # Заполняем очередь элементами из children
            # (можно заменить очередь на рекурсию, если она нравится больше)
            queue.append((f"{key}-{child_idx}", child_item))

    return tree

with open('./static/put/data_tree.json', 'w') as f:
    f.write(json.dumps(make_tree2(data), indent=4))