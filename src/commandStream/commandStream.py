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
class CommandStream(threading.Thread):
        def openStream(self):
        print("Opening Stream...\n")
        try:
            stream = pexpect.spawn(command)
            if(password != "no"):
                stream.expect(['password:'])
                stream.sendline(password)
            
            print("Stream opened:\n")
            self.streamOpened = True
            return self.stream;
        except:
            print("Stream was not opened succsesfully")
            print(str(stream))
            
    def __init__(self, streamID, name, openCommand, password = "no"):
        threading.Thread.__init__(self)
        self.streamID = streamID
        self.name = name
        self.password = password
        self.streamOpened=False
        self.stream = openStream()
            
    def run(self):
        if(streamOpened == False):
            self.openStream()
        
class Event():
        def __init__(self, eventID, name, stream, command, expectation="none"):
            self.eventID = eventID
            self.name = name
            self.command = command
            self.expectation = expectation
            self.stream = stream
        
        def run(self):
            print("Executing " + self.command)
            self.stream.sendline(command)
            if(expectation != "none"):
                self.stream.expect(expectation)
                print(command + " executed succsesfully")
            else:
                print(command + "assumed to have executed")
            
            
class TriggerEvent (threading.Thread):
    def __init__(self, threadID, name, event, stream, trigger):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.trigger = trigger

    def run(self):
        print("Starting " + self.name)
        
        child.sendline(self.command)
        print("Command Executed")
    
    def checkTrigger(result):
        if(result == self.trigger):
            self.event.run()

class TimerEvent (threading.Thread):
    def __init__(self, threadID, name, event, duration, measurement="sec", condition=True):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.condition = condition
        
        if(measurement == "min") or (measurement == "minute") or (measurement == "Minute"):
            self.duration = duration * 60
        elif(measurement == "hour") or (measurement == "hr"):
            self.duration = duration * 120
        else:
            self.duration = duration
        
        self.condition = condition
        
    def run(self):
        while(self.condition):
            self.event.run()

            if(expectation != "none"):
                event.child.expect(expectation)

        time.sleep(duration)

        return;
