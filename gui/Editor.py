# *-* coding:utf-8 *-*

from PySide.QtGui import QPlainTextEdit, QTextCursor
from PySide.QtCore import Qt


class Editor(QPlainTextEdit):

    def __init__(self):
        super(Editor, self).__init__()
        self.FileModified = False
        self.SelectedWord = None
        self.FileDestination = None
        self.FileWasOpened = False
        self.FileName = None
        self.preKeyPress = {
            Qt.Key_Tab: self._TabClicked,
            Qt.Key_Enter: self._EnterClicked,
            Qt.Key_Return: self._EnterClicked,
            Qt.Key_Backspace: self._BackSpaceClicked
            }

    def keyPressEvent(self, event):
        if self.preKeyPress.get(event.key(), lambda x: False)(event):
            return

        QPlainTextEdit.keyPressEvent(self, event)

    def _TabClicked(self, event):
        print('sfg')
        self.textCursor().insertText('        ')
        return True

    def _BackSpaceClicked(self, event):
        Cur = self.textCursor()
        if Cur.hasSelection():
            return False
        Cur.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
        Text = Cur.selection().toPlainText()
        if (len(Text) % 8 == 0) and Text.isspace():
            Cur.movePosition(QTextCursor.StartOfLine)
            Cur.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 8)
            Cur.removeSelectedText()
            return True

    def _EnterClicked(self, event):
        Cur = self.textCursor()
        Cur.insertText('\n')
        Text = Cur.block().previous().text()
        TabLen = 0
        for i in range(len(Text)):
            if Text[i] == ' ':
                TabLen = TabLen + 1
            else:
                break
        Cur.insertText(' ' * TabLen)
        print(TabLen)
        print(len(Text))
        print(Text)
        return True



