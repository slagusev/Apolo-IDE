# *-* coding:utf-8 *-8

from PySide.QtGui import QTabWidget
from PySide import QtGui, QtCore


class TabWidget(QTabWidget):

    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.LastFile = None
        # to see if is new or opened
       # self.setCornerWidget(parent, QtCore.Qt.TopRightCorner)
        #self.tabNavigator = TabNavigator()
        self._already_open = []
        #testar se o arq foi modificado



    #to add a tab, opening or creating a file
    def add_Tab(self, Index, Wdg, Title):
        try:
            self.insertTab(Index, Wdg, Title)
            self.setCurrentIndex(Index)
            print(Index)
        except:
            print('Error')

