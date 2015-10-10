#!/usr/bin/env python
# -*- coding: utf-8 -*-

from iprzedszkole import *

przedszkole = iPrzedszkole('<nazwa przedszkola>', '<uzytkownik>', '<haslo>')
menu = przedszkole.jadlospis()
if menu is not None:
    print menu
