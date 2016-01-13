#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import plugin_adapter

plugin_dir = "plugins"
mod_name = "game"
class_name = "GamePlugin"

class ToolLabel(QtGui.QLabel):
    clicked = QtCore.pyqtSignal()
    def __init__(self, text=""):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText(text)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()

    def add_icon(self, icon_path):
        self.setPixmap(QtGui.QPixmap(icon_path))


class Tool(QtGui.QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(30)

        self.box = QtGui.QHBoxLayout(self)

    def add_button(self, but):
        self.box.addWidget(but)


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(500, 500)
        self.plugins_game_widget = []
        self.controls = []

        self.plugins = plugin_adapter.AdapterPluginsGame(plugin_dir,
                                                         mod_name,
                                                         class_name)
        self.tool = Tool()

        # self.signalMapper = QtCore.QSignalMapper()

        # -------------------------------------------

        self.box = QtGui.QVBoxLayout()
        self.stack = QtGui.QStackedLayout()
        self.box.addLayout(self.stack)
        self.box.addWidget(self.tool)


        # self.controls["first"].clicked.connect(lambda: self.press_game(0))
        # self.controls["sec"].clicked.connect(lambda: self.press_game(1))
        # self.tool.add_button(self.controls["first"])
        # self.tool.add_button(self.controls["sec"])

        self.setLayout(self.box)


    def create_plugin_objects(self, ):
        """

        """
        mod_objects = self.plugins.plugin_objects(self.plugins.paths)
        for game_widget in mod_objects:
            self.plugins_game_widget.append(game_widget())

    def add_plugin_to_stack(self):
        for widget in self.plugins_game_widget:
            self.stack.addWidget(widget)

    def create_tool_buttons(self):
        for widg in self.plugins_game_widget:
            icon = widg.tool_icon

            tool_buttpn = ToolLabel(icon)
            tool_buttpn.add_icon(icon)
            self.tool.add_button(tool_buttpn)




    def press_game(self, s):
        self.stack.setCurrentIndex(s)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.create_plugin_objects()
    main.add_plugin_to_stack()
    main.create_tool_buttons()
    # main.read_plugins_dir()
    main.show()
    sys.exit(app.exec_())