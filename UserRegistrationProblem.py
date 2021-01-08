# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 14:01:23
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 14:11:46

import re


class UserRegistration:

    # UC-1: Validate FirstName(First letter should br capital and name should have min 3 characters)
    def first_name_validation(self):
        """
        function return the first name is valid or not 
        """
        first_name = input("Enter first name: ")
        my_match = re.search("^[A-Z]{1}[a-z]{2,}$", first_name)
        if my_match:
            return first_name
        else:
            return "Invalid First Name! Please try again!"


if __name__ == '__main__':
    RegisterUser = UserRegistration()
    print(RegisterUser.first_name_validation())