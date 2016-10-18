from urllib.request import Request, urlopen
import json

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

req = Request('https://xxxxxx.apiary-mock.com/authors?start=1&size=10&sort=id')
req.add_header('Authorization', 'Basic dXNlcm5hbWU6cGFzc3dvcmQ=')
req.add_header('x-api-version', '1.0')
resp = urlopen(req).read().decode("utf-8") 

pp_json(resp)
