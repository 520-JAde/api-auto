from interface.bespeak import Bespeak
from common.getKeyword import get_result_for_keyword
import unittest
import json


class TestBespeak (unittest.TestCase):
    """预约测试类"""
    url = "http://test.api.neurongenius.com/api/v1/login"
    data = '{"account":"001",' \
           '"password":"123456",' \
           '"isLoading":false,' \
           '"errorInfo":{"type":"","message":""},' \
           '"isRememberPWD":true}'
    method = 'post'

    def setUp(self):
        """
        登录取得token
        :return:
        """
        print ("测试开始")
        response = Bespeak ().login (method=self.method, url=self.url, data=self.data)
        res = get_result_for_keyword (response, 'token')
        self.token = {
            'Authorization': res
        }

    def test_01_add(self):
        """新增预约"""
        header = self.token
        response = Bespeak ().add_bespeak (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        print (result)
        res = get_result_for_keyword (response, 'msg')
        self.assertEqual (res, '新建预约成功')  # 对结果进行断言
        if self.assertEqual (res, "新建预约成功") == None:
            print ('断言成功，接口正常请求')
            print ("预约成功")
        else:
            print ('断言失败')

    def test_02_check(self):
        """查看预约"""
        header = self.token
        response = Bespeak ().get_bespeak (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        code = get_result_for_keyword (response, 'code')
        res = get_result_for_keyword (response, 'msg')
        result = {
            'code': code,
            'msg': res
        }
        if self.assertEqual (code, 10001) == None:
            print ('断言成功，接口正常请求')
            print ("预约成功,返回数据为:", result)
        else:
            print ('断言失败')

    def test_03_update(self):
        """修改预约数据"""
        header = self.token
        response = Bespeak ().update_bespeak (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        print (result)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功，接口正常请求')
            print ("预约成功")
        else:
            print ('断言失败')

    def test_04_delete(self):
        """删除预约数据"""
        header = self.token
        response = Bespeak ().delete_bespeak (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        # print (result)
        res = get_result_for_keyword (response, 'code')
        if self.assertEqual (res, 20002) == None:
            print ('断言成功，接口正常请求')
            print ("预约成功")
        else:
            print ('断言失败')
