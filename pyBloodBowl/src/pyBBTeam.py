# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.0"
__COSTS_FF__ = 10000
__COSTS_CHEERLEADER__ = 10000

import pyBBParser
import pyBBPlayer

class BBTeam:
    """This class represents a BloodBowl Team."""
    def __init__(self, teamname, team, coach, rerolls, fanfactor, cheerleader, apothecary):
        """Create a new Team with a given teamname and race(team)."""
        self.teamname = teamname
        self.team = team
        self.coach = coach
        self.rerolls = rerolls
        self.fanfactor = fanfactor
        self.cheerleader = cheerleader
        self.apothecary = apothecary
        self.treasury = 1000000
        self.players = []
        self.teamparser  = pyBBParser.BBTeamParser()
        self._initProperties()
        
    def _initProperties(self):
        #subtract some costs
        self.rrcosts = self.teamparser.getTeamRRCosts(self.team)
        rrcosts = self.rrcosts * self.rerolls
        self.treasury -= rrcosts
        self.treasury -= self.fanfactor * __COSTS_FF__
        self.treasury -= self.cheerleader * __COSTS_CHEERLEADER__
        
    def buyPlayer(self, player, index):
        """Buy a player to the team rooster at a given index. Treasury will be reduced by the player costs."""
        if not isinstance(player, pyBBPlayer.BBPlayer):
            raise TypeError, "player must be a BBPlayer instance"
        self.players.insert(index, player)
        self.treasury -= player.getCosts()
        
    def buyCheerleaders(self, number):
        """Buy a number of cheerleader. Treasury will be reduced by the costs."""
        self.cheerleader += number
        self.treasury -= number * __COSTS_CHEERLEADER__
        
    def buyRerolls(self, number):
        """Buy a number of rerolls. Treasury will be redueced by the costs."""
        self.rerolls += number
        self.treasury -= number * self.rrcosts
    
    def addPlayer(self, player, index):
        """Add a player to the team rooster at a given index."""
        if not isinstance(player, pyBBPlayer.BBPlayer):
            raise TypeError, "player must be a BBPlayer instance"
        self.players.insert(index, player)
    
    def __setitem__(self, index, player):
        """Add a player to the team rooster at a given index."""
        if not isinstance(player, pyBBPlayer.BBPlayer):
            raise TypeError, "player must be a BBPlayer instance"
        self.players.insert(index, player)
        
    def removePlayer(self, index):
        """Remove a player from the team rooster at a given index."""
        self.players.remove(index)
        
    def getTeamProperties(self):
        """-> tuple
        Returns a tuple of teamproperties (Teamname, Coach, Cheerleader, etc)."""
        props = (self.teamname,self.team,self.coach,self.fanfactor,self.cheerleader,self.apothecary)
        return props
        
    def getPlayers(self):
        """-> list
        Returns all players in a list. See pyBBPlayer.py and BBPlayer."""
        return self.players
        
    def __delitem__(self, index):
        """Remove a player from the team rooster at a given index."""
        self.players.remove(index)
                
    def __repr__(self):
        """String representation of the team."""
        repr = "%s (%s) - Coach: %s\n" % (self.teamname, self.team, self.coach)
        repr += "Treasury: %s Rerolls: %s\n" % (self.treasury, self.rerolls)
        repr += "Players:\n"
        for player in self.players:
            repr += "%s\n" % (unicode(player))
        return repr
        
if __name__ == "__main__":
    team = BBTeam("Rippers","Chaos", "Borak Killer", 4, 3, 0, 0)
    player1 = pyBBPlayer.BBPlayer("Hugo Schwarzhuf", "Chaos", unicode("Tiermensch","latin-1"))
    player2 = pyBBPlayer.BBPlayer("Benni Schwarzhuf", "Chaos", unicode("Tiermensch","latin-1"))
    team.buyPlayer(player1,1)
    team.buyPlayer(player2,2)
    team.buyCheerleaders(2)
    team.buyRerolls(2)
    print team.__repr__().encode("latin-1")