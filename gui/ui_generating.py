# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generating.ui'
#
# Created: Sat Mar 29 19:59:31 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Working(object):
    def setupUi(self, Working):
        Working.setObjectName("Working")
        Working.resize(511, 310)
        self.verticalLayout = QtWidgets.QVBoxLayout(Working)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Working)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)
        self.progressBar = QtWidgets.QProgressBar(Working)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Working)
        QtCore.QMetaObject.connectSlotsByName(Working)

    def retranslateUi(self, Working):
        _translate = QtCore.QCoreApplication.translate
        Working.setWindowTitle(_translate("Working", "Generating in progress"))
        self.label.setText(_translate("Working", "TextLabel"))
        self.label_2.setText(_translate("Working", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Generating key...</span></p><p align=\"center\">The key generation can take some time. Your computer must have enought<br/>entropy to generate very long random numbers.<br/><br/>Please be patient...</p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Working = QtWidgets.QDialog()
    ui = Ui_Working()
    ui.setupUi(Working)
    Working.show()
    sys.exit(app.exec_())

