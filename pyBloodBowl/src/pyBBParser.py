# -*- coding: Cp1252 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.2"
__encoding__ = "Cp1252"

import xml.sax.handler

class BBSkillHandler(xml.sax.handler.ContentHandler):
    """Content Handler for skill.xml file. Used by BBSkillParser."""    
    def __init__(self):
        #xml.sax.handler.ContentHandler.__init__()
        self.buffer = ""
        self.mapping = {}
        
    def startElement(self, name, attributes):
        if name == "skill":
            self.buffer = ""
            self.type = ""
            self.category = ""
            self.name = attributes["name"].encode(__encoding__)
            self.type = attributes["type"].encode(__encoding__)
            self.category = attributes["category"].encode(__encoding__)
 
    def characters(self, data):
        self.buffer += data.encode(__encoding__)
 
    def endElement(self, name):
        if name == "skill":
            self.mapping[self.name] = (self.type, self.category, self.buffer)
            
    def getSkills(self):
        return self.mapping
        
    def getSkill(self, skillname):
        return self.mapping[skillname]

class BBSkillParser:
    """Skill Parser for skill.xml file. Uses BBSkillHandler."""
    def __init__(self, skillfile="../config/skills.xml"):
        self.parser = xml.sax.make_parser()
        self.handler = BBSkillHandler()
        self.parser.setContentHandler(self.handler)
        self.parser.parse(skillfile)
        
    def getSkills(self):
        """-> dict
        Return all Team/Position skills. Key is a tuple of Team and Position."""
        self.skills = self.handler.getSkills()
        return self.skills
        
    def getSkill(self, skillname):
        """-> tuple
        Returns skill properties of a given skill."""
        return self.handler.getSkill(skillname)

class BBTeamHandler(xml.sax.handler.ContentHandler):
    """Content Handler for teams.xml file. Used by BBTeamParser."""
    def __init__(self):
        #xml.sax.handler.ContentHandler.__init__()
        self.buffer = ""
        self.mapping = {}
        self.positions = []
        self.teampositions = {}
        self.skillmapping = {}
        self.pickmapping = {}
        self.rrcosts = {}
        self.teams = []
        self.team = ""
        
    def startElement(self, name, attributes):
        if name == "team":
            self.team = attributes["name"].encode(__encoding__)
            self.rrcosts[self.team] = attributes["rr-cost"]
            self.teams.append(attributes["name"])
            self.teampositions[self.team] = self.positions
        if name == "player":
            self.player = attributes["name"].encode(__encoding__)
            self.mapping[(self.team,self.player)] = (attributes["max"].encode(__encoding__),attributes["ma"].encode(__encoding__),attributes["st"].encode(__encoding__),attributes["ag"].encode(__encoding__),attributes["av"].encode(__encoding__),attributes["cost"].encode(__encoding__))
            self.positions.append(self.player)
            self.skillmapping[(self.team,self.player)] = [] #initialize list
            self.pickmapping[(self.team,self.player)] = [] #initialize list
        if name == "skill":
            self.skillmapping[(self.team,self.player)].append(attributes["name"].encode(__encoding__))
        if name == "pick":
            self.pickmapping[(self.team, self.player)].append(attributes["category"].encode(__encoding__))
    
    def endElement(self, name):
        if name == "team":
            self.teampositions[self.team] = self.positions
            self.positions = []
    
    def getTeams(self):
        return self.teams
        
    def getPlayers(self):
        return self.mapping

    def getTeamPositions(self, team):
        return self.teampositions[team]
        
    def getPlayerSkills(self):
        return self.skillmapping
        
    def getPlayerPicks(self):
        return self.pickmapping
    
    def getRRCosts(self):
        return self.rrcosts

class BBTeamParser:
    """Team Parser for teams.xml file. Uses BBTeamHandler."""
    def __init__(self, teamfile="../config/teams.xml"):
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
        
    def getRRCosts(self):
        """-> Dict
        Returns all reroll costs of the teams in a dictionary. Key is the Team."""
        rrcosts = self.handler.getRRCosts()
        return rrcosts
        
    def getTeamRRCosts(self, team):
        """-> int
        Returns all reroll costs of the teams in a dictionary. Key is the Team."""
        rrcosts = self.handler.getRRCosts()
        rrc = int(rrcosts[team])
        return rrc
    
if __name__ == "__main__":
    ##########################################################################
    ### Test
    ##########################################################################
    import pprint
    p = BBSkillParser("../config/skills.xml")
    pprint.pprint(p.getSkills())
    t = BBTeamParser("../config/teams.xml")
    pprint.pprint(t.getTeams())
    pprint.pprint(t.getPlayers())
    pprint.pprint(t.getPlayerSkills())
    pprint.pprint(t.getPlayerPicks())
    pprint.pprint(t.getTeamPositions("Chaos"))    