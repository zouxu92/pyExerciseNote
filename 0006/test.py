# -*- coding:utf-8 -*-
from collections import Counter

'''
c = collections.Counter('abcdaab')

for letter in 'abcde':
	print '%s : %d' % (letter, c[letter])
'''

c = 'a Counter is a dict subclass for counting hashable objects.'
cnt = Counter()
for word in c.split():
	cnt[word] += 1

print cnt
print "=============="
print cnt.most_common(3)



'''

list_count = ['a', 'is' , 'for']
for cc in list_count:
	cc[word] 
	print ('%s: %d' %(list_count, cc[list_count]))
'''


words = c.lower()

# print ( Counter(words).most_common(10) )