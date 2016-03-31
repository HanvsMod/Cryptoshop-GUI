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

from PyQt5 import QtCore
import gnupg
from PyQt5.QtCore import pyqtSignal


class Worker(QtCore.QThread):
    renderedImage = pyqtSignal(str)
    isstarted = pyqtSignal(str)

    def __init__(self, filename, m_key, encryordecry, lname, sym):
        QtCore.QThread.__init__(self)
        self.filename = filename
        self.m_key = m_key
        self.encryordecry = encryordecry
        self.lname = lname
        self.sym = sym

    def run(self):
        self.isstarted.emit("True")
        if self.encryordecry is True and self.sym is True:
            gpg = gnupg.GPG(use_agent=False)
            gpg.encrypt_file(open(self.filename, "rb"), False, passphrase=self.m_key, symmetric='AES256', armor=True,
                             output=self.filename + ".gpg")
            self.isstarted.emit("False")
            return
        if self.encryordecry is True and self.sym is False:
            gpg = gnupg.GPG(use_agent=False)
            gpg.encrypt_file(open(self.filename, "rb"), self.m_key['fingerprint'], always_trust=True,
                                              output=self.filename + ".gpg")
            self.isstarted.emit("False")
            return

        else:

            gpg = gnupg.GPG(use_agent=False)
            status = gpg.decrypt_file(open(self.filename, "rb"), False, passphrase=self.m_key, output=self.lname)
            if status.ok is False:
                self.renderedImage.emit("False")
            else:
                self.renderedImage.emit("True")

            self.isstarted.emit("False")
