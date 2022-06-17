#!/usr/in/python3
"""Tutorial"""
import requests

CLIENT_ID = '1l-h1XNMQiABfrG1Pq9szw'
SECRET_KEY = '3brPsAUeP6e7kMSrK9PbIFL037EWXQ'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': 'Possibly_a_cat_1398',
    'password': 'Queenbella#1999'
}

headers = {'User-Agent': 'MyAPI/0.0.1'}

