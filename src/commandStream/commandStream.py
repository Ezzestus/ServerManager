  #!/bin/python
#commandStream: send and listen to commands via telnet o$
#Created by David Klumpenhower
#Created May 26, 2017
#Last Updated May 29, 2017

import pexpect
import time
import threading

#vars
command = 'telnet Server00 8081'
password = 'admin2msm883S'
message ='We are working on and should soon have a websi$
response = "'Server': " + message
exitFlag = 0

def commandStream(command):
    print("Opening Stream...\n")
    child = pexpect.spawn(command)

    child.expect(['password:'])
    child.sendline(password)
    print("Stream opened:\n")
    return child;

class events (threading.Thread):
    def __init__(self, threadID, name, child, command, e$
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.child = child
        self.command = command
        self.expectedResponse = expectedResponse

    def run(self):
        print("Starting " + self.name)
        print("Executing " + self.command)
        child.sendline(self.command)
        print("Command Executed")

def timerEvent(duration, event, measurement="sec", expec$
    if(measurement == "min") or (measurement == "minute"$
        duration = duration * 60
    elif(measurement == "hour"):
        duration = duration * 120

    while(condition):
        event.run()


        if(expectation != "none"):
            event.child.expect(expectation)

        time.sleep(duration)

    return;

def event():
    return;

child = commandStream(command)

event1 = events(1, "event1", child, 'say "' + message + $
#event1.start()
timerEvent(25, event1, "min")
#event1.join()
