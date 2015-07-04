# Created by: Storm Shadow http://www.techbliss.org

# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui, Qsci
from PyQt4.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs, QsciScintillaBase
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
        vindu.setStyleSheet(_fromUtf8("QWidget { \n"
"    background-color: #c0c0c0;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 0px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}"))
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
        lexer = QsciLexerPython()
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

        #brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.codebox.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        #try to load api
        api = Qsci.QsciAPIs(lexer)

        api.load('idaapi.py')
        api.prepare()
        self.codebox.setAutoCompletionThreshold(1)
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        self.codebox.setLexer(lexer)

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
        exec str(self.codebox.text())


    def openfile(self, path=None):
        if not path:
            path = QtGui.QFileDialog.getOpenFileName(self.impbtr, "Import",
                    '', "Python Files (*.py *.pyc)")

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
                    '', "Python Files (*.py *.pyc)")
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

