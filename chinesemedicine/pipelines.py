# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.conf import settings
import pymongo
class ChinesemedicinePipeline(object):
    # def __init__(self):
    #     self.file = codecs.open('D:\\PycharmProjects\\medicine1.json', mode='wb', encoding='utf-8')  # 数据存储到data.json
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + "\n"
    #     self.file.write(line.decode("unicode_escape"))
    #     return item
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指向指定的数据库
        mdb = client[dbname]
        # 获取数据库里存放数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        data = dict(item)
        # 向指定的表里添加数据
        self.post.insert(data)
        return item
