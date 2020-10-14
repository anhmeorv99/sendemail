from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
import json

# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)
#
# print("dt_object =", dt_object)

es = Elasticsearch("http://192.168.140.240:9200")
es_local = Elasticsearch("http://localhost:9200")

news = es.search(index="youtube_video_2020_10", body={
    "query": {
        "range": {
            "time": {
                "gte": "now-10d/d",
                "lte": "now/d"
            }
        }
    }

})
f = open("result.json", "w")
actions = []
for video in news['hits']['hits']:


    action = {
        "_index": "youtube_video_2020_10",
        "_type": "video",
        "_id": video['_id'],
        "_source": video['_source']
    }

    actions.append(action)

    helpers.bulk(es_local,actions)

# body = "Xin chào ông A, chúng tôi xin gửi ông những video đáng chú ý trong ngày:\n"
# for index, video in enumerate(news['hits']['hits']):
#     date_time = datetime.fromtimestamp(video['_source']['snippet']['publishedAt'])
#
#     body += str(index + 1) + ". " + video['_source']['snippet']['title'] + ", time : " \
#             + str(date_time) + "\n\n"
#     body += video['_source']['snippet']['description'] + "\n\n"
#     body += "Nguồn : " + video['_source']['snippet']['channelTitle'] + "\n"
#     body += "Link : https://www.youtube.com/watch?v=" + video['_source']['id'] + "\n\n"
#
#
# print(body)
