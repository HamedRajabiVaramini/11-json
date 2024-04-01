'''
simple_programming_

This code deserialize (decode) a JSON 
string to a Python Dictionary 
'''
import json 

json_string = '''{"studentName": "Helma", 
    "grade": "2nd",
    "gender": "female",
    "age": 9,
    "hobbies": ["crafting", "playing Minecraft"]
}''' 

dict = json.loads(json_string) # Deserializes to 
# a Python dictionary
print(dict)


