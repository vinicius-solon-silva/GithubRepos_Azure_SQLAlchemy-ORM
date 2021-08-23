import requests

user = input('Enter the Github username: ')

r = requests.get(f'https://api.github.com/users/{user}/repos')
repos = r.json()

if (r.status_code == 200):
    print(f"\n{user}'s repos:\n")
    for i in repos:
        print("- " + i["name"])
else:
    print('Error: ' + str(r.status_code))

print("\n")
