# -*- coding: Cp1252 -*-
__author__ = "Thorsten Schmidt"
__version__ = "0.1.0"
__IS_TRAIT__ = ["merkmal", "merkmale", "trait", "traits"]

import string

class BBSkill:
    """This class represents a skill, trait or racial characteristic.
    To create a skill object use
    
    >>> skill = BBSkill('Block', skillparser)
    
    The skillname must be found in the skills.xml config file, otherwise all skill properties will be empty."""
    def __init__(self, skillname, skillparser):
        """Constructor"""
        self.skillname = skillname
        self.skillparser = skillparser
        self.__initProperties()
        
    def __initProperties(self):
        """Initialize skill properties."""
        try:
            skillprops = self.skillparser.getSkill(self.skillname)
            self.type = skillprops[0]
            self.category = skillprops[1]
            self.description = skillprops[2]
        except KeyError, err:
            self.type = ""
            self.category = ""
            self.description = ""
            print "Invalid skill:", err
        
    def isTrait(self):
        """-> bool
        Returns true if the skill is a trait, otherwise false."""
        if string.lower(self.type) in __IS_TRAIT__:
            return True
        else:
            return False
        
    def getSkillname(self):
        """-> str
        Returns the name of the skill."""
        return self.skillname
        
    def getCategory(self):
        """-> str
        Returns the category of the skill."""
        return self.category
        
    def getDescription(self):
        """-> str
        Returns a detailed description of the skill/trait."""
        return self.description
        
    def __repr__(self):
        """String representation of a skill."""
        repr = "<BBSkill %s at %s>" % (self.skillname, hex(id(self)))
        return repr

if __name__ == "__main__":
    pass