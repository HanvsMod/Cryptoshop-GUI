#!/usr/bin/env python
# -*-coding:Utf-8 -*

# QPyCrypto- gpg gui
# Copyright(C) 2016 CORRAIRE Fabrice. antidote1911@gmail.com

# ############################################################################
# #This file is part of QPyCrypto.
# #
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

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QLineEdit, QMessageBox, QInputDialog, \
    QProgressDialog
from PyQt5.QtCore import Qt, QFile, QTextStream
from gui.ui_principale import Ui_MainWindow
from fenselectkey import Fenselectkey
from fenselectsignkey import Fenselectsignkey
from feninfos import About
from keymanager import Fenmanager
from hashFiles import *
import gnupg
import os
import Crypto_gpg
import simplecrypt2


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
        self.ui.actionVider_Tampon.triggered.connect(self.vidertampon)
        self.ui.actionOuvrir.triggered.connect(self.ouvrirtexte)
        self.ui.actionSauver.triggered.connect(self.sauvertexte)
        self.ui.actionQuitter.triggered.connect(sys.exit)

        # Menu HASH File:
        self.ui.actionSHA512.triggered.connect(self.hashfilesha512)
        self.ui.actionSHA384.triggered.connect(self.hashfilesha384)
        self.ui.actionSHA256.triggered.connect(self.hashfilesha256)
        self.ui.actionSHA224.triggered.connect(self.hashfilesha224)
        self.ui.actionSHA.triggered.connect(self.hashfilesha)
        self.ui.actionMD5.triggered.connect(self.hashfilemd5)
        self.ui.actionMD4.triggered.connect(self.hashfilemd4)
        self.ui.actionRIPEMD.triggered.connect(self.hashfileripemd)

    def encryptfileenigma(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Sélectionnez le fichier à chiffrer", "",
                                                  "All Files (*);;Text Files (*.txt)")

        if filename:
            m_key, ok = QInputDialog.getText(self, "Entrez votre passphrase",
                                             "Clée:", QLineEdit.Normal)
            if ok and m_key != '':
                f = open(filename, "rb")
                enc = simplecrypt2.encrypt_file(m_key, f)
                with open(filename + ".enc", 'wb') as fo:
                    fo.write(enc.read())

    def decryptfileenigma(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Sélectionnez le fichier à chiffrer", "",
                                                  "All Files (*);;Text Files (*.txt)")

        if filename:
            m_key, ok = QInputDialog.getText(self, "Entrez votre passphrase",
                                             "Clée:", QLineEdit.Normal)
            if ok and m_key != '':
                try:
                    f = open(filename, "rb")
                    enc = simplecrypt2.decrypt_file(m_key, f)
                    with open(filename[:-4], 'wb') as fo:
                        fo.write(enc.read())
                except Exception as e:
                    QMessageBox.warning(self, "What that bug ??", (str(e)), QMessageBox.Ok)

    def signfile(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Selectionez le fichier à signer", "",
                                                  "Tous (*);;Fichiers texte (*.txt)")
        if filename:
            gpg = gnupg.GPG(use_agent=False)
            dialog = Fenselectsignkey(self)
            if dialog.exec_() == QDialog.Accepted:
                keyid = dialog.ui.comboBox.currentText()
                key = dialog.ui.editKey.text()
                with open(filename, 'rb') as f:
                    gpg.sign_file(self, f, keyid, key, detach=True)

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
            QMessageBox.warning(self, "Aucune signature",
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
            self.ui.plainTextEdit.appendPlainText(str("----->>>") + (self.afterfile))

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

            dialog = Fenselectkey(self)

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

    def hashfileripemd(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "RIPEMD: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcripemd(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash RIPEMD -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd4(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD4: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcmd4(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD4 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilemd5(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "MD5: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcmd5(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash MD5 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha512(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA512: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcsha512(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-512 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha384(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA384: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcsha384(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-384 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha256(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA256: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcsha256(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-256 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha224(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA224: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)")
        if filename:
            output = calcsha224(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-224 -->" + filename)
            self.ui.plainTextEdit.appendPlainText(output)

    def hashfilesha(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "SHA-1: Select File.", "",
                                                  "All Files (*);;Text Files (*.txt)", )
        if filename:
            output = calcsha(filename)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("----------------------------------------------")
            self.ui.plainTextEdit.appendPlainText("Hash SHA-1 -->" + filename)
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
