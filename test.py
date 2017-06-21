# -*- coding: utf-8 -*-

#  利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

a = '2234.3434'

length = len(a.split('.')[0])

new_list = []

new_list.append(int(a.split('.')[0].split()[:]))
new_list.append(int(a.split('.')[1][:]))
print new_list
#for i in list(a):
 #   if i != '.':
  #      new_list.append(int(i))
s = reduce(lambda x,y:x*10+y,new_list)*(0.1**(len(new_list)-length))

print s
