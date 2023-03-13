import re

st = "test test academy test andri"
result = re.findall("test", st)
print(result)

pattern = re.compile("te")
result = pattern.findall(st)
print(result)


result = re.findall("e[s, m]", st)
print(result)
