# -*- coding:utf-8 -*-

"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter
s = '''
	A Counter is a dict subclass for counting hashable objects.
	It is an unordered collection where elements are stored as dictionary keys and 
	their counts are stored as dictionary values. Counts are allowed to be any integer value including 
	zero or negative counts. The Counter class is similar to bags or multisets in other languages.
	'''.lower() # 装换成全部小写
c = Counter(s)


# 获取出现频率最高的3个字符
print (c.most_common(3))	
