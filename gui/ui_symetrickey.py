# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symetrickey.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FenKey(object):
    def setupUi(self, FenKey):
        FenKey.setObjectName("FenKey")
        FenKey.resize(626, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(FenKey)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(FenKey)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(FenKey)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.EditConfirm = QtWidgets.QLineEdit(self.frame)
        self.EditConfirm.setObjectName("EditConfirm")
        self.gridLayout.addWidget(self.EditConfirm, 4, 0, 1, 3)
        self.EditPass = QtWidgets.QLineEdit(self.frame)
        self.EditPass.setObjectName("EditPass")
        self.gridLayout.addWidget(self.EditPass, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(FenKey)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboAlgo = QtWidgets.QComboBox(self.frame_2)
        self.comboAlgo.setMinimumSize(QtCore.QSize(150, 0))
        self.comboAlgo.setObjectName("comboAlgo")
        self.comboAlgo.addItem("")
        self.comboAlgo.addItem("")
        self.comboAlgo.addItem("")
        self.horizontalLayout.addWidget(self.comboAlgo)
        self.checkDelete = QtWidgets.QCheckBox(self.frame_2)
        self.checkDelete.setObjectName("checkDelete")
        self.horizontalLayout.addWidget(self.checkDelete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ButtonCancel = QtWidgets.QPushButton(self.frame_2)
        self.ButtonCancel.setObjectName("ButtonCancel")
        self.horizontalLayout.addWidget(self.ButtonCancel)
        self.ButtonOK = QtWidgets.QPushButton(self.frame_2)
        self.ButtonOK.setObjectName("ButtonOK")
        self.horizontalLayout.addWidget(self.ButtonOK)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(FenKey)
        self.ButtonCancel.clicked.connect(FenKey.reject)
        QtCore.QMetaObject.connectSlotsByName(FenKey)

    def retranslateUi(self, FenKey):
        _translate = QtCore.QCoreApplication.translate
        FenKey.setWindowTitle(_translate("FenKey", "Enter secret key"))
        self.label_6.setText(_translate("FenKey", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">Do not forget your key !!! It is impossible to decrypt a file without the key</span></p></body></html>"))
        self.label.setText(_translate("FenKey", "Passphrase"))
        self.label_2.setText(_translate("FenKey", "Confirmation"))
        self.comboAlgo.setItemText(0, _translate("FenKey", "Serpent/GCM"))
        self.comboAlgo.setItemText(1, _translate("FenKey", "Threefish-512/EAX"))
        self.comboAlgo.setItemText(2, _translate("FenKey", "AES-256/CTR-BE"))
        self.checkDelete.setText(_translate("FenKey", "Delete original"))
        self.ButtonCancel.setText(_translate("FenKey", "Cancel"))
        self.ButtonOK.setText(_translate("FenKey", "Ok"))

