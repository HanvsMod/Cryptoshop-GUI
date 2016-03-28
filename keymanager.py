#!/usr/bin/env python3
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

from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QListWidget)
from PyQt5.QtCore import QDate
from gui.ui_keymanager import Ui_Fenkeymanager
from createkey import Createkey
from datetime import date, datetime
import gnupg
import logging

logger = logging.getLogger(__name__)

gpg = gnupg.GPG(use_agent=False)
keylist = gpg.list_keys()
privatekeylist = gpg.list_keys(True)
uid_strings = []
uid_string2key = {}
uid_string = []


class Fenmanager(QDialog):
    def __init__(self, parent=None):

        super(Fenmanager, self).__init__(parent)
        self.ui = Ui_Fenkeymanager()
        self.ui.setupUi(self)
        self.ui.pushDelete.clicked.connect(self.delete)
        self.ui.checkPrivates.toggled.connect(self.remplirliste)
        self.ui.pushCreate.clicked.connect(self.opencreatekey)
        self.ui.pushCancel.clicked.connect(self.closefen)
        self.ui.listWidget.itemClicked.connect(self.keyinfos)
        self.remplirliste()

    def closefen(self):
        self.close()

    def opencreatekey(self):
        dialog = Createkey(self)
        dialog.exec()
        #self.remplirliste()

    def remplirliste(self):
        self.ui.listWidget.clear()
        gpg = gnupg.GPG(use_agent=False)
        keylist = gpg.list_keys()
        privatekeylist = gpg.list_keys(True)
        uid_strings = []
        uid_string2key = {}
        uid_string = []
        self.ui.listWidget.clear()
        if self.ui.checkPrivates.isChecked():
            for key in privatekeylist:
                for uid_string in key['uids']:
                    uid_strings.append(uid_string)
                    uid_string2key[uid_string] = key
                self.ui.listWidget.addItems([uid_string])
        else:
            for key in keylist:
                for uid_string in key['uids']:
                    uid_strings.append(uid_string)
                    uid_string2key[uid_string] = key
                self.ui.listWidget.addItems([uid_string])

    def delete(self):
        global uid_string
        item = self.ui.listWidget.currentItem().text()
        for key in keylist:
            for uid_string in key['uids']:
                uid_strings.append(uid_string)
                uid_string2key[uid_string] = key
        uid = item

        key = uid_string2key[uid]
        print(key['fingerprint'])
        fp = key['fingerprint']
        print(key)
        reply = QMessageBox.question(self, "Supprimer la clé",
                                     'Etes vous certain de vouloir supprimer cette clé ?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        else:
            try:
                print(item)
                gpg.delete_keys(fp,True)
                print(item)
                gpg.delete_keys(fp)
                print(item)
            except:
                self.remplirliste()

        self.remplirliste()

    def keyinfos(self):
        global uid_string
        selecteditem = self.ui.listWidget.currentItem().text()
        uid = selecteditem
        email = uid.split('<')
        name = email[0]
        email = email[-1]
        email = email[:-1]

        for key in keylist:
            for uid_string in key['uids']:
                uid_strings.append(uid_string)
                uid_string2key[uid_string] = key
        key = uid_string2key[uid]
        self.ui.label_empreinte.setText(key['fingerprint'])
        self.ui.label_identifiant.setText(key['keyid'])
        self.ui.label_taille.setText(key['length'])
        self.ui.label_confiance.setText(key['ownertrust'])
        self.ui.label_nom.setText(name)
        if key['ownertrust'] == 'q':
            self.ui.label_confiance.setText('Je ne sais pas')
        elif key['ownertrust'] == 'u':
            self.ui.label_confiance.setText('Ultime')
        elif key['ownertrust'] == 'n':
            self.ui.label_confiance.setText('Jamais')
        elif key['ownertrust'] == 'm':
            self.ui.label_confiance.setText('Marginale')
        elif key['ownertrust'] == 'f':
            self.ui.label_confiance.setText('Complete')
        else:
            self.ui.label_confiance.setText(key['ownertrust'])
        date_created = int(key['date'])
        date_created = date.fromtimestamp(date_created)
        self.ui.label_creation.setText(str(date_created))
        if key["algo"] in ["1", "2", "3"]:
            self.ui.label_algorithme.setText("RSA")
        elif key["algo"] in ["16", "20"]:
            self.ui.label_algorithme.setText("Elgamal")
        elif key["algo"] in ["17"]:
            self.ui.label_algorithme.setText("DSA")
        elif key["algo"] in ["18"]:
            self.ui.label_algorithme.setText("ECDH")
        elif key["algo"] in ["10"]:
            self.ui.label_algorithme.setText("ECDSA")
        elif key["algo"] in ["19"]:
            self.ui.label_algorithme.setText("ECCDSA")
        elif key["algo"] in ["22"]:
            self.ui.label_algorithme.setText("ECC ed25519")
        else:
            self.ui.label_algorithme.setText("algo=" + key["algo"])
        if (key['expires']) != "":
            date_expire = int(key['expires'])
            date_expire = date.fromtimestamp(date_expire)
            self.ui.dateEdit.setDate(date_expire)
            self.ui.label_expiration.setText(str(date_expire))
        else:
            self.ui.label_expiration.setText("Pas d'expiration")
            # self.ui.dateEdit.setDate(date(9000,1,1))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    Fenkeymanager = Fenmanager()
    Fenkeymanager.show()
    sys.exit(app.exec_())
