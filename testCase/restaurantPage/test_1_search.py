#coding=utf-8
"""
Created on 2021-01-20
@author: wangtongjian
Project:测试饭店页查询接口
"""
import requests
import unittest
import json
import re
from common.getAuth import getAuth


class restaurantPageTest(unittest.TestCase):
    def setUp(self):
        self.url = ""
        self.data ={}
        auth = getAuth()
        self.headers = {"Authorization":auth}
    #测试在放大镜中查询饭店
    def test_01(self):
        url = "https://dev.isengard.ricepo.com/v1/restaurants?location=-149.8028579%2C61.1890887&search=rest1"
        data = self.data
        headers = self.headers
        result = requests.get(url, headers=headers).json()
        print (result[0]['_id'])
        self.assertEqual(result[0]['_id'],'rest_2XCwVsaSz')

    # 测试在放大镜中查询菜品
    def test_02(self):
        url = "https://dev.isengard.ricepo.com/v1/restaurants?location=-149.8028579%2C61.1890887&search=%E7%83%A4%E7%BE%8A%E8%85%BF"
        data = self.data
        headers = self.headers
        result = requests.get(url, headers=headers).json()
        print(result[0]['items'][0]['name']['zh-CN'])
        self.assertEqual(result[0]['items'][0]['name']['zh-CN'], '烤羊腿12345')

    def tearDown(self):
        pass

if __name__ == "__main__":

    unittest.main()
