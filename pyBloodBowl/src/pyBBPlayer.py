# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.1"

import pyBBParser

class BBplayer:
    """This class represents a BloodBowl Player."""
    def __init__(self, name, team, position):
        self.name = str(name)
        self.team = team
        self.position = position
        self.teamparser = pyBBParser.BBTeamParser()
        self.skills = []
        self.picks = []
        self._initStats()
        self._initSkills()
        self._initPicks()
    
    def _initStats(self):
        """Initialize player with his initial stats."""
        players = self.teamparser.getPlayers()
        stats = players[(self.team,self.position)]
        self.max = int(stats[0])    #maximum
        self.ma = int(stats[1])     #movement
        self.st = int(stats[2])     #strength
        self.ag = int(stats[3])     #agility
        self.av = int(stats[4])     #armor value
        self.costs = int(stats[5])  #costs
        
    def _initSkills(self):
        """Initialize player with initial skills."""
        skills = self.teamparser.getPlayerSkills()
        self.skills = skills[(self.team, self.position)] #initial skills
        
    def _initPicks(self):
        """Initialize player with his picks."""
        picks = self.teamparser.getPlayerPicks()
        self.picks = picks[(self.team, self.position)]   #players picks
    
    def getMovement(self):
        """-> int
        Returns players movement."""
        return self.ma
        
    def getStrength(self):
        """-> int
        Returns players strength."""
        return self.st
        
    def getAgility(self):
        """-> int
        Returns players agility."""
        return self.ag
        
    def getArmor(self):
        """-> int
        Returns players armor value."""
        return self.av
    
    def addSkill(self, newskill):
        """Add a newskill to the players list of skills."""
        self.skills.append( newskill )
        
    def isValidSkill(self, skill):
        return True
        
    def __repr__(self):
        """String representation of the player."""
        repr = "%s (%s/%s)\nMA:%s\nST:%s\nAG:%s\nAV:%s\nSkills: " % (self.name, self.team, self.position, self.ma, self.st, self.ag, self.av)
        for skill in self.skills:
            repr += "%s " % (skill)
        repr += "\nPick: "
        for pick in self.picks:
            repr += "%s " % (unicode(pick))
        repr += "\nCosts: %s" % (self.costs)
        return repr

if __name__ == "__main__":
    p = BBplayer("Hugo Schwarzhuf", "Amazonen", unicode("Fänger","latin-1"))
    print p.getMovement()
    print p.__repr__().encode("latin-1")