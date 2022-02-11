import requests
response = requests.get("https://gitlab.com/-Your gitlab account")
my_projects = response.json()

# print the whole objects list
print(my_projects)
print(type(my_projects))

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['key-name']}\nProject Url: {project['key-name']}\n")

