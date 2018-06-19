#!/usr/bin/python
# -*- coding:utf-8 -*-
import time, threading
import random
from Tkinter import *

class Aplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self._singName = ["C", "D", "E", "F", "G", "A", "B"]
        self._choiceMode = 0
        self.swt = StringVar()
        self.name = StringVar()
        self.switchTo()
        self.swt.set("STOP")
        self.createwidgets()

    def createwidgets(self):
        self.helloLabel = Label(self, textvariable=self.name, bg="lightblue", width=10, height=4, font=('Arial', 40))
        self.helloLabel.pack(pady=5)
        self.startButton = Button(self, textvariable=self.swt, command=self.switchTo)
        self.startButton.pack(pady=8, side="top")
        self.buttonLabel = Label(self, width=10)
        self.buttonLabel.pack()
        self.slowerButton = Button(self.buttonLabel, text=" << ", command=self.slower)
        self.slowerButton.pack(side="left", padx=30)
        self.fasterButton = Button(self.buttonLabel, text=" >> ", command=self.faster)
        self.fasterButton.pack(side="left", padx=30)
        self.cmButton = Button(self, text="MODE", command=self.changeMode)
        self.cmButton.pack(side="bottom", pady=8)



    def switchTo(self):
        if self.swt.get() == "STOP":
            self.speed = 0
            self.swt.set("START")
            self.pack()
        else:
            self.swt.set("STOP")
            self.speed = 1
            self.t = threading.Thread(target=self.loop, name="changeVar")
            self.t.setDaemon(True)
            self.t.start()
        self.pack()
        # self.slowerButton.flash()

    def slower(self):
        self.speed += 0.5

    def faster(self):
        if(self.speed > 0.5):
            self.speed -=0.5

    def loop(self):
        print("START")
        while self.speed != 0:
            time.sleep(self.speed)
            if self._choiceMode == 0:
                self.name.set(str(random.randint(1, 7)))
            elif self._choiceMode == 1:
                self.name.set(str(random.choice(self._singName)))
            print(self.name.get())

    def changeMode(self):
        if self._choiceMode == 0:
            self._choiceMode = 1
        else:
            self._choiceMode = 0

if __name__ == "__main__":
    app = Aplication()
    app.master.title("Music")
    app.master.minsize(400,200)
    app.mainloop()


