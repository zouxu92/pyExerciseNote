# -*- coding:utf-8 -*-
'''json的字符相关练习'''
import json

js = json.loads('{"insun": "泰囧 / 人在囧途2 / Lost in Thailand "}')
print json.dumps(js)
print json.dumps(js, ensure_ascii=False)

'''
print ('=========begin==========序列化')
data = ['foo', {'bar': ('baz', None, 1.0, 2)}]
print data
print type(data)
json_data = json.dumps(data)
print json_data
print type (json_data)
print ('==========end==============')

print (u'Compact encoding-->压缩编码\n')

data1 = [1,2,3,{'4': 5, '6':7}]
print data1
print type(data1)
data_json = json.dumps(data1)
print data_json
print type(data_json)
print (u"<<<<<===============next==============>>>>>>\n")
data_json2 = json.dumps(data1, sort_keys=True)
print ("data_json2: %s\n" % data_json2)
print type(data_json2)


print (u'=================44444444444===============')
data_json3 = json.dumps(data1, indent=4, sort_keys=True, separators=(',', ':'))
print ('data_json3:\n %s' % data_json3)
print type(data_json3)
'''

print(u"===================>>>>>反序列化>>>>>>>")
obj = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
print type(obj)
str_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
print type(str_json)
obj2 = json.loads(str_json)

print obj2
print (obj2 == obj)


