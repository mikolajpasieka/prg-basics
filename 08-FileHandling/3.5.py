###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('enter username:   ')
password = input('enter password:   ')

# pattern (criteria) for username and password
username_pattern = "[a-z]{6,}"
password_pattern = "[a-zA-Z0-9_]{8,}"

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,username)

# print results
if username_match == username and password_match == password:
   print('you are logged in')
else:
   print('invalid username or password') 