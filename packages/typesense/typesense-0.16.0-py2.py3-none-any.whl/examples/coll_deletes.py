import time

import typesense
import random
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

client = typesense.Client({
  'api_key': 'abcd',
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})


# Create 100 collections and then try deleting them randomly

coll_ids = []
for i in range(0, 110):
    coll_ids.append(i)

for coll_id in coll_ids:
    coll_name = "docs" + str(coll_id)
    client.collections.create({
        "name": coll_name,
        "fields": [
            {"name": "title", "type": "string"},
        ]
    })

    for j in range(0, 3):
        doc = { 'title': "Foo bar " + str(j)}
        client.collections[coll_name].documents.create(doc)

print("Wait for snapshot to happen....")
time.sleep(10)

random.shuffle(coll_ids)

for coll_id in coll_ids:
    client.collections["docs" + str(coll_id)].delete()
