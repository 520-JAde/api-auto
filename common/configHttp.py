#-*- coding:utf-8 -*-
import requests
import json
from common.Log import logger

logger = logger


class RunMain():

    def send_post(self, url, data=None, header=None):
        """
        定义一个方法，传入需要的参数url,data,header
        对header进行判断。
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header != None:
            result = requests.post(url=url, data=data, headers=header).json()
        else:
            result = requests.post(url=url, data=data).json() # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data=None, header=None):
        res = None
        if header != None:
            result = requests.get(url=url, data=data, headers=header)
        else:
            result = requests.get(url=url, data=data)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result
    def send_put(self, url, data=None, header=None):
        """
        定义一个方法，传入需要的参数url,data,header
        对header进行判断。
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header != None:
            result = requests.put(url=url, data=data, headers=header).json()
        else:
            result = requests.put(url=url, data=data).json() # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def run_main(self, method, url=None, data=None, header=None):
        """
        定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        :param method:
        :param url:
        :param data:
        :param header:
        :return:
        """
        result = None
        if method == 'post':
            result = self.send_post(url, data, header)
            logger.info(result)
        elif method == 'get':
            result = self.send_get(url, data, header)
            logger.info(result)
        elif method=='put':
            result = self.send_put(url, data, header)
            logger.info(result)
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result


if __name__ == '__main__':
    # 验证写的请求是否正确
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=yangtao&pwd=123456')
    print(result)
