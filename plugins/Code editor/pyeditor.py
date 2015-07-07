# Created by: Storm Shadow http://www.techbliss.org

# WARNING! All changes made in this file will be lost!

import sys
import os

from PyQt4 import QtCore, QtGui, Qsci
from PyQt4.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs, QsciScintillaBase
from PyQt4.QtGui import QFont, QFontMetrics, QColor




#try to add system varibles YEEE!
os.path.join(os.sep, 'PATH', 'LIB', 'INLCUDE')
os.path.join(os.path.expanduser('~'), os.path.expandvars('%IDADIR%'))
os.path.join(os.path.expanduser('~'), os.path.expandvars('%Path%'))
os.path.join(os.path.expanduser('~'), os.path.expandvars('%INCLUDE%'))

os.path.dirname(os.path.abspath(__file__))
os.environ.get("PATH")
os.path.join(os.environ["PATH"])
os.environ.get("LIB")
os.path.join(os.environ["LIB"])
os.environ.get("INCLUDE")
os.path.join(os.environ["INCLUDE"])

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

class Ui_vindu(object):
    def setupUi(self, vindu):
        self.codebox = Qsci.QsciScintilla(vindu)
        vindu.setObjectName(_fromUtf8("vindu"))
        vindu.resize(1093, 734)
        self.codebox = Qsci.QsciScintilla(vindu)
        self.codebox.setGeometry(QtCore.QRect(-1, -1, 1101, 661))
        self.codebox.setToolTip(_fromUtf8(""))
        self.codebox.setWhatsThis(_fromUtf8(""))
        self.codebox.setObjectName(_fromUtf8("codebox"))
        self.curFile = ''

        #font
        skrift = QFont()
        skrift.setFamily('Consolas')
        skrift.setFixedPitch(True)
        skrift.setPointSize(12)
        self.codebox.setFont(skrift)

        self.runbtr = QtGui.QPushButton(vindu)
        self.runbtr.setGeometry(QtCore.QRect(790, 680, 94, 34))
        self.runbtr.setObjectName(_fromUtf8("runbtr"))
        self.impbtr = QtGui.QPushButton(vindu)
        self.impbtr.setGeometry(QtCore.QRect(890, 680, 94, 34))
        self.impbtr.setObjectName(_fromUtf8("impbtr"))
        self.exbtr = QtGui.QPushButton(vindu)
        self.exbtr.setGeometry(QtCore.QRect(990, 680, 94, 34))
        self.exbtr.setObjectName(_fromUtf8("exbtr"))

        #python style
        lexer = QsciLexerPython(self.codebox)

        #api
        '''
        ida crash when using the api's
        maybe bug with ida pro
        for now use it outside ida.
        if any have good idea how to load so it wont crash please say so.
        #hack to add right folder.
        import sys
        import os
        #idahome = idaapi.idadir("plugins\\Code editor\\")
        #sys.path.append('/idahome')
        #API
        #os.path.dirname( os.path.realpath( __file__ ) )
        #API_DIR = idaapi.idadir("plugins\\Code editor")
        '''
        #api Working so far
        api = Qsci.QsciAPIs(lexer)
        API_FILE = r'idc.api'
        API_FILE2 = r'idaapi.api'
        API_FILE3 = r'python.api'
        api.load(API_FILE)
        api.load(API_FILE2)
        api.load(API_FILE3)
        api.prepare()
        self.codebox.setAutoCompletionThreshold(1)
        self.codebox.setAutoCompletionThreshold(6)
        self.codebox.setAutoCompletionThreshold(8)
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        self.codebox.setLexer(lexer)
        lexer.setDefaultFont(skrift)
        self.codebox.setLexer(lexer)
        self.codebox.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')

        #line numbers
        fontmetrics = QFontMetrics(skrift)
        self.codebox.setMarginsFont(skrift)
        self.codebox.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.codebox.setTabWidth(4)
        #self.codebox.setWhitespaceVisibility(True)
        #self.codebox.setWhitespaceSize(40)
        #self.codebox.setWhitespaceBackgroundColor(QColor(255, 0, 0, 127))
        self.codebox.setMarginLineNumbers(0, True)
        self.codebox.setMarginsBackgroundColor(QColor("#cccccc"))

        #auto line tab when code is right
        '''
        def bob():
        1234print "bob"
         '''
        self.codebox.setAutoIndent(True)

        #brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.codebox.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        #try to load api
        self.retranslateUi(vindu)
        QtCore.QObject.connect(self.runbtr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.codebox.selectAll)
        QtCore.QMetaObject.connectSlotsByName(vindu)

    def retranslateUi(self, vindu):
        vindu.setWindowTitle(_translate("vindu", "Python Editor", None))
        self.runbtr.setToolTip(_translate("vindu", "<html><head/><body><p>Run to interpreter</p></body></html>", None))
        self.runbtr.setText(_translate("vindu", "Run", None))
        self.impbtr.setToolTip(_translate("vindu", "<html><head/><body><p>Import script into editor.</p></body></html>", None))
        self.impbtr.setText(_translate("vindu", "Import", None))
        self.exbtr.setToolTip(_translate("vindu", "<html><head/><body><p>Save your file.</p></body></html>", None))
        self.exbtr.setText(_translate("vindu", "Export", None))
        self.runbtr.clicked.connect(self.runto)
        self.impbtr.clicked.connect(self.openfile)
        self.exbtr.clicked.connect(self.saveFile)
        self.curFile = ''

    def runto(self):
        g = globals()
        exec str(self.codebox.text())


    def openfile(self, path=None):
        if not path:
            path = QtGui.QFileDialog.getOpenFileName(self.impbtr, "Open File",
                    '', "Python Files (*.py *.pyc *pyw)")

        if path:
            inFile = QtCore.QFile(path)
            if inFile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                text = inFile.readAll()

                try:
                    # Python v3.
                    text = str(text, encoding='ascii')
                except TypeError:
                    # Python v2.
                    text = str(text)

                self.codebox.setText(text)

    def saveFile(self, fileName):
        fileName = QtGui.QFileDialog.getSaveFileName(self.exbtr, "Save as",
                    '', "Python Files (*.py *.pyc *.pyw)")
        if fileName:
            self.savetext(fileName)


    def savetext(self, fileName):
        textout = self.codebox.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtGui.QMessageBox.information(self.exbtr, "Unable to open file",
                    file.errorString())

from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    vindu = QtGui.QWidget()
    ui = Ui_vindu()
    ui.setupUi(vindu)
    vindu.show()
    #ui.codebox.setText(open(sys.argv[0]).read())
    app.exec_()

