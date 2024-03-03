from elasticsearch import Elasticsearch
import sys
from config_handling import get_config_value

sys.path.insert(0, '/backend/venv/config/config_handling.py')


def connect_elasticsearch(**kwargs):
    _es_config = get_config_value('elastic', 'es_host')
    _es_hosts = [_es_config]
    if 'hosts' in kwargs.keys():
        _es_hosts = kwargs['hosts']
    _es_obj = None
    _es_obj = Elasticsearch(hosts=_es_hosts, timeout=10)
    if _es_obj.ping():
        print('index Connected')
    else:
        print('Awww it could not connect!')
    return _es_obj

es = connect_elasticsearch()