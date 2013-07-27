# *-* coding:utf-8 *-*

from PySide.QtGui import QTabWidget
from gui.Output import Output

class BottomArea(QTabWidget):

    def __init__(self):
        super(BottomArea, self).__init__()
        Out = Output()
        self.insertTab(0, Out, 'Output')
        self.setCurrentIndex(0)
