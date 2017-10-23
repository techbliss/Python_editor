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

try:
    TemplateFile = idaapi.idadir("plugins\\Code editor\\template\\Plugin_temp")
except NameError:
    TemplateFile = os.getcwd()+r'\\template\\Plugin_temp'

sys.path.insert(0, dn)
sys.path.insert(0, os.getcwd()+r'\\icons')

sys.path.insert(0, os.getcwd()+r'\\template')


import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtGui import QFont, QFontMetrics, QColor
from PyQt5.QtWidgets import QDialog, QMessageBox, QWizard, QWizardPage
from PyQt5.QtCore import QCoreApplication

plugin_path = ""
if sys.platform == "win32":
    if hasattr(sys, "frozen"):
        plugin_path = os.path.join(os.path.dirname(os.path.abspath(sys.executable)), "PyQt5", "plugins")
        QCoreApplication.addLibraryPath(plugin_path)
    else:
        import site
        for dir in site.getsitepackages():
            QCoreApplication.addLibraryPath(os.path.join(dir, "PyQt5", "plugins"))

elif sys.platform == "darwin":
    plugin_path = os.path.join(QCoreApplication.getInstallPrefix(), "Resources", "plugins")

if plugin_path:
    QCoreApplication.addLibraryPath(plugin_path)


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
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
    import icon4
except ImportError:
    pass

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text,
                disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_messageformForm(QtWidgets.QWidget):
    def setupUi1(self, messageformForm):
        messageformForm.setObjectName("messageformForm")
        messageformForm.resize(404, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageformForm.sizePolicy().hasHeightForWidth())
        messageformForm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        messageformForm.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/twa.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        messageformForm.setWindowIcon(icon2)
        self.label = QtWidgets.QLabel(messageformForm)
        self.label.setGeometry(QtCore.QRect(40, 20, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(messageformForm)
        QtCore.QMetaObject.connectSlotsByName(messageformForm)

    def retranslateUi(self, messageformForm):
        _translate = QtCore.QCoreApplication.translate
        messageformForm.setWindowTitle(_translate("messageformForm", "Soon to be fixed"))
        self.label.setText(_translate("messageformForm", "Soon to be fixed"
))

class Ui_Wizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(Ui_Wizard, self).__init__(parent=None)
        Wizard.setObjectName("Wizard")
        Wizard.resize(762, 500)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        Wizard.setFont(font)
        Wizard.setOptions(QtWidgets.QWizard.HelpButtonOnRight)
        self.wizardPage1 = QtWidgets.QWizardPage()
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.wizardPage1.setFont(font)
        self.wizardPage1.setObjectName("wizardPage1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.wizardPage1)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 140, 421, 131))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        Wizard.addPage(self.wizardPage1)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setTitle("")
        self.wizardPage.setSubTitle("")
        self.wizardPage.setObjectName("wizardPage")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.wizardPage)
        self.textBrowser_4.setGeometry(QtCore.QRect(130, 140, 499, 239))
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        Wizard.addPage(self.wizardPage)
        self.tempwizardPage = QtWidgets.QWizardPage()
        self.tempwizardPage.setObjectName("tempwizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tempwizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TemptextEdit = Qsci.QsciScintilla(self.tempwizardPage)
        self.TemptextEdit.setToolTip("")
        self.TemptextEdit.setWhatsThis("")
        self.TemptextEdit.setObjectName("TemptextEdit")
        self.verticalLayout.addWidget(self.TemptextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.temppushButtonopen = QtWidgets.QPushButton(self.tempwizardPage)
        self.temppushButtonopen.setObjectName("temppushButtonopen")
        self.horizontalLayout.addWidget(self.temppushButtonopen)
        self.temppushButtonsave = QtWidgets.QPushButton(self.tempwizardPage)
        self.temppushButtonsave.setObjectName("temppushButtonsave")
        self.horizontalLayout.addWidget(self.temppushButtonsave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Wizard.addPage(self.tempwizardPage)
        self.scriptwizardPage = QtWidgets.QWizardPage()
        self.scriptwizardPage.setObjectName("scriptwizardPage")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.scriptwizardPage)
        self.textBrowser_5.setGeometry(QtCore.QRect(120, 130, 499, 239))
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        Wizard.addPage(self.scriptwizardPage)
        self.wizardPage_3 = QtWidgets.QWizardPage()
        self.wizardPage_3.setObjectName("wizardPage_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.script_textEdit = Qsci.QsciScintilla(self.wizardPage_3)
        self.script_textEdit.setToolTip("")
        self.script_textEdit.setWhatsThis("")
        self.script_textEdit.setObjectName("script_textEdit")
        self.verticalLayout_2.addWidget(self.script_textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.scriptGrabpushButton = QtWidgets.QPushButton(self.wizardPage_3)
        self.scriptGrabpushButton.setObjectName("scriptGrabpushButton")
        self.horizontalLayout_2.addWidget(self.scriptGrabpushButton)
        self.scriptpushButtonopen = QtWidgets.QPushButton(self.wizardPage_3)
        self.scriptpushButtonopen.setObjectName("scriptpushButtonopen")
        self.horizontalLayout_2.addWidget(self.scriptpushButtonopen)
        self.scriptpushButtonsave = QtWidgets.QPushButton(self.wizardPage_3)
        self.scriptpushButtonsave.setObjectName("scriptpushButtonsave")
        self.horizontalLayout_2.addWidget(self.scriptpushButtonsave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        Wizard.addPage(self.wizardPage_3)
        self.wizardPage_2 = QtWidgets.QWizardPage()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.wizardPage_2.setFont(font)
        self.wizardPage_2.setObjectName("wizardPage_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.wizardPage_2)
        self.textBrowser_6.setGeometry(QtCore.QRect(170, 140, 411, 191))
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        Wizard.addPage(self.wizardPage_2)
        #font textedit
        self.skrift = QFont()
        self.skrift.setFamily('Consolas')
        self.skrift.setFixedPitch(True)
        self.skrift.setPointSize(11)
        self.TemptextEdit.setFont(self.skrift)
        self.script_textEdit.setFont(self.skrift)

        #python style temp
        self.lexer = QsciLexerPython(self.TemptextEdit)
        self.lexer.setFont(self.skrift)
        self.lexer.setEolFill(True)
        #Python style scritps
        self.lexer = QsciLexerPython(self.script_textEdit)
        self.lexer.setFont(self.skrift)
        self.lexer.setEolFill(True)
        self.filename = ""
        #python style temp
        self.TemptextEdit.setAutoCompletionThreshold(0)
        self.TemptextEdit.setAutoCompletionThreshold(6)
        self.TemptextEdit.setAutoCompletionThreshold(8)
        self.TemptextEdit.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
#        self.TemptextEdit.setDefaultFont(self.skrift)
        self.TemptextEdit.setLexer(self.lexer)
        self.TemptextEdit.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')
        #python style script
        self.script_textEdit.setAutoCompletionThreshold(0)
        self.script_textEdit.setAutoCompletionThreshold(6)
        self.script_textEdit.setAutoCompletionThreshold(8)
        self.script_textEdit.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
#        self.script_textEdit.setDefaultFont(self.skrift)
        self.script_textEdit.setLexer(self.lexer)
        self.script_textEdit.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')

        #line numbers temp
        fontmetrics = QFontMetrics(self.skrift)
        self.TemptextEdit.setMarginsFont(self.skrift)
        self.TemptextEdit.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.TemptextEdit.setTabWidth(4)
        #line numbers script
        fontmetrics = QFontMetrics(self.skrift)
        self.script_textEdit.setMarginsFont(self.skrift)
        self.script_textEdit.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.script_textEdit.setTabWidth(4)

        #brace temp
        self.TemptextEdit.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        #brace script
        self.script_textEdit.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        #auto line tab =4 temp
        self.TemptextEdit.setAutoIndent(True)
        #auto line tab =4 script
        self.TemptextEdit.setAutoIndent(True)

        #scroolbar
        self.script_textEdit.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 1)
        try:
            bs = open(TemplateFile).read()
            bba = QtCore.QByteArray(bs)
            self.bts = QtCore.QTextStream(bba)
            self.bheysa = self.bts.readAll()
            self.TemptextEdit.setText(self.bheysa)
            self.TemptextEdit.setMarkerBackgroundColor((QColor(66, 66, 255)))
            marker = self.TemptextEdit.markerDefine(PyQt5.Qsci.QsciScintilla.Rectangle, 2)

            self.TemptextEdit.markerAdd(7, 2)
            self.TemptextEdit.markerAdd(11, 2)
            self.TemptextEdit.markerAdd(12, 2)
            self.TemptextEdit.markerAdd(13, 2)
            self.TemptextEdit.markerAdd(14, 2)
            self.TemptextEdit.markerAdd(15, 2)
            self.TemptextEdit.markerAdd(19, 2)
            self.TemptextEdit.markerAdd(27, 2)
            self.TemptextEdit.markerAdd(34, 2)
            self.TemptextEdit.markerAdd(35, 2)
            self.TemptextEdit.markerAdd(40, 2)
            self.TemptextEdit.markerAdd(41, 2)
            self.TemptextEdit.markerAdd(42, 2)
            self.TemptextEdit.markerAdd(43, 2)
            self.TemptextEdit.markerAdd(44, 2)
            self.TemptextEdit.markerAdd(45, 2)

            self.TemptextEdit.markerAdd(48, 2)
            self.TemptextEdit.markerAdd(50, 2)
            self.TemptextEdit.markerAdd(51, 2)
            self.TemptextEdit.markerAdd(52, 2)
            self.TemptextEdit.markerAdd(53, 2)
            self.TemptextEdit.markerAdd(54, 2)
            self.TemptextEdit.markerAdd(55, 2)

            self.TemptextEdit.markerAdd(62, 2)
            self.TemptextEdit.markerAdd(63, 2)
            self.TemptextEdit.markerAdd(64, 2)

            self.TemptextEdit.markerAdd(67, 2)
            self.TemptextEdit.markerAdd(89, 2)

            self.TemptextEdit.markerAdd(97, 2)
            self.TemptextEdit.markerAdd(98, 2)
            self.TemptextEdit.markerAdd(99, 2)
            self.TemptextEdit.markerAdd(102, 2)





        except:
            self.TemptextEdit.setText('Plugin_temp file not found')
            pass


        self.retranslateUi2(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi2(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "           Ida Pro Plugin Wizard"))
        self.textBrowser_2.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri Light\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the plugin wizard.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please follow the steps in the wizard, to tranform your code, to a full Ida Pro plugin.</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri Light\'; font-size:8.14286pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">First we create the plugin loader</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Then we change the higlightet text in the template, and then save the plugin loader in Ida Pro Plugins folder.</span></p></body></html>"))
        self.temppushButtonopen.setText(_translate("Wizard", "Open"))
        self.temppushButtonsave.setText(_translate("Wizard", "Save"))
        self.textBrowser_5.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri Light\'; font-size:8.14286pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Now we grab the editors current script, or open a new script.<br />Remember to save this in the right folder.<br />Plugins\\My_plugin_folder as declared in the template.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.scriptGrabpushButton.setText(_translate("Wizard", "Grab from Editor"))
        self.scriptpushButtonopen.setText(_translate("Wizard", "Open"))
        self.scriptpushButtonsave.setText(_translate("Wizard", "Save"))
        self.textBrowser_6.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri Light\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Loader Template should now be in <br />ida pro\\plugin<br />script should be in a subfolder<br />ida pro\\plugin\\Myplugin\\</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If above are correct your good to go!</p></body></html>"))

        self.temppushButtonopen.clicked.connect(self.opentemp)
        self.temppushButtonsave.clicked.connect(self.savetemp)
        self.scriptpushButtonopen.clicked.connect(self.openscript)
        self.scriptpushButtonsave.clicked.connect(self.savescript)
        self.scriptGrabpushButton.clicked.connect(self.grapper)

    def grapper(self):
        #hellotext = Ui_MainWindow
      #  hello2= hellotext.sendgrapped
#   print str(hello2)

        messageformForm.show()


    def opentemp(self):
        print "hello"
        self.path = QtCore.QFileInfo(self.filename).path()

        # Get filename and show only .writer files
        (self.filename, _) = \
            QtWidgets.QFileDialog.getOpenFileName(self.wizardPage_3,
                'Open File', self.path,
                'Python Files (*.py *.pyc *.pyw)', '')

        if self.filename:
            with open(self.filename, 'r') as self.file:
                self.TemptextEdit.setText(self.file.read())
        os.chdir(str(self.path))


    def savetemp(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        (self.filename, _) = \
            QtWidgets.QFileDialog.getSaveFileName(self, 'Save as'
                , self.path, 'Python Files (*.py *.pyc *.pyw)')
        if self.filename:
            self.savetexttemp(self.filename)
        os.chdir(str(self.path))

    def savetexttemp(self, fileName):
        textout = self.TemptextEdit.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtWidgets.QMessageBox.information(self.tempwizardPage,
                    'Unable to open file', file.errorString())
        os.chdir(str(self.path))

    def openscript(self):
        print "hello"
        self.path = QtCore.QFileInfo(self.filename).path()

        # Get filename and show only .writer files
        (self.filename, _) = \
            QtWidgets.QFileDialog.getOpenFileName(self.wizardPage_3,
                'Open File', self.path,
                'Python Files (*.py *.pyc *.pyw)', '')

        if self.filename:
            with open(self.filename, 'r') as self.file:
                self.script_textEdit.setText(self.file.read())
        os.chdir(str(self.path))


    def savescript(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        (self.filename, _) = \
            QtWidgets.QFileDialog.getSaveFileName(self.wizardPage_3, 'Save as'
                , self.path, 'Python Files (*.py *.pyc *.pyw)')
        if self.filename:
            self.savetextscript(self.filename)
        os.chdir(str(self.path))

    def savetextscript(self, fileName):
        textout = self.script_textEdit.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtWidgets.QMessageBox.information(self.wizardPage_3,
                    'Unable to open file', file.errorString())
        os.chdir(str(self.path))



from PyQt5 import Qsci

import sys
#app2 = QtWidgets.QApplication(sys.argv)






class Ui_MainWindow(QtWidgets.QMainWindow):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent=None)
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.vindu = QtWidgets.QWidget(MainWindow)
        self.vindu.setStyleSheet(_fromUtf8('notusedasyet'))
        #MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.vindu.setObjectName(_fromUtf8("vindu"))
        self.verticalLayout = PyQt5.QtWidgets.QVBoxLayout(self.vindu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8('verticalLayout'))
        self.codebox = Qsci.QsciScintilla(self.vindu)
        self.codebox.setToolTip(_fromUtf8(""))
        self.codebox.setWhatsThis(_fromUtf8(""))
        self.codebox.setAutoFillBackground(False)
        self.codebox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.codebox.setObjectName(_fromUtf8("codebox"))
        self.verticalLayout.addWidget(self.codebox)
        MainWindow.setCentralWidget(self.vindu)
        #toolbar
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar2"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar.addSeparator()
        #toolbar2 debugger
        #self.toolBar2 = QtGui.QToolBar(MainWindow)
        #self.toolBar2.setAutoFillBackground(False)
        #self.toolBar2.setIconSize(QtCore.QSize(32, 32))
        #self.toolBar2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        #self.toolBar2.setObjectName(_fromUtf8("toolBar"))
       # MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar2)
#        self.toolBar2.addSeparator()
        #getting ready for debugger
        self.codebox.setMarginSensitivity(1, True)
        self.codebox.marginClicked.connect(self.on_margin_clicked)
        self.codebox.markerDefine(QsciScintilla.FullRectangle, self.ARROW_MARKER_NUM)
        self.codebox.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        #first action Newfile
        self.toolBar.newAction = QtWidgets.QAction(QtGui.QIcon(":/ico/new.png"),"New",self.toolBar)
        self.toolBar.newAction.setStatusTip("Clear TextBox or make new document.")
        self.toolBar.newAction.setShortcut("Ctrl+N")
        self.toolBar.newAction.triggered.connect(self.newfile)
        #second Action OpenFile
        self.toolBar.secondAction = QtWidgets.QAction(QtGui.QIcon(":/ico/open.png"),"Open",self.toolBar)
        self.toolBar.secondAction.setStatusTip("Create a new document from scratch.")
        self.toolBar.secondAction.setShortcut("Ctrl+O")
        self.toolBar.secondAction.triggered.connect(self.open)
        # action 3 save file
        self.toolBar.Action3 = QtWidgets.QAction(QtGui.QIcon(":/ico/save.png"),"Save",self.toolBar)
        self.toolBar.Action3.setStatusTip("Save Your File.")
        self.toolBar.Action3.setShortcut("Ctrl+S")
        self.toolBar.Action3.triggered.connect(self.savefile)
        #action 4 run file
        self.toolBar.Action4 = QtWidgets.QAction(QtGui.QIcon(":/ico/run32.png"),"Run",self.toolBar)
        self.toolBar.Action4.setStatusTip("Run")
        self.toolBar.Action4.setShortcut("Ctrl+E")
        self.toolBar.Action4.triggered.connect(self.runto)
        #action 21 debug
        #self.toolBar2.Action21 = QtGui.QAction(QtGui.QIcon(":/ico/run32.png"),"Debug",self.toolBar)
        #self.toolBar2.Action21.setStatusTip("Debug File.")
        #self.toolBar2.Action21.setShortcut("Ctrl+7")
        #self.toolBar2.Action21.triggered.connect(self.debugto)
        #action 6 undo
        self.toolBar.Action6 =  QtWidgets.QAction(QtGui.QIcon(":/ico/undo.png"),"Redo",self.toolBar)
        self.toolBar.Action6.setStatusTip("Undo.")
        self.toolBar.Action6.setShortcut("Ctrl+Z")
        self.toolBar.Action6.triggered.connect(self.codebox.undo)
        #action 7 redo
        self.toolBar.Action7 = QtWidgets.QAction(QtGui.QIcon(":/ico/redo.png"),"Redo",self.toolBar)
        self.toolBar.Action7.setStatusTip("Redo.")
        self.toolBar.Action7.setShortcut("Ctrl+Y")
        self.toolBar.Action7.triggered.connect(self.codebox.redo)
        #action8 rerset Folding
        self.toolBar.Action8 = QtWidgets.QAction(QtGui.QIcon(":/ico/align-justify.png"),"Reset Folding",self.toolBar)
        self.toolBar.Action8.setStatusTip("Reset Folding.")
        self.toolBar.Action8.setShortcut("Ctrl+R")
        self.toolBar.Action8.triggered.connect(self.nofoldingl)
        #actions9 CircledTreeFoldStyle
        self.toolBar.Action9 = QtWidgets.QAction(QtGui.QIcon(":/ico/bullet.png"),"Circled Tree Folding",self.toolBar)
        self.toolBar.Action9.setStatusTip("Circled Tree Folding.")
        self.toolBar.Action9.setShortcut("Ctrl+C")
        self.toolBar.Action9.triggered.connect(self.Circledfold)
        #actions10 plainFoldStyle
        self.toolBar.Action10 = QtWidgets.QAction(QtGui.QIcon(":/ico/number.png"),"Plain Folding",self.toolBar)
        self.toolBar.Action10.setStatusTip("Plain Folding")
        self.toolBar.Action10.setShortcut("Ctrl+P")
        self.toolBar.Action10.triggered.connect(self.plainfold)
        # fonts
        self.toolBar.Action21 = QtWidgets.QAction(QtGui.QIcon(":/ico4/font.png"), "Fonts", self.toolBar)
        self.toolBar.Action21.setStatusTip("Fonts")
        self.toolBar.Action21.setShortcut("Ctrl+F")
        self.toolBar.Action21.triggered.connect(self.font_choice)
        #web baby
        self.toolBar.Action11 = QtWidgets.QAction(QtGui.QIcon(":/ico/web.png"),"Hex-rays Homepage",self.toolBar)
        self.toolBar.Action11.setStatusTip("Home of Hex-rays")
        self.toolBar.Action11.setShortcut("Ctrl+W")
        self.toolBar.Action11.triggered.connect(self.webopen)
        #irc
        self.toolBar.Action12 = QtWidgets.QAction(QtGui.QIcon(":/ico3/settings.png"),"Open Ida Pro Python SDK",self.toolBar)
        self.toolBar.Action12.setStatusTip("Ida Pro Python SDK")
        self.toolBar.Action12.setShortcut("Ctrl+I")
        self.toolBar.Action12.triggered.connect(self.sdkopen)
        #github Python
        self.toolBar.Action14 = QtWidgets.QAction(QtGui.QIcon(":/ico/github.png"),"Open git python",self.toolBar)
        self.toolBar.Action14.setStatusTip("Open git python")
        self.toolBar.Action14.setShortcut("Ctrl+G")
        self.toolBar.Action14.triggered.connect(self.gitopen)
        #auther me :)
        self.toolBar.Action15 = QtWidgets.QAction(QtGui.QIcon(":/ico/auth.png"),"Author",self.toolBar)
        self.toolBar.Action15.setStatusTip("Author")
        self.toolBar.Action15.setShortcut("Ctrl+B")
        self.toolBar.Action15.triggered.connect(self.Author)
        #toggle off code regonision
        self.toolBar.Action16 = QtWidgets.QAction(QtGui.QIcon(":/ico2/pythonminus.png"),"Disable Code recognition",self.toolBar)
        self.toolBar.Action16.setStatusTip("Disable Code recognition")
        self.toolBar.Action16.setShortcut("Alt+D")
        self.toolBar.Action16.triggered.connect(self.Diablecode)
        #toogle on
        self.toolBar.Action17 = QtWidgets.QAction(QtGui.QIcon(":/ico2/pypluss.png"),"Enable Code recognition",self.toolBar)
        self.toolBar.Action17.setStatusTip("Enable Code recognition")
        self.toolBar.Action17.setShortcut("Alt+E")
        self.toolBar.Action17.triggered.connect(self.Reiablecode)
        # zoom in
        self.toolBar.Action18 = QtWidgets.QAction(QtGui.QIcon(":/ico3/in.png"),"Zoom In",self.toolBar)
        self.toolBar.Action18.setStatusTip("Zoom In")
        self.toolBar.Action18.setShortcut("CTRL+SHIFT++")
        self.toolBar.Action18.triggered.connect(self.udder)
        #zoom out
        self.toolBar.Action19 = QtWidgets.QAction(QtGui.QIcon(":/ico3/out.png"),"Zoom Out",self.toolBar)
        self.toolBar.Action19.setStatusTip("Zoom Out")
        self.toolBar.Action19.setShortcut("CTRL+SHIFT+-")
        self.toolBar.Action19.triggered.connect(self.odder)

        self.toolBar.Action20 = QtWidgets.QAction(QtGui.QIcon(":/ico3/10.png"),"Profile Code",self.toolBar)
        self.toolBar.Action20.setStatusTip("Profile Code")
        self.toolBar.Action20.setShortcut("CTRL+SHIFT+E")
        self.toolBar.Action20.triggered.connect(self.runtoprob)
        #PLUGINS HERE WE GO
        self.toolBar.Action22 = QtWidgets.QAction(QtGui.QIcon(":/ico5/plugin.png"),"Plugin",self.toolBar)
        self.toolBar.Action22.setStatusTip("Make plugin")
        self.toolBar.Action22.setShortcut("")
        self.toolBar.Action22.triggered.connect(self.plugin_make)
        self.scriptfile = self.codebox.text()
        self.filename = ""


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
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action21)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action22)

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
        self.codebox.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.codebox.setTabWidth(4)

        #brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        #auto line tab =4
        self.codebox.setAutoIndent(True)

        #scroolbar
        self.codebox.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 1)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ida Pro Python Script Editor", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))



    def plugin_make(self):

        Wizard.show()

    def sendgrapped(self):
        print "hello"
        helloclass = Ui_Wizard()
        self.bsout = self.codebox.text()
        helloclass.script_textEdit.setText(self.bsout)




    def hubba(self):
        print "sdfgsdgsgdghsghdg"
        #print str(self.codebox.text())


    def udder(self):
        self.codebox.zoomIn()

    def odder(self):
        self.codebox.zoomOut()

    def newfile(self):
        self.codebox.clear()

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()

        # Get filename and show only .writer files
        (self.filename, _) = \
            QtWidgets.QFileDialog.getOpenFileName(self.vindu,
                'Open File', self.path,
                'Python Files (*.py *.pyc *.pyw)', '')

        if self.filename:
            with open(self.filename, 'r') as self.file:
                self.codebox.setText(self.file.read())
        os.chdir(str(self.path))


    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        (self.filename, _) = \
            QtWidgets.QFileDialog.getSaveFileName(self.vindu, 'Save as'
                , self.path, 'Python Files (*.py *.pyc *.pyw)')
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.codebox.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtWidgets.QMessageBox.information(self.vindu,
                    'Unable to open file', file.errorString())
        os.chdir(str(self.path))

    def runto(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        g = globals()
        os.chdir(str(self.path))
        script = str(self.codebox.text())
        try:
            os.chdir(str(self.path))
            os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
            sys.path.insert(0, str(self.path))
            exec (script, g)
        except Exception as e:
            print e.__doc__
            print e.message
        else:
            pass
            #exec (script, g)

    def runtoprob(self):
        try:
            self.path = QtCore.QFileInfo(self.filename).path()
            self.path = QtCore.QFileInfo(self.filename).path()
            g = globals()
            os.chdir(str(self.path))
            script = str(self.codebox.text())
            import cProfile
            cProfile.run(script)
        except Exception as e:
            print e.__doc__
            print e.message
        else:
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

    def font_choice(self):
        self.lbl = self.lexer
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.codebox.markersAtLine(nline) != 0:
            self.codebox.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.codebox.markerAdd(nline, self.ARROW_MARKER_NUM)







class MyWindow(QtWidgets.QMainWindow):
    '''
    we have to ask user for quiting so we can change back to root dir
    '''

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
#            print dn
            os.chdir(dn)
 #           print dn
            #os.chdir('../..')
  #          print dn
            print '''
###################################################
#              Author Storm Shadow                #
#                                                 #
#              Follow me on twitter               #
#                  @zadow28                       #
###################################################
#              Ida pro  python Editor             #
###################################################
'''
            event.accept()
            os.chdir(dn)
        else:
            event.ignore()
            os.chdir(dn)



from PyQt5 import Qsci


if __name__ == '__main__':
    import sys

    Wizard = QtWidgets.QWizard()
    #Wizard = QtWidgets.QWizard()
    #app = QtWidgets.QApplication.instance() # enable for usage outside
    #if not app:  # enable for usage outside
    #    app = QtWidgets.QApplication([])  # enable for usage outside
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    messageformForm = QtWidgets.QWidget()
    ui2 = Ui_Wizard()
    ui3 = Ui_messageformForm()
    ui3.setupUi1(messageformForm)
    MainWindow.resize(1000, 600)
    MainWindow.show()
   # app.exec_()





