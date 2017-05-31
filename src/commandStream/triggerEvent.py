class TriggerEvent (threading.Thread):
    def __init__(self, threadID, name, event, trigger):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.trigger = trigger

    def run(self, stream):
        print("Starting " + self.name)
        
        stream.sendline(self.command)
        print("Command Executed")
    
    def checkTrigger(result):
        if(result == self.trigger):
            self.event.run()
