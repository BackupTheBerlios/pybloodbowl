# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.1"

import xml.sax.handler

class BBSkillHandler(xml.sax.handler.ContentHandler):
    """Content Handler für skill.xml file. Wird von BBSkillParser verwendet."""    
    def __init__(self):
        self.buffer = ""
        self.mapping = {}
        
    def startElement(self, name, attributes):
        if name == "skill":
            self.buffer = ""
            self.type = ""
            self.category = ""
            self.name = attributes["name"]
            self.type = attributes["type"]
            self.category = attributes["category"]
 
    def characters(self, data):
        self.buffer += data
 
    def endElement(self, name):
        if name == "skill":
            self.mapping[self.name] = (self.type,self.category,self.buffer)
            
    def getSkills(self):
        return self.mapping

class BBSkillParser:
    """Skill Parser für skill.xml file. Verwendet BBSkillHandler."""
    def __init__(self, skillfile="config/skills.xml"):
        self.parser = xml.sax.make_parser()
        self.handler = BBSkillHandler()
        self.parser.setContentHandler(self.handler)
        self.parser.parse(skillfile)
        
    def getSkills(self):
        self.skills = self.handler.getSkills()
        return self.skills

class BBTeamHandler(xml.sax.handler.ContentHandler):
    """Content Handler für teams.xml file. Wird von BBTeamParser verwendet."""
    def __init__(self):
        self.buffer = ""
        self.mapping = {}
        self.positions = []
        self.teampositions = {}
        self.skillmapping = {}
        self.pickmapping = {}
        self.teams = []
        self.team = ""
        
    def startElement(self, name, attributes):
        if name == "team":
            self.team = attributes["name"]
            self.teams.append(attributes["name"])
            self.teampositions[self.team] = self.positions
        if name == "player":
            self.player = attributes["name"]
            self.mapping[(self.team,self.player)] = (attributes["max"],attributes["ma"],attributes["st"],attributes["ag"],attributes["av"],attributes["cost"])
            self.positions.append(self.player)
            self.skillmapping[(self.team,self.player)] = [] #initialize list
            self.pickmapping[(self.team,self.player)] = [] #initialize list
        if name == "skill":
            self.skillmapping[(self.team,self.player)].append(attributes["name"])
        if name == "pick":
            self.pickmapping[(self.team,self.player)].append(attributes["category"])
    
    def endElement(self, name):
        if name == "team":
            self.teampositions[self.team] = self.positions
            self.positions = []
    
    def getTeams(self):
        return self.teams
        
    def getPlayers(self):
        return self.mapping

    def getTeamPositions(self, team):
        print self.teampositions
        return self.teampositions[team]
        
    def getPlayerSkills(self):
        return self.skillmapping
        
    def getPlayerPicks(self):
        return self.pickmapping

class BBTeamParser:
    """Team Parser für teams.xml file. Verwendet BBTeamHandler."""
    def __init__(self, teamfile="config/teams.xml"):
        self.parser = xml.sax.make_parser()
        self.handler = BBTeamHandler()
        self.parser.setContentHandler(self.handler)
        self.parser.parse(teamfile)
        
    def getTeams(self):
        """-> List
        Returns all Teams in a list."""
        teams = self.handler.getTeams()
        return teams
        
    def getTeamPositions(self, team):
        """-> List
        Returns all position of the given team in a list."""
        return self.handler.getTeamPositions(team)
        
    def getPlayers(self):
        """-> Dict
        Returns all Players in a dictionary. Key is a tuple of Team and Position."""
        players = self.handler.getPlayers()
        return players
        
    def getPlayerSkills(self):
        """-> Dict
        Returns all Player Skills in a dictionary. Key is a tuple of Team and Position."""
        playerskills = self.handler.getPlayerSkills()
        return playerskills
    
    def getPlayerPicks(self):
        """-> Dict
        Returns all possible Player picks in a dictionary. Key is a tuple of Team and Position."""
        playerpicks = self.handler.getPlayerPicks()
        return playerpicks
    
if __name__ == "__main__":
    ##########################################################################
    ### Test
    ##########################################################################
    import pprint
    p = BBSkillParser()
    #pprint.pprint(p.getSkills())
    t = BBTeamParser()
    #pprint.pprint(t.getTeams())
    #pprint.pprint(t.getPlayers())
    pprint.pprint(t.getPlayerSkills())
    #pprint.pprint(t.getPlayerPicks())
    #pprint.pprint(t.getTeamPositions("Chaos"))
    