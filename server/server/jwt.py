#!/usr/bin/python
#-*-coding:utf-8-*-

from jose import jwt
import time

data = {
    "created_at": 1559438429,
    "consumer": {
        "id": "9718fb83-e28b-4d63-a994-c7fbe557b2b8"
    },
    "id": "d315cd16-535e-45ea-91fa-7c3edcfd39ac",
    "algorithm": "HS256",
    "secret": "mcwpmRh15VkGCw5WFooVwLrWUy629yn5",
    "key": "980SICpU4qba40zsita3YtLh1js6f4vq"
}

token = jwt.encode( {
        'iss': '980SICpU4qba40zsita3YtLh1js6f4vq',
        'nbf': 1559439638,
        'exp': 1559439648
    },
    'mcwpmRh15VkGCw5WFooVwLrWUy629yn5',
    algorithm='HS256'
    )
print('############ token #######################3')
print(token)
print('############ token end #######################3')

token2 = jwt.decode(token, 'mcwpmRh15VkGCw5WFooVwLrWUy629yn5', algorithms=['HS256'])
print(token2)
