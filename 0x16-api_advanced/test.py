#!/usr/bin/python3
"""tests"""
import requests

if __name__ == "__main__":
    API = "https://oauth.reddit.com"
    CLIENT_ID = '1l-h1XNMQiABfrG1Pq9szw'
    SECRET_KEY = '3brPsAUeP6e7kMSrK9PbIFL037EWXQ'

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'Possibly_a_cat_1398',
        'password': 'Queenbella#1999'
    }
    headers = {
        'User-Agent': 'MYAPI/0.0.0.1',
    }
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    print(res.json())
#    TOKEN = res.json()['access_token']
#    headers['Authorization'] = f'bearer {TOKEN}'
#    query = requests.get('{}/api/search_subreddits?query=programming'.format(API), headers=headers)
#    print(query.status_code)
