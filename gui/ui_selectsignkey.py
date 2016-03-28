# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectsignkey.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Selectsignkey(object):
    def setupUi(self, Selectsignkey):
        Selectsignkey.setObjectName("Selectsignkey")
        Selectsignkey.setWindowModality(QtCore.Qt.WindowModal)
        Selectsignkey.resize(389, 166)
        self.verticalLayout = QtWidgets.QVBoxLayout(Selectsignkey)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Selectsignkey)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Selectsignkey)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(Selectsignkey)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editKey = QtWidgets.QLineEdit(Selectsignkey)
        self.editKey.setEnabled(True)
        self.editKey.setText("")
        self.editKey.setFrame(True)
        self.editKey.setAlignment(QtCore.Qt.AlignCenter)
        self.editKey.setProperty("clearButtonEnabled", False)
        self.editKey.setObjectName("editKey")
        self.verticalLayout.addWidget(self.editKey)
        self.frame = QtWidgets.QFrame(Selectsignkey)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(self.frame)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Selectsignkey)
        self.okButton.clicked.connect(Selectsignkey.accept)
        self.cancelButton.clicked.connect(Selectsignkey.reject)
        QtCore.QMetaObject.connectSlotsByName(Selectsignkey)

    def retranslateUi(self, Selectsignkey):
        _translate = QtCore.QCoreApplication.translate
        Selectsignkey.setWindowTitle(_translate("Selectsignkey", "Sélectionnez clé privée"))
        self.label.setText(_translate("Selectsignkey", "Select a privates key:"))
        self.label_2.setText(_translate("Selectsignkey", "Enter passphrase for this key:"))
        self.cancelButton.setText(_translate("Selectsignkey", "Cancel"))
        self.okButton.setText(_translate("Selectsignkey", "Ok"))

