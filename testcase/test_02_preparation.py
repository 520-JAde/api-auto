from interface.preparation import Preparation
from common.getKeyword import get_result_for_keyword
import unittest
import json


class TestPreparation (unittest.TestCase):
    """报备测试类"""
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
        response = Preparation ().login (method=self.method, url=self.url, data=self.data)
        res = get_result_for_keyword (response, 'token')
        self.token = {
            'Authorization': res
        }
        response = Preparation ().all_preparation (self.token)
        # response = response.json()
        self.userid = get_result_for_keyword (response, 'id')
        # print(self.token)
        # header = self.token
        # response = Preparation().check_preparation(self.token)
        # response = response.json()
        # print(response)
        # self.userid = get_result_for_keyword(response, 'id')

    def test_01_add(self):
        """新增报备"""
        header = self.token
        response = Preparation ().add_preparation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        res1 = '添加成功'
        if self.assertEqual (res, res1) == None:
            print ("断言成功")
            print ('新增成功,返回参数为:', result)
        else:
            print ("断言失败，请检查接口是否请求")

    def test_02_check(self):
        """查看报备接口"""
        header = self.token
        # id = self.userid
        response = Preparation ().check_preparation (header)
        response = response.json ()
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, '查询成功') == None:
            print ('断言成功')
            print ("查看报备接口正常，返回参数为：", result)
        else:
            print ('断言失败')
        # return get_result_for_keyword(response, 'id')

    def test_03_update(self):
        """编辑报备信息接口"""
        header = self.token
        response = Preparation ().update_preparation (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        res1 = '修改成功'
        if self.assertEqual (res, res1) == None:
            print ("断言成功")
            print ('新增成功,返回参数为:', result)
        else:
            print ("断言失败，请检查接口是否请求")

    def test_04_delete(self):
        """删除报备信息接口"""
        header = self.token
        uid = self.userid
        response = Preparation ().delete_preparation (uid, header)
        response = response.json ()
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, '删除成功') == None:
            print ('断言成功')
            print ("删除报备接口正常，返回参数为：", result)
        else:
            print ('断言失败')


if __name__ == '__main__':
    unittest.main ()
