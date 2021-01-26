#coding=utf-8
"""
Created on 2020-1-21
@author: wangtongjian
Project:自动获取auth
"""
import requests
import json
import re


def getAuth():
    #输入手机号
    url = "https://dev.isengard.ricepo.com/v1/auth/customer"
    headers = {
        "User-Agent":"rohan/6.6.30 (com.ricepo.app; build:6.6.30.1; iOS 13.6.0) Alamofire/5.2.2",
        "X-Ricepo-Device":"E2DE4E1C-D0DD-4F14-924F-85938DD5BAD6",
        "X-Ricepo-Client":"Ricepo/6.6.30",
        "Connection":"keep-alive",
        "Content-Type": "application/json",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Accept-Language": "zh-Hans-CN;q=1.0",
        "Content-Length": "39",

    }
    data = {"phone":"+18666602261","method":"sms"}
    result = requests.post(url,data,headers).json()
    #print(result)
    #输入验证码
    data = {"vcode":"6666","phone":"+18666602261"}
    result = requests.post(url, data ,headers).json()
    auth = 'JWT '  + result['token']
    #print (auth)
    return auth


if __name__ == "__main__":

    getAuth()