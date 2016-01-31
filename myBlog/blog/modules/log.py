# -*- coding:utf8 -*-


import logging
import time
import os
from Tornado.myBlog.blog.modules.global_var import *

__all__ = ['log_init', 'log_close', ]

def log_init():
    current_day_str = time.strftime("%Y%m%d")
    if G_DEBUG_FLAG:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    log_fd = logging.getLogger(G_LOG_NAME)
    fd = None

    try:
        log_fd.setLevel(log_level)
        if not os.path.isdir(G_LOG_PATH):
            os.makedirs(G_LOG_PATH)
        log_file = os.path.join(G_LOG_PATH,
                                "%s-%s" % (G_LOG_NAME, current_day_str))
        fd = logging.FileHandler(log_file)
        fd.setLevel(log_level)
        formatter = logging.Formatter(G_LOG_FORMAT)
        fd.setFormatter(formatter)
        log_fd.addHandler(fd)
    except:
        raise
    log_fd.info('='*100)
    return log_fd, fd


def log_close(log_fd, fd):
    log_fd.info("close log handler")
    log_fd.info('='*100)
    if fd:
        fd.close()
    log_fd.removeHandler(fd)
    logging.shutdown()
