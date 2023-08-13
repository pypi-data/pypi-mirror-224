import json
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from ksxt.base.rest_exchange import RestExchange
from ksxt.base.types import Entry


class ImplicitAPI:
    fetchTicker = Entry('fetch_ticker_price', 'stock', 'feeder', 'public', 'GET', {})
    fetchOHLCV = Entry('fetch_ohlcv_stock', 'stock', 'feeder', 'public', 'GET', {})
    fetchIsHoliday = Entry('fetch_calendar_holiday', 'stock', 'feeder', 'public', 'GET', {})

    fetchBalance = Entry('fetch_balance', 'stock', 'feeder', 'private', 'GET', {})
    fetchCash = Entry('fetch_cash', 'stock', 'feeder', 'private', 'GET', {})
    fetchScreenerList = Entry('fetch_screener_list', 'stock', 'feeder', 'private', 'GET', {})
    fetchScreener = Entry('fetch_screener', 'stock', 'feeder', 'private', 'GET', {})

    sendOrderEntry = Entry('send_order_entry', 'stock', 'broker', 'private', 'POST', {})
    sendOrderExit = Entry('send_order_entry', 'stock', 'broker', 'private', 'POST', {})
    sendModifyOrder = Entry('send_modify_order', 'stock', 'broker', 'private', 'POST', {})
    sendCancelOrder = Entry('send_cancel_order', 'stock', 'broker', 'private', 'POST', {})

    fetchOpenedOrder = Entry('fetch_opened_order', 'stock', 'broker', 'private', 'GET', {})
    fetchClosedOrder = Entry('fetch_closed_order_short', 'stock', 'broker', 'private', 'GET', {})

class KoreaInvest(RestExchange, ImplicitAPI):
    def __init__(self, config: Dict=None) -> None:
        super().__init__(config=config)

    def describe(self) -> Dict:
        result = self.deep_extend(super(KoreaInvest, self).describe(), {
            'id': 'KIS',
            'name': 'KoreaInvestment',
            'countries': ['KR'],
            'version': 'v1',
            'rateLimit': 1000,
            'urls': {
                'logo': '',
                'api': {
                    'token': 'https://{hostname}/oauth2/tokenP',
                    'public': 'https://{hostname}',
                    'private': 'https://{hostname}',
                },
                'www': 'https://securities.koreainvestment.com',
                'doc': 'https://apiportal.koreainvestment.com/apiservice/oauth2#L_5c87ba63-740a-4166-93ac-803510bb9c02',
                'fees': '',
            },
        })

        return result
    
    # region _____
    def set_token(self):
        url = self.implode_hostname(self.urls['api']['token'], self.apis['rest']['hostname'])
        request_headers = self.prepare_request_headers()

        body = {
            "grant_type":"client_credentials",
            "appkey":self.open_key, 
            "appsecret":self.secret_key
        }

        body = json.dumps(body, separators=(',', ':'))

        res = self.fetch(url=url, method='POST', headers=request_headers, body=body)
        self.token = res['access_token']

    def sign(self, path, market, module, api: Any = 'public', method='GET', headers: Optional[Any] = None, body: Optional[Any] = None, params: Optional[Dict] = {}, config={}):
        host_url = self.implode_hostname(self.urls['api'][api], self.apis[self.type]['hostname'])
        folder = self.apis[self.type][market]['foldername']
        destination = self.apis[self.type][market][module][path]['url']
        url = host_url + '/' + folder + '/' + self.version + '/' + destination

        tr_id = self.apis['rest'][market][module][path]['tr']
        if headers is None:
            headers = {}
            headers.update(
                {
                    "content-type":"application/json",
                    "authorization": f"Bearer {self.token}",
                    "appKey": self.open_key,
                    "appSecret": self.secret_key,
                    "tr_id": tr_id
                }
            )

        if method.upper() == 'POST':
            body = json.dumps(params)
            params = {}

        return {'url': url, 'method': method, 'headers': headers, 'body': body, 'params': params}
    # endregion ____

    # region public feeder    
    def fetch_ticker(self, symbol: str, base_market: str= 'KRW'):
        params = {
            "FID_COND_MRKT_DIV_CODE":"J",
            "FID_INPUT_ISCD": symbol
        }

        response = self.fetchTicker(self.extend(params))
        return self.parse_ticker(response=response)
    
    def parse_ticker(self, response: dict):
        data = self.safe_value(response, 'output')
        if data is None:
            return response

        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,

            # 종목 코드
            'symbol': self.safe_value(data, 'stck_shrn_iscd'),
            # 현재가
            'price': self.safe_value(data, 'stck_prpr'),
        }
    
    def fetch_historical_data(self, symbol: str, time_frame: str, start: Optional[str] = None, end: Optional[str] = None, base_market: str= 'KRW'):
        limit = 100

        if end is None:
            end = self.now.strftime('%Y%m%d')

        if start is None:
            if time_frame == 'D':
                start = self.now - timedelta(days=limit)
            elif time_frame == 'W':
                start = self.now - timedelta(weeks=limit)
            elif time_frame == 'Y':
                start = self.now - timedelta(days=limit * 365)

            start = start.strftime('%Y%m%d')

        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": symbol,
            "FID_INPUT_DATE_1": start,
            "FID_INPUT_DATE_2": end,
            "FID_PERIOD_DIV_CODE": time_frame,
            "FID_ORG_ADJ_PRC":"1",
        }

        response = self.fetchOHLCV(self.extend(params))
        return self.parse_historical_data(response=response)
    
    def parse_historical_data(self, response: dict):
        data = self.safe_value(response, 'output1')
        data_ohlcv = self.safe_value(response, 'output2')
        if data is None or data_ohlcv is None:
            return response
        
        ohlcv = [self.parse_ohlcva(_) for _ in data_ohlcv]
        sorted_ohlcv = self.sort_by(ohlcv, 0)

        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,

            # 종목코드
            'symbol': self.safe_value(data, 'stck_shrn_iscd'),
            'history' : sorted_ohlcv
        }
    
    def parse_ohlcv(self, ohlcv):
        # convert datetime to timestamp
        ts = self.safe_string(ohlcv, 'stck_bsop_date')
         
        return [
            # timestamp
            ts,
            # open
            self.safe_number(ohlcv, 'stck_oprc'),
            # high
            self.safe_number(ohlcv, 'stck_hgpr'),
            # low
            self.safe_number(ohlcv, 'stck_lwpr'),
            # close
            self.safe_number(ohlcv, 'stck_clpr'),
            # volume
            self.safe_number(ohlcv, 'acml_vol'),
        ]
    
    def parse_ohlcva(self, ohlcva):
        # convert datetime to timestamp
        ts = self.safe_string(ohlcva, 'stck_bsop_date')

        return [
            # timestamp
            ts,
            # open
            self.safe_number(ohlcva, 'stck_oprc'),
            # high
            self.safe_number(ohlcva, 'stck_hgpr'),
            # low
            self.safe_number(ohlcva, 'stck_lwpr'),
            # close
            self.safe_number(ohlcva, 'stck_clpr'),
            # volume
            self.safe_number(ohlcva, 'acml_vol'),
            # amount
            self.safe_number(ohlcva, 'acml_tr_pbmn')
        ]
    
    def fetch_is_holiday(self, dt: datetime, base_market: str= 'KRW'):
        params = {
            "BASS_DT": dt.strftime('%Y%m%d'),
            "CTX_AREA_NK": '',
            "CTX_AREA_FK": ''
        }

        response = self.fetchIsHoliday(self.extend(params))
        result = self.parse_is_holiday(response=response)

        return self.safe_boolean(result['holiday'], dt.strftime('%Y%m%d'))
    
    def parse_is_holiday(self, response: dict):
        data = self.safe_value(response, 'output')
        if data is None:
            return response
        
        info = {}
        for _ in data:
            info.update(self._parse_is_holiday(_))
        
        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,

            # 휴장일 정보
            'holiday': info
        }
    
    def _parse_is_holiday(self, info):
        return {
            # 날짜 (YYYYMMDD) : 개장일 여부 (Y/N)
            self.safe_string(info, 'bass_dt') : (not self.safe_boolean(info, 'opnd_yn')),
        }

    
    # endregion public feeder

    # region private feeder
    def fetch_balance(self, acc_num: str, base_market: str= 'KRW'):
        params = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "AFHR_FLPR_YN": 'N',
            "OFL_YN": '',
            "INQR_DVSN": '01',
            "UNPR_DVSN": '01',
            "FUND_STTL_ICLD_YN": "N",
            "FNCG_AMT_AUTO_RDPT_YN": 'N',
            "PRCS_DVSN": '01',
            "CTX_AREA_FK100": '',
            "CTX_AREA_NK100": ''
        }

        response = self.fetchBalance(self.extend(params))
        return self.parse_balance(response=response)
    
    def parse_balance(self, response: dict):
        data = self.safe_value(response, 'output1')
        if data is None:
            return response
        
        info = [self._parse_balance(_) for _ in data]
        sorted_info = self.sort_by(info, 'symbol')
        
        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,

            # 잔고 정보
            'balance': sorted_info
        }

    def _parse_balance(self, balance):
        total = self.safe_number(balance, 'hldg_qty')
        free = self.safe_number(balance, 'ord_psbl_qty')

        return {
                'symbol': self.safe_string(balance, 'pdno'),
                'name': self.safe_string(balance, 'prdt_name'),
                'position': self.safe_string(balance, 'trad_dvsn_name'),
                'price': self.safe_number(balance, 'pchs_avg_pric'),
                'qty':{
                    'total': total,
                    'free': free,
                    'used': total - free,
                },
                'amount': self.safe_number(balance, 'pchs_amt'),
        }
    
    def fetch_cash(self, acc_num: str, base_market: str= 'KRW'):
        params = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "AFHR_FLPR_YN": 'N',
            "OFL_YN": '',
            "INQR_DVSN": '01',
            "UNPR_DVSN": '01',
            "FUND_STTL_ICLD_YN": "N",
            "FNCG_AMT_AUTO_RDPT_YN": 'N',
            "PRCS_DVSN": '01',
            "CTX_AREA_FK100": '',
            "CTX_AREA_NK100": ''
        }

        response = self.fetchCash(self.extend(params))
        return self.parse_cash(response=response)
    
    def parse_cash(self, response:dict):
        data = self.safe_value(response, 'output2')
        if data is None:
            return response
        
        data = data[0]
        
        return {
            'response': {
                # 성공 실패 여부
                'success' : 0,
                # 응답코드
                'code': '',
                # 응답메세지
                'message': '',
            },
            # 원본 데이터
            'info': response,

            # 정산금액 (KR: D+2 예수금)
            'cash': self.safe_number(data, 'prvs_rcdl_excc_amt')
        }
    
    def fetch_screener_list(self, user_id, base_market: str= 'KRW'):
        params = {
            "USER_ID": user_id
        }

        response = self.fetchScreenerList(self.extend(params))
        return response
    
    def fetch_screener(self, user_id: str, screen_id: str, base_market: str= 'KRW'):
        params = {
            "USER_ID": user_id,
            "SEQ" : screen_id
        }

        response = self.fetchScreener(self.extend(params))
        return response
    # endregion private feeder

    # region broker
    def create_order(self, acc_num: str, symbol: str, ticket_type: str, price: float, qty: float, otype: str, base_market: str= 'KRW'):
        if otype.upper() == 'limit'.upper():
            order_dvsn = '00'
        elif otype.upper() == 'market'.upper():
            order_dvsn = '01'

        body = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "PDNO": symbol,
            "ORD_DVSN": order_dvsn,
            "ORD_QTY": str(qty),    # string type 으로 설정
            "ORD_UNPR": str(price), # string type 으로 설정
        }

        if ticket_type == 'entry_long':
            response = self.sendOrderEntry(self.extend(body))
        elif ticket_type == 'exit_long':
            response = self.sendOrderExit(self.extend(body))
        else:
            return
        
        return self.parse_order_response(response=response)
    
    def cancel_order(self, acc_num: str, order_id: str, qty: float = 0, *args, base_market: str= 'KRW'):
        body = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "KRX_FWDG_ORD_ORGNO": "",
            "ORGN_ODNO":str(order_id),
            "RVSE_CNCL_DVSN_CD":"02",
            "ORD_DVSN":"00",
            "ORD_QTY":str(qty),
            "ORD_UNPR":str(0),
            "QTY_ALL_ORD_YN": "N",
        }

        # 수량 미입력시 전량 취소
        if qty == 0:
            body['QTY_ALL_ORD_YN'] = 'Y'

        response = self.sendCancelOrder(self.extend(body))
        return self.parse_order_response(response=response)
    
    def modify_order(self, acc_num: str, order_id: str, price: float, qty: float, *args, base_market: str= 'KRW'):
        body = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "KRX_FWDG_ORD_ORGNO": "",
            "ORGN_ODNO":str(order_id),
            "RVSE_CNCL_DVSN_CD":"01",
            "ORD_DVSN":"00",
            "ORD_QTY":str(qty),
            "ORD_UNPR":str(price),
            "QTY_ALL_ORD_YN": "N",
        }

        # 수량 미입력시 전량 수정
        if qty == 0:
            body['QTY_ALL_ORD_YN'] = 'Y'

        response = self.sendModifyOrder(self.extend(body))
        return self.parse_order_response(response=response)
    
    def parse_order_response(self, response: dict):
        data = response['output']
        time = self.safe_string(data, 'ORD_TMD')
        today = datetime.today()
        dt = datetime.combine(today, datetime.strptime(time, '%H%M%S').time())

        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,

            # 주문 날짜 (YYYY-mm-DD HH:MM:SS)
            'datetime': datetime.strftime(dt, '%Y-%m-%d %H:%M:%S'),
            # 주문번호
            'order_id': self.safe_string(data, 'ODNO')
        }
    
    def fetch_open_order(self, acc_num: str, symbol: str = '', start: str = '', end: str = '', base_market: str= 'KRW'):
        if start == '':
            start = self.now.strftime('%Y%m%d')

        if end == '':
            end = self.now.strftime('%Y%m%d')
        
        params = {
            'CANO': acc_num,
            'ACNT_PRDT_CD': acc_num[-2:],
            'INQR_STRT_DT': start,
            'INQR_END_DT' : end,
            'SLL_BUY_DVSN_CD' : '00',
            'INQR_DVSN': '00',
            'PDNO': symbol,
            'CCLD_DVSN': '02',
            'ORD_GNO_BRNO': '',
            'ODNO': '',
            'INQR_DVSN_3': '00',
            'INQR_DVSN_1': '',
            'CTX_AREA_FK100': '',
            'CTX_AREA_NK100': ''
        }
        
        response = self.fetchOpenedOrder(self.extend(params))
        return self.parse_open_order(response=response)
    
    def parse_open_order(self, response: dict):
        data = self.safe_value(response, 'output1')
        if data is None:
            return response
        
        orders = [self.parse_open_order_history(_) for _ in data]
        sorted_orders = self.sort_by(orders, 'datetime')

        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,
            # 주문 정보
            'orders': sorted_orders
        }
    
    def parse_open_order_history(self, order):
        date = self.safe_string(order, 'ord_dt')
        time = self.safe_string(order, 'ord_tmd')
        dt = datetime.combine(datetime.strptime(date, '%Y%m%d'), datetime.strptime(time, '%H%M%S').time())

        position = self.safe_string(order, 'sll_buy_dvsn_cd')
        if position == '01':
            position = 'exit_long'
        elif position == '02':
            position = 'entry_long'
        else:
            position = None

        return {
            # 주문 날짜 (YYYY-mm-DD HH:MM:SS)
            'datetime': datetime.strftime(dt, '%Y-%m-%d %H:%M:%S'),
            # 주문번호
            'order_id': self.safe_string(order, 'odno'),
            # 원주문번호
            'org_order_id': self.safe_string(order, 'orgn_odno'),
            # 주문구분
            'order_type': self.safe_string(order, 'ord_dvsn_cd'),
            # long or short
            'position': position,
            # 종목코드
            'symbol': self.safe_string(order, 'pdno'),
            # 주문단가
            'price': self.safe_number(order, 'ord_unpr'),
            'qty': {
                # 주문수량
                'total': self.safe_number(order, 'ord_qty'),
                # 체결수량
                'used': self.safe_number(order, 'tot_ccld_qty'),
                # 잔여수량
                'free': self.safe_number(order, 'rmn_qty')
            }
        }
    
    def fetch_closed_order(self, acc_num: str, symbol: str = '', start: str = '', end: str = '', base_market: str= 'KRW'):
        if start == '':
            start = self.now.strftime('%Y%m%d')

        if end == '':
            end = self.now.strftime('%Y%m%d')

        params = {
            'CANO': acc_num,
            'ACNT_PRDT_CD': acc_num[-2:],
            'INQR_STRT_DT': start,
            'INQR_END_DT' : end,
            'SLL_BUY_DVSN_CD' : '00',
            'INQR_DVSN': '00',
            'PDNO': symbol,
            'CCLD_DVSN': '01',
            'ORD_GNO_BRNO': '',
            'ODNO': '',
            'INQR_DVSN_3': '00',
            'INQR_DVSN_1': '',
            'CTX_AREA_FK100': '',
            'CTX_AREA_NK100': ''
        }
        
        response = self.fetchClosedOrder(self.extend(params))
        return self.parse_closed_order(response=response)
    
    def parse_closed_order(self, response: dict):
        data = self.safe_value(response, 'output1')
        if data is None:
            return response
        
        orders = [self.parse_closed_order_history(_) for _ in data]
        sorted_orders = self.sort_by(orders, 'datetime')

        return {
            'response': {
                # 성공 실패 여부
                'success' : self.safe_string(response, 'rt_cd'),
                # 응답코드
                'code': self.safe_string(response, 'msg_cd'),
                # 응답메세지
                'message': self.safe_string(response, 'msg1'),
            },
            # 원본 데이터
            'info': response,
            # 주문 정보
            'orders': sorted_orders
        }
    
    def parse_closed_order_history(self, order):
        date = self.safe_string(order, 'ord_dt')
        time = self.safe_string(order, 'ord_tmd')
        dt = datetime.combine(datetime.strptime(date, '%Y%m%d'), datetime.strptime(time, '%H%M%S').time())

        position = self.safe_string(order, 'sll_buy_dvsn_cd')
        if position == '01':
            position = 'exit_long'
        elif position == '02':
            position = 'entry_long'
        else:
            position = None

        return {
            # 주문 날짜 (YYYY-mm-DD HH:MM:SS)
            'datetime': datetime.strftime(dt, '%Y-%m-%d %H:%M:%S'),
            # 주문번호
            'order_id': self.safe_string(order, 'odno'),
            # 원주문번호
            'org_order_id': self.safe_string(order, 'orgn_odno'),
            # 주문구분
            'order_type': self.safe_string(order, 'ord_dvsn_cd'),
            # long or short
            'position': position,
            # 종목코드
            'symbol': self.safe_string(order, 'pdno'),
            # 주문단가
            'price': self.safe_number(order, 'ord_unpr'),
            # 체결수량
            'qty': self.safe_number(order, 'tot_ccld_qty')
        }
    
    # endregion broker