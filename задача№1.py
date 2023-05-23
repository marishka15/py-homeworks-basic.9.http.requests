from pprint import pprint

import requests

r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
res = r.json()
pprint(res)
all_list = []
for el in res:
    name_all = el['name']

    if name_all in ["Captain America", "Hulk", "Thanos"]:
        num = el['powerstats']['intelligence']
        all_glossary = {
            'name': name_all,
            'intelligence': num
        }
        all_list.append(all_glossary)
#pprint(all_list)
all_list_sorted = sorted(all_list, key=lambda el: el['intelligence'], reverse=True)
pprint(all_list_sorted[0])





