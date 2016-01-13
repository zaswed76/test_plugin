#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import glob
from importlib import import_module


class GameObject:
    def __init__(self, obj):
        self.obj = obj



class AdapterPluginsGame:
    mod_ext = ".py"

    def __init__(self, plugin_dir, mod_name, class_name):
        """
        :param plugin_dir: путь к пакету с плагинами
        :param mod_name: имя подключаемого модуля
        :param class_name: имя подключаемого класса
        """
        self.class_name = class_name
        self.mod_name = mod_name
        self.plugin_dir = plugin_dir
        self.objects = []


    def plugins_paths(self):
        mod_list = []
        pkg_list = [p for p in glob.glob(self.plugin_dir + "/*")]
        for p in pkg_list:
            mod_list.extend(glob.glob("".join([p, os.sep, "*", self.mod_name + self.mod_ext])))
        return mod_list

    def create_plugin_object(self, path_list_plug):
        for p in path_list_plug:
            m = p[:-3].replace(os.sep, ".")
            mod = import_module(m)
            self.objects.append(getattr(mod, self.class_name))



if __name__ == '__main__':
    plugin_dir = "plugins"
    mod_name = "game"
    class_name = "GamePlugin"
    adapter = AdapterPluginsGame(plugin_dir, mod_name, class_name)
    paths_plug = adapter.plugins_paths()
    adapter.create_plugin_object(paths_plug)
    print(adapter.objects)