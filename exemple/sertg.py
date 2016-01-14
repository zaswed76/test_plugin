#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore

class GamePlugin(QtGui.QFrame):
    def __init__(self, *__args):
        super().__init__()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()

    main.show()
    sys.exit(app.exec_())