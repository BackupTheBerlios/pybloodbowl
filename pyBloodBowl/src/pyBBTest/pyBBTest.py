import unittest
from pprint import pprint

import pyBBSkill
import pyBBParser

class BBSkillTest(unittest.TestCase):
    """
    A test class for the pyBBSkill module.
    """
    
    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.skillparser = pyBBParser.BBSkillParser()
        pass
  
    def tearDown(self):
        """
        tear down any data used in tests
        tearDown is called after each test function execution.
        """
        pass
        
    def testSkill(self):
        self.skills = self.skillparser.getSkills()
        for skill in self.skills.keys():
            s = pyBBSkill.BBSkill(skill)
            print s.__repr__().encode("latin-1")
            pprint(s.isTrait())
            pprint(s.getSkillname().encode("latin-1"))
            pprint(s.getCategory().encode("latin-1"))
            pprint(s.getDescription().encode("latin-1"))
        
if __name__ == '__main__':
    unittest.main()


