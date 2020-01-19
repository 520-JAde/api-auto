#-*- coding:utf-8 -*-
import jsonpath


def get_result_for_keyword(data, keyword):
    """
    通过关键字获取对应的一个值
    :param data:数据源
    :param keyword:关键字
    :return:一个值
    """
    return jsonpath.jsonpath(data, f"$..{keyword}")[0]


def get_results_for_keyword(data, keyword):
    """
    通过关键字获取所有对应的值
    :param data: 数据源
    :param keyword: 关键字
    :return: list
    """
    return jsonpath.jsonpath(data, f"$..{keyword}")



def get_results_for_label_keyword(data, label, keyword):
    """
    通过上层的标签,获取关键字对应的所有数据
    :param data: 数据源
    :param label: 上层标签
    :param keyword: 关键字
    :return: list
    """
    return jsonpath.jsonpath(data, f"$..{label}[*].{keyword}")


if __name__ == '__main__':
    pass

