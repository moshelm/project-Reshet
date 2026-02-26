import json 


def json_serializer(data: dict|list|str):
    return json.dumps(data).encode("utf-8")

def json_deserializer(data:dict|list|str):
    if data is None:
        return None
    return json.loads(data.decode("utf-8"))