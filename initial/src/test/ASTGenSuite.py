import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_declare_simple(self):
        """var declare: int a; """
        input = """ int a, b[10], c, d[20], e[30];
                """
        expect = str(Program([  
                            VarDecl("a", IntType()), 
                            VarDecl("b", ArrayType(10, IntType())),
                            VarDecl("c", IntType()),
                            VarDecl("d", ArrayType(20, IntType())),
                            VarDecl("e", ArrayType(30, IntType())),
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_declare_complex(self):
        """var declare: int a; """
        input = """ int     varInt;
                    float   varFloat;
                    string  strArr[100];
                    boolean varBool1, varBool2; 
                """
        expect = str(Program([  
                            VarDecl("varInt",   IntType()), 
                            VarDecl("varFloat", FloatType()), 
                            VarDecl("strArr",   ArrayType(100, StringType())),
                            VarDecl("varBool1", BoolType()), 
                            VarDecl("varBool2", BoolType()), 
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))


    def test_func_declare_without_param(self):
        """Function declare without parameters """
        input = """ boolean funcA(){}
                    int     funcB(){}
                    float   funcC(){}
                    string  funcD(){} 
                    void    funcE(){}    
                    int[]   funcF(){}              
                """
        expect = str(Program([  
                            FuncDecl( Id("funcA"), [], BoolType(),   Block([]) ),
                            FuncDecl( Id("funcB"), [], IntType(),    Block([]) ),
                            FuncDecl( Id("funcC"), [], FloatType(),  Block([]) ),
                            FuncDecl( Id("funcD"), [], StringType(), Block([]) ),
                            FuncDecl( Id("funcE"), [], VoidType(),   Block([]) ),
                            FuncDecl( Id("funcF"), [], ArrayPointerType(IntType()), Block([]) ),
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    # def test_func_declare_with_params(self):
    #     """Function declare with parameters """
    #     input = """ boolean funcA(boolean varBool, int varInt, float varFloat, string varStr, int varArrList[]){}             
    #             """
    #     expect = str(Program([  
    #                             FuncDecl( 
    #                                     Id("funcA"), 
    #                                     [
    #                                         VarDecl("varBool",    BoolType()), 
    #                                         VarDecl("varInt",     IntType()), 
    #                                         VarDecl("varFloat",   FloatType()),
    #                                         VarDecl("varStr",     StringType()), 
    #                                         VarDecl("varArrList", ArrayPointerType(IntType())), 
    #                                     ], 
    #                                     BoolType(),   
    #                                     Block([]) 
    #                                 )
    #                     ]))
    #     print("Expect result: %s" % (expect))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))

    
    def test_func_declare_with_params(self):
        """Function declare with parameters """
        input = """ boolean funcA(boolean varBool){}             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("varBool",    BoolType())
                                        ], 
                                        BoolType(),   
                                        Block([]) 
                                    )
                        ]))
        print("Expect result: %s" % (expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    # def test_simple_program3(self):
    #     """Simple program: void main() {} """
    #     input = """void main() {} """
    #     expect = str(Program([
    #                     FuncDecl(
    #                             Id("main"),
    #                             [],
    #                             VoidType(),
    #                             Block(["BLOCK_STATEMENT"])
    #                         )
    #                 ]))
    #     print("Expect result: %s" % (expect))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
        
    # def test_simple_program3(self):
    #     """Simple program: int main() {} """
    #     input = """int a;"""
    #     expect = Program([
    #                         VarDecl(Id("a"), IntType())
    #                     ])
    #     print("Expect result: %s" % (expect))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
