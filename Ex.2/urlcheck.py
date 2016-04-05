#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

import urllib.request
import re
import sys

if len(sys.argv) > 1 :

	checkemail = re.compile(r"^(http|https|ftp|file)+://")
	url = str(sys.argv[1])
	
	if checkemail.match(url) is None :
		print("Unknown URL format")
	else :
		try :
			urllib.request.urlopen(url).getcode()
			print("The URL is valid")
		except :
			print("Impossible to load URL")


