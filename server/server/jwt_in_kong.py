#!/usr/bin/python
#-*-coding:utf-8-*-

import requests

from jose import jwt


class JWT_IN_KONG:

    def __init__(self, kong_url):
        self.kong_url = kong_url


    def getJwtInfo(self, consumer):
        """获取jwt中consumer的信息

        :param consumer: 消费者
        :type consumer: str

        :return:
            success:
                {
                    "created_at":1563610464,
                    "consumer":{
                        "id":"0b77a2ac-2fbc-42c6-b8d7-85f27f1705db"
                        },
                    "id":"ac053253-66de-46c7-875e-e187545f54b7",
                    "algorithm":"HS256",
                    "secret":"ruh9atyCzsEE5C6yioklk5vT0a9hv4zl",
                    "key":"Q0iCo8RErSNOzo6lCrypDdx5rhOL2qee"
                }
            failed:
                {"message":"Not found"}
        :rtype: json
        """
        res = requests.post(
                self.kong_url + '/consumers/' + consumer + '/jwt',
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                    }
                )
        return res.json()

    def encode(self, consumer):
        """加密，生成token

        :param consumer: 消费者
        :type consumer: str

        :return: token
                eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJRMGlDbzhSRXJTTk96bzZsQ3J5cERkeDVyaE9MMnFlZSIsIm5iZiI6MTU2MzYxMDQ2NCwiZXhwIjoxNTYzNjEyNDY0fQ.1H6od7gopPg3VN9gXqFhtSnaKCTsrSps5qMWLCNm-jg
        :rtype: str
        """
        data = self.getJwtInfo(consumer)
        token = jwt.encode( {
            'iss': data.get('key'),
            'nbf': data.get('created_at'),
            'exp': int(data.get('created_at')) + 2000
            },
            data.get('secret'),
            algorithm='HS256'
            )
        return token

if __name__ == '__main__':
    j = JWT_IN_KONG('http://192.168.43.114:8001')
    print(j.encode('tom'))
