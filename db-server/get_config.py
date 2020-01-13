import xmltodict
# import json

f = open("config.xml", "r")
config = f.read()

# pp.pprint(json.dumps(xmltodict.parse(xml)))

config_json = xmltodict.parse(config)
# print (config_json)

# print(config_json['abc']['key2'])

# def fetch_config():
#     pass