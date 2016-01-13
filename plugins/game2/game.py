#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class GamePlugin(QtGui.QLabel):

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
        self.setText("Game 2")
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.resize(500, 500)
    main.show()
    sys.exit(app.exec_())