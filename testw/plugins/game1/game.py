#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class GamePlugin(QtGui.QLabel):
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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.resize(500, 500)
    main.show()
    sys.exit(app.exec_())