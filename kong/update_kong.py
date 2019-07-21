#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from pprint import pprint


class KONG:

    def __init__(self, kong_url='http://localhost:8001/'):
        self.kong_url = kong_url


class Service(KONG):

    def __init__(self, kong_url='http://localhost:8001/'):
        KONG.__init__(self, kong_url='http://localhost:8001/')

    def Add(self, name, url):
        res = requests.post(
                self.kong_url + 'services/',
                data = {
                    'name': name,
                    'url': url
                    }
                )
        pprint(res.json())

    def List(self):
        res = requests.get(
                self.kong_url + 'services'
                )
        pprint(res)


class Route(KONG):

    def __init__(self, kong_url='http://localhost:8001/'):
        KONG.__init__(self, kong_url='http://localhost:8001/')

    def Create(self, service_name_or_id, host, name=None, paths=None):
        res = requests.post(
                self.kong_url + 'services/' + service_name_or_id + '/routes',
                data = {
                    'name': name,
                    'paths[]': paths,
                    'hosts[]': host
                    }
                )
        pprint(res.json())

    def Delete(self, name_or_id):
        res = requests.delete(
                self.kong_url + 'routes/' + str(name_or_id)
                )
        pprint(res)

    def List(self, service_name_or_id=None):
        if service_name_or_id:
            url = self.kong_url + 'services/' + \
                    str(service_name_or_id) + '/routes'
        else:
            url = self.kong_url + 'routes'
        res = requests.get(url)
        pprint(res.json())



class Consumer(KONG):

    def __init__(self, kong_url='http://localhost:8001/'):
        KONG.__init__(self, kong_url='http://localhost:8001/')

    def Create(self, username, custom_id, tags=None):
        res = requests.post(
                self.kong_url + 'consumers',
                data = {
                    'username': username,
                    'custom_id': custom_id,
                    'tags': tags
                    }
                )
        pprint(res.json())

    def Delete(self, username_or_id):
        res = requests.delete(
                self.kong_url + 'consumers/' + str(username_or_id)
                )
        pprint(res)

    def List(self):
        res = requests.get(
                self.kong_url + 'consumers'
                )
        pprint(res.json())

if __name__ == '__main__':
    # s = Service()
    # # s.Add('front', 'http://192.168.43.114:8080')
    # s.Add('server', 'http://192.168.43.114:5000')

    # r = Route()
    # r.Create('server', '192.168.43.114', 'server', '/server')

    c = Consumer()
    c.Create('tom', 1)

