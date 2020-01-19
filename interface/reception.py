# -*- coding:utf-8 -*-
from common.configHttp import RunMain
import faker
from common.getKeyword import get_result_for_keyword
import time


class Reception ():
    """接待接口"""

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def get_reception(self, header=None):
        """获取接待的页面数据,取得接待id,后面调取数据使用"""
        url = 'http://test.api.neurongenius.com/api/v2/reception/receptionList'
        data = {
            "startTime": "2020-01-18 00:00:00",
            "endTime": "2020-01-18 23:59:59",
            "customerType": [], "index": 1,
            "size": 15, "getTotalFlag": 1, "source": ''}
        data['startTime'] = time.strftime ("%Y-%m-%d") + " " + '00:00:00'
        data['endTime'] = time.strftime ("%Y-%m-%d") + " " + '23:59:59'
        method = 'post'
        data = str(data)
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def add_reception(self, header=None):
        """新建接待"""
        url = 'http://test.api.neurongenius.com/api/v2/reception/add'
        data = {"immediateTreatFlag": 0, "receptionType": "1",
                "receptionProject": "[{\"dataType\":1,\"dataId\":\"04a4a7b39efb6221db26b9ea3bfebd2a\",\"dataName\":\"皮肤科\"}]",
                "triageToUserId": "9d84c6ac6e0d2696ba815c935408417e", "receiverId": "9d84c6ac6e0d2696ba815c935408417e",
                "assistReceiverId": "", "urgentFlag": 0, "remark": "", "bespeakId": "",
                "customerId": "e176f8f47ca9b286ed871abc07bc4492", "receptionTypeName": "咨询", "assistReceiverName": "",
                "receiverName": "YT", "triageToUserName": "YT"}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def check_reception(self,id=None,header=None):
        """查看接待"""
        url = 'http://test.api.neurongenius.com/api/v2/reception/receptionDetails'
        data = {'id': id}
        method = 'get'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def update_reception(self,id=None,header=None):
        """编辑接待"""
        url = "http://test.api.neurongenius.com/api/v2/reception/update"
        data = {"immediateTreatFlag": 0, "receptionType": "1",
                "receptionProject": "[{\"dataType\":1,\"dataId\":\"04a4a7b39efb6221db26b9ea3bfebd2a\",\"dataName\":\"皮肤科\"}]",
                "triageToUserId": "9d84c6ac6e0d2696ba815c935408417e", "receiverId": "9d84c6ac6e0d2696ba815c935408417e",
                "assistReceiverId": "", "urgentFlag": 0, "remark": "", "bespeakId": "",
                "customerId": "e176f8f47ca9b286ed871abc07bc4492", "receptionTypeName": "咨询", "assistReceiverName": "",
                "receiverName": "YT", "triageToUserName": "YT", "id": "9f2a750ac7c84cf2af06b5558c2731a3"}
        method = 'put'
        data['id'] = id
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def delete_reception(self, id=None,header=None):
        """删除接待"""
        url = 'http://test.api.neurongenius.com/api/v2/reception/cancel?'
        data = {'id': id}
        # data = str (data).encode ()
        method = 'get'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response
