# -*- coding: utf-8 -*-
import logging
import sys

logger = logging.getLogger()

logger.setLevel(logging.ERROR)

sh = logging.StreamHandler(sys.stderr)

logger.addHandler(sh)


logger.info('asdsf')
logger.error('asdasd')
logger.warning('sdfsd')
logger.critical('sdf')

