import json
import base64
import time
import hmac
import copy  # 导入此包的意思是不想修改实参


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):  # payload消息主体部分,key秘钥,exp设置3秒过期
        # 生成token
        # 1 header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)  # json.dumps是把header 转换成json串
        # separators是一个元组,确保两个键值之间去空格。第一个指元素之间用什么做分割,第二个为键值之间用什么做分割
        # sort_keys确保映射的数据有序,确保生成的字符串是有序的,不会每次出来的编码不一致
        print(header_json)
        #header_bs = base64.urlsafe_b64encode(header_json.encode())  # json为字符串,需要encode转换为字节串
        header_bs = Jwt.b64encode(header_json.encode())
        print(header_bs)  # b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
        # 2 payload 载荷
        payload_data = copy.deepcopy(payload)  # 将参数传过来的payload进行深拷贝一份 为了对内部某一个数据所有修改不影响到传进来的实参
        payload_data['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_data, separators=(',', ':'), sort_keys=True)  # 把payload 转换成json串
        # payload_bs = base64.urlsafe_b64encode(payload_json.encode())
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)  # b'eyJleHAiOjE2MDY3OTA4MzguMzU1MjMxLCJ1c2VybmFtZSI6InRlZHUifQ=='
        # 3 签名 生成消息验证码
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        # hm_bs = base64.urlsafe_b64encode(hm.digest())
        hm_bs = Jwt.b64encode(hm.digest())
        print(hm_bs)  # b'9NE8JfLDowwCQ2MJR17KCcCueMaw2fHWHfaQxIQXCyc='
        return header_bs + b'.' + payload_bs + b'.' + hm_bs
    # 去等号操作
    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=',b'')
    # 补加号
    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'='*(4-rem)
        return base64.urlsafe_b64decode(b_s) # 补=之后再解码

    # 验证
    @staticmethod
    def decode(token,key):  # token消息加认证码 ,key共享秘钥
        header_bs,payload_bs,sign = token.split(b'.')
        hm = hmac.new(key.encode(),header_bs+b'.'+payload_bs,digestmod='SHA256')
        if sign != Jwt.b64encode(hm.digest()):  # 此hm.digest()为接收后的
            raise
        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)  # loads为dumps反义
        exp = payload['exp']
        now = time.time()
        if now >exp:
            raise
        return payload


if __name__ == '__main__':
    token = Jwt.encode({'username': 'tedu'}, '123456', 100)
    print(token)
    print(Jwt.decode(token, '123456'))