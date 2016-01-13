#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore


class GamePlugin(QtGui.QLabel):
    _root = os.path.dirname(__file__)
    resorce = "resource"
    icons = "resource/icons"
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = "plug1"
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("""
        background-color:white;
        color: darkblue;
        border: 1px solid blue;
        font-size: 28pt;
        """)
        # -------------------------------------------
        self.setText("Game 1")
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

    @property
    def tool_icon(self):
        return os.path.join(self._root, "resource/icons/tool.png")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.resize(500, 500)
    main.show()
    sys.exit(app.exec_())

    a = "/home/serg/project/test_plugin/plugins/game1/resource/icons/tool.png"
    b = "/home/serg/project/test_plugin/plugins/game1/resource/icons/tool.png"