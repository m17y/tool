# -*- coding: utf-8 -*-
'''
Created on 2016年6月3日

@author: Su
'''
import unittest

from AldyApi import Api
class TestAlidy(unittest.TestCase):
    def test_reg_msg(self):
        sms_type = ""
        phone_num =""
        temp_code = ""
        param =""
        sign_name =""
        Api.send_sms(sms_type, phone_num, temp_code, param, sign_name)
if __name__ == "__main__":
    unittest.main()