# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.0.1"

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
        self.skillmapping = {}
        self.pickmapping = {}
        self.teams = []
        self.team = ""
        
    def startElement(self, name, attributes):
        if name == "team":
            self.team = attributes["name"]
            self.teams.append(attributes["name"])
        if name == "player":
            self.player = attributes["name"]
            self.mapping[(self.team,self.player)] = (attributes["max"],attributes["ma"],attributes["st"],attributes["ag"],attributes["av"],attributes["cost"])
            self.skillmapping[(self.team,self.player)] = [] #initialize list
            self.pickmapping[(self.team,self.player)] = [] #initialize list
        if name == "skill":
            self.skillmapping[(self.team,self.player)].append(attributes["name"])
        if name == "pick":
            self.pickmapping[(self.team,self.player)].append(attributes["category"])

class BBTeamParser:
    """Team Parser für teams.xml file. Verwendet BBTeamHandler."""
    def __init__(self, teamfile="config/teams.xml"):
        self.parser = xml.sax.make_parser()
        self.handler = BBTeamHandler()
        self.parser.setContentHandler(self.handler)
        self.parser.parse(skillfile)
        
if __name__ == "__main__":
    import pprint
    #p = BBSkillParser()
    #pprint.pprint(p.getSkills())
    parser = xml.sax.make_parser()
    handler = BBTeamHandler()
    parser.setContentHandler(handler)
    parser.parse("teams.xml")
    pprint.pprint(handler.teams)
    print ""
    pprint.pprint(handler.mapping)
    print ""
    pprint.pprint(handler.skillmapping)
    print ""
    pprint.pprint(handler.pickmapping)
    