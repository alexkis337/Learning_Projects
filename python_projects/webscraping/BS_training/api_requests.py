import requests

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

print(r.text)
print(r.json())

for elem in r.text:
    print(elem)

for elem in r.json():
    print(elem)

print(type(r.text))
print(type(r.json()))