import unittest
from TestUtils import TestAST
from AST import *
import inspect

class ASTGenSuite(unittest.TestCase):
    def test_var_declare_simple(self):
        """var declare: simple """
        input = """ int a, b[10], c, d[20], e[30];
                """
        expect = str(Program([  
                            VarDecl("a", IntType()), 
                            VarDecl("b", ArrayType(10, IntType())),
                            VarDecl("c", IntType()),
                            VarDecl("d", ArrayType(20, IntType())),
                            VarDecl("e", ArrayType(30, IntType())),
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_declare_complex(self):
        """var declare: complex """
        input = """ int     varInt;
                    float   varFloat; int varInt2; int varInt3;
                    string  strArr[100];
                    boolean varBool1, varBool2; 
                """  
        expect = str(Program([  
                            VarDecl("varInt",   IntType()), 
                            VarDecl("varFloat", FloatType()), 
                            VarDecl("varInt2",   IntType()), 
                            VarDecl("varInt3",   IntType()), 
                            VarDecl("strArr",   ArrayType(100, StringType())),
                            VarDecl("varBool1", BoolType()), 
                            VarDecl("varBool2", BoolType()), 
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
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
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_func_declare_with_params(self):
        """Function declare with parameters """
        input = """ boolean funcA(boolean varBool, int varInt, float varFloat, int varArrList[], string varStr){}             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("varBool",    BoolType()), 
                                            VarDecl("varInt",     IntType()), 
                                            VarDecl("varFloat",   FloatType()),
                                            VarDecl("varArrList", ArrayPointerType(IntType())), 
                                            VarDecl("varStr",     StringType())
                                        ], 
                                        BoolType(),   
                                        Block([]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_func_declare_with_params_in_body(self):
        """Function declare with params in body """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt;
                        float   varFloat; 
                        string  strArr[100];
                        boolean varBool1, varBool2; 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("varArrList", ArrayPointerType(IntType())), 
                                            VarDecl("varStr",     StringType())
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt",   IntType()), 
                                            VarDecl("varFloat", FloatType()), 
                                            VarDecl("strArr",   ArrayType(100, StringType())),
                                            VarDecl("varBool1", BoolType()), 
                                            VarDecl("varBool2", BoolType()), 
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_assignment_statement_simple(self):
        """Assignment statement: simple """
        input = """ int     varInt;
                    float   varFloat; 
                    boolean varBool; 

                    boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt;
                        float   varFloat; 
                        string  strArr[100];
                        boolean varBool1, varBool2; 

                        varInt   = 10;
                        varFloat = 10.4;
                        varBool1 = true; 
                        varBool2 = false; 
                    }       
                """  
        expect = str(Program([  
                        VarDecl("varInt",   IntType()), 
                        VarDecl("varFloat", FloatType()), 
                        VarDecl("varBool",  BoolType()), 
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt",   IntType()), 
                                        VarDecl("varFloat", FloatType()), 
                                        VarDecl("strArr",   ArrayType(100, StringType())),
                                        VarDecl("varBool1", BoolType()), 
                                        VarDecl("varBool2", BoolType()), 

                                        BinaryOp("=", Id("varInt"),    IntLiteral(10)),
                                        BinaryOp("=", Id("varFloat"),  FloatLiteral(10.4)),
                                        BinaryOp("=", Id("varBool1"),  BooleanLiteral(True)),
                                        BinaryOp("=", Id("varBool2"),  BooleanLiteral(False)),
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_assignment_statement_complex(self):
        """Assignment statement: complex1 """
        input = """ int     varInt;
                    float   varFloat; 
                    boolean varBool; 

                    boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt;
                        float   varFloat; 
                        string  strArr[100];
                        //boolean varBool[2]; 

                        varInt     = 10;
                        varFloat   = 10.4;
                        //varBool[0] = true; 
                        //varBool[1] = false; 
                    }       
                """  
        expect = str(Program([  
                        VarDecl("varInt",   IntType()), 
                        VarDecl("varFloat", FloatType()), 
                        VarDecl("varBool",  BoolType()), 
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt",   IntType()), 
                                        VarDecl("varFloat", FloatType()), 
                                        VarDecl("strArr",   ArrayType(100, StringType())),
                                        # VarDecl("varBool1", BoolType()), 
                                        # VarDecl("varBool2", BoolType()), 

                                        BinaryOp("=", Id("varInt"),    IntLiteral(10)),
                                        BinaryOp("=", Id("varFloat"),  FloatLiteral(10.4)),
                                        # BinaryOp("=", Id("varBool1"),  BooleanLiteral(True)),
                                        # BinaryOp("=", Id("varBool2"),  BooleanLiteral(False)),
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_intExpr_ADDOP(self):
        """Int expression: operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 + varInt2 + 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "+", 
                                                            Id("varInt1"),
                                                            BinaryOp( "+",  Id("varInt2"), IntLiteral(100))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_intExpr_SUBOP(self):
        """Int expression: operator('-') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 - varInt2 - 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "-", 
                                                            Id("varInt1"),
                                                            BinaryOp( "-",  Id("varInt2"), IntLiteral(10))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_intExpr_mix_ADDOP_SUBOP(self):
        """Int expression: mix operator('+') and operator('-') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 + varInt2 - 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "+", 
                                                            Id("varInt1"),
                                                            BinaryOp( "-",  Id("varInt2"), IntLiteral(10))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_intExpr_mix_SUBOP_ADDOP(self):
        """Int expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 - varInt2 + 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "-", 
                                                            Id("varInt1"),
                                                            BinaryOp( "+",  Id("varInt2"), IntLiteral(10))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_intExpr_mix_SUBOP_ADDOP2(self):
        """Int expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = (varInt1 - varInt2) + 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=",
                                                  Id("varInt1"),
                                                  BinaryOp( "+", 
                                                            BinaryOp("-", Id("varInt1"),Id("varInt2")),
                                                            IntLiteral(10)
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_intExpr_mix_SUBOP_ADDO3(self):
        """Int expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 - (varInt2 + 10);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp("=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp("=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "-", 
                                                            Id("varInt1"),
                                                            BinaryOp( "+",  Id("varInt2"), IntLiteral(10))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_intExpr_DIVOP(self):
        """Int expression: operator('/') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 * varInt2 * 5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "*", 
                                                            Id("varInt1"),
                                                            BinaryOp( "*",  Id("varInt2"), IntLiteral(5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_intExpr_MULOP(self):
        """Int expression: operator('*') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 / varInt2 / 5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "/", 
                                                            Id("varInt1"),
                                                            BinaryOp( "/",  Id("varInt2"), IntLiteral(5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_intExpr_MODOP(self):
        """Int expression: operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 % varInt2 % 5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", 
                                                  Id("varInt1"), 
                                                  BinaryOp( "%", 
                                                            Id("varInt1"),
                                                            BinaryOp( "%",  Id("varInt2"), IntLiteral(5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_intExpr_mix_DIVOP_MODOP_MODOP(self):
        """Int expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 * varInt2 / 5 % 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=",
                                                  Id("varInt1"),
                                                  BinaryOp("*",
                                                            Id("varInt1"),
                                                            BinaryOp("/",
                                                                    Id("varInt2"),
                                                                    BinaryOp("%",IntLiteral(5),IntLiteral(10)))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_intExpr_mix_DIVOP_MODOP_MODOP2(self):
        """Int expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 * (varInt2 / 5) % 10;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",
                                                Id("varInt1"),
                                                BinaryOp("*",
                                                        Id("varInt1"), 
                                                        BinaryOp("%", 
                                                            BinaryOp("/", 
                                                                    Id("varInt2"),
                                                                    IntLiteral(5)
                                                            ),
                                                        IntLiteral(10))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_intExpr_mix_DIVOP_MODOP_MODOP3(self):
        """Int expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int varInt1;
                        int varInt2; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varInt1 = varInt1 * varInt2 / (5 % 10);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varInt1"),BinaryOp("*",Id("varInt1"),BinaryOp("/",Id("varInt2"),BinaryOp("%",IntLiteral(5),IntLiteral(10)))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_intExpr_LTHOP(self):
        """Int expression: operator('<') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 < varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("<",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_intExpr_LEQOP(self):
        """Int expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 <= varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("<=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_intExpr_GTHOP(self):
        """Int expression: operator('>') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 > varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_intExpr_GEQOP(self):
        """Int expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 >= varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_intExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP(self):
        """Int expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 < varInt2 <= 10 > 5 >= 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">=",BinaryOp("<=",BinaryOp("<",Id("varInt1"),Id("varInt2")),BinaryOp(">",IntLiteral(10),IntLiteral(5))),IntLiteral(100)))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_intExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP2(self):
        """Int expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = (varInt1 < varInt2) <= (10 > 5 >= 100);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", Id("varBool"),BinaryOp("<=",BinaryOp("<",Id("varInt1"),Id("varInt2")),BinaryOp(">=",BinaryOp(">",IntLiteral(10),IntLiteral(5)),IntLiteral(100))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_intExpr_EQOP(self):
        """Int expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 == varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("==",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_intExpr_NEQOP(self):
        """Int expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 != varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("!=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_intExpr_ANDOP(self):
        """Int expression: operator('&&') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 && varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("&&",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_intExpr_OROP(self):
        """Int expression: operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 || varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("||",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_intExpr_mix_EQOP_NEQOP_ANDOP_OROP(self):
        """Int expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 == varInt2 && varInt1 != 100 || varInt2 != 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("varInt1"),Id("varInt2")),BinaryOp("!=",Id("varInt1"),IntLiteral(100))),BinaryOp("!=",Id("varInt2"),IntLiteral(100))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_intExpr_mix_EQOP_NEQOP_ANDOP_OROP2(self):
        """Int expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 == (varInt2 && varInt1) != (100 || varInt2) != 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("!=",BinaryOp("!=",BinaryOp("=""=",Id("varInt1"),BinaryOp("&&",Id("varInt2"),Id("varInt1"))),BinaryOp("||",IntLiteral(100),Id("varInt2"))),IntLiteral(100)))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_floatExpr_ADDOP(self):
        """Float expression: operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 + varFloat2 + 100.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "+", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "+",  Id("varFloat2"), FloatLiteral(100.0))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_floatExpr_SUBOP(self):
        """Float expression: operator('-') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 - varFloat2 - 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "-", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "-",  Id("varFloat2"), FloatLiteral(10.5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_floatExpr_mix_ADDOP_SUBOP(self):
        """Float expression: mix operator('+') and operator('-') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 + varFloat2 - 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "+", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "-",  Id("varFloat2"), FloatLiteral(10.5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_floatExpr_mix_SUBOP_ADDOP(self):
        """Float expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 - varFloat2 + 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "-", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "+",  Id("varFloat2"), FloatLiteral(10.5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_floatExpr_mix_SUBOP_ADDOP2(self):
        """Float expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = (varFloat1 - varFloat2) + 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=",
                                                  Id("varFloat1"),
                                                  BinaryOp( "+", 
                                                            BinaryOp("-", Id("varFloat1"),Id("varFloat2")),
                                                            FloatLiteral(10.5)
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_floatExpr_mix_SUBOP_ADDO3(self):
        """Float expression: mix operator('-') and operator('+') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 - (varFloat2 + 10.5);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp("=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp("=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "-", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "+",  Id("varFloat2"), FloatLiteral(10.5))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_floatExpr_DIVOP(self):
        """Float expression: operator('/') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 * varFloat2 * 5.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "*", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "*",  Id("varFloat2"), FloatLiteral(5.0))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_floatExpr_MULOP(self):
        """Float expression: operator('*') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 / varFloat2 / 5.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "/", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "/",  Id("varFloat2"), FloatLiteral(5.0))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_floatExpr_MODOP(self):
        """Float expression: operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 % varFloat2 % 5.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=", 
                                                  Id("varFloat1"), 
                                                  BinaryOp( "%", 
                                                            Id("varFloat1"),
                                                            BinaryOp( "%",  Id("varFloat2"), FloatLiteral(5.0))
                                                        )
                                                )
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_floatExpr_mix_DIVOP_MODOP_MODOP(self):
        """Float expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 * varFloat2 / 5.0 % 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp( "=",
                                                  Id("varFloat1"),
                                                  BinaryOp("*",
                                                            Id("varFloat1"),
                                                            BinaryOp("/",
                                                                    Id("varFloat2"),
                                                                    BinaryOp("%",FloatLiteral(5.0),FloatLiteral(10.5)))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_floatExpr_mix_DIVOP_MODOP_MODOP2(self):
        """Float expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 * (varFloat2 / 5.0) % 10.5;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",
                                                Id("varFloat1"),
                                                BinaryOp("*",
                                                        Id("varFloat1"), 
                                                        BinaryOp("%", 
                                                            BinaryOp("/", 
                                                                    Id("varFloat2"),
                                                                    FloatLiteral(5.0)
                                                            ),
                                                        FloatLiteral(10.5))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_floatExpr_mix_DIVOP_MODOP_MODOP3(self):
        """Float expression: mix operator('*'), operator('/'), operator('%') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float varFloat1;
                        float varFloat2; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varFloat1 = varFloat1 * varFloat2 / (5.0 % 10.5);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varFloat1"),BinaryOp("*",Id("varFloat1"),BinaryOp("/",Id("varFloat2"),BinaryOp("%",FloatLiteral(5.0),FloatLiteral(10.5)))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_floatExpr_LTHOP(self):
        """Float expression: operator('<') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 < varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("<",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_floatExpr_LEQOP(self):
        """Float expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 <= varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("<=",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_floatExpr_GTHOP(self):
        """Float expression: operator('>') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 > varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_floatExpr_GEQOP(self):
        """Float expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 >= varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">=",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_floatExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP(self):
        """Float expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 > varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_floatExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP2(self):
        """Float expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = (varFloat1 < varFloat2);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("<",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_floatExpr_EQOP(self):
        """Float expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 == varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("==",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_floatExpr_NEQOP(self):
        """Float expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 != varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("!=",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_floatExpr_ANDOP(self):
        """Float expression: operator('&&') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 && varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("&&",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_floatExpr_OROP(self):
        """Float expression: operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 || varFloat2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("||",Id("varFloat1"),Id("varFloat2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_floatExpr_mix_EQOP_NEQOP_ANDOP_OROP(self):
        """Float expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 == varFloat2 && varFloat1 != 100.0 || varFloat2 != 100.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("varFloat1"),Id("varFloat2")),BinaryOp("!=",Id("varFloat1"),FloatLiteral(100.0))),BinaryOp("!=",Id("varFloat2"),FloatLiteral(100.0))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_floatExpr_mix_EQOP_NEQOP_ANDOP_OROP2(self):
        """Float expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        float   varFloat1;
                        float   varFloat2; 
                        boolean varBool; 

                        varFloat1 = 100.0;
                        varFloat2 = 10.5; 
                        varBool = varFloat1 == (varFloat2 && varFloat1) != (100.0 || varFloat2) != 100.0;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varFloat1", FloatType()), 
                                        VarDecl("varFloat2", FloatType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varFloat1"), FloatLiteral(100.0)),
                                        BinaryOp( "=", Id("varFloat2"), FloatLiteral(10.5)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("!=",BinaryOp("!=",BinaryOp("=""=",Id("varFloat1"),BinaryOp("&&",Id("varFloat2"),Id("varFloat1"))),BinaryOp("||",FloatLiteral(100.0),Id("varFloat2"))),FloatLiteral(100.0)))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))


    def test_boolExpr_LTHOP(self):
        """Bool expression: operator('<') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 < varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",  Id("varBool"),BinaryOp("<",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_boolExpr_LEQOP(self):
        """Bool expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 <= varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", Id("varBool"),BinaryOp("<=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_boolExpr_GTHOP(self):
        """Bool expression: operator('>') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 > varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_boolExpr_GEQOP(self):
        """Bool expression: operator('>=') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 >= varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp(">=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_boolExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP(self):
        """Bool expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 < varInt2 <= 10 > 5 >= 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", Id("varBool"),BinaryOp(">=",BinaryOp("<=",BinaryOp("<",Id("varInt1"),Id("varInt2")),BinaryOp(">",IntLiteral(10),IntLiteral(5))),IntLiteral(100)))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_boolExpr_mxi_LTHOP_LEQOP_GTHOP_GTHOP2(self):
        """Bool expression: mix operator('<'), operator('<='), operator('>'), operator('>=') """
        input = """ boolean funcA()
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = (varInt1 < varInt2) <= (10 > 5 >= 100);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp( "=", Id("varBool"),BinaryOp("<=",BinaryOp("<",Id("varInt1"),Id("varInt2")),BinaryOp(">=",BinaryOp(">",IntLiteral(10),IntLiteral(5)),IntLiteral(100))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_boolExpr_EQOP(self):
        """Bool expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 == varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("==",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_boolExpr_NEQOP(self):
        """Bool expression: operator('==') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        int     varInt1;
                        int     varInt2; 
                        boolean varBool; 

                        varInt1 = 100;
                        varInt2 = 10; 
                        varBool = varInt1 != varInt2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varInt1", IntType()), 
                                        VarDecl("varInt2", IntType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varInt1"), IntLiteral(100)),
                                        BinaryOp( "=", Id("varInt2"), IntLiteral(10)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("!=",Id("varInt1"),Id("varInt2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_boolExpr_ANDOP(self):
        """Bool expression: operator('&&') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        boolean varBool1;
                        boolean varBool2; 
                        boolean varBool; 

                        varBool1 = true;
                        varBool2 = false; 
                        varBool  = varBool1 && varBool2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varBool1", BoolType()), 
                                        VarDecl("varBool2", BoolType()), 
                                        VarDecl("varBool",  BoolType()),
                                        BinaryOp( "=", Id("varBool1"), BooleanLiteral(True)),
                                        BinaryOp( "=", Id("varBool2"), BooleanLiteral(False)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("&&",Id("varBool1"),Id("varBool2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_boolExpr_OROP(self):
        """Bool expression: operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        boolean varBool1;
                        boolean varBool2; 
                        boolean varBool; 

                        varBool1 = true;
                        varBool2 = false; 
                        varBool = varBool1 || varBool2;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varBool1", BoolType()), 
                                        VarDecl("varBool2", BoolType()), 
                                        VarDecl("varBool", BoolType()),
                                        BinaryOp( "=", Id("varBool1"), BooleanLiteral(True)),
                                        BinaryOp( "=", Id("varBool2"), BooleanLiteral(False)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("||",Id("varBool1"),Id("varBool2")))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_boolExpr_mix_EQOP_NEQOP_ANDOP_OROP(self):
        """Bool expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        boolean varBool1;
                        boolean varBool2; 
                        int     varInt; 
                        boolean varBool; 

                        varBool1 = true;
                        varBool2 = false; 
                        varInt   = 100; 
                        varBool  = varBool1 == varBool2 && varInt > 100;
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varBool1", BoolType()), 
                                        VarDecl("varBool2", BoolType()), 
                                        VarDecl("varInt",   IntType()), 
                                        VarDecl("varBool",  BoolType()),
                                        BinaryOp( "=", Id("varBool1"), BooleanLiteral(True)),
                                        BinaryOp( "=", Id("varBool2"), BooleanLiteral(False)),
                                        BinaryOp( "=", Id("varInt"),   IntLiteral(100)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("&&",BinaryOp("==",Id("varBool1"),Id("varBool2")),BinaryOp(">",Id("varInt"),IntLiteral(100))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_boolExpr_mix_EQOP_NEQOP_ANDOP_OROP2(self):
        """Bool expression: mix operator('=='), operator('!='), operator('&&'), operator('||') """
        input = """ boolean funcA(int varArrList[], string varStr)
                    {
                        boolean varBool1;
                        boolean varBool2; 
                        int     varInt; 
                        boolean varBool; 

                        varBool1 = true;
                        varBool2 = false; 
                        varInt   = 100; 
                        varBool  = varBool1 == varBool2 && (varInt > 100);
                    }       
                """  
        expect = str(Program([  
                        FuncDecl( 
                                    Id("funcA"), 
                                    [
                                        VarDecl("varArrList", ArrayPointerType(IntType())), 
                                        VarDecl("varStr",     StringType())
                                    ], 
                                    BoolType(),   
                                    Block([
                                        VarDecl("varBool1", BoolType()), 
                                        VarDecl("varBool2", BoolType()), 
                                        VarDecl("varInt",   IntType()), 
                                        VarDecl("varBool",  BoolType()),
                                        BinaryOp( "=", Id("varBool1"), BooleanLiteral(True)),
                                        BinaryOp( "=", Id("varBool2"), BooleanLiteral(False)),
                                        BinaryOp( "=", Id("varInt"),   IntLiteral(100)),
                                        BinaryOp("=",Id("varBool"),BinaryOp("&&",BinaryOp("==",Id("varBool1"),Id("varBool2")),BinaryOp(">",Id("varInt"),IntLiteral(100))))
                                    ]) 
                                )
                    ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_if_statement_without_else(self):
        """If-statement without else """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int varInt; 

                        if(true)
                        {
                            float varFloat; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt", IntType()),
                                            If( 
                                                BooleanLiteral(True), 
                                                Block([
                                                    VarDecl("varFloat", FloatType()),
                                                ]), 
                                                None 
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_if_statement_with_else(self):
        """If-statement with else statement """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int varInt; 

                        if(true)
                        {
                            float varFloat; 
                        }
                        else
                        {
                            string varStr; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt", IntType()),
                                            If( 
                                                BooleanLiteral(True), 
                                                Block([
                                                    VarDecl("varFloat", FloatType()),
                                                ]), 
                                                Block([
                                                    VarDecl("varStr", StringType()),
                                                ]), 
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_if_statement_complex(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int varInt; 

                        if(bFlag == true)
                        {
                            float varFloat; 
                        }
                        else
                        {
                            string varStr; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt", IntType()),
                                            If( 
                                                BinaryOp("==", Id("bFlag"), BooleanLiteral(True)), 
                                                Block([
                                                    VarDecl("varFloat", FloatType()),
                                                ]), 
                                                Block([
                                                    VarDecl("varStr", StringType()),
                                                ]), 
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_if_statement_complex(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int varInt1;
                        int varInt2;
                         
                        varInt1 = 100; 
                        varInt2 = 10; 

                        if(varInt1 > varInt2)
                        {
                            float varFloat; 
                        }
                        else
                        {
                            string varStr; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1", IntType()),
                                            VarDecl("varInt2", IntType()),
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            If( 
                                                BinaryOp(">", Id("varInt1"), Id("varInt2")), 
                                                Block([
                                                    VarDecl("varFloat", FloatType()),
                                                ]), 
                                                Block([
                                                    VarDecl("varStr", StringType()),
                                                ]), 
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_if_statement_complex2(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        if((varInt1 > varInt2) && varBool)
                        {
                            float varFloat; 
                        }
                        else
                        {
                            string varStr; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1", IntType()),
                                            VarDecl("varInt2", IntType()),
                                            VarDecl("varBool", BoolType()),
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            If( BinaryOp("&&",BinaryOp(">",Id("varInt1"),Id("varInt2")),Id("varBool")),
                                                Block([VarDecl("varFloat",FloatType())]),
                                                Block([VarDecl("varStr",StringType())]))
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_if_statement_complex3(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        if(((varInt1 - varInt2) - 50) && (varBool && true))
                        {
                            float varFloat; 
                        }
                        else
                        {
                            string varStr; 
                        }
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1", IntType()),
                                            VarDecl("varInt2", IntType()),
                                            VarDecl("varBool", BoolType()),
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            If( BinaryOp("&&",BinaryOp("-",BinaryOp("-",Id("varInt1"),Id("varInt2")),IntLiteral(50)),BinaryOp("&&",Id("varBool"),BooleanLiteral(True))),
                                                Block([VarDecl("varFloat",FloatType())]),
                                                Block([VarDecl("varStr",StringType())]))
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_if_statement_complex4(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        if(bFlag == true)
                        {
                            float varFloat1; 

                            if(bFlag != true)
                            {
                                float varFloat2; 
                            }
                        }
                    }             
                """
        expect = str(Program([
                                FuncDecl(Id("funcA"),
                                [VarDecl("bFlag",BoolType())],
                                BoolType(),
                                Block([If(BinaryOp("==",Id("bFlag"),BooleanLiteral(True)),
                                        Block([VarDecl("varFloat1",FloatType()),
                                        If( BinaryOp("!=",Id("bFlag"),BooleanLiteral(True)),
                                            Block([VarDecl("varFloat2",FloatType())]), 
                                            None)  
                                        ]), None
                                    )]))
                            ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_if_statement_complex5(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        if(bFlag == true)
                        {
                        }
                        else
                        {
                            float varFloat1; 

                            if(bFlag != true)
                            {
                                float varFloat2; 
                            }
                        }
                    }             
                """
        expect = str(Program([
                                FuncDecl(Id("funcA"),
                                [VarDecl("bFlag",BoolType())],
                                BoolType(),
                                Block([If(BinaryOp("==",Id("bFlag"),BooleanLiteral(True)),
                                        Block([]), 
                                        Block([
                                            VarDecl("varFloat1",FloatType()),
                                            If( BinaryOp("!=",Id("bFlag"),BooleanLiteral(True)),
                                                Block([VarDecl("varFloat2",FloatType())]), 
                                                None) ])
                                    )]))
                            ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_if_statement_complex6(self):
        """If-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        if(bFlag == true)
                        {
                            float varFloat1; 
                        }
                        else
                        {
                            if(bFlag != true)
                            {
                                float varFloat2; 
                            }
                        }
                    }             
                """
        expect = str(Program([
                                FuncDecl(Id("funcA"),
                                [VarDecl("bFlag",BoolType())],
                                BoolType(),
                                Block([If(BinaryOp("==",Id("bFlag"),BooleanLiteral(True)),
                                        Block([
                                            VarDecl("varFloat1",FloatType())
                                        ]), 
                                        Block([
                                            If( BinaryOp("!=",Id("bFlag"),BooleanLiteral(True)),
                                                Block([VarDecl("varFloat2",FloatType())]), 
                                                None) ])
                                    )]))
                            ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_doWhile_statement_simple(self):
        """doWhile-statement """
        input = """ boolean funcA(boolean bFlag)
                    {
                        do
                        {
                            float varFloat; 
                        }
                        while(true);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BooleanLiteral(True))
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_doWhile_statement_simple2(self):
        """doWhile-statement """
        input = """ boolean funcA(boolean bFlag)
                    {
                        do
                        {
                            float varFloat; 
                        }
                        while(false);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BooleanLiteral(False))
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_doWhile_statement_complex(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        do
                        {
                            float varFloat; 
                        }
                        while(bFlag == true);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("==", Id("bFlag"), BooleanLiteral(False))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_doWhile_statement_complex(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int varInt1;
                        int varInt2;
                         
                        varInt1 = 100; 
                        varInt2 = 10; 

                        do
                        {
                            float varFloat; 
                        }
                        while(varInt1 > varInt2);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp(">", Id("varInt1"), Id("varInt2"))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_doWhile_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        do
                        {
                            float varFloat; 
                        }
                        while((varInt1 > varInt2) && varBool);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()),
                                            VarDecl("varBool",BoolType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("&&",BinaryOp(">",Id("varInt1"),Id("varInt2")),Id("varBool"))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_doWhile_statement_complex3(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        do
                        {
                            float varFloat; 
                        }
                        while(((varInt1 - varInt2) - 50) && (varBool && true));
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()),
                                            VarDecl("varBool",BoolType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("&&",BinaryOp("-",BinaryOp("-",Id("varInt1"),Id("varInt2")),IntLiteral(50)),BinaryOp("&&",Id("varBool"),BooleanLiteral(True)))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_doWhile_statement_complex4(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        do
                        {
                            float varFloat; 
                        }
                        while(((varInt1 - varInt2) > 50) && (varBool && true));
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()),
                                            VarDecl("varBool",BoolType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("&&",BinaryOp(">",BinaryOp("-",Id("varInt1"),Id("varInt2")),IntLiteral(50)),BinaryOp("&&",Id("varBool"),BooleanLiteral(True)))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_doWhile_statement_complex5(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        do
                        {
                            float varFloat; 
                        }
                        while(((varInt1 - varInt2) > 50) && (varBool || false));
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()),
                                            VarDecl("varBool",BoolType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("&&",BinaryOp(">",BinaryOp("-",Id("varInt1"),Id("varInt2")),IntLiteral(50)),BinaryOp("||",Id("varBool"),BooleanLiteral(False)))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_doWhile_statement_complex6(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        int     varInt1;
                        int     varInt2;
                        boolean varBool; 
                         
                        varInt1 = 100; 
                        varInt2 = 10; 
                        varBool = true; 

                        do
                        {
                            float varFloat; 
                        }
                        while(((varInt1 / varInt2) < 50) && (varBool || false));
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varInt1",IntType()),
                                            VarDecl("varInt2",IntType()),
                                            VarDecl("varBool",BoolType()), 
                                            BinaryOp("=", Id("varInt1"), IntLiteral(100)), 
                                            BinaryOp("=", Id("varInt2"), IntLiteral(10)), 
                                            BinaryOp("=", Id("varBool"), BooleanLiteral(True)), 
                                            Dowhile(
                                                [
                                                    Block([VarDecl("varFloat",FloatType())])
                                                ],
                                                BinaryOp("&&",BinaryOp("<",BinaryOp("/",Id("varInt1"),Id("varInt2")),IntLiteral(50)),BinaryOp("||",Id("varBool"),BooleanLiteral(False)))
                                            )
                                        ])
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    
    def test_for_statement_simple(self):
        """doWhile-statement """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; varIndex < 10; varIndex = varIndex*2)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("<", Id("varIndex"), IntLiteral(10)),
                                                BinaryOp("=", Id("varIndex"), BinaryOp("*", Id("varIndex"), IntLiteral(2))), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_for_statement_simple2(self):
        """doWhile-statement """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex < 10) && bFlag ; varIndex = varIndex/2)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("&&",BinaryOp("<",Id("varIndex"),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), BinaryOp("/", Id("varIndex"), IntLiteral(2))), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_for_statement_complex(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex < 10) || bFlag ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("||",BinaryOp("<",Id("varIndex"),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_for_statement_complex(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex/10 > 10) && bFlag ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("&&",BinaryOp(">",BinaryOp("/",Id("varIndex"),IntLiteral(10)),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_for_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex < 10) && bFlag ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("&&",BinaryOp("<",Id("varIndex"),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_for_statement_complex3(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex < 10) || bFlag ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("||",BinaryOp("<",Id("varIndex"),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_for_statement_complex4(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; (varIndex < 10) && bFlag ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("&&",BinaryOp("<",Id("varIndex"),IntLiteral(10)),Id("bFlag")),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_for_statement_complex5(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; bFlag == true ; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("==", Id("bFlag"),   BooleanLiteral(True)),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_for_statement_complex6(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        /* for-statement */
                        for(varIndex = 0; bFlag != true; varIndex = 100)
                        {
                            /* Do something */
                            varInt = 12345;
                            varInt = varInt + 100; 
                        } 
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()),
                                            For( 
                                                BinaryOp("=", Id("varIndex"), IntLiteral(0)),
                                                BinaryOp("!=", Id("bFlag"),   BooleanLiteral(True)),
                                                BinaryOp("=", Id("varIndex"), IntLiteral(100)), 
                                                Block([
                                                    BinaryOp("=", Id("varInt"), IntLiteral(12345)), 
                                                    BinaryOp("=", Id("varInt"), BinaryOp("+", Id("varInt"), IntLiteral(100)))
                                                ])
                                            )
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_call_statement_simple(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        putIntLn();
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            CallExpr(Id("putIntLn"),[])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_call_statement_complex(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 

                        putIntLn(varIndex);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            CallExpr(Id("putIntLn"),[Id("varIndex")])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_call_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        putIntLn(varIndex, varIndex2);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            CallExpr(Id("putIntLn"),[Id("varIndex"), Id("varIndex2")])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_call_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        putIntLn(true);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            CallExpr(Id("putIntLn"),[BooleanLiteral(True)])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_call_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        putIntLn(varIndex + varIndex2);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            CallExpr(Id("putIntLn"),[BinaryOp("+", Id("varIndex"), Id("varIndex2"))])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_call_statement_complex2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        putIntLn(varIndex + varIndex2, true);
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            CallExpr(Id("putIntLn"),[BinaryOp("+", Id("varIndex"), Id("varIndex2")), BooleanLiteral(True)])
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))


    def test_return_statement_simple(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        return true;
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            Return(BooleanLiteral(True))
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_return_statement_simple2(self):
        """doWhile-statement: complex """
        input = """ boolean funcA(boolean bFlag)
                    {
                        /* Declare variables */
                        int varIndex; 
                        int varIndex2; 

                        return varIndex > varIndex2;
                    }             
                """
        expect = str(Program([  
                                FuncDecl( 
                                        Id("funcA"), 
                                        [
                                            VarDecl("bFlag", BoolType()), 
                                        ], 
                                        BoolType(),   
                                        Block([
                                            VarDecl("varIndex", IntType()), 
                                            VarDecl("varIndex2", IntType()), 
                                            Return(BinaryOp(">", Id("varIndex"), Id("varIndex2")))
                                        ]) 
                                    )
                        ]))
        print("Function: %s\n --> Expect result: %s" % (inspect.stack()[0][3], expect))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))