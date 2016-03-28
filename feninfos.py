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
from gui.ui_infos import Ui_About


class About(QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    feninfos = About()
    feninfos.show()
    sys.exit(app.exec_())