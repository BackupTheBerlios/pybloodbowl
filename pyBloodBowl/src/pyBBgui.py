# -*- coding: Cp1252 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.0"

import pyBBParser
import tkMessageBox
from Tkinter import Tk, Frame, Label, PhotoImage, \
                    Menu, Entry, StringVar, OptionMenu, \
                    E, N, S, W, GROOVE, SUNKEN, RIGHT

C_TITLE    =    "pyBloodBowl"

class pyBBgui(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.teamparser = pyBBParser.BBTeamParser()
        self.races = self.teamparser.getTeams()
        self.positions = self.teamparser.getTeamPositions("Amazonen")
        self._initMenu()
        self._initHeaderFrame()
        self._initTeam()
        self._initRooster()
        self.title(C_TITLE)
        self.protocol("WM_DELETE_WINDOW", self.onExit)

        self.resizable(0, 0)
    
    def _initHeaderFrame(self):
        self.headerframe = Frame(self, borderwidth=2, relief=SUNKEN)
        self.logo = PhotoImage(file="../ressources/logo.gif")
        lablogo = Label(self.headerframe, image=self.logo)
        lablogo.grid(row=0, column=0)
        self.headerframe.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
        
    def _initMenu(self):
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
        #Filemenu
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="New", command=self.callback)
        self.filemenu.add_command(label="Open...", command=self.callback)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.onExit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
    def _initTeam(self):
        self.teamframe = Frame(self,borderwidth=1, relief=GROOVE)
        labteamname = Label(self.teamframe, text="Teamname:")
        labteamname.grid(row=0, sticky=N+S+E+W)
        txtteamname = Entry(self.teamframe)
        txtteamname.grid(row=0, column=1, sticky=N+S+E+W)
        self.vteamname = StringVar()
        self.vteamname.set("Amazonen") # initialize
        button = apply(OptionMenu, (self.teamframe, self.vteamname) + tuple(self.races))
        button.bind("<FocusOut>", self.changedTeamCallback)
        button.grid(row=2, column=0, sticky=N+S+E+W)
        self.teamframe.grid(row=1, column=0, sticky=N+S+E+W)
        
    def _initRooster(self):
        self.roosterframe = Frame(self)
        self.roosterNr      = []
        self.roosterName    = []
        self.roosterPos     = []
        self.roosterBW      = []
        self.roosterST      = []
        self.roosterGE      = []
        self.roosterRW      = []
        self.roosterSkills  = []
        self.roosterInj     = []
        self.roosterCP      = []
        self.roosterTD      = []
        self.roosterIN      = []
        self.roosterVV      = []
        self.roosterSDT     = []
        self.roosterSSP     = []
        Label(self.roosterframe, text="#").grid(row=0, column=0)
        Label(self.roosterframe, text="Name").grid(row=0, column=1)
        Label(self.roosterframe, text="Position").grid(row=0, column=2)
        Label(self.roosterframe, text="BW").grid(row=0, column=3)
        Label(self.roosterframe, text="ST").grid(row=0, column=4)
        Label(self.roosterframe, text="GE").grid(row=0, column=5)
        Label(self.roosterframe, text="RW").grid(row=0, column=6)
        Label(self.roosterframe, text="Fähigkeiten/Merkmale").grid(row=0, column=7)
        Label(self.roosterframe, text="bl. Verl.").grid(row=0, column=8)
        Label(self.roosterframe, text="CP").grid(row=0, column=9)
        Label(self.roosterframe, text="TD").grid(row=0, column=10)
        Label(self.roosterframe, text="IN").grid(row=0, column=11)
        Label(self.roosterframe, text="VV").grid(row=0, column=12)
        Label(self.roosterframe, text="SDT").grid(row=0, column=13)
        Label(self.roosterframe, text="SSP").grid(row=0, column=14)
        for i in range(1,17):
            self.roosterNr.append( Label(self.roosterframe, text=i, justify=RIGHT) )
            self.roosterNr[i-1].grid(row=i, column=0, sticky=W)
            
            self.roosterName.append( Entry(self.roosterframe) )
            self.roosterName[i-1].grid(row=i, column=1, sticky=W)
            
            self.vposname = StringVar()
            self.vposname.set(self.positions[0]) # initialize
            b = apply(OptionMenu, (self.roosterframe, self.vposname) + tuple(self.positions))
            self.roosterPos.append( b )
            self.roosterPos[i-1].grid(row=i, column=2, sticky=W)
            self.roosterPos[i-1].config(width=16)
            
            #self.roosterPos.append( Entry(self.roosterframe) )
            #self.roosterPos[i-1].grid(row=i, column=2, sticky=W)
            
            self.roosterBW.append( Entry(self.roosterframe, width=3) )
            self.roosterBW[i-1].grid(row=i, column=3, sticky=W)
            
            self.roosterST.append( Entry(self.roosterframe, width=3) )
            self.roosterST[i-1].grid(row=i, column=4, sticky=W)
            
            self.roosterGE.append( Entry(self.roosterframe, width=3) )
            self.roosterGE[i-1].grid(row=i, column=5, sticky=W)
            
            self.roosterRW.append( Entry(self.roosterframe, width=3) )
            self.roosterRW[i-1].grid(row=i, column=6, sticky=W)
            
            self.roosterSkills.append( Entry(self.roosterframe, width=60) )
            self.roosterSkills[i-1].grid(row=i, column=7, sticky=W)
            
            self.roosterInj.append( Entry(self.roosterframe, width=6) )
            self.roosterInj[i-1].grid(row=i, column=8, sticky=W)
            
            self.roosterCP.append( Entry(self.roosterframe, width=3) )
            self.roosterCP[i-1].grid(row=i, column=9, sticky=W)
            self.roosterCP[i-1].bind("<Tab>", self.recalcSSP)
            
            self.roosterTD.append( Entry(self.roosterframe, width=3) )
            self.roosterTD[i-1].grid(row=i, column=10, sticky=W)
            self.roosterTD[i-1].bind("<Tab>", self.recalcSSP)
            
            self.roosterIN.append( Entry(self.roosterframe, width=3) )
            self.roosterIN[i-1].grid(row=i, column=11, sticky=W)
            self.roosterIN[i-1].bind("<Tab>", self.recalcSSP)
            
            self.roosterVV.append( Entry(self.roosterframe, width=3) )
            self.roosterVV[i-1].grid(row=i, column=12, sticky=W)
            self.roosterVV[i-1].bind("<Tab>", self.recalcSSP)
            
            self.roosterSDT.append( Entry(self.roosterframe, width=3) )
            self.roosterSDT[i-1].grid(row=i, column=13, sticky=W)
            self.roosterSDT[i-1].bind("<Tab>", self.recalcSSP)
            
            self.roosterSSP.append( Entry(self.roosterframe, width=3) )
            self.roosterSSP[i-1].grid(row=i, column=14, sticky=W)
        self.roosterframe.grid(row=3, column=0)
    
    def recalcSSP(self, event):
        print "clicked at", event.x, event.y
    
    def callback(self):
        print "called the callback"
        
    def changedTeamCallback(self, event):
        print self.vteamname.get()
        
    def onExit(self):
        '''Beendet die Anwendung'''
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.quit()

if __name__ == "__main__":
    root = pyBBgui()
    root.mainloop()