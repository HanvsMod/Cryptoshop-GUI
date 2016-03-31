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

import os
import botan


def get_file_checksum(filename, algo):
    h = botan.hash_function(algo)
    chunk_size = 8192
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    result = botan.hex_encode(h.final())
    return result


def tests():
    print("test")
