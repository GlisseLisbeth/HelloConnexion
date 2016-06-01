import uuid

import datetime
from connexion import NoContent
hellos = {}


def post(hello):
    hello_id = str(uuid.uuid4())
    hello['time'] = datetime.datetime.now()
    hello['hello_id'] = hello_id
    hellos[hello_id] = hello
    return NoContent, 201


def get(id):
    if hellos.get(id):
        return hellos[id], 200
    else:
        return NoContent, 404


def search(time=None):
    date_parsed = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ") if time else None
    results = [hello for hello in hellos.values() if date_parsed is None or hello['time'] > date_parsed]
    return results, 200
