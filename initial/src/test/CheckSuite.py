import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    """2.1 Redeclared Variable/Function/Parameter"""
    """Check redeclared variable"""
    def test_redeclared_global_variable(self):
        """Redeclared global variable in simple program """
        input = """
                int     varInt;
                float   varFloat;
                boolean varBool;
                int     varInt;

                void main(){}
            """
        expect = "Redeclared Variable: varInt"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_local_variable(self):
        """Redeclared local variable in simple program """
        input = """
                void foo()
                {
                    int     varInt;
                    float   varFloat;
                    boolean varBool;
                    int     varInt;
                }

                void main(){}
            """
        expect = "Redeclared Variable: varInt"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_not_same_scope(self):
        """Redeclared local variable in other scopes """
        input = """
                /* Declare global variables */
                int varInt;

                void foo()
                {
                    int     varInt;
                    float   varFloat;
                    boolean varBool;
                    float   varFloat;
                }

                void main(){}
            """
        expect = "Redeclared Variable: varFloat"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_not_same_scope_complex(self):
        """Redeclared local variable in other scopes """
        input = """
                /* Declare global variables */
                int varInt;

                void foo()
                {
                    int     varInt;
                    float   varFloat;
                    boolean varBool;

                    {
                        string  varString;
                        boolean varBool;
                        string  varString;
                    }
                }

                void main(){}
            """
        expect = "Redeclared Variable: varString"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_not_same_type(self):
        """Redeclared local variable with other data type """
        input = """
                /* Declare global variables */
                int     varInt;
                float   varFloat;
                boolean varBool;
                string  varFloat;
            """
        expect = "Redeclared Variable: varFloat"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable_in_parameter_and_local(self):
        """Redeclared variable in parameter and local declaration """
        input = """
                /* Declare global variables */
                int varInt;

                void foo(int varInt, float varFloat, boolean varBool)
                {
                    float varFloat;
                }

                void main(){}
            """
        expect = "Redeclared Variable: varFloat"
        self.assertTrue(TestChecker.test(input,expect,405))

    """Check duplicate declaration in parameter"""
    def test_redeclared_parameter(self):
        """Redeclared parameter """
        input = """
                /* Declare global variables */
                int varInt;

                void foo(float varFloat, boolean varBool, float varFloat)
                {
                    string varInt;
                }

                void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_parameter_with_other_type(self):
        """Redeclared parameter with other type """
        input = """
                /* Declare global variables */
                int varInt;

                void foo(float varFloat, boolean varBool, string varFloat)
                {
                    string varInt;
                }

                void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_parameter_with_any_param_same_name_with_global_variable(self):
        """Redeclared parameters. There are any parameter the name as gloable variable """
        input = """
                /* Declare global variables */
                int varInt;

                void foo(int varInt, float varFloat, boolean varBool, string varFloat)
                {
                    string varInt;
                }

                void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_parameter_with_any_param_same_name_with_global_variable2(self):
        """Redeclared parameters. There are any parameter the name as gloable variable """
        input = """
                /* Declare global variables */
                int varInt;

                void foo(int varInt, float varFloat, boolean varBool, string varFloat)
                {
                    string varInt;
                }

                void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,409))

    """Test cases to check redeclared function"""
    def test_redeclared_function(self):
        """Redeclared function in simple program """
        input = """
            void foo(){}
            void foo(){}
            void main(){}
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_function_with_other_parameters(self):
        """Redeclared function with other parameters """
        input = """
            void foo(int varInt, float varFloat, boolean varBool){}
            void foo(int varInt, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_function_with_other_type(self):
        """Redeclared function with other type """
        input = """
            void foo(int varInt, float varFloat, boolean varBool){}
            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_mix_redeclared_function_and_redeclared_variable(self):
        """Mix: Redeclared function and redeclared variable """
        input = """
            void foo()
            {
                int     varInt;
                float   varFloat;
                boolean varBool;
                float   varFloat;
            }

            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Variable: varFloat"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_mix_redeclared_function_and_redeclared_parameter(self):
        """Mix: redeclared function and redeclared parameter """
        input = """
            void foo(int varInt, float varFloat, boolean varBool, float varFloat){}
            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_mix_redeclared_function_and_redeclared_variable_and_redeclared_parameter(self):
        """Mix: redeclared function and redeclared variable and redeclared parameter"""
        input = """
            void foo(int varInt, float varFloat, boolean varBool, float varFloat)
            {
                int varInt1;
                int varInt2;
                int varInt1;
            }

            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Parameter: varFloat"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_mix_redeclared_function_and_redeclared_global_variable(self):
        """Mix: redeclared function and redeclared global variable"""
        input = """
            /* Declare global variable */
            int varInt1;
            int varInt2;
            int varInt1;

            void foo(int varInt, float varFloat, boolean varBool, float varFloat){}
            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Variable: varInt1"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_mix_redeclared_function_and_redeclared_global_variable_and_redeclared_local_variable(self):
        """Mix: redeclared function, redeclared global variable and redeclared local variable """
        input = """
            /* Declare global variable */
            int varInt1;
            int varInt2;
            int varInt1;

            void foo(int varInt, float varFloat, boolean varBool, float varFloat)
            {
                float varFloat1;
                float varFloat2;
                float varFloat1;
            }

            int  foo(int varInt, float varFloat, boolean varBool){}
            void main(){}
            """
        expect = "Redeclared Variable: varInt1"
        self.assertTrue(TestChecker.test(input,expect,417))


    """2.2 Undeclared Identifier/Function"""
    """ Check undeclared variable """
    def test_undeclared_variable(self):
        """Undeclared variable """
        input = """
                int main()
                {
                    varInt = 5;
                }
            """
        expect = "Undeclared Variable: varInt"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_variable_in_assingment_statement(self):
        """Undeclared variable in assignment statement"""
        input = """
                void foo()
                {
                    varInt = 5;
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_variable_in_plus_operand(self):
        """Undeclared variable with plus operand """
        input = """
                void foo()
                {
                    int varInt1;
                    int varInt2;

                    varInt1 = varInt2 + varInt3;
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt3"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_variable_with_global_variable_declaration(self):
        """Undeclared variable with global variable declaration """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo()
                {
                    int varInt2;
                    varInt1 = varInt2 - varInt3;
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt3"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_variable_with_parameter_declaration(self):
        """Undeclared variable with parameter declaration """
        input = """
                void foo(int varInt1)
                {
                    int varInt2;
                    varInt1 = varInt2 - varInt3;
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt3"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_variable_with_global_declaration_and_parameter_declaration(self):
        """Undeclared variable with global declaration and parameter declaration """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo(int varInt2)
                {
                    varInt1 = varInt2 - varInt3;
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt3"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_variable_with_variable_declaration_in_block(self):
        """Undeclared variable with variable declaration in block """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo(int varInt2)
                {
                    {
                        int varInt3;

                        varInt1 = varInt2 + varInt3 + varInt4;
                    }
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt4"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_variable_with_variable_declaration_in_many_inner_blocks(self):
        """Undeclared variable with variable declaration in many inner blocks """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo(int varInt2)
                {
                    {
                        int varInt3;
                        {
                            int varInt4;
                            varInt1 = varInt2 + varInt3 + varInt4 + varInt5;
                        }
                    }
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt5"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_variable_with_variable_declaration_in_many_other_blocks(self):
        """Undeclared variable with variable declaration in many other blocks """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo(int varInt2)
                {
                    {
                        int varInt3;
                    }

                    {
                        int varInt4;
                        varInt1 = varInt2 + varInt3 + varInt4;
                    }
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt3"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_variable_with_variable_declaration_in_many_other_blocks2(self):
        """Undeclared variable with variable declaration in many other blocks """
        input = """
                /* Declare global variables */
                int varInt1;

                void foo(int varInt2)
                {
                    int varInt3;
                    {
                        int varInt4;
                        varInt1 = varInt2 + varInt3 + varInt4;
                    }
                    {
                        varInt1 = varInt2 + varInt3 + varInt4;
                    }
                }

                void main(){}
            """
        expect = "Undeclared Variable: varInt4"
        self.assertTrue(TestChecker.test(input,expect,429))

    """ Check undeclared function """
    def test_undeclared_function_simple(self):
        """Undeclared function: simple """
        input = """
                void foo1(){}
                void foo2(){}

                int main()
                {
                    foo3();
                }
            """
        expect = "Undeclared Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_function_in_block(self):
        """Undeclared function in block """
        input = """
                void foo1(){}
                void foo2(){}

                int main()
                {
                    {
                        foo3();
                    }
                }
            """
        expect = "Undeclared Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undeclared_function_with_parameter(self):
        """Undeclared function with parameter """
        input = """
                void foo1(int varInt, float varFloat){}

                int main()
                {
                    foo2();
                }
            """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,432))

    """2.3 Type Mismatch In Statement"""
    def test_mismatch_in_if_statement_with_int_type(self):
        """Mismatch in if statement with int type"""
        input = """
                int main()
                {
                    boolean varBool;
                    int     varInt;

                    if(varBool){}
                    if(varInt){}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varInt),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_mismatch_in_if_statement_with_float_type(self):
        """Mismatch in if statement with float type"""
        input = """
                int main()
                {
                    boolean varBool;
                    float   varFloat;

                    if(varBool){}
                    if(varFloat){}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varFloat),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_mismatch_in_if_statement_with_string_type(self):
        """Mismatch in if statement with string type"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    if(varBool){}
                    if(varString){}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varString),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_mismatch_in_if_else_statement_with_int_type(self):
        """Mismatch in if-else statement with int type"""
        input = """
                int main()
                {
                    boolean varBool;
                    int     varInt;

                    if(varBool){}
                    if(varInt){}
                    else{}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varInt),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_mismatch_in_if_else_statement_with_float_type(self):
        """Mismatch in if-else statement with float type"""
        input = """
                int main()
                {
                    boolean varBool;
                    float   varFloat;

                    if(varBool){}
                    if(varFloat){}
                    else{}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varFloat),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_mismatch_in_if_else_statement_with_string_type(self):
        """Mismatch in if-else statement with string type"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    if(varBool){}
                    if(varString){}
                    else{}
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varString),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_mismatch_in_if_statement_with_inner_if(self):
        """Mismatch in if statement with inner if statement"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    if(varBool)
                    {
                        if(varString){}
                    }
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varString),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_mismatch_in_if_else_statement_with_inner_if_in_else(self):
        """Mismatch in if-else statement with inner if statement in else"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    if(varBool)
                    else
                    {
                        if(varString){}
                    }
                }
            """
        expect = "Type Mismatch In Statement: If(Id(varString),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_mismatch_in_for_statement_with_bool_type_expression1(self):
        """Mismatch in for statement with bool type (expression1)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    boolean varBool2;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varBool2; varBool1; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varBool2);Id(varBool1);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_mismatch_in_for_statement_with_float_type_expression1(self):
        """Mismatch in for statement with float type (expression1)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    float   varFloat;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varFloat; varBool1; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varFloat);Id(varBool1);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_mismatch_in_for_statement_with_string_type_expression1(self):
        """Mismatch in for statement with string type (expression1)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    string  varStr;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varStr; varBool1; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varStr);Id(varBool1);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_mismatch_in_for_statement_with_int_type_expression2(self):
        """Mismatch in for statement with int type (expression2)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    int     varInt2;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varInt2; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varInt2);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_mismatch_in_for_statement_with_float_type_expression2(self):
        """Mismatch in for statement with float type (expression2)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    float   varFloat2;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varFloat2; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varFloat2);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_mismatch_in_for_statement_with_string_type_expression2(self):
        """Mismatch in for statement with string type (expression2)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    string  varStr2;
                    int     varInt1;
                    int     varInt3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varStr2; varInt3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varStr2);Id(varInt3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_mismatch_in_for_statement_with_bool_type_expression3(self):
        """Mismatch in for statement with bool type (expression3)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    int     varInt1;
                    int     varInt3;
                    boolean varBool3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varBool1; varBool3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varBool1);Id(varBool3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_mismatch_in_for_statement_with_float_type_expression3(self):
        """Mismatch in for statement with float type (expression3)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    int     varInt1;
                    int     varInt3;
                    float   varFloat3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varBool1; varFloat3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varBool1);Id(varFloat3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_mismatch_in_for_statement_with_string_type_expression3(self):
        """Mismatch in for statement with string type (expression3)"""
        input = """
                int main()
                {
                    boolean varBool1;
                    int     varInt1;
                    int     varInt3;
                    string  varStr3;

                    for(varInt1; varBool1; varInt3){}
                    for(varInt1; varBool1; varStr3){}
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varBool1);Id(varStr3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_mismatch_in_for_statement_with_inner_for(self):
        """Mismatch in for statement with inner for"""
        input = """
                int main()
                {
                    boolean varBool1;
                    int     varInt1;
                    int     varInt3;
                    string  varStr3;

                    for(varInt1; varBool1; varInt3)
                    {
                        for(varInt1; varBool1; varStr3){}
                    }
                }
            """
        expect = "Type Mismatch In Statement: For(Id(varInt1);Id(varBool1);Id(varStr3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_mismatch_in_do_while_statement_with_int_type(self):
        """Mismatch in do-while statement with int type"""
        input = """
                int main()
                {
                    boolean varBool;
                    int     varInt;

                    do{}
                    while(varBool);

                    do{}
                    while(varInt);
                }
            """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(varInt))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_mismatch_in_do_while_statement_with_float_type(self):
        """Mismatch in do-while statement with float type"""
        input = """
                int main()
                {
                    boolean varBool;
                    float   varFloat;

                    do{}
                    while(varBool);

                    do{}
                    while(varFloat);
                }
            """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(varFloat))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_mismatch_in_do_while_statement_with_string_type(self):
        """Mismatch in do-while statement with string type"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    do{}
                    while(varBool);

                    do{}
                    while(varString);
                }
            """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(varString))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_mismatch_in_do_while_statement_with_inner_while(self):
        """Mismatch in do-while statement with inner while"""
        input = """
                int main()
                {
                    boolean varBool;
                    string  varString;

                    do
                    {
                        do{}
                        while(varString);
                    }
                    while(varBool);
                }
            """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(varString))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_mismatch_in_return_statement_with_void_type(self):
        """Mismatch in return statement with void type"""
        input = """
                void foo()
                {
                    return 1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_mismatch_in_return_statement_with_int_type(self):
        """Mismatch in return statement with int type"""
        input = """
                int foo()
                {
                    return 1.0;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_mismatch_in_return_statement_with_bool_type(self):
        """Mismatch in return statement with bool type"""
        input = """
                boolean foo()
                {
                    return 1.0;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_mismatch_in_return_statement_with_string_type(self):
        """Mismatch in return statement with int type"""
        input = """
                string foo()
                {
                    return 1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_mismatch_in_return_statement_with_plus_operand_int_type(self):
        """Mismatch in return statement with int type"""
        input = """
                float foo()
                {
                    int varInt1;
                    int varInt2;
                    int varInt3;

                    varInt3 = varInt1 + varInt2;
                    return varInt3;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(Id(varInt3))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_mismatch_in_return_statement_with_plus_operand_float_type(self):
        """Mismatch in return statement with int type"""
        input = """
                int foo()
                {
                    float varFloat1;
                    float varFloat2;
                    float varFloat3;

                    varFloat3 = varFloat1 + varFloat2;
                    return varFloat3;
                }

                void main(){}
            """
        expect = "Type Mismatch In Statement: Return(Id(varFloat3))"
        self.assertTrue(TestChecker.test(input,expect,467))


    def test_function_not_return_with_int_type(self):
        """Function not return with int type"""
        input = """
                void foo1(){}
                int  foo2()
                {
                    return 1;
                }
                int  foo3()
                {
                    int varInt;
                    return varInt;
                }
                int  fooInt(){}

                void main(){}
            """
        expect = "Function fooInt Not Return "
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_function_not_return_with_float_type(self):
        """Function not return with float type"""
        input = """
                void  foo1(){}
                float foo2()
                {
                    return 1.0;
                }
                float foo3()
                {
                    float varFloat;
                    return varFloat;
                }
                float fooFloat(){}

                void main(){}
            """
        expect = "Function fooFloat Not Return "
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_function_not_return_with_string_type(self):
        """Function not return with string type"""
        input = """
                void   foo1(){}
                string fooStr(){}

                void main(){}
            """
        expect = "Function fooStr Not Return "
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_function_not_return_with_empty_return(self):
        """Function not return with empty return"""
        input = """
                void foo1()
                {
                    return;
                }
                int foo2(){}
                void main(){}
            """
        expect = "Function foo2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,473))

    """2.4 Type Mismatch In Expression"""
    def test_mismatch_in_binary_expression_with_lhs_int_type(self):
        """Mismatch in binary expression with lhs in int type"""
        input = """
                void foo()
                {
                    int   varInt1;
                    int   varInt2;
                    float varFloat;

                    varInt1 = varInt1 + varInt2;
                    varInt1 = varInt1 + varInt2 + varFloat;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varInt2),Id(varFloat))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_mismatch_in_binary_expression_with_lhs_int_type2(self):
        """Mismatch in binary expression with lhs in int type"""
        input = """
                void foo()
                {
                    int     varInt1;
                    int     varInt2;
                    boolean varBool;

                    varInt1 = varInt1 + varInt2;
                    varInt1 = varInt1 + varInt2 + varBool;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varInt2),Id(varBool))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_mismatch_in_binary_expression_with_lhs_int_type3(self):
        """Mismatch in binary expression with lhs in int type"""
        input = """
                void foo()
                {
                    int    varInt1;
                    int    varInt2;
                    string varStr;

                    varInt1 = varInt1 + varInt2;
                    varInt1 = varInt1 + varInt2 + varStr;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varInt2),Id(varStr))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_mismatch_in_binary_expression_with_lhs_int_type4(self):
        """Mismatch in binary expression with lhs in int type"""
        input = """
                void foo()
                {
                    int    varInt1;
                    int    varInt2;

                    varInt1 = varInt1 + varInt2 + 1;
                    varInt1 = varInt1 + varInt2 + 1.0;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varInt2),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_mismatch_in_binary_expression_with_lhs_float_type(self):
        """Mismatch in binary expression with lhs in float type"""
        input = """
                void foo()
                {
                    float   varFloat1;
                    float   varFloat2;
                    int     varInt1;
                    int     varInt2;
                    boolean varBool;

                    varFloat1 = varFloat1 + varFloat2;
                    varFloat1 = varInt1 + varInt2;
                    varFloat1 = varFloat1 + varBool;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varFloat1),Id(varBool))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_mismatch_in_binary_expression_with_lhs_float_type(self):
        """Mismatch in binary expression with lhs in float type"""
        input = """
                void foo()
                {
                    float   varFloat1;
                    float   varFloat2;
                    int     varInt1;
                    int     varInt2;
                    string  varStr;

                    varFloat1 = varFloat1 + varFloat2;
                    varFloat1 = varInt1 + varInt2;
                    varFloat1 = varFloat1 + varStr;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varFloat1),Id(varStr))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_mismatch_in_binary_expression_with_lhs_bool_type(self):
        """Mismatch in binary expression with lhs in bool type"""
        input = """
                void foo()
                {
                    int     varInt1;
                    boolean varBool1;
                    boolean varBool2;

                    varBool1 = varBool1 && varBool2;
                    varBool1 = varBool1 + varInt1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varBool1),Id(varInt1))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_mismatch_in_binary_expression_with_lhs_bool_type1(self):
        """Mismatch in binary expression with lhs in bool type"""
        input = """
                void foo()
                {
                    float   varFloat1;
                    boolean varBool1;
                    boolean varBool2;

                    varBool1 = varBool1 && varBool2;
                    varBool1 = varBool1 + varFloat1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varBool1),Id(varFloat1))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_mismatch_in_binary_expression_with_lhs_bool_type2(self):
        """Mismatch in binary expression with lhs in bool type"""
        input = """
                void foo()
                {
                    string  varStr1;
                    boolean varBool1;
                    boolean varBool2;

                    varBool1 = varBool1 && varBool2;
                    varBool1 = varBool1 + varStr1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varBool1),Id(varStr1))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_mismatch_in_unary_expression(self):
        """Mismatch in binary expression with lhs in bool type"""
        input = """
                void foo()
                {
                    string  varStr1;
                    boolean varBool1;
                    boolean varBool2;

                    varBool1 = !varBool1;
                    varBool1 = varBool1 + varStr1;
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varBool1),Id(varStr1))"
        self.assertTrue(TestChecker.test(input,expect,482))