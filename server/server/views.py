# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, request, g

from server import app, db
from server.models import Tasks

from flask_restful import Resource, Api, reqparse
from pprint import pprint

import time
import datetime

parser = reqparse.RequestParser(trim=True)
parser.add_argument('name', location='json')
parser.add_argument('share', type=dict)
parser.add_argument('check', location=['json', 'args'])

api = Api(app)


def ifTodoId(todo_id):
    result = Tasks.query.filter_by( id = todo_id ).first_or_404()
    if not result:
        return { 'code': 400 }
    return result

class ToDo(Resource):
    """单个task的操作，包括删除和修改
    """

    # 获取单个任务信息
    def get(self, todo_id):
        return {
                'code': 20000,
                'msg': 'heihei'
                }

    # 删除任务
    def delete(self, todo_id):
        result = ifTodoId(todo_id)
        db.session.delete(result)
        db.session.commit()
        return {
                'code': 20000
                }

    # 修改任务
    def put(self, todo_id):
        parser = reqparse.RequestParser()
        print(parser)
        return ''


class ToDoList(Resource):
    """获取所有任务和增加任务
    """

    def __init__(self):
        self.today = datetime.date.today()

    # 获取今天的任务
    def get(self):
        result = Tasks.query.filter_by( date = self.today).all()
        data = [ dict(id=item.id, task=item.task, remark=item.remark,\
                starttime=item.starttime, endtime=item.endtime, \
                date=item.date, isshare=item.isshare) \
                for item in result]
        return {
                'code': 20000,
                'data': data
                }

    # 增加任务
    def post(self):
       # print(parser)
       # args = parser.parse_args()
        json_data = request.get_json(force=True)
        print(json_data)
       # print(args)
        return {
                'code': 20000,
                'data': 'hello'
                }



api.add_resource(ToDoList, '/todos')
api.add_resource(ToDo, '/todos/<todo_id>')
