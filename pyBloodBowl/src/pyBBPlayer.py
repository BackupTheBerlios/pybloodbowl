# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.1"
__SSP_COMPLETION__ = 1
__SSP_TOUCHDOWN__ = 3
__SSP_INTERCEPTION__ = 2
__SSP_CASUALTY__ = 2
__SSP_MVP__ = 5

import pyBBParser

class BBPlayer:
    """This class represents a BloodBowl Player."""
    def __init__(self, name, team, position):
        self.name = str(name)
        self.team = team
        self.position = position
        self.teamparser  = pyBBParser.BBTeamParser()
        self.skillparser = pyBBParser.BBSkillParser()
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
        self.injury = 0             #injury
        self.ssp = 0                #starplayerpoints
        self.touchdowns = 0         #touchdown
        self.completions = 0        #completions
        self.interceptions = 0      #interceptions
        self.casualties = 0         #casualties
        self.mvpawards = 0          #most valuable player awards
        
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
        
    def setMovement(self, movement):
        """Set the players movement."""
        self.ma = movement
                
    def getStrength(self):
        """-> int
        Returns players strength."""
        return self.st
        
    def setStrength(self, strength):
        """Set the players strength."""
        self.st = strength
        
    def getAgility(self):
        """-> int
        Returns players agility."""
        return self.ag
        
    def setAgility(self, agility):
        """Set the players agility."""
        self.ag = agility
        
    def getArmor(self):
        """-> int
        Returns players armor value."""
        return self.av
        
    def setArmor(self, armor):
        """Set the players armor value."""
        self.av = armor
        
    def getCosts(self):
        """-> int
        Returns players costs."""
        return self.costs
        
    def getSkills(self):
        """-> list
        Returns a list of all player skills."""
        return self.skills
        
    def getPicks(self):
        """-> list
        Returns a list of all player picks."""
        return self.picks
        
    def getTouchdowns(self):
        """-> int
        Returns the number of scored touchdowns."""
        return self.touchdowns
        
    def addTouchdowns(self, number):
        """Adding a number of touchdowns."""
        self.touchdowns += number
        self.ssp += (number * __SSP_TOUCHDOWN__)
        
    def getCompletions(self):
        """- int
        Returns the number of completions."""
        return self.completions
        
    def addCompletions(self, number):
        """Adding a number of completions."""
        self.completions += number
        self.ssp += (number * __SSP_COMPLETION__)
        
    def getInterceptions(self):
        """-> int
        Returns the number of interceptions."""
        return self.interceptions
        
    def addInterceptions(self, number):
        """Adding a number of interceptions."""
        self.interceptions += number
        self.ssp += (number * __SSP_INTERCEPTION__)
        
    def getCasualties(self):
        """-> int
        Returns the number of caused casualties."""
        return self.casualties
        
    def addCasualties(self, number):
        """Adding a number of casualties."""
        self.casualties += number
        self.ssp += (number * __SSP_CASUALTY__)
        
    def getMVPAwards(self):
        """-> int
        Returns the number of earned MVP awards."""
        return self.mvpawards
        
    def addMVPAwards(self, number):
        """Adding a number of MVP Awards."""
        self.mvpawards += number
        self.ssp += (number * __SSP_MVP__)
        
    def getSSP(self):
        """-> int
        Returns the number of StarPlayerPoints."""
        return self.ssp
        
    def addNigglingInjury(self, number):
        """Gain a number of new niggling injuries."""
        self.injury += number
    
    def addSkill(self, newskill):
        """Add a newskill to the players list of skills."""
        self.skills.append( newskill )
        
    def isValidSkill(self, skill):
        """-> bool
        Checks if a given skill is valid for the player."""
        try:
            skills = self.skillparser.getSkills()
            skilldetails = skills[skill]
            if skilldetails[1] in self.picks:
                return True
            else:
                return False
        except KeyError:
            return False
        
    def __repr__(self):
        """String representation of the player."""
        repr = "%s (%s/%s)\nMA:%s\nST:%s\nAG:%s\nAV:%s\nSkills: " % (self.name, self.team, self.position, self.ma, self.st, self.ag, self.av)
        for skill in self.skills:
            repr += "%s " % (skill)
        repr += "\nPick: "
        for pick in self.picks:
            repr += "%s " % (pick)
        repr += "\nCosts: %s" % (self.costs)
        return repr

if __name__ == "__main__":
    p = BBPlayer("Hugo Schwarzhuf", "Chaos", unicode("Tiermensch","latin-1"))

    print p.__repr__().encode("latin-1")
    print p.isValidSkill("bla")
    p.addTouchdowns(2)
    print p.getSSP()