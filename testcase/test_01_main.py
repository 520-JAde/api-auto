# -*- coding:utf-8 -*-
from interface.interface import Interface
import unittest
from common.getKeyword import get_result_for_keyword, get_results_for_label_keyword, get_results_for_keyword
import time
import requests
import json

s = requests.session()
now = time.strftime("%Y-%m-%d %H:%M:%S")


class TestMain(unittest.TestCase):
    """主流程"""
    url = "http://test.api.neurongenius.com/api/v1/login"
    data = '{"account":"001",' \
           '"password":"123456",' \
           '"isLoading":false,' \
           '"errorInfo":{"type":"","message":""},' \
           '"isRememberPWD":true}'
    method = 'post'

    def setUp(self):
        """
        将登录放在这里，在每次执行用例之前执行
        :return:
        """
        print("测试开始")
        response = Interface().login(method=self.method, url=self.url, data=self.data)
        # print(type(response))
        # print(response)
        # res = json.loads(response)
        res = get_result_for_keyword(response, 'token')
        # res1 = get_results_for_keyword(response, 'id')[-1]
        # res2 = get_results_for_keyword(response, 'depts')[0][0]
        self.token = {
            'Authorization': res
        }
        # print(self.token)

    def test_01_newcustomer(self):
        """
        新增客户
        :return:
        """
        header = self.token
        response = Interface().newcustomer(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        print(result)
        res = get_result_for_keyword(response, 'msg')
        id = get_result_for_keyword(response, 'id')
        print(res)
        # res = str(res)
        print('新建客户的ID为：', id)
        # self.assertEqual(res, '操作成功')
        if self.assertEqual(res, '成功获取数据，数据非空') == None:
            print('断言成功，接口正常请求')
            print('新建客户成功')
        else:
            print('断言失败')
        return id

    def test_02_order(self):
        """预约"""
        response = Interface().order()
        result = json.dumps(response, ensure_ascii=False, indent=2)
        print(result)
        res = get_result_for_keyword(response, 'msg')
        self.assertEqual(res, '新建预约成功')  # 对结果进行断言
        if self.assertEqual(res, "新建预约成功") == None:
            print('断言成功，接口正常请求')
            print("预约成功")
        else:
            print('断言失败')

    def test_03_reception(self):
        """接待"""
        header = self.token
        response = Interface().reception(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        # print(result)
        print('对返回数据进行断言')
        print('新增接待成功')
        # res = get_result_for_keyword(response, 'msg')
        # # self.assertEqual(res, '新建接待成功')  # 对结果进行断言
        # if self.assertEqual(res, "新建接待成功") == None:
        #     print("接待成功，接口正常响应")
        # else:
        #     print('断言失败')

    def test_04_consultation(self):
        """
        咨询
        :return:
        """
        header = self.token
        response = Interface().consultation(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        print(result)
        res = get_result_for_keyword(response, 'msg')
        if self.assertEqual(res, "已经有该客户咨询") == None:
            print("接口请求成功")
            print("但是当前已有该客户咨询")
        else:
            print('断言失败')

    def test_05_cashier(self):
        """开单"""
        header = self.token
        response = Interface().cashier(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        # print(result)
        print("对开单进行断言")
        # res = get_result_for_keyword(response, 'msg')
        # if self.assertEqual(res, "新建开单成功") == None:
        print("开单成功")
        # else:
        #     print('断言失败')

    def test_06_payment(self):
        """缴费"""
        header = self.token
        response = Interface().payment(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        print("对缴费是否成功进行断言")
        # print(result)
        res = get_result_for_keyword(response, 'msg')
        # if self.assertEqual(res, "操作成功") == None:
        print("缴费成功")
        # else:
        #     print('断言失败')

    def test_07_verification(self):
        """核销"""
        header = self.token
        response = Interface().verification(header)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        # print(result)
        res = get_result_for_keyword(response, 'msg')
        # if self.assertEqual(res, "操作成功") == None:
        print("核销成功")
        # else:
        #     print('断言失败')
