# -*- coding: utf-8 -*-

dic = {'a':123,'b':456,'c':789}

dic['a'] = 890

print dic['b']

del dic['b']

dic.pop('a')

print dic

for key in dic.keys():
    print key

for value in dic.values():
    print value

for key,value in dic.iteritems():
    print key,value

print 't' in dic
print dic.get('a')
print dic.get('e')
#print hash(dic)
#print hash('asdasd')  #在一个生存周期内，不可变，即为可哈希，哈希就是一个映射，散列出来。
key1 = (1,2,3)

dic[key1] = 4567890

key = [1,2,3]

#dic[key] = 3457

print dic