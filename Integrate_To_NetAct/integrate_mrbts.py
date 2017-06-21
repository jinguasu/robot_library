# -*- coding: utf-8 -*-
from optparse import OptionParser
from glob import glob
import os, threading

from logger import logger
import generate_tpl as tpl
import aif_proxy as proxy

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "outputs"

def parse_args():
    parser = OptionParser()
    parser.add_option('-i','--inputfile',dest='input_file',help='input excel')
    options = parser.parse_args()[0]
    input_file = options.input_file
    logger.info('begin to integrate MRBTS with input:'+ input_file)

    return input_file


def check_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        for file in glob(dir_name + os.sep + '*'):
            os.remove(file)


def prepare_dir():
    check_dir(TEMPLATE_DIR)
    check_dir(OUTPUT_DIR)

def main():
    input_file = parse_args()
    prepare_dir()

    node_tpl_map = tpl.write_conf(input_file,OUTPUT_DIR)
    threads = []
    for node,tpl_file in node_tpl_map.iteritems():
        t = threading.Thread(target=proxy.auto_integrate,name="thread_" + node, args=(node,tpl_file,OUTPUT_DIR))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()   #等待每个线程结束

    print proxy.merge_result(OUTPUT_DIR)


if __name__ == '__main__':
    #parse_args()
    #check_dir('templates')
    main()


