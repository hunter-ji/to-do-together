#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import time
import datetime
# 今天日期
today = datetime.date.today()
# 昨天时间
yesterday = today - datetime.timedelta(days=1)
# 明天时间
tomorrow = today + datetime.timedelta(days=1)
acquire = today + datetime.timedelta(days=2)
# 昨天开始时间戳
yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
# 昨天结束时间戳
yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
# 今天开始时间戳
today_start_time = yesterday_end_time + 1
# 今天结束时间戳
today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
# 明天开始时间戳
tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))
# 明天结束时间戳
tomorrow_end_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
print '今天时间戳'
print today_start_time
print today_end_time
print '昨天时间戳'
print yesterday_start_time
print yesterday_end_time
print '明天时间戳'
print tomorrow_start_time
print tomorrow_end_time
