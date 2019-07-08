# -*- coding: utf-8 -*-
from datetime import datetime

from server import db

class Tasks(db.Model):
    """任务列表
    id: int
    任务: str 200
    备注: text
    开始时间: time
    结束时间: time
    日期: date
    共享: int 0否1是
    完成: int 0否1是
    """
    __tablename = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(50), nullable=False)
    remark = db.Column(db.Text, nullable=True)
    starttime = db.Column(db.Time(), nullable=True)
    endtime = db.Column(db.Time(), nullable=True)
    date = db.Column(db.Date(), nullable=False)
    isshare = db.Column(db.Integer, nullable=False, default=0)
    checked = db.Column(db.Integer, nullable=False, default=0)
