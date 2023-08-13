#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from pitrix.config import Config
from pitrix.constants.constants import Conf
from pitrix.utils.log import log

def add_template_suffix(dir='./',target_suffix=Conf.TEMPLATE_SUFFIX):
    """
    将执行目录下的文件后缀名改为.template
    """
    for root,dir,files in os.walk(dir):
        if files:
            for file in files:
                source_file = os.path.join(root,file)
                file_name, file_extension = os.path.splitext(source_file)
                if file_extension != target_suffix:
                    target_file = source_file + target_suffix
                    log.info(f"源文件:{source_file},目标文件:{target_file}")
                    os.rename(source_file,target_file)





if __name__ == '__main__':
    add_template_suffix(dir=Config.template_dir)