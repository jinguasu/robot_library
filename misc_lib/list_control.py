# -*- coding: utf-8 -*-

def list_intersection(list_a,liat_b):
    return list(set(list_a).intersection(set(liat_b)))

def list_union(list_a,list_b):
    return list(set(list_a).union(set(list_b)))

def list_different(list_a,list_b):
    #get the value in a but not in b
    return list(set(list_a).difference(set(list_b)))

def list_diff_in_two_list(list_a,list_b):

    return list_union(list(a for a in list_a if a not in list_b),list(b for b in list_b if b not in list_a))

a = [1,2,3]
b = [2,3,4]
print list_intersection(a,b)
print list_union(a,b)
print list_different(a,b)
print list_diff_in_two_list(a,b)