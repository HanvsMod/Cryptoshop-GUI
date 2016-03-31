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
from gui.ui_selectkey import Ui_Selectkey
import gnupg


class Fenselectkey(QDialog):
    def __init__(self, parent=None):

        super(Fenselectkey, self).__init__(parent)
        self.ui = Ui_Selectkey()
        self.ui.setupUi(self)
        self.ui.editKey.hide()
        self.remplirliste()
        self.ui.checkSymetric.toggled.connect(self.switchmode)

    def switchmode(self):
        if self.ui.checkSymetric.isChecked():
            self.ui.comboBox.hide()
            self.ui.label.setText("Don't forget this key !!!")
            self.ui.editKey.show()

        else:
            self.ui.label.setText('Only recipient can decrypt :')
            self.ui.editKey.hide()
            self.ui.comboBox.show()

    def remplirliste(self):
        global uid_string
        gpg = gnupg.GPG(use_agent=False)
        keylist = gpg.list_keys()

        uid_strings = []
        uid_string2key = {}

        for key in keylist:
            for uid_string in key['uids']:
                uid_strings.append(uid_string)
                uid_string2key[uid_string] = key

            self.ui.comboBox.addItems([uid_string])

    def annuler(self):
        self.hide()
        print("annuler")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    fen = Fenselectkey()
    fen.show()
    sys.exit(app.exec_())
