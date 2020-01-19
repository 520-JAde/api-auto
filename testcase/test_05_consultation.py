from interface.consultation import Consultation
from common.getKeyword import get_result_for_keyword
import unittest
import json


class TestConsultation (unittest.TestCase):
    """咨询测试类"""
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
        response = Consultation ().login (method=self.method, url=self.url, data=self.data)
        res = get_result_for_keyword (response, 'token')
        self.token = {
            'Authorization': res
        }

    def test_01_add(self):
        """新增咨询"""
        header = self.token
        response = Consultation ().add_consultation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        print (result)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功，接口正常请求')
        else:
            print ('断言失败')

    def test_02_check(self):
        """查看咨询"""
        header = self.token
        response = Consultation ().check_consultation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        code = get_result_for_keyword (response, 'code')
        res = get_result_for_keyword (response, 'msg')
        result = {
            'code': code,
            'msg': res
        }
        if self.assertEqual (res, "查询成功") == None:
            print ('断言成功，接口正常请求')
            print ('咨询查看的接口返回参数为:', result)
        else:
            print ('断言失败')

    def test_03_update(self):
        """修改咨询数据"""
        header = self.token
        response = Consultation ().update_consultation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功，接口正常请求')
            print ('返回结果为:', result)
        else:
            print ('断言失败')

    def test_04_delete(self):
        """删除咨询数据"""
        header = self.token
        response = Consultation ().delete_consultation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if res == '数据不存在或错误':
            self.assertTrue(1)
            print ('接口正常请求')
        elif res == '已处理不能作废':
            self.assertTrue (1)
            print ('接口正常请求')
        else:
            print ('断言失败')
