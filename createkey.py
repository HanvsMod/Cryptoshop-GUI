#!/usr/bin/env python3
# -*-coding:Utf-8 -*

# Cryptoshop- gpg gui
# Copyright(C) 2016 CORRAIRE Fabrice. antidote1911@gmail.com

# ############################################################################
# #This file is part of Cryptoshop.
# #
##    Cryptoshop is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    Cryptoshop is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Cryptoshop.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox)
from gui.ui_createkey import Ui_Createkey
from PyQt5.QtCore import (QThread)
from generating import Working

import gnupg


class Createkey(QDialog):
    def __init__(self, parent=None):
        super(Createkey, self).__init__(parent)
        self.ui = Ui_Createkey()
        self.ui.setupUi(self)

        self.ui.pushCancel.clicked.connect(self.closefen)
        self.ui.pushGenerate.clicked.connect(self.generatekey)
        self.ui.checkExpire.toggled.connect(self.activatedatecombo)

    def activatedatecombo(self):
        if self.ui.checkExpire.isChecked():
            self.ui.dateEdit.setEnabled(False)

        else:
            self.ui.dateEdit.setEnabled(True)

    def closefen(self):
        self.close()

    def generatekey(self):
        name = self.ui.lineName.text()
        email = self.ui.lineEmail.text()
        comment = self.ui.lineComment.text()
        passphrase = self.ui.linePassphrase.text()
        keylength = int(self.ui.comboLength.currentText())
        keytype = self.ui.comboAlgo.currentText()
        subkeytype = self.ui.comboAlgo2.currentText()
        subkeylength = self.ui.comboLength2.currentText()
        expiredate = (self.ui.dateEdit.date().toPyDate())
        print(expiredate)
        if self.ui.checkExpire.isChecked():
            expiredate = 0
        else:
            expiredate = (self.ui.dateEdit.date().toPyDate())

        if name == "":
            QMessageBox.warning(self, 'Pas de nom spécifié',
                                '''Vous devez entrer un nom pour générer une paire de clés.''',
                                QMessageBox.Ok)
            return

        if email == "":
            QMessageBox.warning(self, 'Pas de email spécifié',
                                '''Vous devez entrer une adresse email pour générer une paire de clés.''',
                                QMessageBox.Ok)
            return
        if passphrase == "":
            QMessageBox.warning(self, ''
                                      'Entrez une passprase',
                                '''Pour des raisons de sécurité, les paires de clés sans passphrase ne sont pas autorisés.
                                 Merci d'entrer une passprase secréte.''',
                                QMessageBox.Ok)
            return

        gpg = gnupg.GPG()

        global key_settings
        key_settings = gpg.gen_key_input(key_type=keytype, key_length=keylength, name_real=name, name_email=email,
                                         name_comment=comment, passphrase=passphrase, expire_date=expiredate,
                                         subkey_type=subkeytype,
                                         subkey_length=subkeylength)
        input = gpg.gen_key_input()
        test = \
            Generate(self)
        test.start(QThread.LowPriority)
        global threadgenerate
        threadgenerate = Working(self)
        threadgenerate.exec()

        QMessageBox.warning(self, 'Paire de clés générées avec succès !',
                            '''Maintenant, vous pouvez utiliser votre paire de clés pour signer, chiffrer, déchiffrer..,''',
                            QMessageBox.Ok)

        self.closefen()
        QApplication.processEvents()

        print(input)


class Generate(QThread):
    def __init__(self, parent=None):
        super(Generate, self).__init__(parent)

    @staticmethod
    def run():
        gpg = gnupg.GPG()
        gpg.gen_key(key_settings)
        threadgenerate.close()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    fencreatekey = Createkey()
    fencreatekey.show()
    sys.exit(app.exec_())