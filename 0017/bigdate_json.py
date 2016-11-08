# -*- coding:utf-8 -*-

import json
# dump example
data = [{'lang':('python','java'),'school':"beijing"},"God"]
f = open('test.json', 'w+')
json.dump(data, f)
f.flush()
f.close()

# load example
fb = file('test.json')
js = json.load(fb)
print js

