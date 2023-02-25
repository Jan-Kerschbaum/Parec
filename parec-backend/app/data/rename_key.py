import json

with open('parec-backend/app/data/arxiv_reduced.json') as f:
    json_data = f.read()

data = json.loads(json_data)

for item in data['root']:
    item['paper_id'] = item.pop('id')

# Save the modified data to a new file
with open('parec-backend/app/data/arxiv_reduced_modified.json', 'w') as f:
    json.dump(data, f)