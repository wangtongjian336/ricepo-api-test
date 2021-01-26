# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
import os
import time
import HTMLTestRunner
from common.sentEmail import sentEmail



#用例路径
case_path = os.path.join(os.getcwd())
#报告存放路径
report_path = os.path.join(os.getcwd(),'report')
#print (report_path)
'''
#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu1'))
suite.addTest(test_youdao.YoudaoTest('test_youdao1'))
'''
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    #打印获取了测试用例的名称
    #print(discover)
    return discover

if __name__=='__main__':
    #获取当前时间

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #html报告文件路径

    report_abspath = os.path.join(report_path, "result_" + now + ".html")

    #打开文件，将结果写入file中
    fp = open(report_abspath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'RICEPO接口自动化测试报告：',
                                           description=u'用例执行情况：')
    #执行测试
    runner.run(all_case())

    #发送邮件
    print (report_abspath)

    sentEmail.send_Email(report_abspath)
    fp.close()