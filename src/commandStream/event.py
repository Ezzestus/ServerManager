

class Event():
        def __init__(self, eventID, name, command, expectation="none"):
            self.eventID = eventID
            self.name = name
            self.command = command
            self.expectation = expectation
            
        def run(self, stream):
            print("Executing " + self.command)
            stream.sendline(self.command)
            if(expectation != "none"):
                stream.expect(expectation)
                print(command + " executed succsesfully")
            else:
                print(command + "assumed to have executed")
