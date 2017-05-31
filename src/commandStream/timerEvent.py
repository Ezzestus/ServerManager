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
        
    def run(self, stream):
        while(self.condition):
            #self.event.run(stream)
            stream.sendline(self.event.command)
            
            if(expectation != "none"):
                stream.expect(self.event.expectation)

        time.sleep(duration)

        return;
