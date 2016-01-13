#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSlot


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(500, 300)

        # -------------------------------------------

        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

        self.label = QtGui.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.text = QtGui.QLineEdit()
        self.but = QtGui.QPushButton("clean")
        self.box.addWidget( self.label)
        self.box.addWidget(self.text)
        self.box.addWidget(self.but)



        @self.text.textChanged.connect
        def click(arg):
            self.ch_label(arg)

        @self.but.clicked.connect
        def click():
            self.label.clear()
            self.text.clear()

    def ch_label(self, arg):
        self.label.setText(arg)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())