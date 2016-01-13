#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSlot
import plugin_adapter

plugin_dir = "plugins"
mod_name = "game"
class_name = "GamePlugin"

class ToolLabel(QtGui.QLabel):
    clicked = QtCore.pyqtSignal()
    def __init__(self, text):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText(text)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()



class Tool(QtGui.QFrame):
    def __init__(self):
        super().__init__()

        self.box = QtGui.QHBoxLayout(self)

    def add_button(self, but):
        self.box.addWidget(but)


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(500, 500)

        self.plugins = plugin_adapter.AdapterPluginsGame(plugin_dir,
                                                         mod_name,
                                                         class_name)
        self.tool = Tool()

        # self.signalMapper = QtCore.QSignalMapper()
        self.controls = {}
        # -------------------------------------------

        self.box = QtGui.QVBoxLayout()
        self.stack = QtGui.QStackedLayout()
        self.box.addLayout(self.stack)
        self.box.addWidget(self.tool)

        self.controls["first"] = ToolLabel("1")
        self.controls["first"].clicked.connect(lambda: self.press_game(1))


        self.controls["sec"] = ToolLabel("2")
        self.controls["sec"].clicked.connect(lambda: self.press_game(2))


        self.tool.add_button(self.controls["first"])
        self.tool.add_button(self.controls["sec"])

        self.setLayout(self.box)
        self.add_plugins_game()

    def add_plugins_game(self):
        self.plugins.create_plugin_object(self.plugins.plugins_paths())
        for obg in self.plugins.objects:
            self.stack.addWidget(obg())



    def press_game(self, s):

        print(s)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    # main.read_plugins_dir()
    main.show()
    sys.exit(app.exec_())