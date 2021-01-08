# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 14:01:23
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 15:11:09

import re


class UserRegistration:

    def regex_validation(self):
        """
        function to initialize all regex 
        """
        self.name_match = "^[A-Z]{1}[a-z]{2,}$"

    
    def name_validation(self, my_regex, name):
        """
        function to validate the user name
        """
        my_match = re.search(my_regex, name)
        if my_match:
            return name
        else:
            return "Invalid Name! Please try again!"

    # UC-1: Validate FirstName(First letter should br capital and name should have min 3 characters)
    def first_name_validation(self):
        """
        function return the first name is valid or not 
        """
        first_name = input("Enter first name: ")
        self.regex_validation()
        return RegisterUser.name_validation(self.name_match, first_name)
    

    # UC-2: Validate LastName(First letter should br capital and name should have min 3 characters)
    def last_name_validation(self):
        """
        function return the last name is valid or not 
        """
        last_name = input("Enter last name: ")
        self.regex_validation()
        return RegisterUser.name_validation(self.name_match, last_name)
        


if __name__ == '__main__':
    RegisterUser = UserRegistration()
    print(RegisterUser.first_name_validation())
    print(RegisterUser.last_name_validation())
    