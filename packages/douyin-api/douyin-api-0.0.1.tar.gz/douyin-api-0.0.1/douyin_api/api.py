"""
抖音官方开放接口

抖音官方文档地址：https://developer.open-douyin.com/docs/resource/zh-CN/dop/overview/usage-guide

注：上传文件需要 requests-toolbelt
"""

import os
import json
import time
import hashlib
import random
from pathlib import Path
from pprint import pprint as pp

import requests

from requests import Response
from requests_toolbelt import MultipartEncoder
from urllib.parse import urlparse

from .utils import need_login, BaseClient
from .exception import LoginError

headers = {
    "Content-Type": "application/json",  # application/json;charset=UTF-8
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}


class DouYin(BaseClient):

    def __init__(self, client_key, client_secret, base_url='https://open.douyin.com', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_key = client_key  # 应用唯一标识
        self.client_secret = client_secret  # 应用唯一标识对应的密钥
        self.base_url = base_url
        self.set_headers(headers)
        self.data = {}

    def get_response_data(self, resp):
        """
        解析接口返回的数据
        """
        self.data = resp.json()
        if self.data.get('message', None) != 'success':
            raise ValueError(f'{self.data}')
        return self.data

    def get_client_token(self, ):
        """
        该接口用于获取接口调用的凭证 client_token。该接口适用于抖音授权。

        业务场景
        client_token 用于不需要用户授权就可以调用的接口。

        注意事项
        client_token 的有效时间为 2 个小时，重复获取 client_token 后会使上次的 client_token 失效（但有 5 分钟的缓冲时间，连续多次获取 client_token 只会保留最新的两个 client_token）。

        docs: https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/client-token
        """
        data = {
            "grant_type": "client_credential",
            "client_key": self.client_key,
            "client_secret": self.client_secret,
        }
        url = f"{self.base_url}/oauth/client_token/"
        r = self._session.post(url, json=data)
        return self.get_response_data(r)
