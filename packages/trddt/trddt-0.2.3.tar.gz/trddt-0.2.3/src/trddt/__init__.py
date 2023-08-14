# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta, time, tzinfo, timezone
import re
import os 
import zipfile


import pandas as pd
import holidays


from ipylib.idebug import *
from ipylib import ipath
from ipylib.idatetime import DatetimeParser



File = {
    'InitYear':1980,
    'TimezoneName':'Asia/Seoul',
    'TimezoneHour':+9,
    'MarketTime':{
        '정규장 매매가능 시작시간':{'hour':8, 'minute':20},
        '장전 동시호가 시작시간':{'hour':8, 'minute':30},
    }
}



     


DATA_PATH = os.path.dirname(__file__)


@ftracer
def build_HolidaysCSV(file='C:\pypjts\TradeDatetime\Holidays.xlsx'):
    """Zip파일인지, 엑셀파일인지 감지 후 자동으로 압축풀기"""
    root, ext = os.path.splitext(os.path.basename(file))
    if ext == '.xlsx':
        xls_path = os.path.realpath(file)
        # print({'xls_path': xls_path})
        xls_dir = os.path.dirname(xls_path)
        xls_file = os.path.basename(xls_path)
        # pp.pprint([xls_path, xls_dir, xls_file])
    elif ext == '.zip':
        """압축파일풀기"""
        zip_path = os.path.abspath(file)
        zip_dir = os.path.dirname(zip_path)
        zip_file = os.path.basename(zip_path)
        xls_file, ext = os.path.splitext(zip_file)
        xls_path = os.path.join(zip_dir, xls_file)
        # pp.pprint([zip_dir, zip_file, xls_file, ext, xls_path])
        zipfile.ZipFile(zip_path).extractall(zip_dir)

    """엑셀파일 읽기"""
    filename, ext = os.path.splitext(xls_file)
    # pp.pprint([filename, ext])
    df = pd.read_excel(xls_path)
    print(df)
    
    """CSV파일로 변환저장"""
    csv_path = os.path.join(DATA_PATH, filename+'.csv')
    df.to_csv(csv_path, index=False)


def get_Holidays():
    csv_file = os.path.join(DATA_PATH, 'Holidays.csv')
    df = pd.read_csv(csv_file)
    # df.info()
    # print(df)
    # return df 
    days = list(df.Date)
    days = [datetime.strptime(t, "%Y-%m-%d").astimezone() for t in days]
    return days


HOLIDAYS = get_Holidays()


"""토, 일 + 법정공휴일에 해당하는지 여부"""
def isin_holiday(t):
    return True if t in HOLIDAYS else False

def isin_market_holiday(t):
    return True if t.weekday() in [5,6] or t in HOLIDAYS else False


def now(microsecond=True, testnow=None):
    t = datetime.today().astimezone()
    if microsecond: pass
    else: t = t.replace(microsecond=0)

    # if testnow is None: pass
    # else:
    #     if 0 <= t.hour <= 6:
    #         t -= timedelta(days=1)
    #         # 주말 제외
    #         while t.weekday() in [5,6]: t -= timedelta(days=1)
    #         # 조작할 현재시간을 셋팅
    #         # print('밤샘테스트용 현재시간 강제조정')
    #         t1 = DatetimeParser(testnow)
    #         t = t.replace(hour=t1.hour, minute=t1.minute, second=0)
    #     else: pass
    return t


def today(): return now().replace(hour=0, minute=0, second=0, microsecond=0)


"""법정공휴일 or 주말 제외"""
def _exclude(t, unit):
    while t.weekday() in [5,6] or isin_holiday(t):
        t += timedelta(days=unit)
    return t

"""증권시스템상 새벽시간은 이전날짜로 취급한다"""
def _adjust_midnight(t, **kw):
    _now = now()
    if 0 <= _now.hour < 6: t -= timedelta(**kw)
    return t


def date(day=None, delta=0): 
    day = today() if day is None else DatetimeParser(day)

    _now = now()
    if 0 <= _now.hour < 6: day += timedelta(days=-1)

    if delta == 0:
        day = _exclude(day, -1)
    else:
        unit = +1 if delta > 0 else -1
        for i in range(abs(delta)):
            day += timedelta(days=unit)
            day = _exclude(day, unit)

    return day


def time(t=None, delta=0):
    t = now() if t is None else DatetimeParser(t)
    t = _adjust_midnight(t, hours=6)
    t = _exclude(t, -1)
    return t


"""예측일|거래예정일::최종거래일을 입력하면 거래예정일을 반환한다"""
def predict_day(lastday=None):

    # 시간대에 따른 조정
    _now = now()
    if 0 <= _now.hour < 7:
        day = date(lastday, delta=+1)
    elif 7<= _now.hour < 20: 
        day = date(lastday)
    elif 20 <= _now.hour <= 23:
        day = date(lastday, delta=+1)
    # print({'day': day})

    if day.weekday() in [5,6]:
        day = date(day, delta=+1)
    # print({'day': day})

    return day 


def logtime(): return now().strftime('%H:%M:%S,%f')[:-3]





def trddays(t1=None, t2=None, delta=30):
    """
    t1(start)부터 t2(end)까지 KRX-Market Open Days를 반환.
    """
    t2 = today() if t2 is None else tradeday(t2)
    if t1 is None:
        t1 = date(t2, delta=-delta)
    else:
        t1 = date(t1)

    days = pd.bdate_range(start=t1, end=t2).to_pydatetime()
    return list(days)


def omit_holidays(dts):
    """dts의 dt 는 datetime or pd.Timestamp
    """
    s = pd.Series(dts)
    if s.dt.tz is None:
        s = s.dt.tz_localize(tz=TZ_STRING)
    else:
        s = s.dt.tz_convert(tz=TZ_STRING)

    dts = s[~s.isin(HOLIDAYS)].dt.to_pydatetime()
    return list(dts)


class Holiday:
    # holidays-package 사용 --> 기초적인 공휴일
    # 대체공휴일 추가 필요

    def __init__(self, mkt):
        self.market = mkt
        if self.market == 'KRX':
            self._file = 'HolidayHandler.csv'

    def _read_data(self):
        DataPath = 'C:\pjts\TrdDatetime\Data'
        fpath = ipath.clean_path(f"{DataPath}/{self._file}")
        print('fpath:', fpath)
        df = pd.read_csv(fpath, parse_dates=['dt'])
        df.info()
        print(df)

    def _fetch_data(self):
        # 인터넷에서 수집
        return


class MarketTime:

    def __init__(self): pass

    """정규장 매매가능 시작"""
    @classmethod
    def mkt_buyable_opening(self): return today().replace(hour=8, minute=20)
    """장전 전일종가 시작"""
    @classmethod
    def pre_open(self): return today().replace(hour=8, minute=30)
    """장전 동시호가 시작"""
    @classmethod
    def openingcallprc(self): return today().replace(hour=8, minute=40)
    """정규장 시작"""
    @classmethod
    def open(self): return today().replace(hour=9)
    """장 마감 동시호가 시작"""
    @classmethod
    def closingcallprc(self): return today().replace(hour=15, minute=20)
    """정규장 종료"""
    @classmethod
    def close(self): return today().replace(hour=15, minute=30)
    """장후 당일종가 시작"""
    @classmethod
    def post_open(self): return today().replace(hour=15, minute=40)
    """시간외 단일가 시작"""
    @classmethod
    def after_open(self): return today().replace(hour=16)
    """시간외 단일가 종료"""
    @classmethod
    def after_close(self): return today().replace(hour=18)
    @classmethod
    def stock_is_open(self): return False if now() < self.open() else True

    """장전 동시호가 시간"""
    @classmethod
    def isin_PreMarket(self):
        t1, t2 = self.pre_open(), self.openingcallprc()
        return True if t1 <= now() < t2 else False
    """장전 동시호가 시간"""
    @classmethod
    def isin_OpenCallMarket(self):
        t1, t2 = self.openingcallprc(), self.open()
        return True if t1 <= now() < t2 else False
    """정규장 시간"""
    @classmethod
    def isin_NormalMarket(self):
        t1, t2 = self.open(), self.closingcallprc()
        return True if t1 <= now() < t2 else False
    """장 마감 동시호가 시간"""
    @classmethod
    def isin_CloseCallMarket(self):
        t1, t2 = self.closingcallprc(), self.close()
        return True if t1 <= now() < t2 else False
    """장후 동시호가 시간"""
    @classmethod
    def isin_PostMarket(self):
        t1, t2 = self.post_open(), self.after_open()
        return True if t1 <= now() < t2 else False
    """시간외 단일가 시간"""
    @classmethod
    def isin_AfterMarket(self):
        t1, t2 = self.after_open(), self.after_close()
        return True if t1 <= now() <= t2 else False
    """지금은 무슨 장 시간인가"""
    @classmethod
    def in_which_market(self):
        t = now()
        if t < self.pre_open(): return None
        elif self.pre_open() <= t < self.openingcallprc(): return 'PreMarket'
        elif self.openingcallprc() <= t < self.open(): return 'OpenCallMarket'
        elif self.open() <= t < self.closingcallprc(): return 'NormalMarket'
        elif self.closingcallprc() <= t <= self.close(): return 'CloseCallMarket'
        elif self.close() <= t <= self.after_open(): return 'PostMarket'
        elif self.after_open() <= t <= self.after_close(): return 'AfterMarket'
    @classmethod
    def isin_closeCallprc(self):
        t1, t2 = self.closingcallprc(), self.close()
        return True if t1 <= now() <= t2 else False


    @classmethod
    def is_mkt_open(self):
        funcnm = f"{__name__}.{inspect.stack()[0][3]}"
        t = now()
        if t.weekday() in [5,6]:
            print(f"{t} | {funcnm} | 주말({t.weekday()})에는 시장을 닫는다.")
            return False
        else:
            if (t >= mkt_buyable_opening()) and (t < open()):
                print(f"""{t} | {funcnm}
                    정규장 매수/매도 주문가능시간: 08:20 ~
                    장 시작 동시호가:           08:30 ~ 09:00
                    장전 시간외 종가 거래:       08:30 ~ 08:40 (전일 종가로 거래)
                """)
            elif (t >= open()) and (t < close()):
                print(f"""{t} | {funcnm}
                    한국거래소 정규시간. | 09:00 ~ 15:30
                """)
                return False
            elif (t.hour >= 9) and (t.hour < 16):
                print(f"""{t} | {funcnm}

                    KR_NOW : {t}
                """)
                if (t.hour >= 15) and (t.hour < 16):
                    if (t.minute >= 0) and (t.minute <= 30):
                        print(f"""{t} | {funcnm}
                            장 마감 동시호가.   | 15:20 ~ 15:30
                        """)
                    else:
                        print(f"""{t} | {funcnm}
                            장후 시간외 종가. | 15:40 ~ 16:00 (당일 종가로 거래)
                        """)
                return True
            elif (t.hour >= 16) and (t.hour < 18):
                print(f"""{t} | {funcnm}
                    시간외 단일가. | 16:00 ~ 18:00 (10분단위로 체결, 당일 종가대비 ±10% 가격으로 거래)
                """)
                return False
            else:
                print(f"""{t} | {funcnm}
                    한국거래소 장 종료.
                    KR_NOW : {t}
                    Market Open Time : 09시 ~ 16시
                """)
                return False
