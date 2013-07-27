# *-* coding:utf-8 *-*

from PySide import QtGui, QtCore
from core.file_manager import *
from threading import Thread
import webbrowser




class Actions(object):

    def __init__(self, parent):
        self.Wdg = parent
        self.__BiggerID = 1
        self.FindText = None
        self.OutTxt = None

    def Show_License(self):
        print('sdfsdf')
        Dialog = QtGui.QDialog()
        Text = QtGui.QTextEdit(Dialog)
        Text.resize(500, 450)
        Btn = QtGui.QPushButton(Dialog)
        Btn.setText('Close')
        Btn.move(400, 450)
        f = open('license.txt', 'r')
        Tmp = f.read()
        Text.setText(Tmp)
        Dialog.setMinimumSize(500, 490)
        Dialog.setMaximumSize(500, 490)
        Dialog.setWindowTitle('GNU LESSER GENERAL PUBLIC LICENSE v3.0')
        Btn.clicked.connect(Dialog.reject)
        Dialog.exec_()

    def About_Lua(self):
        Web = webbrowser.get()
        Web.open('http://www.lua.org/')

    def About_IDE(self):
        Web = webbrowser.get()
        Web.open('https://sourceforge.net/p/apoloide/')

    def Online_Help(self):
        Web = webbrowser.get()
        Web.open('https://sourceforge.net/p/apoloide/wiki/Home/')

    def Lua_Help(self):
        Web = webbrowser.get()
        Web.open('http://www.lua.org/docs.html')

    def IDE_Forum(self):
        Web = webbrowser.get()
        Web.open('https://sourceforge.net/p/apoloide/discussion/')


    def Close_File(self, Index=None):
        print('Close File')
        if Index is not None:
            a = Close_File(self.Wdg, Index)
        else:
            a = Close_File(self.Wdg)
        if a != 1:
            self.__BiggerID = self.__BiggerID - 1


    def Close_All(self):
        print('Close All')
        Close_All(self.Wdg)
        self.__BiggerID = self.Wdg.Tabs.count()

    def New_File(self):
        New_File(self.__BiggerID, self.Wdg)
        self.__BiggerID = self.__BiggerID + 1

    def Open_File(self):
        if Open_File(self.__BiggerID, self.Wdg) == 'FileOpened':
            self.__BiggerID = self.__BiggerID + 1


    def Save_File(self):
        Save_File(self.Wdg)

    def Save_All(self):
        print('Save All')
        Save_All(self.Wdg)

    def Cut(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.cut()


    def Copy(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.copy()

    def Paste(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.paste()



    def TextChanged(self, File=None):
        print('Text Changed')
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        CurrentWdg = self.Wdg.Tabs.widget(CurrentIndex)
        if CurrentWdg.FileWasOpened is False:
            pass
        else:
            self.Wdg.Tabs.setTabText(CurrentIndex, CurrentWdg.FileName + '(*)')
        CurrentWdg.FileModified = True


    def Exit(self):
        WantExit = QtGui.QMessageBox()
        Flags = WantExit.StandardButton.Yes | WantExit.StandardButton.No
        Result = WantExit.question(self.Wdg, 'Apolo IDE',
                                             'Do you want to exit?', Flags)
        if Result is WantExit.Yes:
            Close_All(self.Wdg)
            self.__BiggerID = self.Wdg.Tabs.count()
            if self.__BiggerID is 0:
                self.Wdg.close()

    def Redo(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.redo()


    def Undo(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.undo()


    def Select_All(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Edt.selectAll()

    def Find(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Dialog = QtGui.QInputDialog()
        self.FindText, ok = Dialog.getText(self.Wdg, 'Find', 'Word to find: ')
        if ok:
            Found = Edt.find(self.FindText)
            if not Found:
                Edt.moveCursor(QtGui.QTextCursor.Start)
                Found = Edt.find(self.FindText)
                if not Found:
                    Info = QtGui.QMessageBox()
                    Info.information(self.Wdg, 'Find', 'Not Found!!')

    def Find_Next(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        if self.FindText is None:
            self.Find()
        else:
            Found = Edt.find(self.FindText)
            if not Found:
                Edt.moveCursor(QtGui.QTextCursor.Start)
                Found = Edt.find(self.FindText)
                if not Found:
                    Info = QtGui.QMessageBox()
                    Info.information(self.Wdg, 'Find', 'Not found!')


    def Find_Prev(self):
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        if self.FindText is None:
            self.Find()
        else:
            Flag = QtGui.QTextDocument()
            Found = Edt.find(self.FindText, Flag.FindBackward)
            if not Found:
                Edt.moveCursor(QtGui.QTextCursor.End)
                Found = Edt.find(self.FindText, Flag.FindBackward)
                if not Found:
                    Info = QtGui.QMessageBox()
                    Info.information(self.Wdg,'Find', 'Not found!')


    def Stop(self):
        print('Stop')
        try:
            self.Proc.terminate()
        except:
            print('Not worked :(')

    def Run(self):
        self.Th = Thread(self._Run())
        self.Th.start()



    def _Run(self):
        self.Stop()
        CurrentIndex = self.Wdg.Tabs.currentIndex()
        Edt = self.Wdg.Tabs.widget(CurrentIndex)
        Saved = Save_File(self.Wdg)
        if Saved:
            File = Edt.FileDestination
            self.Out = self.Wdg.BtmArea.widget(self.Wdg.BtmArea.currentIndex())
            self.Proc = QtCore.QProcess()
            self.Proc.setWorkingDirectory = '/'
            self.Proc.readyReadStandardError.connect(self.readConsoleError)
            self.Proc.readyReadStandardOutput.connect(self.readConsole)
            self.Proc.start('lua', [File])
        #    self.Proc.waitForFinished()
        #    self.Proc.terminate()


            print('Ok')


    def readConsoleError(self):
        self.OutTxt = str(self.Proc.readAllStandardError())
        self.Out.setPlainText(self.OutTxt)
        print(self.OutTxt)

    def readConsole(self):
        self.OutTxt = str(self.Proc.readAllStandardOutput())
        self.Out.setPlainText(self.OutTxt)
        print(self.OutTxt)



