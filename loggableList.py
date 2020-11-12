import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, val):
        list.append(self, val)
        self.log(val)

x = LoggableList()
x.append(3)