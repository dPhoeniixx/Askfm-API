#!/usr/bin/env python
# -*- coding: utf-8 -*-

import askapi

AskFm = askapi.askapi() # init class
AskFm.login("ASKFM_USERNAME", "ASKFM_PASSWORD") # login 
print AskFm.user # print user data