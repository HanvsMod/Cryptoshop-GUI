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

from PyQt5.QtWidgets import (QApplication, QDialog)
from gui.ui_symetrickey import Ui_FenKey
from PyQt5.QtWidgets import QMessageBox


class Fenselectkey(QDialog):
    def __init__(self, parent=None):

        super(Fenselectkey, self).__init__(parent)
        self.ui = Ui_FenKey()
        self.ui.setupUi(self)
        self.ui.ButtonOK.clicked.connect(self.checkkey)

    def checkkey(self):
        key1 = self.ui.EditPass.text()
        key2 = self.ui.EditConfirm.text()
        if key1 == key2 and key1 != "":
            print("pass match")
            self.accept()
        else:
            QMessageBox.warning(self, "Invalid Passphrase",
                                "Make sure your passphrase and confirmation are equal please...", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    fen = Fenselectkey()
    fen.show()
    sys.exit(app.exec_())
