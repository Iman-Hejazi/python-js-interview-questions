"""
You can use python for this task if you prefer.
in javascript:
1) using fetch function, write code to fetch data from "https://fakestoreapiserver.reactbd.com/users"
2) and print the values for each user to terminal
"""


import requests


API_ENDPOINT = 'https://fakestoreapiserver.reactbd.com/users'

response = requests.get(API_ENDPOINT)

if response.status_code == 200:
    users = response.json()

    for user in users:
        name = user['name']
        print(name)
