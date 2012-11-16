#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setToolTip('This is a <b> QWidget </b> widget')
        
        #显示按钮
        btn = QtGui.QPushButton('Quit', self)
        btn.setToolTip('This is a <b> QPushButton </b> widget')
        #关联鼠标事件
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qt Bars')
        #显示状态栏
        self.statusBar().showMessage('Ready')

        #创建一个动作
        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        #创建一个菜单栏
        #添加一个菜单项，并绑定动作
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        #创建一个工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        
        self.show()
        
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
