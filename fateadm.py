import requests
import hashlib
import time
import json


class fateadm:
    def __init__(self, pd_id, pd_key, app_id, app_key):
        self.pd_id = pd_id
        self.pd_key = pd_key
        self.app_id = app_id
        self.app_key = app_key

    # 计算md5签名
    @staticmethod
    def md5(str):
        m = hashlib.md5()  # 创建一个md5对象
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    # 调用接口识别验证码
    def fateadm(self, img_data, predict_type):
        url = 'http://pred.fateadm.com/api/capreg'
        timestamp = int(time.time())
        data = {'user_id': self.pd_id, 'timestamp': timestamp, 'app_id': self.app_id, 'predict_type': predict_type}
        timestamp = str(timestamp)
        data['sign'] = self.md5(self.pd_id + timestamp + self.md5(timestamp + self.pd_key))
        data['asign'] = self.md5(self.app_id + timestamp + self.md5(timestamp + self.app_key))
        data['img_data'] = img_data
        r = requests.post(url, data, timeout=30)
        try:
            res = r.json()
            if res['RetCode'] == '0':
                res['RspData'] = json.loads(res['RspData'])
                if res['RspData']:
                    return res
                else:
                    print('请求fateadm接口失败', r.text)
                    return False
            else:
                print('请求fateadm接口失败，报错信息', res['ErrMsg'])
                return False
        except:
            print('请求fateadm接口解析失败', r.content)
            return False

    # 识别结果错误 退款
    def fateadm_tui(self, order_id):
        print('订单', order_id, '尝试退款')
        url = 'http://pred.fateadm.com/api/capjust'
        times = int(time.time())
        timestamp = str(times)
        sign = self.md5(self.pd_id + timestamp + self.md5(timestamp + self.pd_key))
        data = {'user_id': self.pd_id, 'timestamp': times, 'request_id': order_id, 'sign': sign}
        print(data)
        r = requests.post(url, data, timeout=30)
        # print(r.text)
        try:
            res = r.json()
            if res['RetCode'] == '0':
                print('退款成功')
            else:
                print('退款失败', res['ErrMsg'])
        except:
            print('退款解析返回结果失败', r.content)