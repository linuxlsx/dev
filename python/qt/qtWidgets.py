#-*- coding:utf-8 -*-
"""
使用Qt的各种Widget
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox  = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('d:/detail2.jpg')
        
        print pixmap.isNull()

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Temp Png')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
