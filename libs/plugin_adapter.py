#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import glob
from importlib import import_module


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
            mod_list.extend(glob.glob("".join([p, os.sep, "*", self.mod_name + self.mod_ext])))
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
            objects.append(obj)
        return tuple(objects)



if __name__ == '__main__':
    plugin_dir = "testw/plugins"
    mod_name = "game"
    class_name = "GamePlugin"
    adapter = AdapterPluginsGame(plugin_dir, mod_name, class_name)

    print(adapter.plugin_objects(adapter.paths))
