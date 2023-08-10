#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: MaJian
@Time: 2023/8/8 16:13
@SoftWare: PyCharm
@Project: mj_tools
@File: var
"""


class MjVar:
    def __init__(self, **kwargs):
        self._namespace = self.Namespace()
        self._dict = dict()
        self.args = None
        self.add(**kwargs)

    def add(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self._add(key, value)
            self.args = self._namespace

    def delete(self, key: list):
        for name in key:
            delattr(self._namespace, name)
            self._dict.pop(name)
        self.args = self._namespace

    def _add(self, key, value):
        if not key.isidentifier():
            raise Exception(f"变量{key}含不合法的标识符")
        self._dict.update({key: value})
        setattr(self._namespace, key, value)

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        for name, value in sorted(self._dict.items()):
            if name.isidentifier():
                arg_strings.append('%s=%r' % (name, value))
        return '%s(%s)' % (type_name, ', '.join(arg_strings))

    class Namespace(object):
        pass
