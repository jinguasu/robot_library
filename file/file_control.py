# -*- coding: utf-8 -*-

import re

def _check_msg_in_file(source_file_path,target_msgs):
    contain_lines = []

    if not isinstance(target_msgs,list):
        target_msgs = [target_msgs]
    unfind_msg = [msg for msg in target_msgs]
    find_msg = []
    with open(source_file_path,'r') as f:
        for line in f.readlines():
            for key in target_msgs:
                if re.search(key,line) != None:
                    find_msg.append(key)
                    contain_lines.append(line)
                    unfind_msg.remove(key)


    return unfind_msg,find_msg,contain_lines


def file_should_contain(source_file_path,target_msgs):
    unfound_msg,found_msg,contain_line = _check_msg_in_file(source_file_path,target_msgs)

    if len(unfound_msg) != 0:
        raise Exception("this key %s not found in %s" % (unfound_msg,source_file_path))

    return contain_line

def file_should_not_contain(source_file_path,target_msgs):
    unfound_msg,found_msg,contain_line = _check_msg_in_file(source_file_path,target_msgs)

    if len(found_msg) != len(target_msgs):
        raise Exception("this key %s found in %s" % (found_msg,source_file_path))

    return contain_line




if __name__ == '__main__':
    #print _check_msg_in_file('sun.txt','sun')
    #print _check_msg_in_file('sun.txt', ['sun','duoduo','asdasc'])
    file_should_not_contain('sun.txt', ['sun','duoduo','asdasc'])