import sys
import json

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file) as values:
    vals = json.load(values)
    
with open(tests_file) as tests:
    tes = json.load(tests)

val_dict = {}
for val in vals.values():
    for v in val:
        val_dict[v['id']] = v['value']

def extract_values(json_obj):
    if isinstance(json_obj, list):
        return [extract_values(jo) for jo in json_obj]
    elif isinstance(json_obj, dict):
        if 'id' in json_obj.keys() and 'value' in json_obj.keys():
            json_obj['value'] = val_dict.get(json_obj['id'], json_obj['value'])
        for k, v in json_obj.items():
            json_obj[k] = extract_values(v)
    return json_obj

with open(report_file, 'w', encoding='utf-8') as report:
    json.dump(extract_values(tes), report, indent=2, ensure_ascii = False)
