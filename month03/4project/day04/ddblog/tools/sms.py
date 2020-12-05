import datetime
import hashlib
import base64
import json

import requests  # 使用它可以发送http请求


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):  # 账户id  令牌  应用id  模板
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    # 1. 构造Url
    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url

    # 时间戳
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    # 计算sig参数
    def get_sig(self, timestamp):
        s = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()  # upper()将字符转为大写

    # 2. 构造包头
    def get_request_header(self, timestamp):
        s = self.accountSid + ':' + timestamp
        b_s = base64.b64encode(s.encode()).decode()
        # s.encode(),将参数由字符串转换成字节串
        # b64encode做base64编码
        # 最后的decode将计算结果由字节串转换为字符串
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': b_s,
        }

    # 3. 构造请求体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        return data

    # 4. 发送请求
    def do_request(self, url, header, body):
        # 1.url:post请求发给哪个资源
        # 2.header:请求头
        # 3.body:请求体
        res = requests.post(url=url, headers=header, data=json.dumps(body))  # data请求体需要序列化，转成串
        return res.text

    # 5. 运行（将以上几部串起来）
    def run(self, phone, code):
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        print(url)
        header = self.get_request_header(timestamp)
        print(header)
        body = self.get_request_body(phone, code)
        print(body)
        res = self.do_request(url, header, body)
        return res

if __name__ == '__main__':
    aid = '8a216da875e463e00176275576ab16db'
    atoken = '48eae267accb48588b6b495242c52e3f'
    appid = '8a216da875e463e001762755779d16e1'
    tid = '1'

    x = YunTongXin(aid,atoken,appid,tid)
    res = x.run('18516159474','123456')  # 验证码
    print(res)