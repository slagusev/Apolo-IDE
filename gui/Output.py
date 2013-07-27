# *-* coding:utf-8 *-*

from PySide.QtGui import QPlainTextEdit

class Output(QPlainTextEdit):

    def __init__(self):
        super(Output, self).__init__()
        self.setReadOnly(True)




