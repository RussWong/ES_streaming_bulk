from elasticsearch import Elasticsearch
from elasticsearch.exceptions import TransportError
create_index_body = {
            "mappings":{
                "properties": {
                    "a": {
                        "type": "string"
                    },
                    "b": {
                        "type": "string"
                    }
                }
            },
        
    "settings":{
    "number_of_shards":1,
    "number_of_replicas":0
    }
}

es=Elasticsearch(["localhost:9200"])
try:
	es.indices.create(index='git',body=create_index_body)
except TransportError as e:
	if e.error=="resource_already_exists_exception":
		pass
	else:
		raise
