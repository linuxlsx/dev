#-*- coding:utf-8 -*-

"""
使用Qt的信号槽
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Singal & slot')

        self.show()
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,'Message',
               "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
               QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        print event.key()
        print QtCore.Qt.Key_Escape
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()
