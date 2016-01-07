import json
import random
import string
from django.core import serializers
from django.db import connection

ESCAPE_STRING_SEQUENCES = (
    (' AND ', '&'),
    (' OR ', '|'),
    ('+', '&'),
)

def to_json(objct, multi=False):
    if not multi:
        obj_str = serializers.serialize('json', [objct, ])
        obj_json = json.loads(obj_str)[0]

        return pretty_json(obj_json)
    else:
        obj_str = serializers.serialize('json', objct)
        obj_json = json.loads(obj_str)

        return [pretty_json(ugly_json) for ugly_json in obj_json]

def pretty_json(ugly_json):
    oid = ugly_json.pop('pk', 0)
    fields = ugly_json.pop('fields', {})
    ugly_json.pop('model', '')

    ugly_json['id'] = oid
    ugly_json.update(fields)

    return ugly_json

def raw_sql_search(query):
    cursor = connection.cursor()

    for sequence in ESCAPE_STRING_SEQUENCES:
        replace_this, for_this = sequence
        query = query.replace(replace_this, for_this)

    params = [query for i in range(0,10)]
    cursor.execute(search.RAW_SQL, params)

    result = [{
        'tipo': row[0],
        'id': row[1],
        'highlight': row[2],
        'fecha': row[3],
    } for row in cursor.fetchall()]

    return result

def secret_key_gen():
    return "".join([random.SystemRandom().choice(string.digits + string.letters) for i in xrange(32)])
