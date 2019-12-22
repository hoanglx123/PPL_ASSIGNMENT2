import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    """2.1 Redeclared Variable/Function/Parameter"""
    """Check redeclared variable"""
    # def test_redeclared_global_variable(self):
    #     """Redeclared global variable in simple program """
    #     input = """
    #             int     varInt;
    #             float   varFloat;
    #             boolean varBool;
    #             int     varInt;

    #             void main(){}
    #         """
    #     expect = "Redeclared Variable: varInt"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_redeclared_local_variable(self):
    #     """Redeclared local variable in simple program """
    #     input = """
    #             void foo()
    #             {
    #                 int     varInt;
    #                 float   varFloat;
    #                 boolean varBool;
    #                 int     varInt;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Variable: varInt"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_redeclared_variable_not_same_scope(self):
    #     """Redeclared local variable in other scopes """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo()
    #             {
    #                 int     varInt;
    #                 float   varFloat;
    #                 boolean varBool;
    #                 float   varFloat;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Variable: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_redeclared_variable_not_same_scope_complex(self):
    #     """Redeclared local variable in other scopes """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo()
    #             {
    #                 int     varInt;
    #                 float   varFloat;
    #                 boolean varBool;

    #                 {
    #                     string  varString;
    #                     boolean varBool;
    #                     string  varString;
    #                 }
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Variable: varString"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_redeclared_variable_not_same_type(self):
    #     """Redeclared local variable with other data type """
    #     input = """
    #             /* Declare global variables */
    #             int     varInt;
    #             float   varFloat;
    #             boolean varBool;
    #             string  varFloat;
    #         """
    #     expect = "Redeclared Variable: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_redeclared_variable_in_parameter_and_local(self):
    #     """Redeclared variable in parameter and local declaration """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo(int varInt, float varFloat, boolean varBool)
    #             {
    #                 float varFloat;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Variable: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # """Check duplicate declaration in parameter"""
    # def test_redeclared_parameter(self):
    #     """Redeclared parameter """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo(float varFloat, boolean varBool, float varFloat)
    #             {
    #                 string varInt;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_redeclared_parameter_with_other_type(self):
    #     """Redeclared parameter with other type """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo(float varFloat, boolean varBool, string varFloat)
    #             {
    #                 string varInt;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_redeclared_parameter_with_any_param_same_name_with_global_variable(self):
    #     """Redeclared parameters. There are any parameter the name as gloable variable """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo(int varInt, float varFloat, boolean varBool, string varFloat)
    #             {
    #                 string varInt;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_redeclared_parameter_with_any_param_same_name_with_global_variable2(self):
    #     """Redeclared parameters. There are any parameter the name as gloable variable """
    #     input = """
    #             /* Declare global variables */
    #             int varInt;

    #             void foo(int varInt, float varFloat, boolean varBool, string varFloat)
    #             {
    #                 string varInt;
    #             }

    #             void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # """Test cases to check redeclared function"""
    # def test_redeclared_function(self):
    #     """Redeclared function in simple program """
    #     input = """
    #         void foo(){}
    #         void foo(){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_redeclared_function_with_other_parameters(self):
    #     """Redeclared function with other parameters """
    #     input = """
    #         void foo(int varInt, float varFloat, boolean varBool){}
    #         void foo(int varInt, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_redeclared_function_with_other_type(self):
    #     """Redeclared function with other type """
    #     input = """
    #         void foo(int varInt, float varFloat, boolean varBool){}
    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_mix_redeclared_function_and_redeclared_variable(self):
    #     """Mix: Redeclared function and redeclared variable """
    #     input = """
    #         void foo()
    #         {
    #             int     varInt;
    #             float   varFloat;
    #             boolean varBool;
    #             float   varFloat;
    #         }

    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Variable: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_mix_redeclared_function_and_redeclared_parameter(self):
    #     """Mix: redeclared function and redeclared parameter """
    #     input = """
    #         void foo(int varInt, float varFloat, boolean varBool, float varFloat){}
    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_mix_redeclared_function_and_redeclared_variable_and_redeclared_parameter(self):
    #     """Mix: redeclared function and redeclared variable and redeclared parameter"""
    #     input = """
    #         void foo(int varInt, float varFloat, boolean varBool, float varFloat)
    #         {
    #             int varInt1;
    #             int varInt2;
    #             int varInt1;
    #         }

    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Parameter: varFloat"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_mix_redeclared_function_and_redeclared_global_variable(self):
    #     """Mix: redeclared function and redeclared global variable"""
    #     input = """
    #         /* Declare global variable */
    #         int varInt1;
    #         int varInt2;
    #         int varInt1;

    #         void foo(int varInt, float varFloat, boolean varBool, float varFloat){}
    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Variable: varInt1"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_mix_redeclared_function_and_redeclared_global_variable_and_redeclared_local_variable(self):
    #     """Mix: redeclared function, redeclared global variable and redeclared local variable """
    #     input = """
    #         /* Declare global variable */
    #         int varInt1;
    #         int varInt2;
    #         int varInt1;

    #         void foo(int varInt, float varFloat, boolean varBool, float varFloat)
    #         {
    #             float varFloat1;
    #             float varFloat2;
    #             float varFloat1;
    #         }

    #         int  foo(int varInt, float varFloat, boolean varBool){}
    #         void main(){}
    #         """
    #     expect = "Redeclared Variable: varInt1"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    def test_mismatch_in_unary_expression(self):
        """Mismatch in binary expression with lhs in bool type"""
        input = """
                int foo()
                {
                    string  varStr1;

                    return "abc";
                }

                void main(){}
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(varBool1),Id(varStr1))"
        self.assertTrue(TestChecker.test(input,expect,482))

















    # """2.2 Undeclared Identifier/Function"""
    # """ Check undeclared variable """
    # def test_undeclared_variable(self):
    #     """Undeclared variable """
    #     input = """
    #             int main()
    #             {
    #                 varInt = 5;
    #             }
    #         """
    #     expect = "Undeclared Variable: varInt"
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_undeclared_variable_in_assingment_statement(self):
    #     """Undeclared variable in assignment statement"""
    #     input = """
    #             void foo()
    #             {
    #                 varInt = 5;
    #             }

    #             int main(){}
    #         """
    #     expect = "Undeclared Variable: varInt"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_undeclared_variable_in_plus_operand(self):
    #     """Undeclared variable """
    #     input = """
    #             void foo()
    #             {
    #                 int varInt1;
    #                 int varInt2;

    #                 varInt1 = varInt2 + varInt3;
    #             }

    #             int main(){}
    #         """
    #     expect = "Undeclared Variable: varInt3"
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_undeclared_variable_with_global_variable_declaration(self):
    #     """Undeclared variable """
    #     input = """
    #             /* Declare global variables */
    #             int varInt1;

    #             void foo()
    #             {
    #                 int varInt2;
    #                 varInt1 = varInt2 - varInt3;
    #             }

    #             int main(){}
    #         """
    #     expect = "Undeclared Variable: varInt3"
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))
