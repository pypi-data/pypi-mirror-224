"""
@Time : 2023/5/25 11:25 
@Author : skyoceanchen
@TEL: 18916403796
@项目：WaterSystemCarMounted
@File : url_parse_operations.by
@PRODUCT_NAME :PyCharm
"""
from urllib import parse

"""
HTTP请求头中的一些字符有特殊含义，转义的时候不会保留，如下：
加号（+）会转换成空格
正斜杠（/）分隔目录和子目录
问号（?）分隔URL和查询参数
百分号（%）制定特殊字符
#号指定书签
&号分隔参数

如若要在HTTP请求头中保留这些特殊字符，需将其转换成百分号（%）加对应的十六进制ASCII码，如：
+ ： %2B
空格 ： %20
/ ： %2F
? ： %3F
% ： %25
# ： %23
& ： %26
= ： %3D

 // URL内中文编码
 String s2 = Utils.encodeURIComponent(stringURL, "UTF-8");
 // ：和/都会被编码，导致http链接就会失效处理
 sEncodeURL = s2.replaceAll("\\%3A", ":").replaceAll("\\%2F", "/");
"""


class UrlParse(object):
    # 字典转换成url参数
    def dict_to_url_params(self, params: dict):
        """
        dic = {'username': 'username', 'password': 'password',}
        :param dic:
        :return: username=username&password=password
        """
        return parse.urlencode(params)

    # url参数转换成字典
    def url_params_to_dic(self, params: str):
        """
        params = 'https://www.baidu.com/s?&wd=python&ie=utf-8'或者
        params = '&wd=python&ie=utf-8'
        :param params:
        :return:{'wd': 'python', 'ie': 'utf-8'}
        """
        url = 'https://www.baidu.com/s?&wd=python&ie=utf-8'
        # 提取url参数
        if '?' in params:
            query = parse.urlparse(params).query  # wd=python&ie=utf-8
        else:
            query = params
        # 将字符串转换为字典
        params = parse.parse_qs(query)  # {'wd': ['python'], 'ie': ['utf-8']}
        """所得的字典的value都是以列表的形式存在，若列表中都只有一个值"""
        result = {key: params[key][0] for key in params}
        return result

    # 汉字转换成unicode编码
    def chinese_to_unicode(self, params: str, special_characters=False):
        """
        URL只允许一部分ASCII字符，其他字符（如汉字）是不符合标准的，此时就要进行编码。
        :param params:A中B国
        :return:A%E4%B8%ADB%E5%9B%BD
        :param special_characters:
        quote_plus 编码了斜杠,加号等特殊字符
        """
        if special_characters:
            return parse.quote_plus(params)
        else:
            return parse.quote(params)

    # unicode编码转换成汉字
    def unicode_to_chinese(self, params: str, special_characters=False):
        """
        :param params:A%E4%B8%ADB%E5%9B%BD
        :param special_characters:
        :return:A中B国
        unquote_plus 把加号解码成空格等特殊字符
        """
        if special_characters:
            return parse.unquote_plus(params)
        else:
            return parse.unquote(params)
