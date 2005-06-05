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
    A test class for the pyBBSkill module.
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
#        for skill in self.skills.keys():
#            s = pyBBSkill.BBSkill(skill)
#            print s.__repr__().encode("latin-1")
#            pprint(s.getSkillname())
#            pprint(s.isTrait())
#            pprint(s.getCategory())
#            pprint(s.getDescription())
            
    def testTeamProperties(self):
        self.team = pyBBTeam.BBTeam("Rippers","Chaos", "Borak Killer", 4, 3)
        self.failUnless(self.team.getTeamProperties() == ('Rippers', 'Chaos', 'Borak Killer', 3, 0, 0), "Wrong team properties")
        print "testTeamProperties........................................passed"
        
    def testTeamSquad(self):
        self.team = pyBBTeam.BBTeam("Rippers","Chaos", "Borak Killer", 4, 3)
        self.failUnless(isinstance(self.team.getSquad(), pyBBSquad.BBSquad), "Squad must be instance of pyBBSquad.BBSquad")                    
        print "testTeamSquad.............................................passed"
        
    def testSquadSize(self):
        self.squad = pyBBSquad.BBSquad("Amazonen")
        p1 = pyBBPlayer.BBPlayer("Heino","Amazonen","Blitzer")
        p2 = pyBBPlayer.BBPlayer("Ludwig","Amazonen","Werfer")
        p3 = pyBBPlayer.BBPlayer("Rudi","Amazonen","Werfer")
        self.squad.addPlayer(1,p1)
        self.squad[2] = p2
        self.failUnless(len(self.squad) == 2, "Wrong number of squad members")
        self.squad.removePlayer(2)
        self.failUnless(len(self.squad) == 1, "Wrong number of squad members")
        self.squad.addPlayer(1, p3)
        self.failUnless(len(self.squad) == 1, "Wrong number of squad members")
        self.squad.removePlayer(1)
        self.failUnless(len(self.squad) == 0, "Wrong number of squad members")
        print "testSquadSize.............................................passed"
    
    def testSquadValidation(self):
        self.squad = pyBBSquad.BBSquad("Amazonen")
        p1 = pyBBPlayer.BBPlayer("Heino","Chaos","Tiermensch")
        p2 = pyBBPlayer.BBPlayer("Ludwig","Chaoszwerge","Hobgoblin")
        p3 = pyBBPlayer.BBPlayer("Rudi","Amazonen","Werfer")
        self.assertEqual(self.squad.isValidPlayer(p1), False, "Player should not be valid")
        self.assertEqual(self.squad.isValidPlayer(p2), False, "Player should not be valid")
        self.assertEqual(self.squad.isValidPlayer(p3), True, "Player should be valid")
        print "testSquadValidation.......................................passed"
        
if __name__ == '__main__':
    unittest.main()


