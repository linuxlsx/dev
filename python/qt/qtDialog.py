#-*- coding:utf-8 -*-

"""
使用Qt的对话框
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

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 60)

        self.btn2 = QtGui.QPushButton('Color', self)
        self.btn2.move(20, 100)
        self.btn2.clicked.connect(self.showColorDialog)
        
        col = QtGui.QColor(0, 0, 0)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet('QWidget {background:%s}' % col.name())
        self.frm.setGeometry(100,160, 200, 60)
        
        openFile = QtGui.QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Dialog')

        self.show()

    def showFileDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', 'c:/Users/niba')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.le.setText(data)
        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
                                              'Enter you name:')
    
        if ok:
            self.le.setText(str(text))

    def showColorDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget {background-color : %s}' % col.name())

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()
