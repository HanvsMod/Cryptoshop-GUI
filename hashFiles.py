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


import hashlib

chunk_size = 8192


def hash_file(filename, hash_type, var):
    with open(filename, 'rb') as f:
        for data in iter(lambda: f.read(chunk_size), b''):
            hash_type.update(data)
    output = hash_type.hexdigest()

    saved_file = filename + var

    file = open(saved_file, "w")
    file.write(filename + ": " + var + ": " + output)
    return output


def calcsha512(filename):
    var = "SHA-512"
    hash_type = hashlib.sha512()
    output = hash_file(filename, hash_type, var)
    return output


def calcsha384(filename):
    var = "SHA-384"
    hash_type = hashlib.sha384()
    output = hash_file(filename, hash_type, var)
    return output


def calcsha256(filename):
    var = "SHA-256"
    hash_type = hashlib.sha256()
    output = hash_file(filename, hash_type, var)
    return output


def calcsha224(filename):
    var = "SHA-224"
    hash_type = hashlib.sha224()
    output = hash_file(filename, hash_type, var)
    return output


def calcsha(filename):
    var = "SHA-1"
    hash_type = hashlib.sha1()
    output = hash_file(filename, hash_type, var)
    return output


def calcmd5(filename):
    var = "MD5"
    hash_type = hashlib.md5()
    output = hash_file(filename, hash_type, var)
    return output


def calcmd4(filename):
    var = "MD4"
    hash_type = hashlib.new('md4')
    output = hash_file(filename, hash_type, var)
    return output


def calcripemd(filename):
    var = "RIPEMD"
    hash_type = hashlib.new('ripemd160')
    output = hash_file(filename, hash_type, var)
    return output