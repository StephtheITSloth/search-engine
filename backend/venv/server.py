

from flask import Flask
from flask import send_file, jsonify,request
from io import BytesIO
import json
from elasticsearch_connection import es


app = Flask(__name__)



# from api.insert_data import 
@app.route('/home/', methods=['GET'])
def search():
    query_param = request.args.get('searchQuery', "")
    query = {"query": {"match_all": {}}}

    file_path = 'static/files/search_data.txt'

    if query_param:
        query = {"query": {"match": {"Physician_Profile_ID": query_param}}}

    res = es.search(index="search-payment-csv",body=query)
    # print(results)
    # data = (res['hits']['hits'])
    hits_data = [hit['_source'] for hit in res['hits']['hits']]

    # Create a file-like object in memory to write the JSON data
    json_bytes = json.dumps(hits_data).encode('utf-8')
    file_obj = BytesIO(json_bytes)

    # Return the file as a download with a customized filename
    return send_file(file_obj, as_attachment=True, download_name='search_results.json', mimetype='application/json')

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


if __name__ == "__main__":
    app.run(debug=True)
