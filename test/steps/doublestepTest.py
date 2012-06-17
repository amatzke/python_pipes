import unittest

from pipes.steps.doublestep import Step

class doublestepTest(unittest.TestCase):
    """
    A test class for the doublestep module.
    """
    
    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.originalKey = 'original'
        self.originalValue = 'Hello Python'
        self.inputList = {self.originalKey: self.originalValue}     
        self.doubleKey = 'DOUBLE';


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
        self.assertEqual(self.originalValue + ' ' + self.originalValue, 
                         self.inputList[self.doubleKey])
                
        self.assertNotEqual(self.originalValue, self.inputList[self.doubleKey])
      

    def runExtendedTest(self):

        step = Step()
        self.inputList.clear();
        self.inputList = {self.originalKey:""}          
        step.run(self.inputList)
        self.assertEqual(" ", self.inputList[self.doubleKey])
                
   
      
        