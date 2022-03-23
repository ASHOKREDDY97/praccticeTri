import yaml

with open('sample.yml') as file:
    data=yaml.load(file)
    print(data)