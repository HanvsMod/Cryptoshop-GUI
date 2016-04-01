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
# import simplecrypt2
import simplehash
import botancrypt


def keymanager():
    dialog = Fenmanager()
    dialog.exec()


def openabout():
    dialog = About()
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
                                                  "Select the file to crypt", "",
                                                  "All Files (*)")
        if filename:
            dialog = Fenselectkey(self)
            if dialog.exec_() == QDialog.Accepted:
                m_key = dialog.ui.EditPass.text()
                algo = dialog.ui.comboAlgo.currentText()
                enc = botancrypt.encrypt(filename, m_key, algo)
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
                    enc = botancrypt.decrypt(filename, m_key)
                    print(enc)
                    if enc == "Invalid Header":
                        QMessageBox.warning(self, "Invalid Header",
                                            "This file have an invalid or missing header. This is not a Cryptoshop file.",
                                            QMessageBox.Ok)
                    if enc == "Invalid Hmac verification":
                        QMessageBox.warning(self, "Error",
                                            "Wrong Passphrase, or invalid authentification code (modified file)",
                                            QMessageBox.Ok)
                    if enc == "Successfully Decrypted":
                        self.ui.statusbar.showMessage("File " + filename + " is decrypted.", 50000)
                except Exception as e:
                    QMessageBox.warning(self, "What that bug ??", (str(e)), QMessageBox.Ok)

    def signfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select a file to sign", "",
                                                  "All files (*)")
        if filename:
            gpg = gnupg.GPG(use_agent=False)
            dialog = Fenselectsignkey(self)
            if dialog.exec_() == QDialog.Accepted:
                keyid = dialog.ui.comboBox.currentText()
                key = dialog.ui.editKey.text()
                with open(filename, 'rb') as signfile:
                    gpg.sign_file(signfile, keyid, key, clearsign=True, detach=True, output=(filename + ".sig"))
                    signfile.close()

    def verifysignfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Select the file to decrypt", "",
                                                  "sign Files (*.sig);;All Files (*)")
        if filename:
            with open(filename, 'rb') as stream:
                gpg = gnupg.GPG(use_agent=False)
                data=os.path.splitext(filename)[0].split("_")[-1]
                verified = gpg.verify_file(stream,data)
                print(verified.trust_text)
                print(verified.TRUST_FULLY)
                print(verified.trust_level)
                print(verified.status)
                print(verified.username)
                if verified.trust_level is not None and verified.trust_level >= verified.TRUST_FULLY:
                    print('Trust level: %s' % verified.trust_text)
                if not verified: raise ValueError("Signature could not be verified!")
                else:
                    print(verified)


    def tamponverify(self):
        texttoverify = self.ui.plainTextEdit.toPlainText()
        gpg = gnupg.GPG(use_agent=False)
        verified_data = gpg.verify(texttoverify)
        # print("fingerprint "+verified_data.fingerprint)
        # print("creation_date "+verified_data.creation_date)
        # print("status "+verified_data.status)
        # print("expire_timestamp "+verified_data.expire_timestamp)
        # print("key_id "+verified_data.key_id)
        # print("stderr "+verified_data.stderr)
        # print("trust_text "+verified_data.trust_text)
        # print("username "+verified_data.username)
        if verified_data.valid is False and verified_data.status is None:
            QMessageBox.warning(self, "No valid signature",
                                "Le texte ne comporte aucune signature valide.",
                                QMessageBox.Ok)
            return
        if verified_data.valid is False:
            QMessageBox.warning(self, "Signature Invalide",
                                "La signature de " + verified_data.username +
                                "\nID " + verified_data.key_id +
                                " est INVALIDE." + "\n\nGPG Message:\n" + verified_data.stderr,
                                QMessageBox.Ok)
        if verified_data.valid is True:
            QMessageBox.information(self, "Signature Valide",
                                    "Signature correcte de " + verified_data.username +
                                    "\nID " + verified_data.key_id + "\n\nEmpreinte:\n"
                                    + verified_data.fingerprint + "\n\nGPG Message:\n" + verified_data.stderr,
                                    QMessageBox.Ok)

    def updatePixmap(self, boll):
        if boll == "False":
            QMessageBox.warning(self, "Déchiffrage de impossible",
                                " La passphrase est invalide pour déchiffrer " + self.originalfile,
                                QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText(
                "QPyCrypto-->Impossible de déchiffrer le fichier " + self.originalfile)
            self.ui.plainTextEdit.appendPlainText(str("Passphrase Invalide"))
        else:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("QPyCrypto-->Le fichier " + self.originalfile + " a été déchiffré.")
            self.ui.plainTextEdit.appendPlainText(str("----->>>") + self.afterfile)

    def tamponsign(self):
        texttosign = self.ui.plainTextEdit.toPlainText()
        gpg = gnupg.GPG(use_agent=False)
        dialog = Fenselectsignkey(self)
        if dialog.exec_() == QDialog.Accepted:
            key = dialog.ui.comboBox.currentText()
            signed_data = gpg.sign(texttosign, keyid=key)
            if str(signed_data) == "":
                QMessageBox.critical(self, 'Echec Signature...',
                                     '''La passphrase entrée n'est pas valide pour déverrouiller cette clée.''',
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
                                                  "Selectionez le fichier à chiffrer", "",
                                                  "Tous (*);;Fichiers texte (*.txt)")

        if filename:

            dialog = Fenselectkeygpg(self)

            if dialog.exec_() == QDialog.Accepted:
                m_key = dialog.ui.editKey.text().strip()

                if dialog.ui.checkSymetric.isChecked():
                    if dialog.ui.editKey.text() == "":
                        QMessageBox.warning(self, 'Erreur...',
                                            '''Vous devez tapez une passphrase secrette pour chiffrer un fichier.''',
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

                    self.ui.plainTextEdit.clear()
                    self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
                    self.ui.plainTextEdit.appendPlainText("QPyCrypto-->Le fichier a été chiffré.")
                    self.ui.plainTextEdit.appendPlainText(str(filename + ".gpg"))

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
                    self.ui.plainTextEdit.appendPlainText("QPyCrypto-->Le fichier a été chiffré.")
                    self.ui.plainTextEdit.appendPlainText(str(filename + ".gpg"))

    def aboutqt(self):
        QMessageBox.aboutQt(self, 'Qt is the best !')

    def tamponencrypt(self):
        dialog = Fenselectkey(self)

        if dialog.exec_() == QDialog.Accepted:
            self.m_key = dialog.ui.editKey.text().strip()
            if dialog.ui.checkSymetric.isChecked():
                if dialog.ui.editKey.text() == "":
                    QMessageBox.warning(self, 'Erreur',
                                        '''Vous devez tapez une passphrase secrette pour chiffrer.''',
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
                QMessageBox.warning(self, "Save",
                                    "Ecriture impossible %s:\n%s." % (filename, file.errorString()))
                return
            outstr = QTextStream(file)
            outstr << self.ui.plainTextEdit.toPlainText()
            QMessageBox.information(self, "Sauver fichier",
                                    "Le fichier à été chiffré. \n%s" % (file.fileName()))

    def ouvrirtexte(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        if filename:
            file = QFile(filename)
            if not file.open(QFile.ReadOnly | QFile.Text):
                QMessageBox.warning(self, "Ouvrir fichier",
                                    "Lecture impossible %s:\n%s." % (filename, file.errorString()))
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
            QMessageBox.warning(self, "Déchiffrage impossible",
                                ''' La passphrase est invalide''',
                                QMessageBox.Ok)
            return

    def hashfileripemd_160(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "RIPEMD: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'RIPEMD-160')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash RIPEMD-160 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileripemd_128(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "RIPEMD: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'RIPEMD-128')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash RIPEMD-128 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd2(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD4: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD2')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD2 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd4(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD4: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD4')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD4 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd5(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD5: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'MD5')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD5 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha512(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA512: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-512')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-512 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha384(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA384: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-384')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-384 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha256(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA256: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-256')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-256 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha224(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA224: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-224')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-224 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'SHA-1')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-1 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileWhirlpool(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Whirlpool')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Whirlpool -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileTiger(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Tiger')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Tiger -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileAdler32(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Adler32')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Adler32 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileCrc24(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'CRC24')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash CRC24 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileCrc32(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'CRC32')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash CRC32 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileKeccak_1600(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Keccak-1600')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Keccak-1600 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileSkein_512(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = simplehash.get_file_checksum(filename, 'Skein-512')
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash Skein-512 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfileGOST_34_11(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
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
            m_key, ok = QInputDialog.getText(self, "Entrez votre passphrase",
                                             "Clée:", QLineEdit.Normal)
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
                QMessageBox.warning(self, 'Erreur',
                                    ''' Vous devez choisir une passphrase ''',
                                    QMessageBox.Ok)

    def isstarted(self, status):
        if status == "True":
            self.progress = QProgressDialog("Calculs en cours...", "Annuler", 0, 0)
            self.progress.setWindowModality(Qt.ApplicationModal)
            self.progress.exec()
        else:
            self.progress.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    master = MasterForm()
    master.show()
    sys.exit(app.exec_())
