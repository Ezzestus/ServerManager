  #!/bin/python
#commandStream: send and listen to commands via telnet o$
#Created by David Klumpenhower
#Created May 26, 2017
#Last Updated May 29, 2017

import pexpect
import time
import threading

#vars


#classes



class CommandStream():
    
    def __init__(self, streamID, name, openCommand, password = "no", streamOpened = False):
        threading.Thread.__init__(self)
        self.streamID = streamID
        self.name = name
        self.password = password
        self.streamOpened = False
        self.events = []
        self.triggers = []
        self.timers = []
    
    def openStream(self):
        if(self.streamOpened == True):
            print("Opening Stream...\n")
            try:
                stream = pexpect.spawn(openCommand)
                if(password != "no"):
                    stream.expect(['password:'])
                    stream.sendline(password)
            
                print("Stream opened:\n")
                self.streamOpened = True
                return stream;
            except:
                print("Stream was not opened succsesfully")
                print(str(self.stream))
    
    def run(self):
        if(self.streamOpened == False):
            self.openStream()
        elif(self.streamOpened):
            while(len(self.events) > 0):
                count = 0
                for expectation in self.triggers:
                    e = 1
                    
    def addEvent(self, threadID, name, command, expectation="none"):
        eventItem = Event(threadID, name, command, expectation)
        self.events.append(eventItem)
    
    def removeEvent(self, eventID):
            self.events.remove(eventID)
            
    def addTrigger(self, threadID, name, event, trigger):
        if(len(self.events) > 0):
            tiggerItem = TriggerEvent(threadID, name, event, trigger)
            self.triggers.append(triggerItem)
        else:
            print("No events, Triggers require an event to trigger")
    
    def removeTrigger(self, triggerID):
        self.triggers.remove(triggerID)
        
    def addTimer(self, threadID, name, event, duration, measurement="sec", condition=True):
        if(len(self.events) > 0):
            timerItem = TimerEvent(threadID, name, event, duration, measurement="sec", condition=True)
            self.timers.append(timerItem)
        else:
            print("No events, Timers require an event to trigger")
            
    def removeTimer(self, timerID):
        self.timers.remove(timerID)
        
    def startTimer(self, timerID):
        self.timers[timerID].run(self.openStream())
