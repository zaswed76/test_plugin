#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import os


class GamePlugin(QtGui.QLabel):
    _root = os.path.dirname(__file__)
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = "plug2"

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("""
        background-color:white;
        color: green;
        border: 1px solid grey;
        font-size: 28pt;
        """)
        # -------------------------------------------
        self.setText("Game 3")
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