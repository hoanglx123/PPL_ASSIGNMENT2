import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """void main() {
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_doWhile_statement(self):
        """More complex program"""
        input = """int funcName1(boolean varBool, int varInt, float varFloat, string varString)
                    {
                        /* Declare variables */
                        boolean bFlag; 
                        int     varInt; 

                        /* Assignment */
                        bFlag = true; 

                        /* do-while statement */
                        do
                        {
                            int a; 
                        }
                        while(bFlag == true); 
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_for_statement(self):
        """More complex program"""
        input = """boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; varIndex < 10; varIndex = 100)
                        {
                            /* Do something */
                            varIndex = 12345;

                            varIndex = varIndex + 1.0; 
                        } 
                    }            
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_if_statement(self):
        """More complex program"""
        input = """boolean funcA(boolean bFlag)
                    {
                        int varInt; 

                        if(bFlag == true)
                        {
                            float varFloat; 
                            // varInt = 10;
                        }
                        else
                        {
                            string varStr; 
                        }
                    }                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    