import unittest

from pipes.steps.uppercase import Step

class uppercaseTest(unittest.TestCase):
    """
    A test class for the uppercaseTest module.
    """
    
    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.originalKey = 'original'
        self.originalValue = 'Hello Python'
        self.inputList = {self.originalKey: self.originalValue}
        


    def runTest(self):
        """
        Test a successful run. 
        1.The original value should not have changed. 
        2.The upper case value should be correct  
        """
        step = Step()
        step.run(self.inputList)

        
        self.assertEqual(self.originalValue, self.inputList[self.originalKey])
        self.assertEqual(self.originalValue.upper(), self.inputList['UCASE'])
        
        
        self.assertNotEqual(self.originalValue, self.inputList['UCASE'])
        

        