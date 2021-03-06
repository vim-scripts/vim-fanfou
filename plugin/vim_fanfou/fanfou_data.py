#!/usr/bin/env python
"""
    vim_fanfou.fanfou_data:
    ~~~~~~~~~~~~~~~~~~~
    The data container of fanfou response

    :copyright: (c) 2014 by xiong-jia.le ( lexiongjia@gmail.com )
    :license: Vim license. See :help license
"""

class FanfouDataType(object):
    EMPTY = 0
    HOME_TIMELINE = 1
    MENTIONS = 2
    FAVORITES = 3

    DATA_TITLE = {
        HOME_TIMELINE: "Fanfou Home Timeline",
        MENTIONS: "Fanfou Mentions",
        FAVORITES: "Fanfou Favorites",
    }


class FanfouData(object):
    def __init__(self):
        self._data = []
        self._type = FanfouDataType.EMPTY

    def get_data_type(self):
        return self._type

    def get_items(self):
        return self._data

    def set_items(self, data_type, items):
        self._type = data_type
        self._data = items

    def push_item(self, data_type, item):
        if data_type != self._type:
            return False
        self._data.insert(0, item)
        return True

    def get_data_title(self):
        return FanfouDataType.DATA_TITLE.get(self._type, "Fanfou")


