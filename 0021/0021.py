# -*- coding:utf-8 -*-
''''关于加密解密
利用hashlib.sha256对密码进行16位转换 添加一个随机盐值(salt) 当然如果需要更精密，还可以加多个盐值
或者是加密算法组合的情况。中间用一些特殊符号分割开来，同样的方法对这些值进行解密后验证就可以
'''


import uuid
import hashlib

def hash_password(password):
	# uuid is used to generate a random number
	salt = uuid.uuid4().hex
	print salt
	return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
	password, salt = hashed_password.split(':')
	return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = raw_input('Please enter a password:')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = raw_input('Now Please enter the password again to check: ')
if check_password(hashed_password, old_pass):
	print('You entered the right password')
else:
	print('I am sorry but the password does not match')
