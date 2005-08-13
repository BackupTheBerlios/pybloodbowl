import unittest
import os
from pprint import pprint

import pyBBSkill
import pyBBParser
import pyBBTeam
import pyBBSquad
import pyBBPlayer

class BBTest(unittest.TestCase):
    """
    A test class for the pyBloodBowl project.
    """
    
    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.skillparser = pyBBParser.BBSkillParser()
        self.teamparser  = pyBBParser.BBTeamParser()
  
    def tearDown(self):
        """
        tear down any data used in tests
        tearDown is called after each test function execution.
        """
        pass
        
    def testSkills(self):
        self.skills = self.skillparser.getSkills()
        self.failUnless(type(self.skills) == type({}), "Skills must be a dictionary")
        for skill in self.skills.keys():
            skillobj = pyBBSkill.BBSkill(skill, self.skillparser)
            self.failUnless(isinstance(skillobj, pyBBSkill.BBSkill), "Skills must be an instance of pyBBSkill.BBSkill")
        #print "testSkills................................................passed"
        
    def testSkill(self):
        skill = pyBBSkill.BBSkill("Blocken", self.skillparser)
        self.failUnless(skill.getSkillname() == "Blocken", "Wrong skillname")
        self.failUnless(skill.getCategory() == "Allgeimein", "Wrong category")
        self.failUnless(skill.isTrait() == False, "Skill should not be trait")
        #print "testSkill.................................................passed"
            
    def testTeamProperties(self):
        self.team = pyBBTeam.BBTeam("Rippers","Chaos", "Borak Killer", 4, 3)
        self.failUnless(self.team.getTeamProperties() == ('Rippers', 'Chaos', 'Borak Killer', 3, 0, 0), "Wrong team properties")
        #print "testTeamProperties........................................passed"
        
    def testTeamSquad(self):
        self.team = pyBBTeam.BBTeam("Rippers","Chaos", "Borak Killer", 4, 3)
        self.failUnless(isinstance(self.team.getSquad(), pyBBSquad.BBSquad), "Squad must be instance of pyBBSquad.BBSquad")                    
        #print "testTeamSquad.............................................passed"
        
    def testSquadSize(self):
        self.squad = pyBBSquad.BBSquad(self.teamparser, "Amazonen")
        p1 = pyBBPlayer.BBPlayer("Heino","Amazonen","Blitzer", self.teamparser, self.skillparser)
        p2 = pyBBPlayer.BBPlayer("Ludwig","Amazonen","Werfer", self.teamparser, self.skillparser)
        p3 = pyBBPlayer.BBPlayer("Rudi","Amazonen","Werfer", self.teamparser, self.skillparser)
        self.squad.addPlayer(1,p1)
        self.squad[2] = p2
        self.failUnless(len(self.squad) == 2, "Wrong number of squad members")
        self.squad.removePlayer(2)
        self.failUnless(len(self.squad) == 1, "Wrong number of squad members")
        self.squad.addPlayer(1, p3)
        self.failUnless(len(self.squad) == 1, "Wrong number of squad members")
        self.squad.removePlayer(1)
        self.failUnless(len(self.squad) == 0, "Wrong number of squad members")
        #print "testSquadSize.............................................passed"
    
    def testSquadValidation(self):
        self.squad = pyBBSquad.BBSquad(self.teamparser, "Amazonen")
        p1 = pyBBPlayer.BBPlayer("Heino","Chaos","Tiermensch", self.teamparser, self.skillparser)
        p2 = pyBBPlayer.BBPlayer("Ludwig","Chaoszwerge","Hobgoblin", self.teamparser, self.skillparser)
        p3 = pyBBPlayer.BBPlayer("Rudi","Amazonen","Werfer", self.teamparser, self.skillparser)
        self.assertEqual(self.squad.isValidPlayer(p1), False, "Player should not be valid")
        self.assertEqual(self.squad.isValidPlayer(p2), False, "Player should not be valid")
        self.assertEqual(self.squad.isValidPlayer(p3), True, "Player should be valid")
        #print "testSquadValidation.......................................passed"
        
    def testSquadGetPlayers(self):
        self.squad = pyBBSquad.BBSquad(self.teamparser, "Amazonen")
        p1 = pyBBPlayer.BBPlayer("Lara","Amazonen","Feldspieler", self.teamparser, self.skillparser)
        p2 = pyBBPlayer.BBPlayer("Tara","Amazonen","Feldspieler", self.teamparser, self.skillparser)
        p3 = pyBBPlayer.BBPlayer("Mara","Amazonen","Werfer", self.teamparser, self.skillparser)
        self.squad.addPlayer(1, p1)
        self.squad.addPlayer(3, p2)
        self.squad.addPlayer(5, p3)
        playersdict = self.squad.getPlayers()
        self.failUnless(type(playersdict) == type({}), "Method getPlayers() should return a dictionary")
        self.failUnless(playersdict.has_key(1), "Player dictionary should contain no 1")
        self.failUnless(playersdict.has_key(3), "Player dictionary should contain no 3")
        self.failUnless(playersdict.has_key(5), "Player dictionary should contain no 5")
        self.failIf(playersdict.has_key(2), "Player dictionary should not contain no 2")
        #print "testSquadGetPlayers.......................................passed"
        
if __name__ == '__main__':
    unittest.main()


