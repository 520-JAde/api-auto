# -*- coding:utf-8 -*-

from common.configHttp import RunMain
import faker
from common.getKeyword import get_result_for_keyword
import time


class Bespeak ():
    """预约接口"""

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def add_bespeak(self, header=None):
        """新建预约"""
        url = 'http://test.api.neurongenius.com/api/v2/bespeak/add'
        # 新增的用户为user8
        data = {"anaesthesia": "[]", "fileId": "[]",
                "startTime": "2020-01-16 17:00:00", "endTime": "2020-01-16 17:30:00",
                "expertId": "9d84c6ac6e0d2696ba815c935408417e",
                "expertName": "YT", "customerId": "90af681799e5a7e0ef0a8f449e552afc",
                "bespeakTypeValue": "1", "bespeakTypeName": "咨询", "bespeakTypeColor": "#98d8a6", "operationFlag": 0,
                "inviteId": "9d84c6ac6e0d2696ba815c935408417e", "inviteName": "YT",
                "bespeakUserId": "9d84c6ac6e0d2696ba815c935408417e", "bespeakUserName": "YT",
                "bespeakProject": [{"dataType": 1, "dataId": "04a4a7b39efb6221db26b9ea3bfebd2a", "dataName": "皮肤科"}]}
        method = 'post'
        data['startTime'] = time.strftime ("%Y-%m-%d") + " " + '15:00:00'  # 新增预约在每天的三点
        # test = get_result_for_keyword(data,'startTime')
        # print(test)
        data['endTime'] = time.strftime ("%Y-%m-%d") + " " + '15:30:00'  # 结束时间在每天的三点半
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def get_bespeak(self, header=None):
        """预约列表"""
        url = 'http://test.api.neurongenius.com/api/v2/bespeak/bespeakList'
        data = {"index": 1, "size": 15, "endTime": "2020-01-16 23:59:59", "startTime": "2020-01-16 00:00:00",
                "getTotalFlag": 1}
        method = 'post'
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def check_bespeak(self, header=None):
        """查看预约"""
        url = 'http://test.api.neurongenius.com/api/v2/bespeak/getBespeakById?'
        data = {'id': '90af681799e5a7e0ef0a8f449e552afc'}
        method = 'get'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def update_bespeak(self, header=None):
        """编辑预约"""
        url = "http://test.api.neurongenius.com/api/v2/bespeak/update"
        data = {"anaesthesia": "[]", "purpose": "", "fileId": "[]", "id": "81305b8c3e7d45609ec6363258674e51",
                "startTime": "2020-01-18 15:00:00", "endTime": "2020-01-18 15:30:00",
                "expertId": "9d84c6ac6e0d2696ba815c935408417e", "expertName": "YT",
                "customerId": "90af681799e5a7e0ef0a8f449e552afc", "bespeakTypeValue": "1", "bespeakTypeName": "咨询",
                "bespeakTypeColor": "#98d8a6", "operationFlag": 0, "inviteId": "9d84c6ac6e0d2696ba815c935408417e",
                "inviteName": "YT", "bespeakUserId": "9d84c6ac6e0d2696ba815c935408417e", "bespeakUserName": "YT",
                "bespeakProject": [{"dataType": 1, "dataId": "04a4a7b39efb6221db26b9ea3bfebd2a", "dataName": "皮肤科"}]}
        method = 'put'
        data['startTime'] = time.strftime ("%Y-%m-%d") + " " + '17:00:00'  # 修改预约在每天的五点
        # test = get_result_for_keyword(data,'startTime')
        # print(test)
        data['endTime'] = time.strftime ("%Y-%m-%d") + " " + '17:30:00'  # 结束时间在每天的五半
        data = str (data).encode ()
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response

    def delete_bespeak(self, header=None):
        """删除预约"""
        url = 'http://test.api.neurongenius.com/api/v2/bespeak/cancel'
        data = '{"reason": "测试", "id": "90af681799e5a7e0ef0a8f449e552afc", "refundFlag": false}'
        # data = str (data).encode () # 字符串中有中文
        data = data.encode()
        method = 'put'
        response = RunMain ().run_main (method=method, url=url, data=data, header=header)
        return response


if __name__ == '__main__':
    Bespeak ().add_bespeak ()
