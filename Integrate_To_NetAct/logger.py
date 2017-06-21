# -*- coding: utf-8 -*-
import logging
import os
#from logging.config import fileConfig

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s:::%(levelname)s---%(message)s')

logger.setLevel(logging.INFO)

#设置一个处理器，处理log，是直接打印出来呢还是写入到文件里，这里是logging的处理器
#sh = logging.StreamHandler()    #直接打印出来
sh = logging.FileHandler('logs/log.txt')   #写入文件里面
sh.setFormatter(formatter)


#将这个处理器加到这个logger上面
logger.addHandler(sh)

if __name__ == '__main__':
    logger.error('asd')
    logger.critical('sdfkkk')
    logger.info('dsfsdf')