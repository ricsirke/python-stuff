import Tkinter, random, time
import socket, sys, serial

class App:

    def white(self):
        self.lines=[]
        self.lastpos=0

        self.c.create_rectangle(0, 0, 800, 512, fill="black")
        for y in range(0,512,50):
            self.c.create_line(0, y, 800, y, fill="#333333",dash=(4, 4))
            self.c.create_text(5, y-10, fill="#999999", text=str(y*2), anchor="w")
        for x in range(100,800,100):
            self.c.create_line(x, 0, x, 512, fill="#333333",dash=(4, 4))
            self.c.create_text(x+3, 500-10, fill="#999999", text=str(x/100)+"s", anchor="w")

        self.lineRedraw=self.c.create_line(0, 800, 0, 0, fill="red")

        self.lines1text=self.c.create_text(800-3, 10, fill="#00FF00", text=str("TEST"), anchor="e")
        for x in range(800):
            self.lines.append(self.c.create_line(x, 0, x, 0, fill="#00FF00"))

    def addPoint(self,val):
        self.data[self.xpos]=val
        self.line1avg+=val
        if self.xpos%10==0:
            self.c.itemconfig(self.lines1text,text=str(self.line1avg/10.0))
            self.line1avg=0
        if self.xpos>0:self.c.coords(self.lines[self.xpos],(self.xpos-1,self.lastpos,self.xpos,val))
        if self.xpos<800:self.c.coords(self.lineRedraw,(self.xpos+1,0,self.xpos+1,800))
        self.lastpos=val
        self.xpos+=1
        if self.xpos==800:
            self.xpos=0
            self.totalPoints+=800
            print "FPS:",self.totalPoints/(time.time()-self.timeStart)
        t.update()

    def __init__(self, t):
        self.xpos=0
        self.line1avg=0
        self.data=[0]*800
        self.c = Tkinter.Canvas(t, width=800, height=512)
        self.c.pack()
        self.totalPoints=0
        self.white()
        self.timeStart=time.time()

t = Tkinter.Tk()
a = App(t)

#ser = serial.Serial('COM1', 19200, timeout=1)
ser = serial.Serial('COM17', 9600, timeout=1)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    while True: #try to get a reading
        #print "LISTENING"
        raw=str(ser.readline())
        #print raw
        #raw=raw.replace("n","").replace("r","")
        raw=raw.strip()
        raw=raw.split(" ")
        #print raw
        try:
            point=(int(raw[0]))*2
            #print point
            break
        except:
            print "FAIL"
            pass
    point=point/2
    a.addPoint(point)