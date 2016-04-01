# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principale.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushDecrypt = QtWidgets.QPushButton(self.frame)
        self.pushDecrypt.setObjectName("pushDecrypt")
        self.gridLayout.addWidget(self.pushDecrypt, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushEncrypt = QtWidgets.QPushButton(self.frame)
        self.pushEncrypt.setObjectName("pushEncrypt")
        self.gridLayout.addWidget(self.pushEncrypt, 1, 3, 1, 1)
        self.pushSign = QtWidgets.QPushButton(self.frame)
        self.pushSign.setObjectName("pushSign")
        self.gridLayout.addWidget(self.pushSign, 1, 0, 1, 1)
        self.pushVerify = QtWidgets.QPushButton(self.frame)
        self.pushVerify.setObjectName("pushVerify")
        self.gridLayout.addWidget(self.pushVerify, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 23))
        self.menubar.setObjectName("menubar")
        self.menuInfos = QtWidgets.QMenu(self.menubar)
        self.menuInfos.setObjectName("menuInfos")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuTampon = QtWidgets.QMenu(self.menubar)
        self.menuTampon.setObjectName("menuTampon")
        self.menuToolbar = QtWidgets.QMenu(self.menubar)
        self.menuToolbar.setObjectName("menuToolbar")
        self.menuEnigma = QtWidgets.QMenu(self.menubar)
        self.menuEnigma.setObjectName("menuEnigma")
        self.menuHash = QtWidgets.QMenu(self.menubar)
        self.menuHash.setObjectName("menuHash")
        self.menuSHA_3 = QtWidgets.QMenu(self.menuHash)
        self.menuSHA_3.setObjectName("menuSHA_3")
        self.menuSHA = QtWidgets.QMenu(self.menuHash)
        self.menuSHA.setObjectName("menuSHA")
        self.menuObsoletes = QtWidgets.QMenu(self.menuHash)
        self.menuObsoletes.setObjectName("menuObsoletes")
        self.menuChecksums = QtWidgets.QMenu(self.menuHash)
        self.menuChecksums.setObjectName("menuChecksums")
        MainWindow.setMenuBar(self.menubar)
        self.actionInfos_QPyCrypto = QtWidgets.QAction(MainWindow)
        self.actionInfos_QPyCrypto.setObjectName("actionInfos_QPyCrypto")
        self.actionInfos_Qt = QtWidgets.QAction(MainWindow)
        self.actionInfos_Qt.setObjectName("actionInfos_Qt")
        self.actionChiffrerfichier = QtWidgets.QAction(MainWindow)
        self.actionChiffrerfichier.setObjectName("actionChiffrerfichier")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setCheckable(False)
        self.actionQuitter.setChecked(False)
        self.actionQuitter.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuitter.setIcon(icon)
        self.actionQuitter.setStatusTip("")
        font = QtGui.QFont()
        self.actionQuitter.setFont(font)
        self.actionQuitter.setIconVisibleInMenu(True)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionDechiffrerfichier = QtWidgets.QAction(MainWindow)
        self.actionDechiffrerfichier.setObjectName("actionDechiffrerfichier")
        self.actionMD2 = QtWidgets.QAction(MainWindow)
        self.actionMD2.setObjectName("actionMD2")
        self.actionMD4 = QtWidgets.QAction(MainWindow)
        self.actionMD4.setObjectName("actionMD4")
        self.actionMD5 = QtWidgets.QAction(MainWindow)
        self.actionMD5.setObjectName("actionMD5")
        self.actionSHA224 = QtWidgets.QAction(MainWindow)
        self.actionSHA224.setObjectName("actionSHA224")
        self.actionSHA256 = QtWidgets.QAction(MainWindow)
        self.actionSHA256.setObjectName("actionSHA256")
        self.actionSHA384 = QtWidgets.QAction(MainWindow)
        self.actionSHA384.setObjectName("actionSHA384")
        self.actionSHA512 = QtWidgets.QAction(MainWindow)
        self.actionSHA512.setObjectName("actionSHA512")
        self.actionChiffrer_OpenPGP = QtWidgets.QAction(MainWindow)
        self.actionChiffrer_OpenPGP.setObjectName("actionChiffrer_OpenPGP")
        self.actionDechiffrer_OpenPGP = QtWidgets.QAction(MainWindow)
        self.actionDechiffrer_OpenPGP.setObjectName("actionDechiffrer_OpenPGP")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOuvrir.setIcon(icon1)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionSauver = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icones/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSauver.setIcon(icon2)
        self.actionSauver.setObjectName("actionSauver")
        self.actionVider_Tampon = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icones/empty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVider_Tampon.setIcon(icon3)
        self.actionVider_Tampon.setObjectName("actionVider_Tampon")
        self.actionCopier = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icones/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopier.setIcon(icon4)
        self.actionCopier.setObjectName("actionCopier")
        self.actionColler = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icones/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColler.setIcon(icon5)
        self.actionColler.setObjectName("actionColler")
        self.actionCacher = QtWidgets.QAction(MainWindow)
        self.actionCacher.setCheckable(True)
        self.actionCacher.setObjectName("actionCacher")
        self.actionAbout_GNUPG = QtWidgets.QAction(MainWindow)
        self.actionAbout_GNUPG.setObjectName("actionAbout_GNUPG")
        self.actionKeymanager = QtWidgets.QAction(MainWindow)
        self.actionKeymanager.setObjectName("actionKeymanager")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icones/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon6)
        self.actionCut.setObjectName("actionCut")
        self.actionShow_text_icons = QtWidgets.QAction(MainWindow)
        self.actionShow_text_icons.setCheckable(True)
        self.actionShow_text_icons.setObjectName("actionShow_text_icons")
        self.actionChiffrer_un_fichier_Enigma = QtWidgets.QAction(MainWindow)
        self.actionChiffrer_un_fichier_Enigma.setObjectName("actionChiffrer_un_fichier_Enigma")
        self.actionD_chiffrer_un_fichier_Enigma = QtWidgets.QAction(MainWindow)
        self.actionD_chiffrer_un_fichier_Enigma.setObjectName("actionD_chiffrer_un_fichier_Enigma")
        self.actionImporter_une_cl_e = QtWidgets.QAction(MainWindow)
        self.actionImporter_une_cl_e.setObjectName("actionImporter_une_cl_e")
        self.actionSigner_un_fichier = QtWidgets.QAction(MainWindow)
        self.actionSigner_un_fichier.setObjectName("actionSigner_un_fichier")
        self.actionVerifier_signature = QtWidgets.QAction(MainWindow)
        self.actionVerifier_signature.setObjectName("actionVerifier_signature")
        self.actionChiffrer_un_fichier_Enigma_Test = QtWidgets.QAction(MainWindow)
        self.actionChiffrer_un_fichier_Enigma_Test.setObjectName("actionChiffrer_un_fichier_Enigma_Test")
        self.actionD_chiffrer_un_fichier_Enigma_Test = QtWidgets.QAction(MainWindow)
        self.actionD_chiffrer_un_fichier_Enigma_Test.setObjectName("actionD_chiffrer_un_fichier_Enigma_Test")
        self.actionSHA_3_winner_Keccak_1600 = QtWidgets.QAction(MainWindow)
        self.actionSHA_3_winner_Keccak_1600.setObjectName("actionSHA_3_winner_Keccak_1600")
        self.actionSHA_3_candidate_Skein_512 = QtWidgets.QAction(MainWindow)
        self.actionSHA_3_candidate_Skein_512.setObjectName("actionSHA_3_candidate_Skein_512")
        self.actionMD5_2 = QtWidgets.QAction(MainWindow)
        self.actionMD5_2.setObjectName("actionMD5_2")
        self.actionAdler32 = QtWidgets.QAction(MainWindow)
        self.actionAdler32.setObjectName("actionAdler32")
        self.actionCRC24 = QtWidgets.QAction(MainWindow)
        self.actionCRC24.setObjectName("actionCRC24")
        self.actionCRC32 = QtWidgets.QAction(MainWindow)
        self.actionCRC32.setObjectName("actionCRC32")
        self.actionCBC_MAC = QtWidgets.QAction(MainWindow)
        self.actionCBC_MAC.setObjectName("actionCBC_MAC")
        self.actionX9_19_DES_MAC = QtWidgets.QAction(MainWindow)
        self.actionX9_19_DES_MAC.setObjectName("actionX9_19_DES_MAC")
        self.actionHAS_160 = QtWidgets.QAction(MainWindow)
        self.actionHAS_160.setObjectName("actionHAS_160")
        self.actionRIPEMD_128 = QtWidgets.QAction(MainWindow)
        self.actionRIPEMD_128.setObjectName("actionRIPEMD_128")
        self.actionRIPEMD_129 = QtWidgets.QAction(MainWindow)
        self.actionRIPEMD_129.setObjectName("actionRIPEMD_129")
        self.actionRIPEMD_160 = QtWidgets.QAction(MainWindow)
        self.actionRIPEMD_160.setObjectName("actionRIPEMD_160")
        self.actionSHA_1 = QtWidgets.QAction(MainWindow)
        self.actionSHA_1.setObjectName("actionSHA_1")
        self.actionTiger = QtWidgets.QAction(MainWindow)
        self.actionTiger.setObjectName("actionTiger")
        self.actionWhirlpool = QtWidgets.QAction(MainWindow)
        self.actionWhirlpool.setObjectName("actionWhirlpool")
        self.actionGOST_34_11 = QtWidgets.QAction(MainWindow)
        self.actionGOST_34_11.setObjectName("actionGOST_34_11")
        self.actionAbout_Botan = QtWidgets.QAction(MainWindow)
        self.actionAbout_Botan.setObjectName("actionAbout_Botan")
        self.toolBar.addAction(self.actionQuitter)
        self.toolBar.addAction(self.actionOuvrir)
        self.toolBar.addAction(self.actionSauver)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionVider_Tampon)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopier)
        self.toolBar.addAction(self.actionColler)
        self.toolBar.addSeparator()
        self.menuInfos.addAction(self.actionInfos_QPyCrypto)
        self.menuInfos.addAction(self.actionInfos_Qt)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionChiffrerfichier)
        self.menuFichier.addAction(self.actionDechiffrerfichier)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionSigner_un_fichier)
        self.menuFichier.addAction(self.actionVerifier_signature)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionKeymanager)
        self.menuTampon.addAction(self.actionOuvrir)
        self.menuTampon.addAction(self.actionSauver)
        self.menuTampon.addSeparator()
        self.menuTampon.addAction(self.actionCut)
        self.menuTampon.addAction(self.actionCopier)
        self.menuTampon.addAction(self.actionColler)
        self.menuTampon.addSeparator()
        self.menuTampon.addAction(self.actionVider_Tampon)
        self.menuTampon.addSeparator()
        self.menuTampon.addAction(self.actionChiffrer_OpenPGP)
        self.menuTampon.addAction(self.actionDechiffrer_OpenPGP)
        self.menuTampon.addSeparator()
        self.menuToolbar.addAction(self.actionCacher)
        self.menuToolbar.addAction(self.actionShow_text_icons)
        self.menuEnigma.addAction(self.actionChiffrer_un_fichier_Enigma)
        self.menuEnigma.addAction(self.actionD_chiffrer_un_fichier_Enigma)
        self.menuEnigma.addAction(self.actionQuitter)
        self.menuSHA_3.addAction(self.actionSHA_3_winner_Keccak_1600)
        self.menuSHA_3.addAction(self.actionSHA_3_candidate_Skein_512)
        self.menuSHA.addAction(self.actionSHA224)
        self.menuSHA.addAction(self.actionSHA256)
        self.menuSHA.addAction(self.actionSHA384)
        self.menuSHA.addAction(self.actionSHA512)
        self.menuObsoletes.addAction(self.actionMD5_2)
        self.menuObsoletes.addAction(self.actionMD4)
        self.menuObsoletes.addAction(self.actionMD2)
        self.menuObsoletes.addAction(self.actionRIPEMD_128)
        self.menuChecksums.addAction(self.actionAdler32)
        self.menuChecksums.addAction(self.actionCRC24)
        self.menuChecksums.addAction(self.actionCRC32)
        self.menuHash.addAction(self.actionSHA_1)
        self.menuHash.addAction(self.menuSHA.menuAction())
        self.menuHash.addAction(self.menuSHA_3.menuAction())
        self.menuHash.addAction(self.actionWhirlpool)
        self.menuHash.addAction(self.actionGOST_34_11)
        self.menuHash.addAction(self.actionTiger)
        self.menuHash.addAction(self.actionRIPEMD_160)
        self.menuHash.addAction(self.menuChecksums.menuAction())
        self.menuHash.addAction(self.menuObsoletes.menuAction())
        self.menubar.addAction(self.menuEnigma.menuAction())
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuHash.menuAction())
        self.menubar.addAction(self.menuTampon.menuAction())
        self.menubar.addAction(self.menuToolbar.menuAction())
        self.menubar.addAction(self.menuInfos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptoshop"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Welcome to Cryptoshop.\n"
""))
        self.pushDecrypt.setText(_translate("MainWindow", "Decrypt (GnuPG)"))
        self.pushEncrypt.setText(_translate("MainWindow", "Encrypt (GnuPG)"))
        self.pushSign.setText(_translate("MainWindow", "Sign (GnuPG)"))
        self.pushVerify.setText(_translate("MainWindow", "Verify (GnuPG)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuInfos.setTitle(_translate("MainWindow", "About"))
        self.menuFichier.setTitle(_translate("MainWindow", "GnuPG"))
        self.menuTampon.setTitle(_translate("MainWindow", "Editor"))
        self.menuToolbar.setTitle(_translate("MainWindow", "Toolbar"))
        self.menuEnigma.setTitle(_translate("MainWindow", "File"))
        self.menuHash.setTitle(_translate("MainWindow", "Hash"))
        self.menuSHA_3.setTitle(_translate("MainWindow", "SHA-3"))
        self.menuSHA.setTitle(_translate("MainWindow", "SHA-2"))
        self.menuObsoletes.setTitle(_translate("MainWindow", "Obsoletes"))
        self.menuChecksums.setTitle(_translate("MainWindow", "Checksums"))
        self.actionInfos_QPyCrypto.setText(_translate("MainWindow", "About Cryptoshop"))
        self.actionInfos_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionChiffrerfichier.setText(_translate("MainWindow", "Encrypt file (GnuPG)"))
        self.actionQuitter.setText(_translate("MainWindow", "Quit"))
        self.actionDechiffrerfichier.setText(_translate("MainWindow", "Decrypt file (GnuPG)"))
        self.actionMD2.setText(_translate("MainWindow", "MD2"))
        self.actionMD4.setText(_translate("MainWindow", "MD4"))
        self.actionMD5.setText(_translate("MainWindow", "MD5"))
        self.actionSHA224.setText(_translate("MainWindow", "SHA224"))
        self.actionSHA256.setText(_translate("MainWindow", "SHA256"))
        self.actionSHA384.setText(_translate("MainWindow", "SHA384"))
        self.actionSHA512.setText(_translate("MainWindow", "SHA512"))
        self.actionChiffrer_OpenPGP.setText(_translate("MainWindow", "Encrypt Editor (not implented)"))
        self.actionDechiffrer_OpenPGP.setText(_translate("MainWindow", "Decrypt Editor (not implanted)"))
        self.actionOuvrir.setText(_translate("MainWindow", "Open txt file"))
        self.actionSauver.setText(_translate("MainWindow", "Save"))
        self.actionVider_Tampon.setText(_translate("MainWindow", "Empty Editor"))
        self.actionCopier.setText(_translate("MainWindow", "Copy"))
        self.actionColler.setText(_translate("MainWindow", "Paste"))
        self.actionCacher.setText(_translate("MainWindow", "Hide buttons"))
        self.actionAbout_GNUPG.setText(_translate("MainWindow", "About GNUPG"))
        self.actionKeymanager.setText(_translate("MainWindow", "Key Manager"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionShow_text_icons.setText(_translate("MainWindow", "Show text"))
        self.actionChiffrer_un_fichier_Enigma.setText(_translate("MainWindow", "Encrypt File"))
        self.actionD_chiffrer_un_fichier_Enigma.setText(_translate("MainWindow", "Decrypt file"))
        self.actionImporter_une_cl_e.setText(_translate("MainWindow", "Importer une clée"))
        self.actionSigner_un_fichier.setText(_translate("MainWindow", "Sign file"))
        self.actionVerifier_signature.setText(_translate("MainWindow", "Verify"))
        self.actionChiffrer_un_fichier_Enigma_Test.setText(_translate("MainWindow", "Chiffrer un fichier (Enigma Test)"))
        self.actionD_chiffrer_un_fichier_Enigma_Test.setText(_translate("MainWindow", "Déchiffrer un fichier (Enigma Test)"))
        self.actionSHA_3_winner_Keccak_1600.setText(_translate("MainWindow", "SHA-3 winner Keccak-1600"))
        self.actionSHA_3_candidate_Skein_512.setText(_translate("MainWindow", "SHA-3 candidate Skein-512"))
        self.actionMD5_2.setText(_translate("MainWindow", "MD5"))
        self.actionAdler32.setText(_translate("MainWindow", "Adler32"))
        self.actionCRC24.setText(_translate("MainWindow", "CRC24"))
        self.actionCRC32.setText(_translate("MainWindow", "CRC32"))
        self.actionCBC_MAC.setText(_translate("MainWindow", "CBC-MAC"))
        self.actionX9_19_DES_MAC.setText(_translate("MainWindow", "X9.19 DES-MAC"))
        self.actionHAS_160.setText(_translate("MainWindow", "HAS-160"))
        self.actionRIPEMD_128.setText(_translate("MainWindow", "RIPEMD-128"))
        self.actionRIPEMD_129.setText(_translate("MainWindow", "RIPEMD-128"))
        self.actionRIPEMD_160.setText(_translate("MainWindow", "RIPEMD-160"))
        self.actionSHA_1.setText(_translate("MainWindow", "SHA-1"))
        self.actionTiger.setText(_translate("MainWindow", "Tiger"))
        self.actionWhirlpool.setText(_translate("MainWindow", "Whirlpool"))
        self.actionGOST_34_11.setText(_translate("MainWindow", "GOST 34.11"))
        self.actionAbout_Botan.setText(_translate("MainWindow", "About Botan"))

