import requests


def get_github_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        return None


username = 'IvySue60248'
repositories = get_github_repositories(username)
if repositories:
    for repo in repositories:
        print(repo['name'])
else:
    print('Failed to fetch repositories')