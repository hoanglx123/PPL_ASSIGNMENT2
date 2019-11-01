import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = str(Program([  
                            VarDecl(Id("a"), IntType())
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """int a, b[10], c, d[100];"""
        expect = str(Program([  
                            VarDecl(Id("a"), IntType()),
                            VarDecl(Id("b"), ArrayType(10, IntType())),
                            VarDecl(Id("c"), IntType()),
                            VarDecl(Id("d"), ArrayType(100, IntType())),
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))


    def test_simple_program3(self):
        """Simple program: void main() {} """
        input = """void main() {} """
        expect = str(Program([
                        FuncDecl(
                                Id("main"),
                                [],
                                VoidType(),
                                Block(["BLOCK_STATEMENT"])
                            )
                    ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
        
    # def test_simple_program3(self):
    #     """Simple program: int main() {} """
    #     input = """int a;"""
    #     expect = Program([
    #                         VarDecl(Id("a"), IntType())
    #                     ])
    #     print("Expect result: %s" % (expect))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
