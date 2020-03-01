# 欢迎使用 fateadm斐斐打码Python工具包

**这里不是官方Python SDK，仅是个人平时使用的分享给大家，使用Python3编写**
**斐斐打码官网[www.fateadm.com](http://www.fateadm.com)**

# 快速使用

先安装fateadm所需依赖


    import requests
    import hashlib
    import time
    import json
将fateadm.py放入工程下
 

    import requests
    import fateadm
    import base64
    
    fa = fateadm.fateadm('您的pd_id', '您的pd_key', '您的app_id', '您的app_key')
    fateadm_res = fa.fateadm(base64.b64encode(r2.content), '30400')
具体使用方法也可参考fateadm-demo.py

# 几点说明
pd_id、pd_key注册登录后在"个人中心"查看

app_id、app_key登陆后在"开发者"查看

fateadm函数中第二个参数需要填写验证码类型，请参考[官方文档](http://docs.fateadm.com/web/#/1?page_id=36)

# 关于斐斐打码
> 斐斐打码平台是一家专业的打码网站，使用前沿的人工智能识别技术，智能识别各种码类型，用机器算法代理低效的人力代打模式，在效率、性能、价格上都有比较大的突破

> 斐斐平台建立的宗旨，是要优化各大网站一些非必要的识别码，简化用户上网的流程，以及协助识别障碍人士方便上网，同时改变市面上的人工代打码模式，真正实现解放人力、方便使用的目的
