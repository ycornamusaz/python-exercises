#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

import urllib.request
import re
import sys

# Check if argument is present
if len(sys.argv) > 1 :
    
    # Set regex and recover argument
    checkurl = re.compile(r"^(http|https|ftp|file)+://")
    url = str(sys.argv[1])

    # Check if url is valid
    if checkurl.match(url) is None :
        print("Unknown URL format")
    # If yes test if url exist
    else :
	try :
	    urllib.request.urlopen(url).getcode()
                print("The URL is valid")
	except :
		print("Impossible to load URL")

