from api import *
import threading, os, sys

class myThread (threading.Thread):
   def __init__(self, botId):
      threading.Thread.__init__(self)
      self.botId = botId

   def run(self):
      os.system("python code.py "+str(self.botId))



level = get_level()
if level == 1:
    os.system("python code.py 0")
    print("The final score is: " + str(get_score()))
elif level == 2:
    os.system("python code.py 0")
    print("The final score is: " + str(get_score()))
elif level == 3:
    threads = []
    for i in range(2):
        thread = myThread(i)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 4:
    threads = []
    for i in range(get_numbots()):
        thread = myThread(i)
        threads.append(thread)
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 5:
    threads = []
    for i in range(2):
        thread = myThread(i)
        threads.append(thread)
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 6:
    threads = []
    for i in range(get_numbots()):
        thread = myThread(i)
        threads.append(thread)
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
