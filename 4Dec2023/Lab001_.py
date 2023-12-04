import json
import jsonschema
import requests

original_schema = {
       "$schema": "https://json-schema.org/draft/2019-09/schema",
       "$id": "http://example.com/example.json",
       "title": "Root Schema",
       "description": "The root schema is the schema that comprises the entire JSON document.",
       "type": "array",
       "default": [],
       "additionalItems": true,
       "items": {
           "title": "A Schema",
           "description": "An explanation about the purpose of this instance.",
           "type": "object",
           "required": [
               "bookingid"
           ],
           "additionalProperties": True,
           "properties": {
               "bookingid": {
                   "title": "The bookingid Schema",
                   "description": "An explanation about the purpose of this instance.",
                   "type": "integer",
                   "examples": [
                       1200,
                       1742,
                       1116
                   ]
               }
           },
           "examples": [{
               "bookingid": 1200
           },
               {
                   "bookingid": 1742
               },
               {
                   "bookingid": 1116
               }]
       },
       "examples": [
           [{
               "bookingid": 1200
           },
               {
                   "bookingid": 1742
               },
               {
                   "bookingid": 1116
               }]
       ],
       "uniqueItems": True
   }

response = requests.get("https://restful-booker.herokuapp.com/booking")

try:
    jsonschema.validate(response.text, original_schema)
except Exception as error:
    print(error)


# try:
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     schema = json.loads(original_schema)
#     print(schema)
#     # assert original_schema == schema, "Schema not matching"
#     assert jsonschema.validate(response.json(), schema), "Invalid JSON Schema"
# except Exception as error:
#     print(error)
