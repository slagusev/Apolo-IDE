# *-* coding:utf-8 *-*

from PySide import QtGui
from gui.Editor import Editor



def Open_File(ID, Wdg):
    try:
        print('Open File')
        Dialog = QtGui.QFileDialog()
        FileDestination, _ = Dialog.getOpenFileName(Wdg, 'Open File',
                                                    None, 'Lua Files (*.lua);;'
                                                           + 'All Files(*)')
        FileName = FileDestination.split('/')
        FileName.reverse()
        FileName = FileName[0]
        f = open(FileDestination, 'r')
        with f:
            OpenedFile = f.read()
            Edt = Editor()
            Edt.setObjectName('Editor' + str(ID))
            Wdg.Tabs.add_Tab(ID, Edt, FileName)
            Edt.FileWasOpened = True
            Edt.FileDestination = FileDestination
            Edt.setPlainText(OpenedFile)
            Edt.FileName = FileName
            Edt.textChanged.connect(Wdg.Act.TextChanged)
            print(ID)
            return ('FileOpened')

    except:
        print('Error when trying to open file')


def New_File(ID, Wdg):
    FileName = 'New File'
    Edt = Editor()
    Edt.setObjectName('Editor' + str(ID))
    Wdg.Tabs.add_Tab(ID, Edt, FileName)
    Edt.textChanged.connect(Wdg.Act.TextChanged)
    print(ID)


def Save_All(Wdg):
    Quant = Wdg.Tabs.count()
    print Quant
    for iCont in range(Quant):
        Save_File(Wdg, iCont)


def Save_File(Wdg, CurrentIndex=None):
    try:
        if CurrentIndex is  None:
            CurrentIndex = Wdg.Tabs.currentIndex()
        CurrentEditor = Wdg.Tabs.widget(CurrentIndex)
        Content = CurrentEditor.toPlainText()
        Dialog = QtGui.QFileDialog()
        Destination = CurrentEditor.FileDestination
        if CurrentEditor.FileWasOpened is False:
            Destination, _ = Dialog.getSaveFileName(Wdg, 'Save File', None,
                                                            'Lua File (*.lua)')
        f = open(Destination, 'w')
        f.write(Content)
        f.close()
        CurrentEditor.FileWasOpened = True
        CurrentEditor.FileDestination = Destination
        CurrentEditor.FileModified = False
        FileName = Destination.split('/')
        FileName.reverse()
        FileName = FileName[0]
        Wdg.Tabs.widget(CurrentIndex).FileName = FileName
        Wdg.Tabs.setTabText(CurrentIndex, FileName)
        print(Destination)
        return True
    except:
        print('Error when trying to save')


def Close_All(Wdg):
    Quant = Wdg.Tabs.count()
    print (Quant)
    for iCont in reversed(range(Quant)):
        Close_File(Wdg, iCont)


def Close_File(Wdg, CurrentIndex=None):
        Dialog = QtGui.QMessageBox()
        if CurrentIndex is None:
            CurrentIndex = Wdg.Tabs.currentIndex()
        print('*' + str(CurrentIndex))
        Edt = Wdg.Tabs.widget(CurrentIndex)
        Flags = Dialog.StandardButton.Yes
        Flags |= Dialog.StandardButton.No
        Flags |= Dialog.StandardButton.Cancel
        Result = Dialog.question(Wdg, 'Apolo IDE',
                                     'Do you want to save before closing?',
                                                                        Flags)
        if Result is Dialog.Yes:
            Save_File(Wdg, CurrentIndex)
        elif Result is Dialog.Cancel:
            return 1
        Wdg.Tabs.removeTab(CurrentIndex)







