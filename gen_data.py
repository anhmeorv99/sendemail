from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

result = es.search(index="youtube_channel", body='{"query":{"match_all": {}}}')['hits']['hits']

list_channel = set()
for value in result:
    list_channel.add(value['_source']['channel_title'])

body = "Xin chào ông A, chúng tôi xin gửi ông những video đáng chú ý trong ngày:\n"

for index_channel, channel in enumerate(list_channel):
    body += str(index_channel + 1) + ". " + channel + "\n\n"
    for value in result:
        if value['_source']['channel_title'] == channel:
            body += value['_source']['video_title'] + "\n\n"
            body += value['_source']['video_description'] + "\n"
            body += "link : https://www.youtube.com/watch?v=" + value['_source']['video_id'] + "\n\n"

print(body)
