

from flask import Flask
from flask import send_file, jsonify,request
from flask_cors import CORS
from elasticsearch_connection import es

app = Flask(__name__)
CORS(app)


# from api.insert_data import 
@app.route('/api/v1/payments', methods=['GET'])
def search():
    query_param = request.args.get('doctorId', "")
    query = {"query": {"match_all": {}}}

    if query_param:
        query = {"query": {"match": {"Physician_Profile_ID": query_param}}}

    res = es.search(index="search-payment-csv",body=query)
    # Return the file as a download with a customized filename
    # Convert the Elasticsearch search result to a dictionary
    res_dict = {
        'hits': res['hits']['hits'] if 'hits' in res and 'hits' in res['hits'] else []
    }
    return jsonify(res_dict)

if __name__ == "__main__":
    app.run(debug=True)
