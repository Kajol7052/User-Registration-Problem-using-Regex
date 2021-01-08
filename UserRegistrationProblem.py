# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 14:01:23
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 16:38:54
# @Title: User Validation System needs to ensure that all validations are in place during the user entry.

import re


class UserRegistration:

    def regex_validation(self):
        """
        function to initialize all regex 
        """
        self.name_match = "^[A-Z]{1}[a-z]{2,}$"
        self.email_match = "^\w{3,}(\.\w{3,})*\@[a-z]{2,}\.[a-z]{2,3}(\.[a-z]{2})*$"
        self.phone_match = "^(\\+91|91)[ ]{1}[6-9]{1}[0-9]{9}$"
        self.password_match = "(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$"
        
    
    def input_validation(self, my_regex, name):
        """
        function to validate the user input
        """
        my_match = re.search(my_regex, name)
        if my_match:
            return name
        else:
            return "Invalid Input! Please try again!"

    # UC-1: Validate FirstName(First letter should br capital and name should have min 3 characters)
    def first_name_validation(self):
        """
        function return the first name is valid or not 
        """
        first_name = input("Enter first name: ")
        self.regex_validation()
        return RegisterUser.input_validation(self.name_match, first_name)
    

    # UC-2: Validate LastName(First letter should br capital and name should have min 3 characters)
    def last_name_validation(self):
        """
        function return the last name is valid or not 
        """
        last_name = input("Enter last name: ")
        self.regex_validation()
        return RegisterUser.input_validation(self.name_match, last_name)

    # UC-3: Validate Email Address     
    def email_validation(self):
        """
        function return the email is valid or not
        """
        email = input("Enter email: ")
        return RegisterUser.input_validation(self.email_match, email)


    # UC-4: Validate Mobile Number
    def mobile_validation(self):
        """
        function return the mobile number is valid or not
        """
        mobile = input("Enter mobile number: ")
        return RegisterUser.input_validation(self.phone_match, mobile)


    # UC-5: Validate User Password to have minimum 8 characters(Rule-1)
    # UC-6: Validate User Password to have atleast 1 uppercase character(Rule-2)
    # UC-7: Validate User Password to have atleast 1 numeric number(Rule-3)
    # UC-8: Validate User Password to have atleast 1 special character(Rule-4)
    def password_validation(self):
        """
        function return the password is valid or not
        """
        password = input("Enter password: ")
        return RegisterUser.input_validation(self.password_match, password)


if __name__ == '__main__':
    RegisterUser = UserRegistration()
    print(RegisterUser.first_name_validation())
    print(RegisterUser.last_name_validation())
    print(RegisterUser.email_validation())
    print(RegisterUser.mobile_validation())
    print(RegisterUser.password_validation())
    