# -*- coding:utf-8 -*-

from common.configHttp import RunMain
import faker
from common.getKeyword import get_result_for_keyword

f = faker.Faker('zh-cn')


class Preparation():
    """报备的相关接口"""

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def all_preparation(self,header=None):
        """当前页面的所有报备"""
        url = 'http://test.api.neurongenius.com/api/v1/preparation/page'
        data = {"page":1,"limit":15,"ifPay":"","ifBook":"","states":"","ifReception":""}
        method = 'post'
        data = str(data)
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def add_preparation(self, header=None):
        """新增报备的接口"""
        url = "http://test.api.neurongenius.com/api/v1/preparation/add"
        data = {"customerName": [{"name": "y2", "ismain": 1}], "projectIds": ["dict_04a4a7b39efb6221db26b9ea3bfebd2a"],
                "preTypeId": "5", "preUserId": "9d84c6ac6e0d2696ba815c935408417e",
                "preDeptId": "bfb24660a14d9be2f9d2e7a0af7e4b87",
                "customerPhone": [{"phone": "18782450012", "ismain": 1}], "fileId": [], "sourceTypeDetailType": ""}
        method = 'post'
        data['customerName'][0]['name'] = f.name_male()
        data['customerPhone'][0]['phone'] = f.phone_number()
        # self.name = get_result_for_keyword(data, 'name')
        # self.phone = get_result_for_keyword(data, 'phone')
        data = str(data)
        data = data.encode()
        # print(test1,test2,type(test1),type(test2))
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def check_preparation(self, header=None):
        """查看新增报备接口"""
        url = 'http://test.api.neurongenius.com/api/v1/preparation/ckDetail?'
        data = {'id': '1d42e07592a2988c0c3f676ee504c2c1'}
        # data = 'id=1301470e00c65f8d8bef4ba831dedd91'
        method = 'get'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def update_preparation(self,header=None):
        """修改报备的接口"""
        url = "http://test.api.neurongenius.com/api/v1/preparation/update"
        data = {"customerName": [{"name": "王建国", "ismain": 1}], "comeDate": "",
                "projectIds": ["dict_04a4a7b39efb6221db26b9ea3bfebd2a"], "preTypeId": "5", "remark": "",
                "preUserId": "9d84c6ac6e0d2696ba815c935408417e", "preDeptId": "bfb24660a14d9be2f9d2e7a0af7e4b87",
                "fileId": [], "customerPhone": [{"phone": "18512385958", "ismain": 1}],
                "id": "1dce9306777b67ad79b65c8a3758da18", "sourceTypeDetailType": ""}
        method = 'post'
        # pre_name = get_result_for_keyword(data,'name')
        # pre_phone = get_result_for_keyword(data,"phone")
        # print("修改前名字为：",pre_name)
        # print("修改前手机号为：",pre_phone)
        data['customerName'][0]['name'] = f.name_male()
        data['customerPhone'][0]['phone'] = f.phone_number()
        after_name = get_result_for_keyword(data,'name')
        after_phone = get_result_for_keyword(data,"phone")
        print("修改后名字为：", after_name)
        print("修改后手机号为：", after_phone)
        data = str(data)
        data = data.encode()
        # id = get_result_for_keyword(data,'id')
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def delete_preparation(self, uid=None,header=None):
        """删除报备的接口"""
        url = 'http://test.api.neurongenius.com/api/v1/preparation/delete?'
        data = {'id': uid}
        method = 'delete'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response


if __name__ == '__main__':
    response = Preparation().update_preparation(5)
    # response2 = Preparation().update_preparation()
    print(response)
