# encoding: utf-8 
import json

import requests
import logging
import requests
from requests.exceptions import RequestException


class TestApiGroup:
    def __init__(self, url='http://localhost:8080'):
        self.headers = {'Content-Type': 'application/json'}
        self.url = url + '/xdata/api_test/test'
        logging.basicConfig(
            level=logging.DEBUG,  # 设置日志级别为DEBUG
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    # 用来测试的api
    def testApi(self, id,name):
        params = {'id':id,'name':name}
        data = {"apiKey": "4fddfd63c67fa51ee7d5ff5e560b43d5", "currPage": 1, "pageSize": 10000}
        data["params"] = params
        self.httpSender(data)

    # ${apiName}
    def testApi2rd(self):
        data = {"apiKey": "5612de279f58b2a82502b35a6340596e", "currPage": 1, "pageSize": 10000}
        self.httpSender(data)

    

    def httpSender(self, data):
        logger = logging.getLogger('TestApiGroup')
        logger.debug('传入参数为: %s', data)
        try:
            res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        except RequestException as e:
            logger.error("远程使用http请求数据服务异常：", e)
            return
        logger.debug('接口请求结果为: %s', res.text)
        res_body = json.loads(res.text)
        code_ = res_body['code']
        if 200 == code_ and res_body['data']['success']:
            logger.debug('远程调用数据服务成功')
            data_ = res_body['data']['data']
            logger.debug('接口获取数据为: %s', data_)
        else:
            logger.error('远程调用数据服务失败, 原因:{}', res_body['message'])

