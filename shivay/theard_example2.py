# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:02:55 2022

@author: 91990
"""

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()
        print_time(self.name, 1, self.counter)
        threadLock.release()
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []
# Create new threads
thread1 = myThread(1, "payment", 5)
time.sleep(0.2)
thread2 = myThread(2, "email confirmation", 10)
time.sleep(0.2)
thread3 = myThread(3, "Thank you for order", 8)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("Exiting Main Thread", time.ctime(time.time()))
