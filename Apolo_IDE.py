# *-* coding:utf-8 *-*

import sys

from PySide.QtGui import QApplication, QMainWindow, QIcon
from PySide import QtCore
from gui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUiMainWindow(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    IDE = MainWindow()
    IDE.setWindowTitle('Apolo IDE')
    IDE.setWindowIcon(QIcon('gui/icons/ide.png'))
    IDE.show()
    app.exec_()
