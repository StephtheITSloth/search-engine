
# /////////////////////////////////

from flask import Flask
from flask import jsonify, request
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# app.config['USERNAME'] = os.getenv('USERNAME')
# app.config['PASSWORD'] = os.getenv('PASSWORD')
# app.config['CLOUD_ID'] = os.getenv('SECRET_KEY')

cloud_id = "be6ec3baaca345a3a87d741fac6fe7cf:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDg1NmNiNjJlNTA5ZjQ1OTRhN2RmNmI4MDZhM2FiNjAxJDJkNGQwNjM3NmQxYzRjZGNhMzE1NTQ3YWNhMzUzYzNm"
username = "rimkstylish1"
password = "Stephrimk1$"
es = Elasticsearch(cloud_id=cloud_id, http_auth=(username, password))

response = es.cluster.health()
print(response)

# ////////////////////////




es = Elasticsearch(cloud_id=cloud_id, http_auth=(username, password))



# load_dotenv()


# from api.insert_data import 
@app.route('/', methods=['GET'])
def home():
    print('Server is running')


# @app.route('/get_user', methods=['GET'])
# def get_user():
#     user_id = request.form['id']
#     results = es.get(index='user', id=user_id)
#     return jsonify(results['_source'])


# @app.route('/search_user', methods=['GET'])
# def search_user():
#     keyword = request.form['keyword']

#     query_body = {
#         "query": {
#             "match": {
#                 "name": keyword
#             }
#         }
#     }

#     res = es.search(index="user", body=query_body)

#     return jsonify(res['hits']['hits'])

# client = Elasticsearch(
#   "https://856cb62e509f4594a7df6b806a3ab601.us-central1.gcp.cloud.es.io:443",
#   api_key=""
# )



# client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")

# client.info()
# client.search(index="search-paymentdata2024", q="snow")

# @app.route("/")
# def hello_world():
#     return "<p>Hello world</p>"

if __name__ == "__main__":
    app.run(debug=True)
