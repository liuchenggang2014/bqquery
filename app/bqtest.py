# -*-coding:utf-8-*-

from google.cloud import bigquery
from flask import Flask
from flask import request
import json

 
BQ_TIMEOUT = 240

# Client 认证by adc
def bq_InitConnection():
    return bigquery.Client()


# 向BigQuery请求数据
def bq_query(sql):
    client = bq_InitConnection()
    # print(bqSql)
    bqJob = client.query(sql)

    records = [dict(row) for row in bqJob]
    json_obj = json.dumps(str(records))

    return json_obj


def query_stackoverflow(a):
    sql = \
        """ 
        select id, price, product from cliu201.ds201.mobilelog 
        where id='{id}'
        
        """ \
            .format(id=a)

    results = bq_query(sql)
    print(results)
    return results

# if __name__ == "__main__":
#     id='1'
#     # sss is a list of list: 
#     sss = query_stackoverflow(id)


#     print (sss)

app = Flask(__name__)

# for testing
@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World2!\n"

@app.route('/', methods=['GET'])
def api():
    # return generate_jwt(sa_keyfile, sa_email, audience)
    id = request.args.get('id')
    sss = query_stackoverflow(id)
    return sss

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)