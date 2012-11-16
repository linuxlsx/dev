#-*- coding:utf-8 -*-

"""
发送一个自定义事件
"""

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        btn1 = QtGui.QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton('Button 2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event sender')

        self.show()
    
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()
