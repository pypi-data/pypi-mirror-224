"""
@Time : 2023/5/25 11:32 
@Author : skyoceanchen
@TEL: 18916403796
@项目：WaterSystemCarMounted
@File : request_parse.by
@PRODUCT_NAME :PyCharm
"""
'''
headers = """accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
cache-control: no-cache
cookie: _ga=GA1.2.221399358.1578065734; __gads=ID=4df8a0420d9d97d4:T=1578065745:S=ALNI_MZLl3VF82H__z73FimSvjSPEEP3bw; UM_distinctid=170cf17a7bb413-0ddca1483240a5-4313f6b-144000-170cf17a7bd5f5; Hm_lvt_f1efa4dd0c4c1bdecd84dd62ecd602bc=1584714581; sc_is_visitor_unique=rx10890287.1585142350.D77706BECC854FF6BCE903A6B0BBAF9B.2.2.2.2.2.2.2.2.2; .CNBlogsCookie=BB254006969E71F3A98F5083C38181D35004ACCECDE4613542084BFA090A3887F4A94C45F72CBF961EEFCCFC091C030DACCF90BED81EB1A536F43977A83391E29CF9A8A0B47A4426A252897783333BBC75FEA283; _gid=GA1.2.1238470412.1587021206; .Cnblogs.AspNetCore.Cookies=CfDJ8B9DwO68dQFBg9xIizKsC6S-uJdcDdi_D3jcrVPifdxLT_LnW-CRpQc4LTd5Eph4WFGp8PxkTjH9DSYOT2H1iThP-KSsHl8IEaenQ8Gjb_6VBHAxSRe2-qdsyT9KC5Nf9PbK1ayiNBdpMeQSq0-ryK4MTQqukbztxIPZa6LHFRunAemQJpCtZWf-Gws2jHqi0vlt4lvdjSoFDpXFgwEu9Wj57la3c_fc4LvM23-XcRd6_37tg-O6FTuKproEmlRKo8IwH3dINLpgF6T5FOSq5qr6lT04uqawrOW81AZ2pJ8QSSquV9BuHXaQaWx6q_6OArQEOhEYF2dtZ7UtFIKyTQ92wtGWmkDULy87iHX1W7MV71e6PrtS3zDpdNHglEegeQtgh_oa-9eDZEUk2XfDlrvchPhUDNM_2DshOithXXgIxlAnzPMRmeSlEv0ClCTeN_kCKfmjINNB4SpEWBlISk1AoJCGyqRG4-2WphYtuWlh06MIpuSErFWYja39McH5-8m6UULAhiK2jYFe_-IFBm_S_-1yogWHue9A5jIG6Th_YUWZYyEybRW5DyAFPMcOnQ; _gat_gtag_UA_48445196_1=1
pragma: no-cache
referer: https://i-beta.cnblogs.com/posts/edit
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 chrome-extension chrome-extension
x-blog-id: 526720
"""



'''


class RequestParse(object):

    def analysis_header(self, headers):
        header_list = headers.strip(' ').strip('\n').split('\n')
        # print(header_list)
        header_lis = dict()
        for header in header_list:
            # pass
            # print(header_list)
            # header = head.split(':')
            header_lis[header.split(":", 1)[0]] = header.split(":", 1)[1]
        return header_lis

    def analysis_cookies(self, cookies):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        url = 'https://www.yaozh.com/member/'
        # cookies是一个字典或者对象
        # cookies = "acw_tc=2f624a6c15681000021367682e6b3e0142e0d99eb63cf4b240f962532ebfef; PHPSESSID=09f00am6llg7cmodj751rj8b54; _ga=GA1.2.1617503464.1568100004; _gid=GA1.2.1446416891.1568100004; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1568100005; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1568100020"
        # cookies = "hello=1; _ga=GA1.2.1304839036.1579713995; _gid=GA1.2.300468293.1580308967; rr=https://cn.aq101.club/; last_login=ceshi%40qq.com; lt=eyJpdiI6IkNMcXFVeFplOVorV2xydnVwcDRqVGc9PSIsInZhbHVlIjoicXlpREIyQ2FFUHFGWitKN1NLNlZRWFhHRXNKOXBsbEV6RUdFc09Jait0cz0iLCJtYWMiOiJiOTVkMzUzMGZiOWZjOTRlMWNmYjY5ODFjODRiMmYwYWI2NGRmNWQxNmJmNmNkMGNjYjMwZjQzZjViNjliNTY4In0%3D; _gat_gtag_UA_78207029_9=1; XSRF-TOKEN=eyJpdiI6IlM2T2hkWjZcL0F3d0VCMEN3a2pOb0h3PT0iLCJ2YWx1ZSI6ImN4eDZaU2RseUQ2OVhySFhpYUUwZHBxc0IxaXVTQ1JSc2pFTWx3Q1BQbExjSUJBNUlPNHdGYllva1RBZzIxc2QiLCJtYWMiOiI5ZGZiODJkMDgzYzA3YmVhMmFkZWUyNjNhMDgzMWM0NjUzNTRjYWVjODM2ZjIyNTY2ZmRkOTJhYzRmMTEzN2U3In0%3D; miao_cn=eyJpdiI6Im1pZzBFZEl6UzFzd01HMGV3c2lab1E9PSIsInZhbHVlIjoiNzNmQmZlOG5UdXcxa0JjMmVIWldRZUg5cXRcL1BTRnZPXC9uZk8wM044WlhnWlFONGEzdlRUU1F2NnJyOGZBbTFSIiwibWFjIjoiN2QwNDBmZjI2YzZkNDI0YzE0MGZhNGY3NWRiZmFlMWU0NjMxNjhjMmVhY2Y2ZTVhYmM5MzdlZjA5NjYzMDFlZCJ9"
        # cookies = "lianjia_uuid=53fb8ed4-d6dd-4223-bf03-9a95c5a3abb5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216fd6645af54be-0b5f0714a2a0e1-7711439-1327104-16fd6645af7376%22%2C%22%24device_id%22%3A%2216fd6645af54be-0b5f0714a2a0e1-7711439-1327104-16fd6645af7376%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-shytl0-84as1-33we6te3dky6iv5-203i1t2pz; login_ucid=2000000096534040; lianjia_token=2.0057730a462b2899b246de2377d6542c94; lianjia_ssid=8e0ae7f4-c548-4e19-9dae-4d2a6d6fcb16; select_city=310000"
        # cookies = '_ga=GA1.2.221399358.1578065734; __gads=ID=4df8a0420d9d97d4:T=1578065745:S=ALNI_MZLl3VF82H__z73FimSvjSPEEP3bw; UM_distinctid=170cf17a7bb413-0ddca1483240a5-4313f6b-144000-170cf17a7bd5f5; Hm_lvt_f1efa4dd0c4c1bdecd84dd62ecd602bc=1584714581; sc_is_visitor_unique=rx10890287.1585142350.D77706BECC854FF6BCE903A6B0BBAF9B.2.2.2.2.2.2.2.2.2; .CNBlogsCookie=BB254006969E71F3A98F5083C38181D35004ACCECDE4613542084BFA090A3887F4A94C45F72CBF961EEFCCFC091C030DACCF90BED81EB1A536F43977A83391E29CF9A8A0B47A4426A252897783333BBC75FEA283; _gid=GA1.2.1238470412.1587021206; .Cnblogs.AspNetCore.Cookies=CfDJ8B9DwO68dQFBg9xIizKsC6S-uJdcDdi_D3jcrVPifdxLT_LnW-CRpQc4LTd5Eph4WFGp8PxkTjH9DSYOT2H1iThP-KSsHl8IEaenQ8Gjb_6VBHAxSRe2-qdsyT9KC5Nf9PbK1ayiNBdpMeQSq0-ryK4MTQqukbztxIPZa6LHFRunAemQJpCtZWf-Gws2jHqi0vlt4lvdjSoFDpXFgwEu9Wj57la3c_fc4LvM23-XcRd6_37tg-O6FTuKproEmlRKo8IwH3dINLpgF6T5FOSq5qr6lT04uqawrOW81AZ2pJ8QSSquV9BuHXaQaWx6q_6OArQEOhEYF2dtZ7UtFIKyTQ92wtGWmkDULy87iHX1W7MV71e6PrtS3zDpdNHglEegeQtgh_oa-9eDZEUk2XfDlrvchPhUDNM_2DshOithXXgIxlAnzPMRmeSlEv0ClCTeN_kCKfmjINNB4SpEWBlISk1AoJCGyqRG4-2WphYtuWlh06MIpuSErFWYja39McH5-8m6UULAhiK2jYFe_-IFBm_S_-1yogWHue9A5jIG6Th_YUWZYyEybRW5DyAFPMcOnQ; _gat_gtag_UA_48445196_1=1'
        cook_dic = dict()
        cookies_list = cookies.split('; ')
        for cook in cookies_list:
            cook_dic[cook.split('=')[0]] = cook.split('=')[1]
        # reponse = requests.get(url=url,headers = headers,cookies = cook_dic)
        # print(reponse.content.decode())
        print(cook_dic)
