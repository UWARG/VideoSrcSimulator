#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

print(sys.path.append('../'))
from obswebsocket import obsws, requests  # noqa: E402

#connecting via obs-websocket

host = "localhost"
port = 4444
# can make password anything, just configure on OBS
password = "UWARG"

ws = obsws(host, port, password)
ws.connect()

#MAIN
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    
    ws.call(requests.CreateScene('test'))
    ws.call(requests.SetCurrentScene('test'))
    #create source 
    ws.call(requests.CreateSource('browser', 'browser_source', 'test', setVisible=True))
    #print(ws.call(requests.GetSourcesList()))

    #can set to a url instead, param: url= "https://..."
    ws.call(requests.SetBrowserSourceProperties('browser', is_local_file = True, local_file = '/Users/mikashaw/code/warg/python-to-control-OBS/google2.0.0.jpg'))
    print(ws.call(requests.GetBrowserSourceProperties('browser')))

    #recording a 5-second snippet of the image
    ws.call(requests.StartRecording())
    time.sleep(5)
    ws.call(requests.StopRecording())

    print("End")

except KeyboardInterrupt:
    pass

#DISCONNECT
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ws.disconnect()