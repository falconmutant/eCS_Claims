import json
import random
import string
from django.core import serializers
from django.db import connection
from .queries import search

ESCAPE_STRING_SEQUENCES = (
    (' AND ', '&'),
    (' OR ', '|'),
    ('+', '&'),
)

def get_url(hostname, route):
    return "http://%s/%s" % (hostname, route)


def raw_sql_search(query, pac_id):
    cursor = connection.cursor()

    for sequence in ESCAPE_STRING_SEQUENCES:
        replace_this, for_this = sequence
        query = query.replace(replace_this, for_this)

    params = []

    for i in range(0,6):
        params += [query, pac_id, query]

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
