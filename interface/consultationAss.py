# -*- coding:utf-8 -*-
from common.configHttp import RunMain
import faker
from common.getKeyword import get_result_for_keyword


class ConsultationAss ():
    """面诊接口"""

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def add_consultationAss(self, header=None):
        """新建面诊"""
        url = 'http://test.api.neurongenius.com/api/v1/consultationInfo/add'
        data = {"id": "", "nowPill": [], "nowPillRemark": "", "channelType": [], "channelTypeRemark": "",
                "diagnosis": [], "consultationReceptionType": "1", "bellState": "", "monthState": "", "sleepState": "",
                "undealType": "", "plasticFlag": 1, "plasticRemark": "", "undealRemark": "", "handleRemark": "测试面诊",
                "customerRemark": "测试面诊", "proIds": [], "proTypes": [], "purposeProIds": [], "purposeTypes": [],
                "customerId": "abebe37e485fd9e6e08a268a5b5f3be8"}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def get_consultationAss(self, header=None):
        """面诊列表,获取我新增的面诊记录,取得id查看"""
        url = 'http://test.api.neurongenius.com/api/v1/assessment/page'
        data = {"page": 1, "size": 15, "types": [], "status": 2}
        method = 'post'
        data = str (data)
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def sure_consultationAss(self, id=None, header=None):
        """确认面诊"""
        url = 'http://test.api.neurongenius.com/api/v1/consultationInfo/sureAss'
        data = {"id": id, "nowPill": [], "nowPillRemark": "", "channelType": [],
                "channelTypeRemark": "", "diagnosis": [], "consultationReceptionType": "1", "bellState": "",
                "monthState": "", "sleepState": "", "undealType": "", "plasticFlag": 1, "plasticRemark": "",
                "undealRemark": "", "handleRemark": "测试新增面诊", "customerRemark": "测试新增面诊", "proIds": [], "proTypes": [],
                "purposeProIds": [], "purposeTypes": [], "customerId": "c0c4dadb50ac390d3b5ca33145950d0b",
                "ifChange": 0}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def check_consultationAss(self, id=None, header=None):
        """查看面诊"""
        url = 'http://test.api.neurongenius.com/api/v1/consultationInfo/detailAss?'
        data = {'id': id}
        method = 'get'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def update_consultationAss(self, header=None):
        """编辑面诊"""
        url = "http://test.api.neurongenius.com/api/v1/consultationInfo/updateAss"
        data = {"id": "f98400250688e1dc792ed45b0410c639", "nowPill": [], "nowPillRemark": "", "channelType": [],
                "channelTypeRemark": "", "diagnosis": [], "consultationReceptionType": "1", "bellState": "",
                "monthState": "", "sleepState": "", "undealType": "", "plasticFlag": 1, "plasticRemark": "",
                "undealRemark": "", "handleRemark": "修改面诊", "customerRemark": "修改面诊", "proIds": [], "proTypes": [],
                "purposeProIds": [], "purposeTypes": [], "customerId": "abebe37e485fd9e6e08a268a5b5f3be8"}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def delete_consultationAss(self, id=None, header=None):
        """删除面诊"""
        url = 'http://test.api.neurongenius.com/api/v1/flowbrandinfo/cancelCard'
        data = {"opType": 2, "cardType": 2, "id": id}
        data = str (data)
        method = 'post'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response
