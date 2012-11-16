#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setToolTip('This is a <b> QWidget </b> widget')
        
        btn = QtGui.QPushButton('Quit', self)
        btn.setToolTip('This is a <b> QPushButton </b> widget')
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit Button')

        self.show()
        # 
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,'Message',
               "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
               QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()
