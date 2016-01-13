#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

plug_dir = "/home/serg/project/testplugin/plugins"

class BaseWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(500, 500)

        # -------------------------------------------

        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

        plugs = __import__("plugins.game2_plugin.game")
        pkg = getattr(plugs, "game2_plugin")
        print(dir(pkg))
        mod = getattr(pkg, "game")
        obj = getattr(mod, "BaseWindow")()
        self.box.addWidget(obj)




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())