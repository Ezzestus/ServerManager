import time
import threading

from commandStream import *

class TimerEvent (threading.Thread):
    def __init__(self, timerID, name, event, duration, writeStream, measurement = "sec", condition = True):
        threading.Thread.__init__(self)
        self.timerID = timerID
        self.name = name
        self.event = event
        self.condition = condition
        self.writeStream = writeStream
        
        if(measurement == "min") or (measurement == "minute") or (measurement == "Minute"):
            self.duration = duration * 60
        elif(measurement == "hour") or (measurement == "hr"):
            self.duration = duration * 120
        else:
            self.duration = duration
        
        self.condition = condition
        
    def run(self):
        while(self.condition):
            #self.event.run(stream)
            self.writeStream.addCommand(self.event.command)
            
            #if(self.event.expectation != "none"):
                #stream.expect(self.event.expectation)

        time.sleep(duration)

        return;
