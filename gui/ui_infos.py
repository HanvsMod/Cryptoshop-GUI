# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infos.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(636, 346)
        self.verticalLayout = QtWidgets.QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(About)
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tabWidget = QtWidgets.QTabWidget(About)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setSource(QtCore.QUrl("file:///home/antidote/PycharmProjects/Cryptoshop/gui/infos.html"))
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setSource(QtCore.QUrl("file:///home/antidote/PycharmProjects/Cryptoshop/gui/infos_gnupg.html"))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setSource(QtCore.QUrl("file:///home/antidote/PycharmProjects/Cryptoshop/gui/infos_botan.html"))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_3.addWidget(self.textBrowser_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setSource(QtCore.QUrl("file:///home/antidote/PycharmProjects/Cryptoshop/gui/infos_pyqt.html"))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_4.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(About.accept)
        self.buttonBox.rejected.connect(About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Cryptoshop"))
        self.title_label.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#550000;\">Cryptoshop 1.0</span></p></body></html>"))
        self.label_2.setText(_translate("About", "Python/Qt GUI for GPG and crypto tools"))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; color:#e23033;\">Copyrights (C) 2016 @ CORRAIRE Fabrice<br /></span><a href=\"http://www.testgffg.com/\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#000000;\">Contact: </span></a><a href=\"mailto:antidote1911@gmail.com\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">antidote1911@gmail.com</span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0057ae;\"><br /><br /></span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; color:#000000;\">Cryptoshop is a little cryptographic tool written in Python 3 and PyQt5 for the gui. It can encrypt, sign, generate assymetric key pairs etc... with GnuPG. GnuPG command line tool need to be installed. On Windows system, you can install Gpg4win.<br /><br /></span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; text-decoration: underline; color:#000000;\">ENCRYPTION<br /><br /></span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; color:#000000;\">Cryptoshop can encrypt files in various strong cryptographics formats. Serpent 256, AES 256, and ThreeFish 512. Serpent and ThreeFish use mode GCM and EAX. Authentification is included in this recents modes.<br />AES use the mode CTR-BE. There is no authentification in this mode. Cryptoshop use an HMAC SHA-256 for authentication. This is one of the best method.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; color:#000000;\">Cryptoshop is fast. It use the very good C++ crypto library Botan.</span><a href=\"mailto:antidote1911@gmail.com\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\"><br /><br /></span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; text-decoration: underline; color:#000000;\">NOTE ON SECURITY<br /><br /></span><a href=\"mailto:antidote1911@gmail.com\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; color:#000000;\">Cryptography is not magic... No need the secret key to decrypt your files If a keylogger or trojans run secretly on your computer !<br />PROTECT YOUR OS FIRST.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("About", "Cryptoshop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("About", "GnuPG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("About", "Botan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("About", "PyQt"))

