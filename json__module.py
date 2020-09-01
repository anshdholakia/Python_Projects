import json

data='{"var1":"ansh","var2":33}'


# parsed= json.loads(data)
# print(parsed["var2"])


# Task=json.load - what does it do?

# Used to open json files
# Accepts file object

# with open("json_data.json", "r") as content:
#     print(json.load(content))


data2={"Channel name":"Ansh Dholakia", "fridge":("roti", "disc kulfi"),"is good":True,"cars": ["Toyota","Mahindra","Hyundai"]}
# It is not compatible with javascript so we use json dumps

jscomp=json.dumps(data2,sort_keys=True)
print(jscomp)
