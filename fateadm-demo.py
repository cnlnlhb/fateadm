import requests
import fateadm
import base64

con = requests.Session()
url_p = '这里配置验证码地址'
r2 = con.get(url_p)
fa = fateadm.fateadm('您的pd_id', '您的pd_key', '您的app_id', '您的app_key')
fateadm_res = fa.fateadm(base64.b64encode(r2.content), '30400')
print(fateadm_res)
