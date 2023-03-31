import json
x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'

data = json.loads(x)
print(data)
for key, value in data.items():
    print(key, value)

file = open("in.json")
data = json.load(file)
print(data)
for key, value in data.items():
    print(key, value)

json_data = json.dumps(data)

print(type(json_data), json_data)
with open("out.json", "w") as js_file:
    json_data = json.dump(data, js_file)