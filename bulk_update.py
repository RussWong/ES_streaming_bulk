from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
es=Elasticsearch(["localhost"])
UPDATES = [
    {
         "_type": "test",
         "_id": "vOZREWsB65GizZ1G_aix",
         "_op_type": "update",
         "doc": {"user": "Kyle Kuzma"},
     },
     {
         "_type": "test",
         "_id": "veZREWsB65GizZ1G_aix",
         "_op_type": "update",
         "doc": {"user": "PJ Tucker"},
     },
 ]
success,what=bulk(es,UPDATES,index="my-index",doc_type="test")
print(success)#2
print(what)#[]
es.indices.refresh(index="my-index")#必须要refresh一下才有作用
a=es.get(index="my-index",doc_type="test",id="veZREWsB65GizZ1G_aix")
print(a)