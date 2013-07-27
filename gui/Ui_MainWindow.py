# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui
from Actions import Actions
from gui.TabWdg import TabWidget
from gui.Editor import Editor
from gui.BottomArea import BottomArea




class Ui_MainWindow(object):
    def setupUiMainWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 551)
        self.Frame = QtGui.QFrame()
        #MainWindow.setCentralWidget(self.Frame)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSerach = QtGui.QMenu(self.menubar)
        self.menuSerach.setObjectName("menuSerach")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionNew_File.setShortcut('Ctrl+N')
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setShortcut('Ctrl+O')
        self.actionSave_File = QtGui.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_File.setShortcut('Ctrl+S')
        self.actionSave_All = QtGui.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionSave_All.setShortcut('Ctrl+Shift+S')
        self.actionClose_File = QtGui.QAction(MainWindow)
        self.actionClose_File.setObjectName("actionClose_File")
        self.actionClose_File.setShortcut('Ctrl+W')
        self.actionClose_All = QtGui.QAction(MainWindow)
        self.actionClose_All.setObjectName("actionClose_All")
        self.actionClose_All.setShortcut('Ctrl+Shift+S')
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut('Ctrl+Z')
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut('Ctrl+Y')
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.setShortcut('Ctrl+X')
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.setShortcut('Ctrl+C')
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.setShortcut('Ctrl+V')
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSelect_All.setShortcut('Ctrl+A')
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next = QtGui.QAction(MainWindow)
        self.actionFind_Next.setObjectName("actionFind_Next")
        self.actionFind_Next.setShortcut('Ctrl+G')
        self.actionFind.setShortcut('Ctrl+F')
        self.actionFind_Prev = QtGui.QAction(MainWindow)
        self.actionFind_Prev.setObjectName("actionFind_Prev")
        self.actionFind_Prev.setShortcut('Ctrl+Shift+G')
        self.actionOnline_Help = QtGui.QAction(MainWindow)
        self.actionOnline_Help.setObjectName("actionOnline_Help")
        self.actionOnline_Help.setShortcut('F1')
        self.actionLua_Help = QtGui.QAction(MainWindow)
        self.actionLua_Help.setObjectName("actionLua_Help")
        self.actionAbout_Lua = QtGui.QAction(MainWindow)
        self.actionAbout_Lua.setObjectName("actionAbout_Lua")
        self.actionAbout_Apolo = QtGui.QAction(MainWindow)
        self.actionAbout_Apolo.setObjectName("actionAbout_Apolo")
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionReport_bug = QtGui.QAction(MainWindow)
        self.actionReport_bug.setObjectName("actionReport_bug")
        self.actionSuggestions = QtGui.QAction(MainWindow)
        self.actionSuggestions.setObjectName("actionSuggestions")
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_File)
        self.menuFile.addAction(self.actionClose_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuSerach.addAction(self.actionFind)
        self.menuSerach.addSeparator()
        self.menuSerach.addAction(self.actionFind_Next)
        self.menuSerach.addAction(self.actionFind_Prev)
        self.menuHelp.addAction(self.actionOnline_Help)
        self.menuHelp.addAction(self.actionLua_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionSuggestions)
        self.menuHelp.addAction(self.actionReport_bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionAbout_Lua)
        self.menuHelp.addAction(self.actionAbout_Apolo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSerach.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.BtmArea = BottomArea()


        self.Split = QtGui.QSplitter(QtCore.Qt.Vertical)

        self.layout = QtGui.QHBoxLayout()
        self.Frame.setLayout(self.layout)
        self.Split.insertWidget(0, self.Frame)
        self.Split.insertWidget(1, self.BtmArea)
        self.Split.setStretchFactor(0, 10)
        self.Split.setStretchFactor(1, 5)



        self.setCentralWidget(self.Split)





        #instance de tabs
        self.Tabs = TabWidget()
        self.layout.addWidget(self.Tabs)
        #instance editor
        self.Edt = Editor()
        self.Edt.setPlainText('Welcome')
        self.Edt.setReadOnly(True)
        self.Edt.FileName = 'Start Page'
        self.Tabs.add_Tab(0, self.Edt, 'Start Page')

        self.retranslateUi(self)#to turn toolbox visible

        #instance Actions
        self.Act = Actions(self)

        #drawing toolbar
        self.ToolBar = self.addToolBar('ToolBar')


        #new File
        Action_NewFile = QtGui.QAction(QtGui.QIcon('gui/icons/new_file.png'),
                                                    'New File', self)
        self.ToolBar.addAction(Action_NewFile)
        Action_NewFile.triggered.connect(self.Act.New_File)
        #Open File
        self.Action_OpenFile = QtGui.QAction(
            QtGui.QIcon('gui/icons/open_file.png'), 'Open File', self)
        self.ToolBar.addAction(self.Action_OpenFile)
        self.Action_OpenFile.triggered.connect(self.Act.Open_File)
        #Save File
        Action_SaveFile = QtGui.QAction(QtGui.QIcon('gui/icons/save_file.png'),
                                                     'Save File', self)
        self.ToolBar.addAction(Action_SaveFile)
        Action_SaveFile.triggered.connect(self.Act.Save_File)
        #Save All
        Action_SaveAll = QtGui.QAction(QtGui.QIcon('gui/icons/save_all.png'),
                                                        'Save All', self)
        self.ToolBar.addAction(Action_SaveAll)
        Action_SaveAll.triggered.connect(self.Act.Save_All)
        #Separator
        self.ToolBar.addSeparator()
        #Cut
        Action_Cut = QtGui.QAction(QtGui.QIcon('gui/icons/cut.png'), 'Cut',
                                                                        self)
        self.ToolBar.addAction(Action_Cut)
        Action_Cut.triggered.connect(self.Act.Cut)
        #Copy
        Action_Copy = QtGui.QAction(QtGui.QIcon('gui/icons/copy.png'), 'Copy',
                                                                        self)
        self.ToolBar.addAction(Action_Copy)
        Action_Copy.triggered.connect(self.Act.Copy)
        #Paste
        Action_Paste = QtGui.QAction(QtGui.QIcon('gui/icons/paste.png'),
                                                    'Paste', self)
        self.ToolBar.addAction(Action_Paste)
        Action_Paste.triggered.connect(self.Act.Paste)
        #Separator
        self.ToolBar.addSeparator()
        #Run
        Action_Run = QtGui.QAction(QtGui.QIcon('gui/icons/run.png'), 'Run',
                                                                        self)
        self.ToolBar.addAction(Action_Run)
        Action_Run.triggered.connect(self.Act.Run)
        #Stop
        Action_Stop = QtGui.QAction(QtGui.QIcon('gui/icons/stop.png'), 'Stop',
                                                                        self)
        self.ToolBar.addAction(Action_Stop)
        Action_Stop.triggered.connect(self.Act.Stop)

        #tab signal
      #  self.Tabs.tabCloseRequested.connect(self.Act.Close_File)
        self.Tabs.connect(self.Tabs, QtCore.SIGNAL("tabCloseRequested(int)"),
                                self.Act.Close_File)


        #menu signals....
        self.actionNew_File.triggered.connect(self.Act.New_File)
        self.actionOpen_File.triggered.connect(self.Act.Open_File)
        self.actionSave_File.triggered.connect(self.Act.Save_File)
        self.actionSave_All.triggered.connect(self.Act.Save_All)
        self.actionClose_File.triggered.connect(self.Act.Close_File)
        self.actionClose_All.triggered.connect(self.Act.Close_All)
        self.actionExit.triggered.connect(self.Act.Exit)
        self.actionRedo.triggered.connect(self.Act.Redo)
        self.actionUndo.triggered.connect(self.Act.Undo)
        self.actionCut.triggered.connect(self.Act.Cut)
        self.actionPaste.triggered.connect(self.Act.Paste)
        self.actionCopy.triggered.connect(self.Act.Copy)
        self.actionSelect_All.triggered.connect(self.Act.Select_All)
        self.actionFind.triggered.connect(self.Act.Find)
        self.actionFind_Next.triggered.connect(self.Act.Find_Next)
        self.actionFind_Prev.triggered.connect(self.Act.Find_Prev)
        self.actionOnline_Help.triggered.connect(self.Act.Online_Help)
        self.actionLua_Help.triggered.connect(self.Act.Lua_Help)
        self.actionReport_bug.triggered.connect(self.Act.IDE_Forum)
        self.actionSuggestions.triggered.connect(self.Act.IDE_Forum)
        self.actionLicense.triggered.connect(self.Act.Show_License)









        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSerach.setTitle(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_File.setText(QtGui.QApplication.translate("MainWindow", "New File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_File.setText(QtGui.QApplication.translate("MainWindow", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_File.setText(QtGui.QApplication.translate("MainWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_All.setText(QtGui.QApplication.translate("MainWindow", "Save All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_File.setText(QtGui.QApplication.translate("MainWindow", "Close File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_All.setText(QtGui.QApplication.translate("MainWindow", "Close All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Next.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Prev.setText(QtGui.QApplication.translate("MainWindow", "Find Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOnline_Help.setText(QtGui.QApplication.translate("MainWindow", "Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLua_Help.setText(QtGui.QApplication.translate("MainWindow", "Lua Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Lua.setText(QtGui.QApplication.translate("MainWindow", "About Lua", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Apolo.setText(QtGui.QApplication.translate("MainWindow", "About Apolo IDE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("MainWindow", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReport_bug.setText(QtGui.QApplication.translate("MainWindow", "Report bug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuggestions.setText(QtGui.QApplication.translate("MainWindow", "Suggestions", None, QtGui.QApplication.UnicodeUTF8))

