import webbrowser
import time


for i in range(3):
    print("Program started at " + time.ctime())
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=ebXbLfLACGM")
