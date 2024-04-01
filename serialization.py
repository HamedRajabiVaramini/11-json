'''
simple_programming_

This code serialize (encode) a Python 
dictionary to JSON 
'''
import json 

data = {
    "studentName": "Helma",
    "grade": "2nd",
    "gender": "female",
    "age": 9,
    "hobbies": ["crafting", "playing Minecraft"]
}

json_string = json.dumps(data) # Serializes data
print(json_string)


