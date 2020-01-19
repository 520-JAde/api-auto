# -*- coding:utf-8 -*-
from common.configHttp import RunMain
import faker
from common.getKeyword import get_result_for_keyword
import time


class Consultation ():
    """咨询接口"""

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def get_consultation(self, header=None):
        """咨询列表,获取我新增的记录,取得id查看"""
        url = 'http://test.api.neurongenius.com/api/v1/assessment/page'
        data = {"page": 1, "size": 15, "types": [], "status": 2}
        method = 'post'
        data = str (data)
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def add_consultation(self, header=None):
        """新建咨询"""
        url = 'http://test.api.neurongenius.com/api/v1/consultationInfo/add'
        data = {"nowPill": [], "nowPillRemark": "", "channelType": [], "channelTypeRemark": "", "diagnosis": [],
                "plasticFlag": 1, "bellState": "", "monthState": "", "sleepState": "", "undealRemark": "",
                "handleRemark": "测试新建咨询是否成功", "customerRemark": "会尝试删除,不会影响业务", "id": "", "proIds": [], "proTypes": [],
                "purposeProIds": [], "purposeTypes": [], "toUserId": "", "ifExit": 0, "consultationReceptionType": "1",
                "customerId": "4bfe6fe44f680b508b84870ed10cdb7f"}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def check_consultation(self, header=None):
        """查看咨询"""
        url = 'http://test.api.neurongenius.com/api/v1/consultation/page'
        data = {"page": 1, "size": 15, "types": [], "startTime": "2020-01-18", "endTime": "2020-01-18", "status": 2}
        method = 'post'
        data['startTime'] = time.strftime ("%Y-%m-%d")
        data['endTime'] = time.strftime ("%Y-%m-%d")
        data = str (data)
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def update_consultation(self, header=None):
        """编辑咨询"""
        url = "http://test.api.neurongenius.com/api/v1/consultationInfo/update"
        data = {"nowPill": [], "nowPillRemark": "", "channelType": [], "channelTypeRemark": "", "diagnosis": [],
                "proIds": [], "proTypes": [], "purposeProIds": [], "purposeTypes": [], "bellState": "",
                "monthState": "", "sleepState": "", "plasticRemark": "", "undealRemark": "",
                "handleRemark": "该条信息最后会被删除，不会影响到业务", "customerRemark": "测试新增咨询接口",
                "id": "2d8aff5e85b36427ac65b18a1a57c000", "customerId": "4bfe6fe44f680b508b84870ed10cdb7f",
                "consultationReceptionType": "1"}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def delete_consultation(self, header=None):
        """删除咨询"""
        url = 'http://test.api.neurongenius.com/api/v1/flowbrandinfo/cancelCard'
        data = {"opType": 1, "cardType": 1, "id": "f372cdd4478c81f4f717c1199e43882a"}
        data = str (data)
        method = 'post'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response
