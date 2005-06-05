# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.0"
__date__ = "06.10.2004"

import pyBBParser
import pyBBPlayer

class BBSquad:
    """This class represents the squad of the team.
    Players can be added by calling the addPlayer method e.g.
    >>> myTeam = BBTeam("Menschen")
    >>> myTeam.addPlayer(3, BBPlayer("Rudi","Menschen","Werfer"))
    or
    >>> myTeam[3] = BBPlayer("Rudi","Menschen","Werfer")"""
    def __init__(self, team, max=16):
        """Constructor
        Specify a team and maximum number of players in the squad."""
        self.teamparser = pyBBParser.BBTeamParser()
        self.validteams = self.teamparser.getTeams()
        if self.isValidTeam(team) == False:
            err = "invalid team %s. valid teams are %s" % (team, self.validteams)
            raise TypeError, err
        self.team = team
        self.max = max
        self.players = {}
        
    def isValidPlayer(self, player):
        """-> bool
        Return true if the specified player can be added to the squad, otherwise false."""
        if player.getTeam() == self.team:
            return True
        else:
            return False
            
    def isValidTeam(self, team):
        """-> bool
        Return true if the specified team is valid, otherwise false."""
        if team in self.validteams:
            return True
        else:
            return False
        
    def addPlayer(self, number, player):
        """Adding a player with a specified number to the squad.
        Player must be an instance of pyBBPlayer.BBPlayer class."""
        if not isinstance(player, pyBBPlayer.BBPlayer):
            raise TypeError, "player must be a BBPlayer instance"
        if number > self.max:
            raise IndexError, "player number must between 1 and " + str(self.max)
        if self.isValidPlayer(player) == False:
            raise TypeError, "player must be valid for team " + str(self.team)
        self.players[number] = player
        
    def __setitem__(self, number, player):
        """Add a player to the squad with a specified number."""
        if not isinstance(player, pyBBPlayer.BBPlayer):
            raise TypeError, "player must be a BBPlayer instance"
        if number > self.max:
            raise IndexError, "player number must between 1 and " + str(self.max)
        if self.isValidPlayer(player) == False:
            raise TypeError, "player must be valid for team " + str(self.team)
        self.players[number] = player
        
    def removePlayer(self, number):
        """Remove a player from the squad with a specified number."""
        del(self.players[number])
        
    def __delitem__(self, number):
        """Remove a player from the squad with a specified number."""
        del(self.players[number])
        
    def getPlayer(self, number):
        """-> BBPlayer
        Return the player with the specified number."""
        try:
            return self.players[number]
        except KeyError:
            return None
        
    def __getitem__(self, number):
        """-> BBPlayer
        Return the player with the specified number."""
        try:
            return self.players[number]
        except KeyError:
            return None
        
    def getPlayers(self):
        """-> dict
        Return all players in a dictionary. See pyBBPlayer.BBPlayer."""
        return self.players
        
    def __len__(self):
        """-> int
        Return size of the squad."""
        return len(self.players)
        
    def __repr__(self):
        """String representation of the squad."""
        repr = "<BBTeam %s at %s>" % (self.max, hex(id(self)))
        return repr
        
if __name__ == "__main__":

    s = BBSquad("Amazonen")
    
    p1 = pyBBPlayer.BBPlayer("Heino","Amazonen","Blitzer")
    p2 = pyBBPlayer.BBPlayer("Ludwig","Amazonen","Werfer")
    p3 = pyBBPlayer.BBPlayer("Rudi","Amazonen","Werfer")
    s.addPlayer(1,p1)
    s[2] = p2
    print s.getPlayers()
    print len(s)
    s.removePlayer(2)
    print s.getPlayers()
    print len(s)
    s[4] = p2