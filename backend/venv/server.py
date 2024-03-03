from flask import Flask
from api.elastic_test import connect_elasticsearch
# from dotenv import load_dotenv
# from elasticsearch import Elasticsearch
# import os

es = connect_elasticsearch()


# load_dotenv()

app = Flask(__name__)

from api.insert_data import *
from api.retrieve_data import *


# client = Elasticsearch(
#   "https://856cb62e509f4594a7df6b806a3ab601.us-central1.gcp.cloud.es.io:443",
#   api_key=""
# )

# documents = [
#   { "index": { "_index": "search-paymentdata2024", "_id": "9780553351927"}},
#   {"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
#   { "index": { "_index": "search-paymentdata2024", "_id": "9780441017225"}},
#   {"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
#   { "index": { "_index": "search-paymentdata2024", "_id": "9780451524935"}},
#   {"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
#   { "index": { "_index": "search-paymentdata2024", "_id": "9781451673319"}},
#   {"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
#   { "index": { "_index": "search-paymentdata2024", "_id": "9780060850524"}},
#   {"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
#   { "index": { "_index": "search-paymentdata2024", "_id": "9780385490818"}},
#   {"name": "The Handmaid's Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": true},
# ]

# client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")

# client.info()
# client.search(index="search-paymentdata2024", q="snow")

# @app.route("/")
# def hello_world():
#     return "<p>Hello world</p>"

if __name__ == "__main__":
    app.run(debug=True)
