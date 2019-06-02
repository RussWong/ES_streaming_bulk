from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk,bulk
import pandas as pd
data=pd.read_csv("data.csv",sep=",")
print(data)
print(len(data.index))
print(data.iloc[0].user)
es=Elasticsearch(["localhost"])
def action(data):
	for i in range(len(data.index)):
		yield {
		"user":data.iloc[i].user,
		"passwd":data.iloc[i].passwd
		}
# result=streaming_bulk(es,action(data),index="my-index",doc_type="test")
# print(type(result))
for ok,result in streaming_bulk(es,action(data),index="my-index",doc_type="test"):
	#action(data)必须要是一个iterable，这里是yield,也可以是list等
	print(result)
	action, result = result.popitem#这行可要可不要

	doc_id = "/{}/test/{}".format("my-index", result["_id"])
	if not ok:
		print("error")
	else:
		print(doc_id)
#print(ok)#True
#print(result)#{'_index': 'my-index', '_type': 'test', '_id': 'PeZEEWsB65GizZ1GJp9C', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 11, '_primary_term': 1, 'status': 201}
#print(action)#index
#下面是updates操作
# UPDATES = [
#     {
#         "_type": "test",
#         "_id": "vOZREWsB65GizZ1G_aix",
#         "_op_type": "update",
#         "doc": {"user": "Kyle Kuzma"},
#     },
#     {
#         "_type": "test",
#         "_id": "veZREWsB65GizZ1G_aix",
#         "_op_type": "update",
#         "doc": {"user": "PJ Tucker"},
#     },
# ]
# success,what=bulk(es,UPDATES,index="my-index",doc_type="test")



