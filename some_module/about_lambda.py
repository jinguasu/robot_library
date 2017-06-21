# -*- coding: utf-8 -*-

#lambda argument1,argument2....argumentN  :  expression  using arguments

"""
lambda 的规则
1. 一般也就一行，必须有返回值
2. 没有return
3. 可以没有参数，也可以有一个或多个参数


"""

print filter(lambda x:x>3,[2,4,6])

print (lambda x:x.startswith('a'))('asd')

print map(lambda x:x*2,[1,2,3,4])#  将函数作用于后面的每一个元素
print reduce(lambda x,y:x*y,[1,2,3,4])# 必须接受2个参数，并且跟后面的元素做累积计算



namelist = ['adam', 'LISA', 'barT']

def change(name):
    return name[0].upper()+name[1:].lower()

print map(change,namelist)

def prod(l):
    return reduce(lambda x,y:x*y,l)

print prod([1,2,3,4,5])

