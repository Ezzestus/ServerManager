  #!/bin/python
#commandStream: send and listen to commands via telnet o$
#Created by David Klumpenhower
#Created May 26, 2017
#Last Updated May 29, 2017

import pexpect
import time
import threading

#project imports
from timerEvent import *
from triggerEvent import *

#vars


#classes
class CommandStream(threading.Thread):
    
    def __init__(self, streamID, name, openCommand, password = "no", streamOpened = False):
        threading.Thread.__init__(self)
        self.streamID = streamID
        self.name = name
        self.password = password
        self.streamOpened = False
        self.expectations = []
        
        if(self.streamOpened == True):
            print("Opening Stream...\n")
            try:
                self.stream = pexpect.spawn(openCommand)
                if(password != "no"):
                    self.stream.expect(['password:'])
                    self.stream.sendline(password)
            
                print("Stream opened:\n")
                self.streamOpened = True
            except:
                print("Stream was not opened succsesfully")
                print(str(self.stream))

class ReadStream(CommandStream):
        def __init__ (self, streamID, name, openCommand, password = "no", streamOpened = False):
            ComandStream.__init__(self,streamID, name, openCommand, password = "no", streamOpened = False)
            self.expectations = []
            self.triggers = []
            
        def addExpectation(self, trigerID, name, event, trigger):
            triggerItem = TriggerEvent(trigerID, name, event, trigger)
            self.expectations.append(triggerItem.trigger)
            triggerItem.trigerID = (len(self.expectations) -1)
            self.triggers.append(triggerItem)
            
        def removeExpectation(self, triggerID):
            self.expectations.remove(triggerID)
            self.triggers.remove(triggerID)
            
        def run(self):
            while(streamOpened):
                result = self.stream.expect(self.expectations)
        
class WriteStream(CommandStream):
    
    def __init__ (self, streamID, name, openCommand, password = "no", streamOpened = False):
            CommandStream.__init__(self, streamID, name, openCommand, password = "no", streamOpened = False)
            self.commands = []
            
    def run(self):
        while(self.streamOpened):
            if(len(self.commands) > 0):
                self.stream.sendline(command)
            else:
                print("No commands to write")
                
    def addCommand(self, command):
        self.commands.append(command)
        
