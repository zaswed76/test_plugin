#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import glob
from importlib import import_module
from PyQt4 import QtGui


class ErrorIndex(Exception): pass


class ErrorChange(Exception): pass


class ErrorType(Exception): pass


_ERROR_CHANGE_MESSAGE = "нельзя изменить атрибут"


class WidgetPlugin(QtGui.QFrame):
    _root_path = os.path.dirname(__file__)
    _resource = "resource"
    _icons = "resource/icons"

    def __init__(self):
        super().__init__()
        self._index = 1
        self._tool_icon = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        if i != 0:
            self._index = i
        else:
            raise ErrorIndex("индекс не может быть 0")

    @property
    def tool_icon(self):
        return self._tool_icon

    @tool_icon.setter
    def tool_icon(self, icon_path):
        self._tool_icon = icon_path

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, path):
        raise ErrorChange(_ERROR_CHANGE_MESSAGE)

    @property
    def icons(self):
        return self._icons

    @icons.setter
    def icons(self, path):
        raise ErrorChange(_ERROR_CHANGE_MESSAGE)

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, path):
        self._root_path = path

    def __repr__(self):
        return self


class AdapterPluginsGame:
    mod_ext = ".py"

    def __init__(self, plugin_dir, mod_name, class_name):
        """
        :param plugin_dir: относительный путь к пакету с плагинами
        :param mod_name: имя подключаемого модуля без расширения
        :param class_name: имя подключаемого класса
        """
        self.class_name = class_name
        self.mod_name = mod_name
        self.plugin_dir = plugin_dir

    @property
    def paths(self):
        mod_list = []
        pkg_list = [p for p in glob.glob(self.plugin_dir + "/*")]
        for p in pkg_list:
            mod_list.extend(glob.glob("".join(
                [p, os.sep, "*", self.mod_name + self.mod_ext])))
        return mod_list

    def plugin_objects(self, path_list_plug):

        """
        относительные пути к плагинам
        @:param path_list_plug: list -> str
        @:rtype: tuple -> PyQt4.QtCore.pyqtWrapperType
        """

        objects = []
        for p in path_list_plug:
            m = p[:-3].replace(os.sep, ".")
            mod = import_module(m)
            obj = getattr(mod, self.class_name)()
            if not isinstance(obj, WidgetPlugin):
                raise ErrorType(
                    "плагин должен быть унаследован от WidgetPlugin")
            objects.append(obj)
        return tuple(objects)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = WidgetPlugin()
    main.show()
    sys.exit(app.exec_())
