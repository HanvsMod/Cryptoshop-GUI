#!/usr/bin/env python3
# -*-coding:Utf-8 -*

# Cryptoshop- gpg gui
# Copyright(C) 2016 CORRAIRE Fabrice. antidote1911@gmail.com

# ############################################################################
# This file is part of Cryptoshop.
#
#    Cryptoshop is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Cryptoshop is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Cryptoshop.  If not, see <http://www.gnu.org/licenses/>.
# ###########################################################################

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QLineEdit, QMessageBox, QInputDialog, \
    QProgressDialog
from PyQt5.QtCore import Qt, QFile, QTextStream
from gui.ui_principale import Ui_MainWindow
from fenselectkey import Fenselectkeygpg
from fenselectsignkey import Fenselectsignkey
from fensymetrickey import Fenselectkey
from feninfos import About
from keymanager import Fenmanager
import gnupg
import os
import Crypto_gpg
import simplehash
from py_cryptoshop import encryptfile
from py_cryptoshop import decryptfile

appname = " Cryptoshop "
version = " 1.0 "


def keymanager():
    dialog = Fenmanager()
    dialog.setWindowTitle(appname + version + " Key manager")
    dialog.exec()


def openabout():
    dialog = About()
    dialog.ui.title_label.setText(appname + version)
    dialog.setWindowTitle(appname + version + " About")
    dialog.exec()


global originalfile
global afterfile


class MasterForm(QMainWindow):
    def __init__(self, parent=None):
        super(MasterForm, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Encrypt/Decrypt button
        self.ui.pushEncrypt.clicked.connect(self.tamponencrypt)
        self.ui.pushDecrypt.clicked.connect(self.tampondecrypt)
        self.ui.pushSign.clicked.connect(self.tamponsign)
        self.ui.pushVerify.clicked.connect(self.tamponverify)

        # Menu connexions
        self.ui.actionCopier.triggered.connect(self.ui.plainTextEdit.copy)
        self.ui.actionColler.triggered.connect(self.ui.plainTextEdit.paste)
        self.ui.actionCut.triggered.connect(self.ui.plainTextEdit.cut)
        self.ui.actionCacher.triggered.connect(self.toolbarvisibility)
        self.ui.actionShow_text_icons.triggered.connect(self.texticonsvisibility)
        self.ui.actionKeymanager.triggered.connect(keymanager)
        self.ui.actionInfos_QPyCrypto.triggered.connect(openabout)
        self.ui.actionInfos_Qt.triggered.connect(self.aboutqt)
        self.ui.actionChiffrerfichier.triggered.connect(self.encryptfile)
        self.ui.actionDechiffrerfichier.triggered.connect(self.decryptfile)

        self.ui.actionChiffrer_un_fichier_Enigma.triggered.connect(self.encryptfileenigma)
        self.ui.actionD_chiffrer_un_fichier_Enigma.triggered.connect(self.decryptfileenigma)

        self.ui.actionSigner_un_fichier.triggered.connect(self.signfile)
        self.ui.actionVerifier_signature.triggered.connect(self.verifysignfile)

        self.ui.actionVider_Tampon.triggered.connect(self.vidertampon)
        self.ui.actionOuvrir.triggered.connect(self.ouvrirtexte)
        self.ui.actionSauver.triggered.connect(self.sauvertexte)
        self.ui.actionQuitter.triggered.connect(sys.exit)

        # Menu HASH File:
        self.ui.actionSHA512.triggered.connect(self.hashfilesha512)
        self.ui.actionSHA384.triggered.connect(self.hashfilesha384)
        self.ui.actionSHA256.triggered.connect(self.hashfilesha256)
        self.ui.actionSHA224.triggered.connect(self.hashfilesha224)
        self.ui.actionSHA_1.triggered.connect(self.hashfilesha)
        self.ui.actionMD5_2.triggered.connect(self.hashfilemd5)
        self.ui.actionMD2.triggered.connect(self.hashfilemd2)
        self.ui.actionMD4.triggered.connect(self.hashfilemd4)
        self.ui.actionRIPEMD_160.triggered.connect(self.hashfileripemd_160)
        self.ui.actionRIPEMD_128.triggered.connect(self.hashfileripemd_128)
        self.ui.actionWhirlpool.triggered.connect(self.hashfileWhirlpool)
        self.ui.actionTiger.triggered.connect(self.hashfileTiger)
        self.ui.actionAdler32.triggered.connect(self.hashfileAdler32)
        self.ui.actionCRC24.triggered.connect(self.hashfileCrc24)
        self.ui.actionCRC32.triggered.connect(self.hashfileCrc32)
        self.ui.actionSHA_3_winner_Keccak_1600.triggered.connect(self.hashfileKeccak_1600)
        self.ui.actionSHA_3_candidate_Skein_512.triggered.connect(self.hashfileSkein_512)
        self.ui.actionGOST_34_11.triggered.connect(self.hashfileGOST_34_11)

    def encryptfileenigma(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select the file to encrypt", "",
                                                  "All Files (*)")
        if filename:
            dialog = Fenselectkey(self)
            if dialog.exec_() == QDialog.Accepted:
                m_key = dialog.ui.EditPass.text()
                algorithm = dialog.ui.comboAlgo.currentText()
                if algorithm == "Serpent-256":
                    algo = "srp"
                if algorithm == "AES-256":
                    algo = "aes"
                if algorithm == "Twofish-256":
                    algo = "twf"

                result = encryptfile(filename, m_key, algo)
                if result["success"] == "successfully encrypted":
                    QMessageBox.information(self, "Successfully encrypted",
                                            "File: " + filename + " is encrypted with " + algorithm,
                                            QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "Encryption Error",
                                            "Encryption error: " + result["success"],
                                            QMessageBox.Ok)

                self.ui.statusbar.showMessage("File " + filename + " is encrypted.", 50000)
                return

    def decryptfileenigma(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select the file to decrypt", "",
                                                  "Cryptoshop Files (*.cryptoshop);;All Files (*)")

        if filename:
            m_key, ok = QInputDialog.getText(self, "Enter your passphrase",
                                             "Key:", QLineEdit.Normal)
            if ok and m_key != '':
                try:
                    result = decryptfile(filename, m_key)
                    if result["success"] == "successfully decrypted":
                        QMessageBox.information(self, "Successfully Decrypted",
                                                "File: " + filename + " encrypted with " + result[
                                                    "algorithm"] + " was successfully decrypted",
                                                QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self, "Decryption Error",
                                            "Decryption Error " + result["success"],
                                            QMessageBox.Ok)

                except Exception as e:
                    QMessageBox.warning(self, appname + version + "What that bug ??", (str(e)), QMessageBox.Ok)

    def signfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select a file to sign", "",
                                                  "All files (*)")
        if filename:
            gpg = gnupg.GPG(use_agent=False)
            gpg.encoding = 'utf-8'
            dialog = Fenselectsignkey(self)
            if dialog.exec_() == QDialog.Accepted:
                keyid = dialog.ui.comboBox.currentText()
                key = dialog.ui.editKey.text()
                with open(filename, 'rb') as data:
                    signed_data = gpg.sign_file(file=data, keyid=keyid, output=filename + ".sig", detach=True)
                    print(signed_data)
                    data.close()

    def verifysignfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select the sig file", "",
                                                  "sig Files (*.sig);;asc Files (*.asc);;All Files (*)")
        if filename:
            with open(filename, 'rb') as stream:
                gpg = gnupg.GPG(use_agent=False)
                gpg.encoding = 'utf-8'
                data = os.path.splitext(filename)[0].split("_")[-1]
                verified = gpg.verify_file(stream, data)
                stream.close()

            if verified.valid is True:
                QMessageBox.information(self, appname + version + "Good Signature",
                                        "Good signature from:  " + verified.username +
                                        "\n\nFingerprint:  " + verified.fingerprint +
                                        "\nKey Id:  " + verified.key_id +
                                        "\nThe signature was created at " + verified.creation_date + "\n\nTrust  :" + verified.trust_text,
                                        QMessageBox.Ok)
                return
            if verified.valid is False and verified.username is None:
                QMessageBox.warning(self, appname + version + "No signature found",
                                    "No signature found:  " + verified.stderr, QMessageBox.Ok)
                return
            else:
                QMessageBox.warning(self, appname + version + "Bad Signature",
                                    "Bad signature from:  " + verified.username +
                                    "\nKey Id:  " + verified.key_id + "\n\nTHE FILE IS CORRUPTED." + "\n\nDetails  :\n" + verified.stderr,
                                    QMessageBox.Ok)

    def tamponverify(self):
        texttoverify = self.ui.plainTextEdit.toPlainText()
        gpg = gnupg.GPG(use_agent=False)
        gpg.encoding = 'utf-8'
        verified_data = gpg.verify(texttoverify)
        if verified_data.valid is False and verified_data.status is None:
            QMessageBox.warning(self, "No valid signature",
                                "No valid signature.",
                                QMessageBox.Ok)
            return
        if verified_data.valid is False:
            QMessageBox.warning(self, appname + version + "Bad Signature",
                                "BAD SIGNATURE " + "\nDATA ARE CORRUPTED:\n\n" + "GnuPG Message: \n" + verified_data.stderr,
                                QMessageBox.Ok)
            return
        if verified_data.valid is True:
            QMessageBox.information(self, appname + version + "Good Signature",
                                    "Good signature from:  " + verified_data.username +
                                    "\nID " + verified_data.key_id + "\n\nFingerprint: \n"
                                    + verified_data.fingerprint + "\n\nGnuPG Message:\n" + verified_data.stderr,
                                    QMessageBox.Ok)
        else:
            QMessageBox.warning(self, appname + version + "Error",
                                " Error ",
                                QMessageBox.Ok)

    def updatePixmap(self, boll):
        if boll == "False":
            QMessageBox.warning(self, appname + version + "Error",
                                " Wrong passphrase " + self.originalfile,
                                QMessageBox.Ok)
            return
        else:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Cryptoshop-->The file " + self.originalfile + " is decrypted")
            self.ui.plainTextEdit.appendPlainText(str("----->>>") + self.afterfile)

    def tamponsign(self):
        texttosign = self.ui.plainTextEdit.toPlainText()
        gpg = gnupg.GPG(use_agent=False)
        dialog = Fenselectsignkey(self)
        if dialog.exec_() == QDialog.Accepted:
            key = dialog.ui.comboBox.currentText()
            signed_data = gpg.sign(texttosign, keyid=key)
            if str(signed_data) == "":
                QMessageBox.critical(self, appname + version + "Can't Sign...",
                                     '''The passphrase is invalid for unlock this key.''',
                                     QMessageBox.Ok)
                return
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText(str(signed_data))

    def toolbarvisibility(self):
        if self.ui.actionCacher.isChecked():
            self.ui.toolBar.hide()
        else:
            self.ui.toolBar.show()

    def texticonsvisibility(self):
        if self.ui.actionShow_text_icons.isChecked():
            self.ui.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        else:
            self.ui.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def hidetexticons(self):
        self.ui.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def encryptfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select file to encrypt", "",
                                                  "All (*)")

        if filename:

            dialog = Fenselectkeygpg(self)

            if dialog.exec_() == QDialog.Accepted:
                m_key = dialog.ui.editKey.text().strip()

                if dialog.ui.checkSymetric.isChecked():
                    if dialog.ui.editKey.text() == "":
                        QMessageBox.warning(self, appname + version + "Error...",
                                            '''You must type a passphrase.''',
                                            QMessageBox.Ok)
                        return
                    encryordecry = True
                    lname = "not used for encrypt"
                    sym = True
                    self.originalfile = filename

                    self.myLongTask = Crypto_gpg.Worker(filename, m_key, encryordecry, lname, sym)
                    self.myLongTask.renderedImage.connect(self.updatePixmap)
                    self.myLongTask.isstarted.connect(self.isstarted)

                    self.myLongTask.start()

                    QMessageBox.warning(self, appname + version + "The file is encrypted",
                                        filename + ".gpg",
                                        QMessageBox.Ok)

                else:
                    sym = False
                    item = dialog.ui.comboBox.currentText()
                    print(item)
                    gpg = gnupg.GPG(use_agent=False)
                    keylist = gpg.list_keys()

                    uid_strings = []
                    uid_string2key = {}
                    for key in keylist:
                        for uid_string in key['uids']:
                            uid_strings.append(uid_string)
                            uid_string2key[uid_string] = key
                    uid = item
                    m_key = uid_string2key[uid]
                    encryordecry = True
                    lname = "not used for encrypt"
                    sym = False
                    self.myLongTask = Crypto_gpg.Worker(filename, m_key, encryordecry, lname, sym)
                    self.myLongTask.renderedImage.connect(self.updatePixmap)
                    self.myLongTask.isstarted.connect(self.isstarted)

                    self.myLongTask.start()

                    self.ui.plainTextEdit.clear()
                    self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
                    self.ui.plainTextEdit.appendPlainText("Cryptoshop-->The file is encrypted.")
                    self.ui.plainTextEdit.appendPlainText(str(filename + ".gpg"))

    def aboutqt(self):
        QMessageBox.aboutQt(self, appname + version + "Qt is the best !")

    def tamponencrypt(self):
        dialog = Fenselectkeygpg(self)

        if dialog.exec_() == QDialog.Accepted:
            self.m_key = dialog.ui.editKey.text().strip()
            if dialog.ui.checkSymetric.isChecked():
                if dialog.ui.editKey.text() == "":
                    QMessageBox.warning(self, appname + version + "Error",
                                        '''You must type a passphrase.''',
                                        QMessageBox.Ok)
                    return

                gpg = gnupg.GPG(use_agent=False)
                plaintext = self.ui.plainTextEdit.toPlainText()
                crypted = gpg.encrypt(plaintext, False, passphrase=self.m_key, symmetric='AES256',
                                      armor=True)
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(str(crypted))

            else:
                item = dialog.ui.comboBox.currentText()
                print(item)
                gpg = gnupg.GPG()
                keylist = gpg.list_keys()

                uid_strings = []
                uid_string2key = {}

                for key in keylist:
                    for uid_string in key['uids']:
                        uid_strings.append(uid_string)
                        uid_string2key[uid_string] = key

                uid = item
                key = uid_string2key[uid]
                unencrypted_string = self.ui.plainTextEdit.toPlainText()
                encrypted_data = gpg.encrypt(unencrypted_string, key['fingerprint'], always_trust=True)
                encrypted_string = str(encrypted_data)
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(encrypted_string)

    def sauvertexte(self):
        filename, _ = QFileDialog.getSaveFileName(self)
        if filename:
            file = QFile(filename)
            if not file.open(QFile.WriteOnly | QFile.Text):
                QMessageBox.critical(self, appname + version + "Save",
                                     "Writing Error %s:\n%s." % (filename, file.errorString()))
                return
            outstr = QTextStream(file)
            outstr << self.ui.plainTextEdit.toPlainText()
            QMessageBox.information(self, appname + version + "Save file",
                                    "The file is saved. \n%s" % (file.fileName()))

    def ouvrirtexte(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        if filename:
            file = QFile(filename)
            if not file.open(QFile.ReadOnly | QFile.Text):
                QMessageBox.critical(self, appname + version + "Open File",
                                     "Reading Error %s:\n%s." % (filename, file.errorString()))
                return
            instr = QTextStream(file)
            self.ui.plainTextEdit.setPlainText(instr.readAll())

    def vidertampon(self):
        self.ui.plainTextEdit.clear()

    def tampondecrypt(self):
        encrypted_string = str(self.ui.plainTextEdit.toPlainText())
        gpg = gnupg.GPG(use_agent=False)

        decrypted_data = gpg.decrypt(encrypted_string)

        if decrypted_data.ok is True:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText(str(decrypted_data))
        else:
            QMessageBox.warning(self, appname + version + "Invalid passphrase",
                                ''' Invalid passphrase.''',
                                QMessageBox.Ok)
            return

    def hashfileripemd_160(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "RIPEMD-160: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'RIPEMD-160')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash RIPEMD-160 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileripemd_128(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "RIPEMD-128: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'RIPEMD-128')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash RIPEMD-128 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd2(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD2: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD2')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD2 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd4(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD4: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD4')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD4 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd5(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD5: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD5')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD5 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha512(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-512: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-512')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-512 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha384(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-384: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-384')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-384 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha256(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-256: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-256')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-256 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha224(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-224: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-224')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-224 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-1')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-1 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileWhirlpool(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Whirlpool: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Whirlpool')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Whirlpool -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileTiger(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Tiger: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Tiger')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Tiger -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileAdler32(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Adler32: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Adler32')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Adler32 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileCrc24(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Crc24: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'CRC24')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash CRC24 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileCrc32(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Crc32: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'CRC32')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash CRC32 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileKeccak_1600(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-3 Keccak-1600: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Keccak-1600')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-3 Keccak-1600 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileSkein_512(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Skein_512: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Skein-512')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Skein-512 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileGOST_34_11(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "GOST 34.11: Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'GOST-34.11')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash GOST 34.11 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def decryptfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select encrypted file", "",
                                                  "GPG files (*.gpg);;Tous (*)")
        if filename:
            m_key, ok = QInputDialog.getText(self, "Enter your passphrase",
                                             "Key:", QLineEdit.Normal)
            if ok and m_key != '':
                lname = os.path.splitext(filename)[0].split("_")[-1]

                self.originalfile = filename
                self.afterfile = lname
                encryordecry = False
                sym = False

                self.myLongTask = Crypto_gpg.Worker(filename, m_key, encryordecry, lname, sym)
                self.myLongTask.renderedImage.connect(self.updatePixmap)
                self.myLongTask.isstarted.connect(self.isstarted)
                self.myLongTask.start()

            else:
                QMessageBox.warning(self, appname + version + "Error",
                                    ''' You must enter a passphrase ''',
                                    QMessageBox.Ok)

    def isstarted(self, status):
        if status == "True":
            self.progress = QProgressDialog("Work in progress...", "Cancel", 0, 0)
            self.progress.setWindowTitle(appname + version)
            self.progress.setWindowModality(Qt.ApplicationModal)
            self.progress.exec()
        else:
            self.progress.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    master = MasterForm()
    master.setWindowTitle(appname + version)
    master.show()
    sys.exit(app.exec_())
