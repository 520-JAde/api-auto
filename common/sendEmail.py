# _*_ coding: utf-8 _*_

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpathInfo
from common import readConfig
import time
from common.Log import logger

# read_conf = readConfig.ReadConfig()
# subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
now = time.strftime("%Y_%m_%d %H-%M")  # 获取发送邮件的时间
# app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
# addressee = read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
# cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'report', 'report.html')  # 获取测试报告路径
logger = logger

class SendEmail:

    def sendEmail(self):
        # 1.准备发送邮件的基本信息
        smtpserver = 'smtp.163.com'
        sender = "yt18782452291@163.com"
        password = "YTZY01201216"
        addresses = [sender,'228289351@qq.com']
        # ,'fujia@neurongenius.com'

        # 2.编辑邮件
        # 创建一个带附件的邮件
        message = MIMEMultipart()
        message['from'] = sender
        message['to'] = ";".join(addresses)
        message['subject'] = "接口自动化测试报告"+now
        # 编辑正文
        text = "接口测试自动化报告"
        body = MIMEText(_text=text, _subtype='plain', _charset='utf-8')
        message.attach(body)
        # 添加附件
        with open(mail_path, 'rb')as fp:
            file_body = fp.read()

        att = MIMEText(_text=file_body, _subtype='base64', _charset='utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename=youjian.html'
        message.attach(att)
        # 3.发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        # 登录邮箱
        smtp.login(sender, password)
        # 发送邮件
        smtp.sendmail(sender, addresses, message.as_string())
        # 关闭邮箱
        smtp.quit()
        logger.info('send email ok!!!')


if __name__ == '__main__':
    SendEmail().sendEmail()
