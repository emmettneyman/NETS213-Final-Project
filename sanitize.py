import json
import sys

json_data = open(sys.argv[1]).read()
data = json.loads(json_data)

for elem in data:
    elem.pop('tag_good')
    if len(elem['children']) > 0:
        for i in range(len(elem['children'])):
            try:
               del elem['children'][i]['tag_endorse']
            except:
                x=1

print json.dumps(data,indent=2)