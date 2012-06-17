import unittest
import datetime

        
from pipes.steps.datestep import Step

class datestepTest(unittest.TestCase):
    """
    A test class for the dateStep module.
    """
    
    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.originalKey = 'original'
        self.originalValue = 'Hello Python'
        self.inputList = {self.originalKey: self.originalValue}     
        self.dateKey = 'DATE';


    def runBasicTest(self):
        """
        Test a successful run. 
        1.The original value should not have changed. 
        2.The upper case value should be correct  
        """
        step = Step()
        step.run(self.inputList)

        """check original value is not changed"""
        self.assertEqual(self.originalValue, self.inputList[self.originalKey])
        
        """check that new value is correct"""
        now = datetime.datetime.now() 
        self.assertEqual(str(now), self.inputList[self.dateKey])
                
        self.assertNotEqual(self.originalValue, self.inputList[self.dateKey])
      

        