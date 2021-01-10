# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-09 23:08:19
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-09 23:40:46
import unittest
from UserRegistrationProblem import UserRegistration

class SquareRootTest(unittest.TestCase):

    def setUp(self):
            self.userRegOb= UserRegistration()
            self.invalidEmailList = ["abc", "abc@.com.my", "abc123@gmail.a", "abc123@.com",
                            "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com",
                            "abc@%*.com", "abc..2002@gmail.com", "abc@1.com", "abc.@gmail.com",
                            "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]
            self.validEmailList = ["abc@yahoo.com", "abc-100@yahoo.com",
                          "abc.100@yahoo.com", "abc111@abc.com",
                          "abc-100@abc.net", "abc.100@abc.com.au",
                          "abc@gmail.com.com", "abc+100@gmail.com"]
            self.validPhoneList = ["+91 8317030424","91 8317030424", "91 7899856021"]
            self.invalidPhoneList = ["+91 768934567","91 5678901234","92 5465434"]

    def test_positive_email(self):
        self.userRegOb.regex_validation()
        for valid_email in self.validEmailList :
            self.assertEqual(valid_email, self.userRegOb.input_validation(self.userRegOb.email_match,valid_email))

    def test_negative_sqrt(self):
        self.userRegOb.regex_validation()
        for invalid_email in self.invalidEmailList :
            self.assertNotEqual(invalid_email, self.userRegOb.input_validation(self.userRegOb.email_match,invalid_email))

    def test_positive_phone(self):
        self.userRegOb.regex_validation()
        for valid_phone in self.validPhoneList :
            self.assertEqual(valid_phone, self.userRegOb.input_validation(self.userRegOb.phone_match,valid_phone))
  
    def test_negetive_phone(self):
        self.userRegOb.regex_validation()
        for invalid_phone in self.invalidPhoneList :
            self.assertNotEqual(invalid_phone, self.userRegOb.input_validation(self.userRegOb.phone_match,invalid_phone))
            

if __name__ == '__main__':
    unittest.main()