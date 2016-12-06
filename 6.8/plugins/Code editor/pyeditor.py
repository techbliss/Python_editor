# Created by Storm Shadow www.techbliss.org

# Created by Storm Shadow www.techbliss.org
print "\n" #getting the box fit
print " ###################################################\n" \
    " #              Author Storm Shadow                # \n" \
    " #                   Hotkeys                       # \n" \
    " #         NewFile:            Ctrl+N              #\n" \
    " #         OpenFile:           Ctrl+O              #\n" \
    " #         SaveFile:           Ctrl+S              #\n" \
    " #         RunScript:          Ctrl+E              #\n" \
    " #         Undo:               Ctrl+Z              #\n" \
    " #         Redo:               Ctrl+Y              #\n" \
    " #         SelectALL:          Ctrl+A              #\n" \
    " #         Paste:              Ctrl+V              #\n" \
    " #         Font:               Ctrl+F              #\n" \
    " #         ResetFolding:       Ctrl+R              #\n" \
    " #         CircleFolding:      Ctrl+C              #\n" \
    " #         PlainFolding:       Ctrl+P              #\n" \
    " #         HEX-ray Home:       Ctrl+W              #\n" \
    " #         Ida Pro Python SDK  Ctrl+I              #\n" \
    " #         IDAPROPythonGit:    Ctrl+G              #\n" \
    " #         Author:             Ctrl+B              #\n" \
    " #         Enable Reg:         Alt+E               #\n" \
    " #         Disable Reg:        Alt+D               #\n" \
    " #         Zoom in             Ctrl+Shift+ +       #\n" \
    " #         Zoom Out            Ctrl+Shift+ -       #\n" \
    " #         Profile Code        Ctrl+Shift+ E       #\n" \
    " ###################################################\n" \
    " #              IDA PRO python Editor              #\n" \
    " ###################################################\n"

import os
import sys

try:
    dn = idaapi.idadir("plugins\\Code editor")
except NameError:
    dn = os.getcwd()
sys.path.insert(0, dn)
sys.path.insert(0, os.getcwd()+r'\icons')

from PyQt4 import QtCore, QtGui
from PyQt4.Qsci import QsciScintilla, QsciLexerPython
from PyQt4.QtGui import *
from PyQt4.QtCore import QTextStream
from PyQt4.QtCore import qDebug

try:
    import ico
except ImportError:
    import icons.ico

try:
    import iconsmore
except ImportError:
    import icons.iconsmore

try:
    import icons3
except ImportError:
    import icons.icons3

try:
    import iconf
except ImportError:
    import icons.iconf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    ARROW_MARKER_NUM = 8
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.vindu = QtGui.QWidget(MainWindow)
        self.vindu.setStyleSheet(_fromUtf8('notusedasyet'))
        #MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.filename = ""
        self.vindu.closeEvent = self.closeEvent
        self.vindu.setObjectName(_fromUtf8("vindu"))
        self.verticalLayout = QtGui.QVBoxLayout(self.vindu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.codebox = Qsci.QsciScintilla(self.vindu)
        self.codebox.setToolTip(_fromUtf8(""))
        self.codebox.setWhatsThis(_fromUtf8(""))
        self.codebox.setAutoFillBackground(False)
        self.codebox.setFrameShape(QtGui.QFrame.NoFrame)
        self.codebox.setObjectName(_fromUtf8("codebox"))
        self.verticalLayout.addWidget(self.codebox)
        MainWindow.setCentralWidget(self.vindu)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar.addSeparator()
        #getting ready for debugger
        self.codebox.setMarginSensitivity(1, True)
        self.codebox.connect(self.codebox, QtCore.SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'), self.on_margin_clicked)
        self.codebox.markerDefine(QsciScintilla.FullRectangle, self.ARROW_MARKER_NUM)
        self.codebox.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        #first action Newfile
        self.toolBar.newAction = QtGui.QAction(QtGui.QIcon(":/ico/new.png"),"New",self.toolBar)
        self.toolBar.newAction.setStatusTip("Clear TextBox or make new document.")
        self.toolBar.newAction.setShortcut("Ctrl+N")
        self.toolBar.newAction.triggered.connect(self.newfile)
        #second Action OpenFile
        self.toolBar.secondAction = QtGui.QAction(QtGui.QIcon(":/ico/open.png"),"Open",self.toolBar)
        self.toolBar.secondAction.setStatusTip("Create a new document from scratch.")
        self.toolBar.secondAction.setShortcut("Ctrl+O")
        self.toolBar.secondAction.triggered.connect(self.open)
        # action 3 save file
        self.toolBar.Action3 = QtGui.QAction(QtGui.QIcon(":/ico/save.png"),"Save",self.toolBar)
        self.toolBar.Action3.setStatusTip("Save Your File.")
        self.toolBar.Action3.setShortcut("Ctrl+S")
        self.toolBar.Action3.triggered.connect(self.savefile)
        #action 4 run file
        self.toolBar.Action4 = QtGui.QAction(QtGui.QIcon(":/ico/run32.png"),"Run To Debugger",self.toolBar)
        self.toolBar.Action4.setStatusTip("Run your file within debugger.")
        self.toolBar.Action4.setShortcut("Ctrl+E")
        self.toolBar.Action4.triggered.connect(self.runto)
        #action 6 undo
        self.toolBar.Action6 =  QtGui.QAction(QtGui.QIcon(":/ico/undo.png"),"Redo",self.toolBar)
        self.toolBar.Action6.setStatusTip("Undo.")
        self.toolBar.Action6.setShortcut("Ctrl+Z")
        self.toolBar.Action6.triggered.connect(self.codebox.undo)
        #action 7 redo
        self.toolBar.Action7 = QtGui.QAction(QtGui.QIcon(":/ico/redo.png"),"Redo",self.toolBar)
        self.toolBar.Action7.setStatusTip("Redo.")
        self.toolBar.Action7.setShortcut("Ctrl+Y")
        self.toolBar.Action7.triggered.connect(self.codebox.redo)
        #action8 rerset Folding
        self.toolBar.Action8 = QtGui.QAction(QtGui.QIcon(":/ico/align-justify.png"),"Reset Folding",self.toolBar)
        self.toolBar.Action8.setStatusTip("Reset Folding.")
        self.toolBar.Action8.setShortcut("Ctrl+R")
        self.toolBar.Action8.triggered.connect(self.nofoldingl)
        #actions9 CircledTreeFoldStyle
        self.toolBar.Action9 = QtGui.QAction(QtGui.QIcon(":/ico/bullet.png"),"Circled Tree Folding",self.toolBar)
        self.toolBar.Action9.setStatusTip("Circled Tree Folding.")
        self.toolBar.Action9.setShortcut("Ctrl+C")
        self.toolBar.Action9.triggered.connect(self.Circledfold)
        #actions10 plainFoldStyle
        self.toolBar.Action10 = QtGui.QAction(QtGui.QIcon(":/ico/number.png"),"Plain Folding",self.toolBar)
        self.toolBar.Action10.setStatusTip("Plain Folding")
        self.toolBar.Action10.setShortcut("Ctrl+P")
        self.toolBar.Action10.triggered.connect(self.plainfold)
        # fonts
        self.toolBar.Action21 = QtGui.QAction(QtGui.QIcon(":/ico4/font.png"), "Fonts", self.toolBar)
        self.toolBar.Action21.setStatusTip("Fonts")
        self.toolBar.Action21.setShortcut("Ctrl+F")
        self.toolBar.Action21.triggered.connect(self.font_choice)
        #web baby
        self.toolBar.Action11 = QtGui.QAction(QtGui.QIcon(":/ico/web.png"),"Hex-rays Homepage",self.toolBar)
        self.toolBar.Action11.setStatusTip("Home of Hex-rays")
        self.toolBar.Action11.setShortcut("Ctrl+W")
        self.toolBar.Action11.triggered.connect(self.webopen)
        #irc
        self.toolBar.Action12 = QtGui.QAction(QtGui.QIcon(":/ico3/settings.png"),"Open Ida Pro Python SDK",self.toolBar)
        self.toolBar.Action12.setStatusTip("Ida Pro Python SDK")
        self.toolBar.Action12.setShortcut("Ctrl+I")
        self.toolBar.Action12.triggered.connect(self.sdkopen)
        #github Python
        self.toolBar.Action14 = QtGui.QAction(QtGui.QIcon(":/ico/github.png"),"Open git python",self.toolBar)
        self.toolBar.Action14.setStatusTip("Open git python")
        self.toolBar.Action14.setShortcut("Ctrl+G")
        self.toolBar.Action14.triggered.connect(self.gitopen)
        #auther me :)
        self.toolBar.Action15 = QtGui.QAction(QtGui.QIcon(":/ico/auth.png"),"Author",self.toolBar)
        self.toolBar.Action15.setStatusTip("Author")
        self.toolBar.Action15.setShortcut("Ctrl+B")
        self.toolBar.Action15.triggered.connect(self.Author)
        #toggle off code regonision
        self.toolBar.Action16 = QtGui.QAction(QtGui.QIcon(":/ico2/pythonminus.png"),"Disable Code recognition",self.toolBar)
        self.toolBar.Action16.setStatusTip("Disable Code recognition")
        self.toolBar.Action16.setShortcut("Alt+D")
        self.toolBar.Action16.triggered.connect(self.Diablecode)
        #toogle on
        self.toolBar.Action17 = QtGui.QAction(QtGui.QIcon(":/ico2/pypluss.png"),"Enable Code recognition",self.toolBar)
        self.toolBar.Action17.setStatusTip("Enable Code recognition")
        self.toolBar.Action17.setShortcut("Alt+E")
        self.toolBar.Action17.triggered.connect(self.Reiablecode)
        # zoom in
        self.toolBar.Action18 = QtGui.QAction(QtGui.QIcon(":/ico3/in.png"),"Zoom In",self.toolBar)
        self.toolBar.Action18.setStatusTip("Zoom In")
        self.toolBar.Action18.setShortcut("CTRL+SHIFT++")
        self.toolBar.Action18.triggered.connect(self.udder)
        #zoom out
        self.toolBar.Action19 = QtGui.QAction(QtGui.QIcon(":/ico3/out.png"),"Zoom Out",self.toolBar)
        self.toolBar.Action19.setStatusTip("Zoom Out")
        self.toolBar.Action19.setShortcut("CTRL+SHIFT+-")
        self.toolBar.Action19.triggered.connect(self.odder)

        self.toolBar.Action20 = QtGui.QAction(QtGui.QIcon(":/ico3/10.png"),"Profile Code",self.toolBar)
        self.toolBar.Action20.setStatusTip("Profile Code")
        self.toolBar.Action20.setShortcut("CTRL+SHIFT+E")
        self.toolBar.Action20.triggered.connect(self.runtoprob)

        #actions
        self.toolBar.addAction(self.toolBar.newAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.secondAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action7)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action9)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action10)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action21)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action11)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action12)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action14)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action15)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action16)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action17)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action18)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action19)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action20)

        #font
        self.skrift = QFont()
        self.skrift.setFamily('Consolas')
        self.skrift.setFixedPitch(True)
        self.skrift.setPointSize(12)
        self.codebox.setFont(self.skrift)

        #python style
        self.lexer = QsciLexerPython(self.codebox)
        self.lexer.setFont(self.skrift)
        self.lexer.setEolFill(True)
        #api test not working
        api = Qsci.QsciAPIs(self.lexer)
        API_FILE = dn+'\\Python.api'
        API_FILE2 = dn+'\\idc.api'
        API_FILE3 = dn+'\\idaapi.api'
        api.load(API_FILE)
        api.load(API_FILE2)
        api.load(API_FILE3)

        api.prepare()
        self.codebox.setAutoCompletionThreshold(0)
        self.codebox.setAutoCompletionThreshold(6)
        self.codebox.setAutoCompletionThreshold(8)
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        self.lexer.setDefaultFont(self.skrift)
        self.codebox.setLexer(self.lexer)
        self.codebox.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')

        #line numbers
        fontmetrics = QFontMetrics(self.skrift)
        self.codebox.setMarginsFont(self.skrift)
        self.codebox.setMarginWidth(0, fontmetrics.width("0000") + 6)
        self.codebox.setTabWidth(4)

        #brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        #auto line tab =4
        self.codebox.setAutoIndent(True)

        #scroolbar
        self.codebox.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lbl = self.codebox
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ida Pro Python Script Editor", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))


    def udder(self):
        self.codebox.zoomIn()

    def odder(self):
        self.codebox.zoomOut()

    def newfile(self):
        self.codebox.clear()

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(
                   self.vindu, 'Open File', self.path, "Python Files (*.py *.pyc *.pyw)",
                   '')

        if self.filename:
            with open(self.filename,"r") as self.file:
                self.codebox.setText(self.file.read())
        os.chdir(str(self.path))



    def fontFamily(self,font):
        self.text.setCurrentFont(font)

    def fontSize(self, fontsize):
            self.text.setFontPointSize(int(fontsize))


    def fontFamily(self,font):
        self.codebox.text.setCurrentFont(font)

    def fontSize(self, fontsize):
        self.codebox.text.setFontPointSize(int(fontsize))

    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        self.filename = QtGui.QFileDialog.getSaveFileName(
            self.vindu, "Save as", self.path, "Python Files (*.py *.pyc *.pyw)",
            )
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.codebox.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtGui.QMessageBox.information(self.vindu, "Unable to open file",
                    file.errorString())
        os.chdir(str(self.path))

    def runto(self):
        try:
            self.path = QtCore.QFileInfo(self.filename).path()
        except AttributeError:
            pass
        g = globals()
        os.chdir(str(self.path))
        os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
        script = str(self.codebox.text())
        try:
            exec (script, g)
            QtGui.QCloseEvent()


        except ImportError:
            os.chdir(str(self.path))
            os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
            sys.path.append(str(self.path))
            exec (script, g)
            QtGui.QCloseEvent()

            if TypeError (QTextStream):
                g = globals()
                os.chdir(str(self.path))
                os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
                sys.path.insert(0, str(self.path))
                exec int(script)
                QtGui.QCloseEvent()

    def runtoprob(self):
        try:
            self.path = QtCore.QFileInfo(self.filename).path()
        except AttributeError:
            pass
        self.path = QtCore.QFileInfo(self.filename).path()
        g = globals()
        os.chdir(str(self.path))
        script = str(self.codebox.text())
        import cProfile
        cProfile.run(script)


    def Diablecode(self):
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsNone)

    def Reiablecode(self):
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)

    def nofoldingl(self):
        self.codebox.setFolding(QsciScintilla.NoFoldStyle)

    def Circledfold(self):
        self.codebox.setFolding(QsciScintilla.CircledTreeFoldStyle)

    def plainfold(self):
        self.codebox.setFolding(QsciScintilla.PlainFoldStyle)

    def webopen(self):
        import webbrowser
        webbrowser.open('https://www.hex-rays.com/')

    def sdkopen(self):
        import webbrowser
        webbrowser.open('https://www.hex-rays.com/products/ida/support/idapython_docs/')

    def gitopen(self):
        import webbrowser
        webbrowser.open('https://github.com/idapython/src/tree/build-1.7.2')

    def Author(self):
        import webbrowser
        webbrowser.open('https://github.com/techbliss')


    def closeEvent(self, event):
        print("event")
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def font_choice(self):
        self.lbl = self.lexer
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.codebox.markersAtLine(nline) != 0:
            self.codebox.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.codebox.markerAdd(nline, self.ARROW_MARKER_NUM)


from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance() # We add this so we can use editor outside Ida
    if not app:
        app = QtGui.QApplication([])
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.resize(1000, 600)
    if app.exec_():
        os.chdir(dn)# Created by Storm Shadow www.techbliss.org

# Created by Storm Shadow www.techbliss.org
print "\n" #getting the box fit
print " ###################################################\n" \
    " #              Author Storm Shadow                # \n" \
    " #                   Hotkeys                       # \n" \
    " #         NewFile:            Ctrl+N              #\n" \
    " #         OpenFile:           Ctrl+O              #\n" \
    " #         SaveFile:           Ctrl+S              #\n" \
    " #         RunScript:          Ctrl+E              #\n" \
    " #         Undo:               Ctrl+Z              #\n" \
    " #         Redo:               Ctrl+Y              #\n" \
    " #         SelectALL:          Ctrl+A              #\n" \
    " #         Paste:              Ctrl+V              #\n" \
    " #         Font:               Ctrl+F              #\n" \
    " #         ResetFolding:       Ctrl+R              #\n" \
    " #         CircleFolding:      Ctrl+C              #\n" \
    " #         PlainFolding:       Ctrl+P              #\n" \
    " #         HEX-ray Home:       Ctrl+W              #\n" \
    " #         Ida Pro Python SDK  Ctrl+I              #\n" \
    " #         IDAPROPythonGit:    Ctrl+G              #\n" \
    " #         Author:             Ctrl+B              #\n" \
    " #         Enable Reg:         Alt+E               #\n" \
    " #         Disable Reg:        Alt+D               #\n" \
    " #         Zoom in             Ctrl+Shift+ +       #\n" \
    " #         Zoom Out            Ctrl+Shift+ -       #\n" \
    " #         Profile Code        Ctrl+Shift+ E       #\n" \
    " ###################################################\n" \
    " #              IDA PRO python Editor              #\n" \
    " ###################################################\n"

import os
import sys

try:
    dn = idaapi.idadir("plugins\\Code editor")
except NameError:
    dn = os.getcwd()
sys.path.insert(0, dn)
sys.path.insert(0, os.getcwd()+r'\icons')

from PyQt4 import QtCore, QtGui
from PyQt4.Qsci import QsciScintilla, QsciLexerPython
from PyQt4.QtGui import *
from PyQt4.QtCore import QTextStream
from PyQt4.QtCore import qDebug

try:
    import ico
except ImportError:
    import icons.ico

try:
    import iconsmore
except ImportError:
    import icons.iconsmore

try:
    import icons3
except ImportError:
    import icons.icons3

try:
    import iconf
except ImportError:
    import icons.iconf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    ARROW_MARKER_NUM = 8
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.vindu = QtGui.QWidget(MainWindow)
        self.vindu.setStyleSheet(_fromUtf8('notusedasyet'))
        #MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.filename = ""
        self.vindu.closeEvent = self.closeEvent
        self.vindu.setObjectName(_fromUtf8("vindu"))
        self.verticalLayout = QtGui.QVBoxLayout(self.vindu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.codebox = Qsci.QsciScintilla(self.vindu)
        self.codebox.setToolTip(_fromUtf8(""))
        self.codebox.setWhatsThis(_fromUtf8(""))
        self.codebox.setAutoFillBackground(False)
        self.codebox.setFrameShape(QtGui.QFrame.NoFrame)
        self.codebox.setObjectName(_fromUtf8("codebox"))
        self.verticalLayout.addWidget(self.codebox)
        MainWindow.setCentralWidget(self.vindu)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar.addSeparator()
        #getting ready for debugger
        self.codebox.setMarginSensitivity(1, True)
        self.codebox.connect(self.codebox, QtCore.SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'), self.on_margin_clicked)
        self.codebox.markerDefine(QsciScintilla.FullRectangle, self.ARROW_MARKER_NUM)
        self.codebox.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        #first action Newfile
        self.toolBar.newAction = QtGui.QAction(QtGui.QIcon(":/ico/new.png"),"New",self.toolBar)
        self.toolBar.newAction.setStatusTip("Clear TextBox or make new document.")
        self.toolBar.newAction.setShortcut("Ctrl+N")
        self.toolBar.newAction.triggered.connect(self.newfile)
        #second Action OpenFile
        self.toolBar.secondAction = QtGui.QAction(QtGui.QIcon(":/ico/open.png"),"Open",self.toolBar)
        self.toolBar.secondAction.setStatusTip("Create a new document from scratch.")
        self.toolBar.secondAction.setShortcut("Ctrl+O")
        self.toolBar.secondAction.triggered.connect(self.open)
        # action 3 save file
        self.toolBar.Action3 = QtGui.QAction(QtGui.QIcon(":/ico/save.png"),"Save",self.toolBar)
        self.toolBar.Action3.setStatusTip("Save Your File.")
        self.toolBar.Action3.setShortcut("Ctrl+S")
        self.toolBar.Action3.triggered.connect(self.savefile)
        #action 4 run file
        self.toolBar.Action4 = QtGui.QAction(QtGui.QIcon(":/ico/run32.png"),"Run To Debugger",self.toolBar)
        self.toolBar.Action4.setStatusTip("Run your file within debugger.")
        self.toolBar.Action4.setShortcut("Ctrl+E")
        self.toolBar.Action4.triggered.connect(self.runto)
        #action 6 undo
        self.toolBar.Action6 =  QtGui.QAction(QtGui.QIcon(":/ico/undo.png"),"Redo",self.toolBar)
        self.toolBar.Action6.setStatusTip("Undo.")
        self.toolBar.Action6.setShortcut("Ctrl+Z")
        self.toolBar.Action6.triggered.connect(self.codebox.undo)
        #action 7 redo
        self.toolBar.Action7 = QtGui.QAction(QtGui.QIcon(":/ico/redo.png"),"Redo",self.toolBar)
        self.toolBar.Action7.setStatusTip("Redo.")
        self.toolBar.Action7.setShortcut("Ctrl+Y")
        self.toolBar.Action7.triggered.connect(self.codebox.redo)
        #action8 rerset Folding
        self.toolBar.Action8 = QtGui.QAction(QtGui.QIcon(":/ico/align-justify.png"),"Reset Folding",self.toolBar)
        self.toolBar.Action8.setStatusTip("Reset Folding.")
        self.toolBar.Action8.setShortcut("Ctrl+R")
        self.toolBar.Action8.triggered.connect(self.nofoldingl)
        #actions9 CircledTreeFoldStyle
        self.toolBar.Action9 = QtGui.QAction(QtGui.QIcon(":/ico/bullet.png"),"Circled Tree Folding",self.toolBar)
        self.toolBar.Action9.setStatusTip("Circled Tree Folding.")
        self.toolBar.Action9.setShortcut("Ctrl+C")
        self.toolBar.Action9.triggered.connect(self.Circledfold)
        #actions10 plainFoldStyle
        self.toolBar.Action10 = QtGui.QAction(QtGui.QIcon(":/ico/number.png"),"Plain Folding",self.toolBar)
        self.toolBar.Action10.setStatusTip("Plain Folding")
        self.toolBar.Action10.setShortcut("Ctrl+P")
        self.toolBar.Action10.triggered.connect(self.plainfold)
        # fonts
        self.toolBar.Action21 = QtGui.QAction(QtGui.QIcon(":/ico4/font.png"), "Fonts", self.toolBar)
        self.toolBar.Action21.setStatusTip("Fonts")
        self.toolBar.Action21.setShortcut("Ctrl+F")
        self.toolBar.Action21.triggered.connect(self.font_choice)
        #web baby
        self.toolBar.Action11 = QtGui.QAction(QtGui.QIcon(":/ico/web.png"),"Hex-rays Homepage",self.toolBar)
        self.toolBar.Action11.setStatusTip("Home of Hex-rays")
        self.toolBar.Action11.setShortcut("Ctrl+W")
        self.toolBar.Action11.triggered.connect(self.webopen)
        #irc
        self.toolBar.Action12 = QtGui.QAction(QtGui.QIcon(":/ico3/settings.png"),"Open Ida Pro Python SDK",self.toolBar)
        self.toolBar.Action12.setStatusTip("Ida Pro Python SDK")
        self.toolBar.Action12.setShortcut("Ctrl+I")
        self.toolBar.Action12.triggered.connect(self.sdkopen)
        #github Python
        self.toolBar.Action14 = QtGui.QAction(QtGui.QIcon(":/ico/github.png"),"Open git python",self.toolBar)
        self.toolBar.Action14.setStatusTip("Open git python")
        self.toolBar.Action14.setShortcut("Ctrl+G")
        self.toolBar.Action14.triggered.connect(self.gitopen)
        #auther me :)
        self.toolBar.Action15 = QtGui.QAction(QtGui.QIcon(":/ico/auth.png"),"Author",self.toolBar)
        self.toolBar.Action15.setStatusTip("Author")
        self.toolBar.Action15.setShortcut("Ctrl+B")
        self.toolBar.Action15.triggered.connect(self.Author)
        #toggle off code regonision
        self.toolBar.Action16 = QtGui.QAction(QtGui.QIcon(":/ico2/pythonminus.png"),"Disable Code recognition",self.toolBar)
        self.toolBar.Action16.setStatusTip("Disable Code recognition")
        self.toolBar.Action16.setShortcut("Alt+D")
        self.toolBar.Action16.triggered.connect(self.Diablecode)
        #toogle on
        self.toolBar.Action17 = QtGui.QAction(QtGui.QIcon(":/ico2/pypluss.png"),"Enable Code recognition",self.toolBar)
        self.toolBar.Action17.setStatusTip("Enable Code recognition")
        self.toolBar.Action17.setShortcut("Alt+E")
        self.toolBar.Action17.triggered.connect(self.Reiablecode)
        # zoom in
        self.toolBar.Action18 = QtGui.QAction(QtGui.QIcon(":/ico3/in.png"),"Zoom In",self.toolBar)
        self.toolBar.Action18.setStatusTip("Zoom In")
        self.toolBar.Action18.setShortcut("CTRL+SHIFT++")
        self.toolBar.Action18.triggered.connect(self.udder)
        #zoom out
        self.toolBar.Action19 = QtGui.QAction(QtGui.QIcon(":/ico3/out.png"),"Zoom Out",self.toolBar)
        self.toolBar.Action19.setStatusTip("Zoom Out")
        self.toolBar.Action19.setShortcut("CTRL+SHIFT+-")
        self.toolBar.Action19.triggered.connect(self.odder)

        self.toolBar.Action20 = QtGui.QAction(QtGui.QIcon(":/ico3/10.png"),"Profile Code",self.toolBar)
        self.toolBar.Action20.setStatusTip("Profile Code")
        self.toolBar.Action20.setShortcut("CTRL+SHIFT+E")
        self.toolBar.Action20.triggered.connect(self.runtoprob)

        #actions
        self.toolBar.addAction(self.toolBar.newAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.secondAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action7)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action9)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action10)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action21)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action11)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action12)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action14)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action15)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action16)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action17)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action18)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action19)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action20)

        #font
        self.skrift = QFont()
        self.skrift.setFamily('Consolas')
        self.skrift.setFixedPitch(True)
        self.skrift.setPointSize(12)
        self.codebox.setFont(self.skrift)

        #python style
        self.lexer = QsciLexerPython(self.codebox)
        self.lexer.setFont(self.skrift)
        self.lexer.setEolFill(True)
        #api test not working
        api = Qsci.QsciAPIs(self.lexer)
        API_FILE = dn+'\\Python.api'
        API_FILE2 = dn+'\\idc.api'
        API_FILE3 = dn+'\\idaapi.api'
        api.load(API_FILE)
        api.load(API_FILE2)
        api.load(API_FILE3)

        api.prepare()
        self.codebox.setAutoCompletionThreshold(0)
        self.codebox.setAutoCompletionThreshold(6)
        self.codebox.setAutoCompletionThreshold(8)
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        self.lexer.setDefaultFont(self.skrift)
        self.codebox.setLexer(self.lexer)
        self.codebox.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')

        #line numbers
        fontmetrics = QFontMetrics(self.skrift)
        self.codebox.setMarginsFont(self.skrift)
        self.codebox.setMarginWidth(0, fontmetrics.width("0000") + 6)
        self.codebox.setTabWidth(4)

        #brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        #auto line tab =4
        self.codebox.setAutoIndent(True)

        #scroolbar
        self.codebox.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lbl = self.codebox
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ida Pro Python Script Editor", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))


    def udder(self):
        self.codebox.zoomIn()

    def odder(self):
        self.codebox.zoomOut()

    def newfile(self):
        self.codebox.clear()

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(
                   self.vindu, 'Open File', self.path, "Python Files (*.py *.pyc *.pyw)",
                   '')

        if self.filename:
            with open(self.filename,"r") as self.file:
                self.codebox.setText(self.file.read())
        os.chdir(str(self.path))



    def fontFamily(self,font):
        self.text.setCurrentFont(font)

    def fontSize(self, fontsize):
            self.text.setFontPointSize(int(fontsize))


    def fontFamily(self,font):
        self.codebox.text.setCurrentFont(font)

    def fontSize(self, fontsize):
        self.codebox.text.setFontPointSize(int(fontsize))

    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        self.filename = QtGui.QFileDialog.getSaveFileName(
            self.vindu, "Save as", self.path, "Python Files (*.py *.pyc *.pyw)",
            )
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.codebox.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtGui.QMessageBox.information(self.vindu, "Unable to open file",
                    file.errorString())
        os.chdir(str(self.path))

    def runto(self):
        try:
            self.path = QtCore.QFileInfo(self.filename).path()
        except AttributeError:
            pass
        g = globals()
        os.chdir(str(self.path))
        os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
        script = str(self.codebox.text())
        try:
            exec (script, g)
            QtGui.QCloseEvent()


        except ImportError:
            os.chdir(str(self.path))
            os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
            sys.path.append(str(self.path))
            exec (script, g)
            QtGui.QCloseEvent()

            if TypeError (QTextStream):
                g = globals()
                os.chdir(str(self.path))
                os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
                sys.path.insert(0, str(self.path))
                exec int(script)
                QtGui.QCloseEvent()

    def runtoprob(self):
        try:
            self.path = QtCore.QFileInfo(self.filename).path()
        except AttributeError:
            pass
        self.path = QtCore.QFileInfo(self.filename).path()
        g = globals()
        os.chdir(str(self.path))
        script = str(self.codebox.text())
        import cProfile
        cProfile.run(script)


    def Diablecode(self):
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsNone)

    def Reiablecode(self):
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)

    def nofoldingl(self):
        self.codebox.setFolding(QsciScintilla.NoFoldStyle)

    def Circledfold(self):
        self.codebox.setFolding(QsciScintilla.CircledTreeFoldStyle)

    def plainfold(self):
        self.codebox.setFolding(QsciScintilla.PlainFoldStyle)

    def webopen(self):
        import webbrowser
        webbrowser.open('https://www.hex-rays.com/')

    def sdkopen(self):
        import webbrowser
        webbrowser.open('https://www.hex-rays.com/products/ida/support/idapython_docs/')

    def gitopen(self):
        import webbrowser
        webbrowser.open('https://github.com/idapython/src/tree/build-1.7.2')

    def Author(self):
        import webbrowser
        webbrowser.open('https://github.com/techbliss')


    def closeEvent(self, event):
        print("event")
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def font_choice(self):
        self.lbl = self.lexer
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.codebox.markersAtLine(nline) != 0:
            self.codebox.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.codebox.markerAdd(nline, self.ARROW_MARKER_NUM)


from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    #app = QtGui.QApplication.instance() # We add this so we can use editor outside Ida
    #if not app:
      #  app = QtGui.QApplication([])
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.resize(1000, 600)
    #if app.exec_():
        #os.chdir(dn)