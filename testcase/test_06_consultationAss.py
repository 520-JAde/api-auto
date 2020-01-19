from interface.consultationAss import ConsultationAss
from common.getKeyword import get_result_for_keyword
import unittest
import json


class TestConsultationAss (unittest.TestCase):
    """面诊测试类"""
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
        response = ConsultationAss ().login (method=self.method, url=self.url, data=self.data)
        res = get_result_for_keyword (response, 'token')
        self.token = {
            'Authorization': res
        }
        response = ConsultationAss ().get_consultationAss (self.token)
        self.consultationAss_id = get_result_for_keyword (response, 'id')

    def test_01_add(self):
        """新增面诊"""
        header = self.token
        response = ConsultationAss ().add_consultationAss (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功，接口正常请求')
            print ('请求返回数据为:', result)
        else:
            print ('断言失败')

    def test_02_check(self):
        """查看面诊"""
        header = self.token
        consultationAss_id = self.consultationAss_id
        response = ConsultationAss ().check_consultationAss (consultationAss_id, header).json ()
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'code')
        if self.assertEqual (res, 10001) == None:
            print ('断言成功，接口正常请求')
            print ('该条面诊记录为:', result)
        else:
            print ('断言失败')

    def test_03_update(self):
        """修改面诊数据"""
        header = self.token
        consultationAss_id = self.consultationAss_id
        if_uid = ConsultationAss ().sure_consultationAss(consultationAss_id,header)
        print(if_uid)
        response = ConsultationAss ().update_consultationAss (header)
        result = json.dumps (response, ensure_ascii=False, indent=2)
        res = get_result_for_keyword (response, 'msg')
        if self.assertEqual (res, "操作成功") == None:
            print ('断言成功，接口正常请求')
            print ('修改面诊后返回参数:', result)
        else:
            print ('断言失败')

    def test_04_delete(self):
        """删除面诊数据"""
        header = self.token
        consultationAss_id = self.consultationAss_id
        response = ConsultationAss ().delete_consultationAss (consultationAss_id, header)
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
