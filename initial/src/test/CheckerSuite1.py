import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
            a,b :real;
        procedure main (); begin
        end"""
                        
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare0(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure foo(f:integer);
        var f: real;
        begin
        end"""
                        
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare1(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure b(f:integer);
        begin
        end"""
                        
        expect = "Redeclared Procedure: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare2(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure foo(f:integer);
        var a:integer;
            c,d,a:real;
        begin
        return a;
        end"""
                        
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclare3(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure foo(f:integer);
        var a:integer;
        begin
        end
        function foo():integer;
        begin 
        return 0;
        end"""
                        
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclare4(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure foo(f:integer;f:real);
        var a:integer;
        begin
        end"""
                        
        expect = "Redeclared Parameter: f"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclare5(self):
        """More complex program"""
        input = """
        var a,b,c: integer;
        procedure main ();
        begin
        end
        procedure foo(f:integer);
        var a:integer;
        begin
        end

        function f(i:integer):real;
        var a: real;
        begin
        return a;
        end

        var f:real;
        """
                        
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Noentrypoint1(self):
        """More complex program"""
        input = """
        procedure main (i:real);
        begin
        end
        """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Noentrypoint2(self):
        """More complex program"""
        input = """
        function main ():real;
        var a:real;
        begin
        return a;
        end
        """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_Noentrypoint3(self):
        """More complex program"""
        input = """
        procedure foo(f:integer);
        var a:integer;
        begin
        end
        function f(i:integer):real;
        var a: real;
        begin
        return a;
        end
        function main ():real;
        var a:real;
        begin
        return a;
        end
        """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_TypeMismatchInAssign1(self):
        """More complex program"""
        input = """
        function f(i:integer):real;
        var a: real;
            c: string;
        begin
            a:= c;
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_TypeMismatchInAssign2(self):
        """More complex program"""
        input = """
        function f(i:integer):real;
        var a: real;
        begin
            a:= "main";
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),StringLiteral(main))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_TypeMismatchInAssign3(self):
        """More complex program"""
        input = """
        function f(i:integer):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b := "main";
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),StringLiteral(main))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_TypeMismatchInAssign4(self):
        """More complex program"""
        input = """
        function foo(f:integer;h:real):real;
        var a:integer;
        begin
        return h;
        end
        function f(i:integer):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b := foo(a);
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_TypeMismatchInAssign5(self):
        """More complex program"""
        input = """
        function foo(f:integer;h:real):real;
        var a:integer;
        begin
        return h;
        end
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b := foo(a,b);
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_assign(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b := foo(a,b);
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_recursion(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b := f(a,b);
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(f),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_BreakNotInLoop(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b;
            Break;
            return a;
        end
        procedure main ();
        begin
        end
        """
                        
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_ContinueNotInLoop(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            a := b;
            Continue;
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_ContinueNotInLoop1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0  then begin
                a := b;
                Continue;
                end
            else begin
            end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_ContinueNotInLoop2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0 then begin
                a := b;
            end
            else begin
                a := b;
                Continue;
            end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_BreakNotInLoop1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0 then begin
                a := b;
                break;
                end
            else begin
            end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_BreakNotInLoop2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0 then begin
                a := b;
                return a;
                end
            else begin
                a := b;
                break;
            end

        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_ConditionFor1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            for a:=5 to 10 do begin end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(5),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_ConditionFor2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            for b:=5.2 to 10 do begin end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: For(Id(b)FloatLiteral(5.2),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_ConditionFor3(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            for b:=5 to 10.5 do begin end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: For(Id(b)IntLiteral(5),FloatLiteral(10.5),True,[])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_BreakInLoop1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            for b:=5 to 10 do begin
                c := "main"; 
                break;
            end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),StringLiteral(main))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_BreakInLoop2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            for b:=5 to 10 do begin
                break;
                if a > 0 then begin
                    a := b;
                end
            end
            return a;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Unreachable statement: If(BinaryOp(>,Id(a),IntLiteral(0)),[AssignStmt(Id(a),Id(b))],[])"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_ReturnType1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            return;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_ReturnType2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            return c;
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_ReturnType3(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0 then begin
                return 0.5;
            end
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_ReturnType4(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            if a > 0 then begin
                return a;   
            end
        end
        procedure main ();
        var b:real;
        begin
         b:=f(1,8.2);   
        end
        """
                        
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_ReturnType5(self):
        """More complex program"""
        input = """
        procedure main ();
        begin
            return a;
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_ReturnType6(self):
        """More complex program"""
        input = """
        procedure main ();
        var a:integer;
        begin
            for a:= 0 to 12 do
            begin
                if a > 0 then begin
                    return;
                    a:=5;
                end
            end

        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_If1(self):
        """More complex program"""
        input = """
        procedure main ();
        var a:integer;
        begin
            for a:= 0 to 12 do
            begin
                if a then begin
                end
            end
        end
        """
                        
        expect = "Type Mismatch In Statement: If(Id(a),[],[])"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_If2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            return a;
        end
        procedure main ();
        var a:integer;
            b: boolean;
            c:real;
        begin
             c:=f(1,8.2);   
            for a:= 0 to 12 do
            begin
                if b then begin
                    continue;
                    a:= 5;
                end
            end
        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_If3(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: real;
            b: integer;
            c: string;
        begin
            return a;
        end
        procedure main ();
        var a:integer;
            b: boolean;
            c:real;
        begin
            c :=f(1,8.2);
            for a:= 0 to 12 do
            begin
                if b then begin
                    b := a > 1;
                end
                else 
                begin
                    continue;
                    b := true;
                end
            end
        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(b),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_ReturnType7(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: integer;
            b: boolean;
            c: string;
        begin
            for a:= 0 to 12 do
            begin
                if b then begin
                    b := a > 1;
                end
                else 
                begin
                    return 0.5;
                    b := True;
                end
            end
        end
        procedure main ();
        var a:integer;
            b: real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(b),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_ReturnType8(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: integer;
            b: boolean;
            c: string;
        begin
            for a:= 0 to 12 do
            begin
                if b then begin
                    b := a > 1;
                end
                else 
                begin
                    b := True;
                end
            end
        end
        procedure main ();
        var a:integer;
            b: real;
        begin
         b:=f(1,8.2);
        end
        """
                        
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_While1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: integer;
            b: boolean;
            c: string;
        begin
            while a do 
            begin 
                a:= 0;
            end
            return j;
        end
        procedure main ();
        var a:integer;
            b: real;
        begin
            b:=f(1,8.2);
        end
        """
                        
        expect = "Type Mismatch In Statement: While(Id(a),[AssignStmt(Id(a),IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_While2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):real;
        var a: integer;
            b: boolean;
            c: string;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                    break;
                    a:= 0;
                end
            end
            return j;
        end
        procedure main ();
        var a:integer;
            b: real;
        begin
            b:=f(1,2.3);
        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_Arraytype1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):array [1 .. 2] of integer;
        var a: integer;
            b: boolean;
            c: string;
            d: array [1 .. 3] of real;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                    a:= 0;
                end
            end
            return d;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:=f(1,2.3)[0];
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_Arraytype2(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):array [1 .. 2] of integer;
        var a: integer;
            b: boolean;
            c: string;
            d: array [3 .. 2] of integer;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                    d[1]:= 0;
                end
            end
            return d;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:=f(1,2.3)[0];
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_Arraytype3(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):array [1 .. 2] of integer;
        var a: integer;
            b: boolean;
            c: string;
            d: array [1 .. 2] of integer;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                    a[1]:= 0;
                end
            end
            return d;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:=f(1,2.3)[0];
        end
        """
                        
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_Arraytype4(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):array [1 .. 2] of integer;
        var a: integer;
            b: boolean;
            c: integer;
            d: array [1 .. 8] of integer;
        begin
            while a > 0 do 
            begin 
                if c = 0 then
                begin
                    d[1]:= 0;
                end
            end
            return d;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:=f(1,2.3)[0];
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_BreakNotInLoop3(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):integer;
        var a: integer;
            b: boolean;
            c: string;
            d:integer;
        begin
            with a,b: real;c:array [1 .. 2] of real; do
               a := c[d] + b;
               break;
            return a;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            d:=f(i,2.3);
        end
        """
                        
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_Global1(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):integer;
        var a: integer;
        begin
            a := a +b;
            return d;
        end
        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            d:=f(a,d);
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_1(self):
        input = """
        function f(i:integer;j:real):integer;
        var a: integer;
        begin
            a := a +b;
            return a;
        end
        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
        end
        """
                        
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_2(self):
        input = """
        function f(i:integer;j:real):integer;
        var a: integer;
        begin
            a := a +b;
            return a;
        end
        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            d := d + f(a,d);
            return b;
        end
        """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_3(self):
        input = """
        function foo(i:integer;j:real):integer;
        var a: integer;
        begin
            return a;
        end

        function f(i:integer;j:real):integer;
        var a: integer;
        begin
            a := a +b;
            return a;
        end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            d := d + f(a,d);
        end
        """
                        
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_4(self):
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:real;
            do begin
                return 100;
            end
            x:= x+1; 
            end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a := d + f();
        end
        """
                        
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_5(self):
        input = """
        function f():integer;
        var x,y:integer;
            k:real;
        begin
            x:= putInt(y);
            return y;
        end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a := d + f();
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Id(putInt),[Id(y)]))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_6(self):
        input = """
        procedure f();
        var x,y:integer;
            k:real;
        begin
            putInt(k);
        end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            f();
        end
        """
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putInt),[Id(k)])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_7(self):
        input = """
        function foo(k:integer):integer;
        var foo:boolean;
        begin
            b:= foo();
            return b;
        end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a := f(a);
        end
        """
                        
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_8(self):
        input = """
        function foo(k:integer):integer;
        begin
            b:= foo(k);
            return b;
        end

        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
        end
        """
                        
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_9(self):
        input = """
        function foo(k:integer):integer;
        begin
            return b;
        end
        function foo1(k:integer):integer;
        begin
            return foo(1);
        end
        var b: integer;
            d: real;
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            
        end
        """
                        
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,459))


    def test_60(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            return x;
        end
        procedure main ();
        var x:real;
        begin
        end
        """ 
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_61(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            if(x>y)then
                return 1;
            return 2;
        end
        procedure main ();
        var x:real;
        begin
        end
        """ 
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_62(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            if(x>y)then
                return 1;
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_63(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            if(x>y)then
                x:=y;
            else
                return 1;
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_64(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            x:=y;
            y:=x+1;
            y:=x*x;
            if(x>y)then
                return x;
            else
                return y;

        end
        procedure main ();
        var x:real;
        begin
        end
        """ 
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_65(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:boolean;
                z:real;
            do begin
                return y;
            end

        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Type Mismatch In Statement: Return(Some(Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_66(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            if(x>y)then
                return x;
            else
                return y;
            x:=y;
        end
        procedure main ();
        var x:real;
        begin
            x := f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_67(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:boolean;
                z:real;
            do begin
                if (x>10) then return 10;
            end

        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_68(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:boolean;
                z:real;
            do begin
                if (x>10) then return 10;
                else return 100;
                x:=100;
            end
            x:=50;

        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),IntLiteral(100))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_69(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:boolean;
                z:real;
            do begin
                if (x>10) then return 10;
            end
            x:=50;
            return 10;
            return 100;

        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: Return(Some(IntLiteral(100)))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_70(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            with
                x:integer;
                y:boolean;
                z:real;
            do begin
                if (x>10) then return 10;
            end
            x:=50;
            return 10;
            return 100;

        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: Return(Some(IntLiteral(100)))"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_71(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            for x:=5 to 100 do
            begin
                return 10;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_72(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                return 10;
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_73(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                if(x=5) then return 1;
                else return 10;
                x:=x+1;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_74(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                with x:integer;y:real; do
                begin
                    return x*x;
                end
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                with x:integer;y:real; do
                begin
                    with a: integer; do
                        return a;
                end
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                with x:integer;y:real; do
                begin
                    if 1>0 then
                        return x;
                    else 
                        return 3;
                end
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                with x:integer;y:real; do
                begin
                    if 1>0 then
                        return 3.5;
                end
                return 3;
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(3.5)))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin

            while(x<y) do
            begin
                with x:integer;y:real; do
                begin
                    if 1>0 then
                        return 3;
                end
                x:=x+y;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        """More complex program"""
        input = """
        function foo():integer;
        begin
            return 4;
        end
        function k():real;
        begin
        return 3.4;
        end
        function f():integer;
        var x,y:integer;
        begin

        return foo();
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        """ 
        expect = "Unreachable Function: k"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        """More complex program"""
        input = """
        function f():integer;
        var x,y:integer;
        begin
            return d[0];
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        var x,y,z:integer;
            d: array [1 .. 3] of real;
        """ 
        expect = "Type Mismatch In Statement: Return(Some(ArrayCell(Id(d),IntLiteral(0))))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        """More complex program"""
        input = """
        function f():real;
        var x,y:integer;
        begin
            return x;
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
            return x;
        end
        var x,y,z:integer;
            d: array [1 .. 3] of real;
        """ 
        expect = "Type Mismatch In Statement: Return(Some(Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of real;
        var x,y:integer;
        begin
            return d;
        end
        procedure main ();
        var x:real;
        begin
            x:=f();
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Id(f),[]))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of real;
        var x,y:integer;
        begin
            return d;
        end
        procedure main ();
        var x:real;
        begin
            x:=f()[3];
            return x;
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "Type Mismatch In Statement: Return(Some(Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of real;
        var x,y:integer;
        begin
            if "main" > 0 then
                d[1] := f()[0]; 
            return d;
        end
        procedure main ();
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "Type Mismatch In Expression: BinaryOp(>,StringLiteral(main),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of real;
        var x,y:integer;
        begin
            if 5 and then 8 then
                d[1] := f()[0]; 
            return d;
        end
        procedure main (b:integer);
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of real;
        var x,y:integer;
        begin
            if 5 and then 8 then
                d[1] := f()[0]; 
            return d;
        end
        procedure main (b:integer);
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of integer;
        var x,y:integer;
        begin
            return d;
        end
        procedure main ();
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of real;
        """ 
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of integer;
        var x,y:integer;
        begin
            d := f();
            return f();
        end
        procedure main ();
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of real;
        """ 
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),CallExpr(Id(f),[]))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of integer;
        var x,y:integer;
        begin
            return f();
        end
        procedure main ();
        var x:real;
        begin
            //x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of real;
        """ 
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        """More complex program"""
        input = """
        function f():array [1 .. 3] of integer;
        var x,y:integer;
        begin
            for x:= 0 to 5 do begin
                if 3<y then
                    return d;
                return d;
            end
        end
        procedure main ();
        var x:real;
        begin
            x:=f()[3];
        end
        var x,y,z:integer;
            d: array [1 .. 3] of integer;
        """ 
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,490))


    def test_91(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real):array [1 .. 2] of integer;
        var a: integer;
            b: boolean;
            c: string;
            d: array [1 .. 2] of integer;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                end
            end
            return d;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
        end
        """
                        
        expect = "Unreachable Function: f"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real): integer;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                end
            end
            return 1;
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:= f(1,2.5);
        end
        """
                        
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        """More complex program"""
        input = """
        function f(i:integer;j:real): integer;
        var a: integer;
        begin
            while a > 0 do 
            begin 
                if a <0 then
                begin
                end

            return 1;
            end
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:= f(1,2.5);
        end
        """
                        
        expect = "Function fNot Return "
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
        """More complex program"""
        input = """
        procedure k();
        begin
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
        end
        """
                        
        expect = "Unreachable Procedure: k"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
        """More complex program"""
        input = """
        procedure k(i:integer);
        begin
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            k();
        end
        """
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(k),[])"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
        """More complex program"""
        input = """
        procedure k(i:integer);
        begin
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:= True * 2;
        end
        """
                        
        expect = "Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
        """More complex program"""
        input = """
        procedure k(i:integer);
        begin
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            a:= k(a);
        end
        """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),CallExpr(Id(k),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
        """More complex program"""
        input = """
        procedure k(i:integer);
        begin
            main();
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin

        end
        """
                        
        expect = "Unreachable Procedure: k"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        """More complex program"""
        input = """
        procedure k(i:integer);
        begin
            main(i);
        end
        procedure main ();
        var a:integer;
            b: boolean;
        begin
            k(a);
        end
        """
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,499))