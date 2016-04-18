import json
import sys

json_data = open(sys.argv[1]).read()
data = json.loads(json_data)

output = {}

for elem in data:
     output[elem['history'][0]['subject'].encode('utf8')] = elem['history'][0]['content'].encode('utf8')

print output