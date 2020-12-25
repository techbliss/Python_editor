# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginwizard.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(727, 582)
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
        self.TemptextEdit = Qsci.QsciScintilla(self.tempwizardPage)
        self.TemptextEdit.setGeometry(QtCore.QRect(-11, 9, 711, 391))
        self.TemptextEdit.setToolTip("")
        self.TemptextEdit.setWhatsThis("")
        self.TemptextEdit.setObjectName("TemptextEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tempwizardPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 410, 141, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temppushButtonopen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.temppushButtonopen.setObjectName("temppushButtonopen")
        self.horizontalLayout.addWidget(self.temppushButtonopen)
        self.temppushButtonsave = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.temppushButtonsave.setObjectName("temppushButtonsave")
        self.horizontalLayout.addWidget(self.temppushButtonsave)
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
        self.script_textEdit = Qsci.QsciScintilla(self.wizardPage_3)
        self.script_textEdit.setGeometry(QtCore.QRect(-7, -1, 711, 401))
        self.script_textEdit.setToolTip("")
        self.script_textEdit.setWhatsThis("")
        self.script_textEdit.setObjectName("script_textEdit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.wizardPage_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(480, 410, 221, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scriptGrabpushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.scriptGrabpushButton.setObjectName("scriptGrabpushButton")
        self.horizontalLayout_2.addWidget(self.scriptGrabpushButton)
        self.scriptpushButtonopen = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.scriptpushButtonopen.setObjectName("scriptpushButtonopen")
        self.horizontalLayout_2.addWidget(self.scriptpushButtonopen)
        self.scriptpushButtonsave = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.scriptpushButtonsave.setObjectName("scriptpushButtonsave")
        self.horizontalLayout_2.addWidget(self.scriptpushButtonsave)
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

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Ida Pro Plugin Wizard"))
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

from PyQt5 import Qsci

