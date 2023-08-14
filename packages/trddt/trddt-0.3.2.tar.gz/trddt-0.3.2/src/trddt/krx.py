# -*- coding: utf-8 -*-
import json 
from time import sleep 
from datetime import datetime


from ipylib.idebug import *


import requests 






################################################################
"""Request 파트"""
################################################################


Cookie = 'SCOUTER=x2uhfnqbd6tuvg; __utma=139639017.1028108896.1598516984.1673956930.1675903012.18; JSESSIONID=JyHENb3LQtcXeuFX0tWPrk1a1vu3zIm4gIOXlGY6a6hiVuOtxYPpl21WREhOLG4p.bWRjX2RvbWFpbi9tZGNvd2FwMi1tZGNhcHAxMQ==; _ga=GA1.1.1599836722.1691917298; _ga_Z6N0DBVT2W=GS1.1.1691917298.1.1.1691917309.0.0.0; JSESSIONID=AD3A1C07E4EF02DCC6868EA946A6DAF9.58tomcat3; _ga_808R2EHLL3=GS1.1.1691917310.1.0.1691917310.0.0.0'


def gen_headers():
    return { 
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8,es;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': Cookie,
        'Dnt': '1',
        'Referer': 'https://open.krx.co.kr/contents/MKD/01/0110/01100305/MKD01100305.jsp',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':"Windows",
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'X-Requested-With':'XMLHttpRequest',
    }


def inspect_response(res, title=None):
    if title is not None: pretty_title(title)
    else: print('\n\n')
    print(res)
    pp.pprint(res.__dict__)


def get_OTP():
    """
    OTP의 경우 내IP가 차단되지 않았다. 프록시 불필요.
    requests.post|.get 둘다 정상동작한다 ==> 잉? KRX 개웃기네 ㅋㅋㅋ
    """
    url = 'https://open.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F01%2F0110%2F01100305%2Fmkd01100305_01&name=form&_=1691917310145'
    res = requests.get(url, headers=gen_headers())
    # inspect_response(res, 'get_OTP')
    print({'OTP': res.text})
    return res.text


"""한국거래소 [KRX 시장/시장동향/증시일정/휴장일] 데이터를 수집한다"""
def fetch_holidays():
    url = 'https://open.krx.co.kr/contents/OPN/99/OPN99000001.jspx'

    data = []

    # 2009년부터 검색할 수 있음
    thisyear = datetime.today().year
    for year in range(2009, thisyear+2):
        payload = {
            'search_bas_yy': str(year),
            'gridTp': 'KRX',
            'pagePath': '/contents/MKD/01/0110/01100305/MKD01100305.jsp',
            'code': get_OTP(),
        }
        res = requests.post(url, data=payload)
        # inspect_response(res)
        
        d = json.loads(res.text)
        # pp.pprint(d)
        print({'year': year, 'DataLen': len(d['block1'])})
        data += d['block1']
        sleep(2)
        # break 

    logger.info(['휴장일 데이터 수집완료. 데이타 총길이:', len(data)])
    return data 
    