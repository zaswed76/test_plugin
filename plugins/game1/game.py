#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from libs import plugin


class GamePlugin(plugin.WidgetPlugin):
    def __init__(self, *__args):
        super().__init__()
        self.root_path = os.path.dirname(__file__)
        self.tool_icon = os.path.join(self.root_path, self.icons,"tool.png")
        self.index = 1

        self.label = QtGui.QLabel()

        self.name = "plug1"
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
        background-color:white;
        color: darkblue;
        border: 1px solid blue;
        font-size: 28pt;
        """)
        # -------------------------------------------
        self.label.setText("Game 1")
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.box.addWidget(self.label)




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.resize(500, 500)
    main.show()
    sys.exit(app.exec_())

    a = "/home/serg/project/test_plugin/plugins/game1/resource/icons/tool.png"
    b = "/home/serg/project/test_plugin/plugins/game1/resource/icons/tool.png"