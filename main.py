
#IMPORTS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
from obswebsocket import obsws, requests

#MAIN
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class OBSConfig:

    def __init__(self, host, port, password):
        self.ws = obsws(host, port, password)
        self.ws.connect()

    def setup_scene(self, scene_name):
        self.ws.call(requests.CreateScene(scene_name))
        self.ws.call(requests.SetCurrentScene(scene_name))

    def setup_file_source(self, scene_name, source_name, filepath):

        '''

            scene: name of scene
            source_name: desired name of source
            filepath: path to destination of img

        '''

        self.ws.call(requests.CreateSource(source_name, "browser_source", scene_name, setVisible=True))
        self.ws.call(requests.SetBrowserSourceProperties(source_name, is_local_file = True, local_file = filepath))
        return self.ws.call(requests.GetBrowserSourceProperties(source_name))

    def record(self, record_time):

        '''

        record_time: desired duration of time to record in seconds

        '''

        self.ws.call(requests.StartRecording())
        time.sleep(record_time)
        self.ws.call(requests.StopRecording())
        
    def __del__(self):
        self.ws.disconnect()






