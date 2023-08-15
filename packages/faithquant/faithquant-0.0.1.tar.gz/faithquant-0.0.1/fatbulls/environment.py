#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2023 datavita.com.cn, Inc. All Rights Reserved
#
########################################################################


"""
File: environment.py
Author: wangjiangfeng(wangjiangfeng@hcyjs.com)
Date: 2023/8/14 16:33:27
"""

from datetime import datetime
from typing import Optional, Dict, List
from itertools import chain

import fatbulls
from fatbulls.utils.logger import system_log, user_log, user_system_log
from fatbulls.core.global_var import GlobalVars


class Environment(object):
    _env = None  # type: Environment

    def __init__(self, config):
        Environment._env = self
        self.config = config
        self.global_vars = GlobalVars()
        self.system_log = system_log
        self.user_log = user_log
        self.user_system_log = user_system_log


    @classmethod
    def get_instance(cls):
        """
        返回已经创建的 Environment 对象
        """
        if Environment._env is None:
            raise RuntimeError("Environment has not been created. Please Use `Environment.get_instance()` after FatBulls init")
        return Environment._env

