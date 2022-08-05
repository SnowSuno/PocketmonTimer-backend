# from app.models import User
import json
import requests

username='snowsuno'
token = ''
headers = {'Authorization': f"bearer {token}"}
URL = f'https://api.github.com/search/commits?q=author:{username}'
# query = 'query {user(login: "%s") {contributionsCollection{totalCommitContributions}}}' % username
r = requests.get(URL, headers=headers)
info = r.json()
print(info['total_count'])