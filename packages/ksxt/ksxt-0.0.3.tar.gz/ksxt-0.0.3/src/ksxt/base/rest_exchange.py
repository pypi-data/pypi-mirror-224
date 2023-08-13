import json
import os
from typing import Any, Dict, Optional

from ksxt.base.exchange import Exchange


class RestExchange(Exchange):
    required_credentials = {
        'open_key': True,
        'secret_key': True,
        'uid': False,
        'login': False,
        'password': False,
        'token': False
    }

    headers = None
    token = None
    type = 'rest'

    def __init__(self, config: Dict=None) -> None:
        super().__init__()

        self.headers = dict() if self.headers is None else self.headers

        if config is None:
            config = {}

        settings = self.deep_extend(self.describe(), config)
        Exchange.set_attr(self, settings)

        apis = self._get_api_from_file()
        Exchange.set_attr(self, apis)
        
        self.set_token()

    def _get_api_from_file(self):
        tr_config_filename = 'tr_dev.json' if self.is_dev else 'tr_app.json'

        current_path = os.path.dirname(__file__)
        config_path = os.path.join(current_path, '..\\config', tr_config_filename)

        with open(config_path, encoding='utf-8',) as f:
            c = json.load(f)
            return { 'apis': c[self.name] }

    def set_token(self):
        pass

    def prepare_request_headers(self, headers=None):
        headers = headers or {}

        if self.session:
            headers.update(self.session.headers)

        self.headers.update(headers)

        headers.update({"content-type":"application/json"})
        #headers.update({'appKey':self.open_key})
        #headers.update({'appsecret':self.secret_key})

        return headers


    def describe(self) -> Dict:
        return {}

    def fetch(self, url, method='GET', headers=None, body=None, params=None):
        request_headers = headers #self.prepare_request_headers(headers=headers)
        request_body = body
        request_params = params

        self.session.cookies.clear()

        http_response = None
        http_status_code = None
        http_status_text = None
        json_response = None

        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=request_headers,
                data=request_body,
                params=request_params,
                timeout=int(self.timeout / 1000)
            )

            response.encoding = 'utf-8'

            headers = response.headers
            http_status_code = response.status_code
            http_status_text = response.reason
            http_response = response.text.strip()
            json_response = self.parse_json(http_response)

        except TimeoutError as e:
            details = ' '.join([self.id, method, url])
            raise TimeoutError(details) from e
        
        if json_response:
            return json_response

    def sign(self, path, market, module, api: Any = 'public', method='GET', headers: Optional[Any] = None, body: Optional[Any] = None, params: Optional[Any] = None, config={}):
        pass

    def fetch2(self, path, market, module, api: Any = 'public', method='GET', params={}, headers: Optional[Any] = None, body: Optional[Any] = None, config={}):
        # Rate Limit 체크 후 throttle 처리

        is_activate = self.apis[self.type][market][module][path]['activate']
        if not is_activate:
            return f'지원하지 않는 함수({path}) 입니다.'

        request = self.sign(path, market, module, api, method, headers, body, params, config)
        return self.fetch(request['url'], request['method'], request['headers'], request['body'], request['params'])

    def request(self, path, market, module, api: Any='public', method='GET', params={}, headers: Optional[Any] = None, body: Optional[Any] = None, config={}):
        return self.fetch2(path, market, module, api, method, params, headers, body, config)