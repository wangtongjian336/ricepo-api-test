#coding=utf-8
"""
Created on 2020-1-21
@author: wangtongjian
Project: 发送邮件到指定邮箱
"""

import smtplib    # 导入smtplib模块
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


class sentEmail():


    def send_Email(report_path):

          with open(report_path, 'r', encoding='utf-8') as f:
              mail_body = f.read()                                    # 打开测试报告，读取报告内容作为邮件内容
          sender = '63307596@qq.com'                                  # 发出邮箱
          receivers = ['tongjianwang336@gmail.com','tongjian@ricepo.com']                   # 接收邮箱
          mail_server = 'smtp.qq.com'                                 # 发送邮箱服务地址，这里qq邮箱
          subject = '自动化测试报告'                                    # 邮件标题
          username = '63307596@qq.com'                                # 邮箱登录名
          passwd = 'kolmnqhrorxsbihe'                                 # 密码

          # 设置邮件格式
          message = MIMEMultipart()
          text_msg = MIMEText(mail_body, 'html', 'utf8')
          message.attach(text_msg)

          # 添加附件
          att = MIMEText(open(report_path, "rb").read(), "base64", "utf-8")
          att["Content-Type"] = "application/octet-stream"
          att.add_header('content-disposition', 'attachment', filename=report_path.split('/')[-1])
          message.attach(att)
          message['Subject'] = Header(subject, charset='utf-8')

          # 自定义发件人和收件人信息
          def _format_addr(s):
               addr = parseaddr(s)
               return formataddr(addr)
          message['From'] =  _format_addr(u'王同健 <%s>'%sender)
          for receiver in receivers:
               message['to'] = _format_addr(receiver)

          # 邮箱登录
          smtp = smtplib.SMTP_SSL(mail_server,465)                     # 实例化smtplib.SMTP_SSL()类对象
          smtp.login(username, passwd)                                 # 登录


          # 发送邮件
          for i in receivers:
              smtp.sendmail(sender, i, message.as_string())
          smtp.quit()
if __name__ == '__main__':
     pass