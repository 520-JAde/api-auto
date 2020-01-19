#-*- coding:utf-8 -*-
import unittest
import time
from common import HTMLTestRunnerPlugins
from common import sendEmail
import getpathInfo
# from common import readConfig

# read_conf = readConfig.ReadConfig()
on_off = 'on'

# 获取测试用例的文件夹
case_dir = './testcase'

# 建立测试报告存放路径
report_dir = './report'

# 将需要执行的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*")

# 规定生成测试报告的格式
now = time.strftime("%Y_%m_%d %H_%M")
file = open(report_dir + '\\' + 'report.html', 'wb')

# 实例化对象
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
                                        stream=file,
                                        title='接口自动化测试报告',
                                        description='预约--接待--咨询--开单--缴费--核销--出库'
                                                    '报备增删改查-预约增删改查-接待增删改查-咨询增删改查-面诊增删改查',
                                        verbosity=2,
                                        retry=0
                                        )

runner.run(discover)
file.close()
if on_off == 'on':
    send = sendEmail.SendEmail().sendEmail()
else:
    print("请在配置中打开发送邮箱开关")
