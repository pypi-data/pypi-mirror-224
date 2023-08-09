# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 17:18:24
# @Author  : Pane Li
# @File    : inmongodb.py
"""
inmongodb

"""
from pymongo import MongoClient
import logging


class Mongodb:
    """mongodb数据库操作类

    数据类型：
            ObjectId： from bson.objectid import ObjectId   ex: ObjectId("5f1f5b9d9c1b9b0b8c8b4567")
            NumberLong: from bson.int64 import Int64   ex: Int64(123456789)
            NumberInt: from bson.int32 import Int32   ex: Int32(123456789)
            ISODate: from dateutil import parser   ex: parser.parse("2020-07-07T00:39:31.961Z")


    """

    def __init__(self, host: str, port: int, user: str = None, password: str = None):
        """
        初始化
        :param host: 主机
        :param port: 端口
        :param user: 用户名
        :param password: 密码
        """

        self.client = MongoClient(host, port, username=user, password=password)

    def insert(self, db: str, collection: str, data: dict):
        """
        插入数据
        :param db: 数据库
        :param collection: 集合
        :param data: 数据
                     数据类型：
                    ObjectId： from bson.objectid import ObjectId   ex: ObjectId("5f1f5b9d9c1b9b0b8c8b4567")
                    NumberLong: from bson.int64 import Int64   ex: Int64(123456789)
                    NumberInt: from bson.int32 import Int32   ex: Int32(123456789)
                    ISODate: from dateutil import parser   ex: parser.parse("2020-07-07T00:39:31.961Z")
        :return:
        """
        self.client[db][collection].insert_one(data, ordered=False)
        logging.info('insert data success')

    # 删除数据
    def delete(self, db: str, collection: str, data: dict):
        """
        删除数据
        :param db: 数据库
        :param collection: 集合
        :param data: 数据
        :return:
        """
        self.client[db][collection].delete_one(data)
        logging.info('delete data success')

    # 插入多条数据
    def insert_many(self, db: str, collection: str, data: list):
        """
        插入多条数据
        :param db: 数据库
        :param collection: 集合
        :param data: 数据
                    数据类型：
                    ObjectId： from bson.objectid import ObjectId   ex: ObjectId("5f1f5b9d9c1b9b0b8c8b4567")
                    NumberLong: from bson.int64 import Int64   ex: Int64(123456789)
                    NumberInt: from bson.int32 import Int32   ex: Int32(123456789)
                    ISODate: from dateutil import parser   ex: parser.parse("2020-07-07T00:39:31.961Z")
        :return:
        """
        self.client[db][collection].insert_many(data, ordered=False)
        logging.info('insert data success')

    # 更新数据
    def update_many(self, db: str, collection: str, data: dict, new_data: dict):
        """
        更新数据
        :param db: 数据库
        :param collection: 集合
        :param data: 数据     {'name': 'liwei'}
        :param new_data: 新数据  {'$set': {'name': 'liwei111'}}
                        数据类型：
                        ObjectId： from bson.objectid import ObjectId   ex: ObjectId("5f1f5b9d9c1b9b0b8c8b4567")
                        NumberLong: from bson.int64 import Int64   ex: Int64(123456789)
                        NumberInt: from bson.int32 import Int32   ex: Int32(123456789)
                        ISODate: from dateutil import parser   ex: parser.parse("2020-07-07T00:39:31.961Z")
        :return:
        """
        self.client[db][collection].update_many(data, new_data)
        logging.info('update data success')

    # 查询数据
    def find(self, db: str, collection: str, data: dict):
        """
        查询数据
        :param db: 数据库
        :param collection: 集合
        :param data: 数据     {'name': 'liwei'}
        :return:
        """
        return self.client[db][collection].find(data)

    # 聚合查询 且返回数据
    def aggregate(self, db: str, collection: str, data: list):
        """
        聚合查询
        :param db: 数据库
        :param collection: 集合
        :param data: 数据     [{'$match': {'name': 'liwei'}}]
        :return:
        """
        return list(self.client[db][collection].aggregate(data))

