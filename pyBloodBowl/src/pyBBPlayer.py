# -*- coding: utf-8 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.0.1"

class BBplayer:
    
    def __init__(self, name, rasse, position):
        self.name = str(name)
        self.rasse = rasse
        self.position = position
        self.skills = []
    
    def addSkill(self, newskill):
        self.skills.append( newskill )
        
    def isValidSkill(self, skill):
        return True