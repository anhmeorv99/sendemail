import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from workers.celeryapp import app
from elasticsearch import Elasticsearch
from datetime import datetime
from settings import ELASTICSEARCH


@app.task
def send_email():
    es = Elasticsearch(
        ELASTICSEARCH["HOST"],
        scheme=ELASTICSEARCH["SCHEME"],
        port=ELASTICSEARCH["PORT"],
    )
    fromaddr = "anhmeorv240219@gmail.com"
    toaddr = "anhmeorv99@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CÁC VIDEO ĐÁNG CHÚ Ý TRONG NGÀY"

    news = es.search(index="youtube_video_2020_10", body={
        "query": {
            "range": {
                "time": {
                    "gte": "now-1d/d",
                    "lte": "now/d"
                }
            }
        },
        "size": 30
    })

    body = "Xin chào ông Tuấn Anh, chúng tôi xin gửi ông những video đáng chú ý trong ngày:\n"
    for index, video in enumerate(news['hits']['hits']):
        date_time = datetime.fromtimestamp(video['_source']['snippet']['publishedAt'])

        body += str(index + 1) + ". " + video['_source']['snippet']['title'] + ", time : " \
                + str(date_time) + "\n\n"
        body += video['_source']['snippet']['description'] + "\n\n"
        body += "Nguồn : " + video['_source']['snippet']['channelTitle'] + "\n"
        body += "Link : https://www.youtube.com/watch?v=" + video['_source']['id'] + "\n\n"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "phuongthanh9x")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
