# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, request, g

from server import app, db
from server.models import Tasks

from flask_restful import Resource, Api
from pprint import pprint

import json
import time
import datetime

api = Api(app)


def ToDo(Resource):
    """单个task的操作，包括删除和修改
    """
    def __init__(self):
        self.result = tasks.query.filter_by( id = todo_id ).first()
        if not self.result:
            return { 'code': 400 }

    # 删除任务
    def delete(self, todo_id):
        db.session.delete(self.result)
        db.session.commit()
        return {
                'code': 200
                }

    # 修改任务
    def post(self, todo_id):
        parser = reqparse.RequestParser()
        return ''


def ToDoList(Resource):
    """获取所有任务和增加任务
    """
    def __init__(self):
        self.today = datetime.date.today()

    # 获取今天的任务
    def get(self):
        result = tasks.query.filter_by( date = self.today ).all()
        data = [ dict(id=item.id, task=item.task, remark=item.remark,\
                starttime=item.starttime, endtime=item.endtime, \
                date=item.date, isshare=item.isshare) \
                for item in result]
        return {
                'code': 200,
                'data': data
                }

    # 增加任务
    def post(self):
        parser = reqparse.RequestParser()
        print(parser)
        return ''



api.add_resource(ToDo, '/todo/<todo_id>')
api.add_resource(ToDoList, '/todos')
