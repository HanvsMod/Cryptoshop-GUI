# coding=utf-8

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
