# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectkey.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Selectkey(object):
    def setupUi(self, Selectkey):
        Selectkey.setObjectName("Selectkey")
        Selectkey.setWindowModality(QtCore.Qt.WindowModal)
        Selectkey.resize(441, 155)
        self.verticalLayout = QtWidgets.QVBoxLayout(Selectkey)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Selectkey)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Selectkey)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.editKey = QtWidgets.QLineEdit(Selectkey)
        self.editKey.setEnabled(True)
        self.editKey.setFrame(True)
        self.editKey.setAlignment(QtCore.Qt.AlignCenter)
        self.editKey.setProperty("clearButtonEnabled", False)
        self.editKey.setObjectName("editKey")
        self.verticalLayout.addWidget(self.editKey)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Selectkey)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkSymetric = QtWidgets.QCheckBox(self.frame)
        self.checkSymetric.setObjectName("checkSymetric")
        self.horizontalLayout.addWidget(self.checkSymetric)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(self.frame)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Selectkey)
        self.okButton.clicked.connect(Selectkey.accept)
        self.cancelButton.clicked.connect(Selectkey.reject)
        QtCore.QMetaObject.connectSlotsByName(Selectkey)

    def retranslateUi(self, Selectkey):
        _translate = QtCore.QCoreApplication.translate
        Selectkey.setWindowTitle(_translate("Selectkey", "Select key"))
        self.label.setText(_translate("Selectkey", "Select recipient"))
        self.editKey.setText(_translate("Selectkey", "Enter Passphrase"))
        self.checkSymetric.setText(_translate("Selectkey", "Symetric encryption"))
        self.cancelButton.setText(_translate("Selectkey", "Cancel"))
        self.okButton.setText(_translate("Selectkey", "Ok"))

