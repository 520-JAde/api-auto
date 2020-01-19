from interface.reception import Reception
from common.getKeyword import get_result_for_keyword
import unittest
import json


class TestReception (unittest.TestCase):
    """接待测试类"""
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
        response = Reception ().login (method=self.method, url=self.url, data=self.data)
        res = get_result_for_keyword (response, 'token')
        self.token = {
            'Authorization': res
        }
        response = Reception ().get_reception (self.token)
        if_id = get_result_for_keyword (response, 'total')
        if if_id == 0:
            print ('当前没有接待')
        else:
            self.reception_id = get_result_for_keyword (response, 'id')

    def test_01_add(self):
        """新增接待"""
        header = self.token
        response = Reception ().add_reception (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        print (result)
        res = get_result_for_keyword (response, 'msg')
        if res == '新建接待成功' or '该客户已有接待信息':
            self.assertTrue (1)
            print ('断言成功，接口正常请求')
        else:
            print ('断言失败')

    def test_02_check(self):
        """查看接待"""
        header = self.token
        reception_id = self.reception_id
        response = Reception ().check_reception (reception_id, header)
        response = response.json ()
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功')
            print ('查看接待成功请求,返回数据为:', result)
        else:
            print ('断言失败')

    def test_03_update(self):
        """修改接待数据"""
        header = self.token
        reception_id = self.reception_id
        response = Reception ().update_reception (reception_id,header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if res == '保存成功':
            self.assertTrue(1)
            print ('断言成功，接口正常请求')
            print ('接口返回数据为:', result)
        elif res == '客户已完成接诊，无法修改':
            self.assertTrue (1)
            print ('断言成功，接口正常请求')
            print ('接口返回数据为:', result)
        else:
            print ('断言失败')

    def test_04_delete(self):
        """删除接待数据"""
        header = self.token
        reception_id = self.reception_id
        response = Reception ().delete_reception (reception_id, header).json ()
        result = json.dumps (response, ensure_ascii=False, indent=2)
        # print (result)
        res = get_result_for_keyword (response, 'msg')
        if res == '操作成功':
            self.assertTrue(1)
            print ('断言成功，接口正常请求')
            print ('接口返回数据为:', result)
        elif res == '当前接待已产生业务，不能作废':
            self.assertTrue (1)
            print ('断言成功，接口正常请求')
            print ('接口返回数据为:', result)
        else:
            print ('断言失败')
