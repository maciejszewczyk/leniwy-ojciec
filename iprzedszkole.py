#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cookielib
import urllib2
import urllib
import re
import json


class iPrzedszkole(object):

    def __init__(self, kindergarten, login, password):
        self.kindergartenName = kindergarten
        self.kindergartenLogin = login
        self.kindergartenPassword = password
        self.baseURL = 'https://iprzedszkole.progman.pl'
        self.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'

    def jadlospis(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        request = urllib2.Request(self.baseURL + '/iprzedszkole/Authentication/Login.aspx')
        request.add_header('User-Agent', self.userAgent)
        result = opener.open(request).read()

        viewState = re.search('<input\s+type="hidden"\s+name="__VIEWSTATE"\s+id="__VIEWSTATE"\s+value="([/+=\w]+)"\s+/>', result)
        viewState = viewState.group(1)

        viewStateGenerator = re.search('<input\s+type="hidden"\s+name="__VIEWSTATEGENERATOR"\s+id="__VIEWSTATEGENERATOR"\s+value="([/+=\w]+)"\s+/>', result)
        viewStateGenerator = viewStateGenerator.group(1)

        eventValidation = re.search('<input\s+type="hidden"\s+name="__EVENTVALIDATION"\s+id="__EVENTVALIDATION"\s+value="([/+=\w]+)"\s+/>', result)
        eventValidation = eventValidation.group(1)


        formParameters = {'__VIEWSTATE': viewState,
                          '__VIEWSTATEGENERATOR': viewStateGenerator,
                          '__EVENTVALIDATION': eventValidation,
                          'ctl00$cphContent$txtDatabase': self.kindergartenName,
                          'ctl00$cphContent$txtLogin': self.kindergartenLogin,
                          'ctl00$cphContent$txtPassword': self.kindergartenPassword,
                          'ctl00$cphContent$Button1': 'Zaloguj'
                          }

        formData = urllib.urlencode(formParameters)

        request = urllib2.Request(self.baseURL + '/iprzedszkole/Authentication/Login.aspx')
        request.add_data(formData)
        request.add_header('User-Agent', self.userAgent)
        opener.open(request)

        request = urllib2.Request(self.baseURL + '/iprzedszkole/Pages/PanelRodzica/Jadlospis/Jadlospis.aspx')
        request.add_header('User-Agent', self.userAgent)
        result = opener.open(request).read()

        childmasterid = re.search('<option\s+selected="selected"\s+value="(\d+)">', result)
        childmasterid = childmasterid.group(1)

        requestpayload = "{idDziecko: %s, tydzien: 0}" % childmasterid

        request = urllib2.Request(self.baseURL + '/iprzedszkole/Pages/PanelRodzica/Jadlospis/ws_JadlospisPr.asmx/pobierzListe')
        request.add_data(requestpayload)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        result = opener.open(request).read()

        jedzenie = json.loads(result)
        jadlospis = jedzenie['d']['ListK']

        i = 0
        for p in jadlospis:
            if p['wolne'] == 0:
                if p['dzis'] is True:  # "dzis": true,
                    breakfast = jadlospis[i]['posilki'][0]['opis']
                    dinner = jadlospis[i]['posilki'][1]['opis']
                    teatime = jadlospis[i]['posilki'][2]['opis']
                    return "\n".join([breakfast, dinner, teatime])
            i += 1