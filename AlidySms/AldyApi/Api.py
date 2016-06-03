# -*- coding: utf-8 -*-
'''
Created on 2016年6月3日

@author: Su
'''
from config import APPKEY
from config import SECRET
import top.api
# class AldyApi():
def send_sms(sms_type,phone_num,temp_code,param, sign_name, extend=None, appkey=APPKEY, secret=SECRET):
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    # 设置应用的key和 secret
    req.set_app_info(top.appinfo(appkey, secret))
    req.extend = extend
    req.sms_type = sms_type
    req.sms_free_sign_name = sign_name
    req.sms_param = param
    req.rec_num = phone_num
    req.sms_template_code = temp_code
    try:
        resp = req.getResponse()
        return resp
    except Exception, e:
        return e
