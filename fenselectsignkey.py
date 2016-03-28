#!/usr/bin/env python
# -*-coding:Utf-8 -*

# QPyCrypto- gpg gui
# Copyright(C) 2014 CORRAIRE Fabrice. antidote1911@gmail.com

#############################################################################
##This file is part of QPyCrypto.
##
##    QPyCrypto is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    QPyCrypto is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with QPyCrypto.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

from PyQt5.QtWidgets import (QApplication, QDialog)
from gui.ui_selectsignkey import Ui_Selectsignkey
import gnupg


class Fenselectsignkey(QDialog):
    def __init__(self, parent=None):

        super(Fenselectsignkey, self).__init__(parent)
        self.ui = Ui_Selectsignkey()
        self.ui.setupUi(self)
        self.remplirliste()

    def remplirliste(self):
        global uid_string
        gpg = gnupg.GPG(use_agent=False)
        keylist = gpg.list_keys(True)

        uid_strings = []
        uid_string2key = {}

        for key in keylist:
            for uid_string in key['uids']:
                uid_strings.append(uid_string)
                uid_string2key[uid_string] = key

            self.ui.comboBox.addItems([uid_string])

    def annuler(self):
        self.hide()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    fen = Fenselectsignkey()
    fen.show()
    sys.exit(app.exec_())
