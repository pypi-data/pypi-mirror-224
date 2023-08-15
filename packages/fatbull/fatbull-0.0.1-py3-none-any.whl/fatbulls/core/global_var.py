#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2023 datavita.com.cn, Inc. All Rights Reserved
#
########################################################################


"""
File: global_var.py
Author: wangjiangfeng(wangjiangfeng@hcyjs.com)
Date: 2023/8/14 16:40:11
"""

import pickle
from fatbulls.utils.logger import user_system_log, system_log


class GlobalVars(object):
    def get_state(self):
        dict_data = {}
        for key, value in self.__dict__.items():
            try:
                dict_data[key] = pickle.dumps(value)
            except Exception:
                user_system_log.warn("g.{} can not pickle", key)
        return pickle.dumps(dict_data)

    def set_state(self, state):
        dict_data = pickle.loads(state) # noqa
        for key, value in dict_data.items():
            try:
                self.__dict__[key] = pickle.loads(value) # noqa
                system_log.debug("restore g.{} {}", key, type(self.__dict__[key]))
            except Exception:
                user_system_log.warn("g.{} restore failed", key)