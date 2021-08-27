import json
from os import system
#json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
#with open('distros.json', 'r') as f:
with open('F:\Vscode\python\python_json\distros.json',  encoding="utf8",) as f:
    distros_dict = json.load(f)
#system.path.insert('F:\Vscode\python\python_json\distros.json')
for distro in distros_dict:
    print(distro['name'],distro['lat'])
    #print(distro['lat'])