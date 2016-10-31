# -*- coding: utf-8 -*-
"""
deque其实是 double-ended queue 的缩写，翻译过来就是双端队列，它最大的好处
就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft() 。
#
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

fancy_loading = deque('>-----------------------')

while True:
	print '%s'  % ''.join(fancy_loading), fancy_loading.rotate(2) 
	sys.stdout.flush() # 这个加不加在windows上都一样的效果，而在linux系统下必须加上
	time.sleep(0.18)