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
from gui.ui_generating import Ui_Working


class Working(QDialog):
    def __init__(self, parent=None):
        super(Working, self).__init__(parent)
        self.ui = Ui_Working()

        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    fenworking = Working()
    fenworking.show()
    sys.exit(app.exec_())