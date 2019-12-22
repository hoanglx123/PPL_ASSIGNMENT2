
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

import functools

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType(partype: %s, rettype: %s)" % (self.partype, self.rettype)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(name: %s, mtype: %s, value: %s)" % (self.name, self.mtype, self.value)

def CheckTypeCoercions(leftType, rightType):
    bCheckResult = True
    if type(leftType) is IntType and type(rightType) is IntType:
        bCheckResult = True
    elif type(leftType) is FloatType and type(rightType) is FloatType:
        bCheckResult = True
    elif type(leftType) is FloatType and type(rightType) is IntType:
        bCheckResult = True
    elif type(leftType) is BoolType and type(rightType) is BoolType:
        bCheckResult = True
    elif type(leftType) is StringType and type(rightType) is StringType:
        bCheckResult = True
    else:
        bCheckResult = False
    return bCheckResult

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putIntLn",MType([IntType()],VoidType()))
    ]

    def __init__(self,ast):
        # print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        allVar = functools.reduce(lambda env, decl: env + [self.visit(decl, env)], ast.decl, [])
        return allVar

    def visitFuncDecl(self,ast, c):
        print("visitFuncDecl: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        # if ast.name.name in c:
        found = self.lookup(ast.name.name, c, lambda x: x.name)
        if found:
            raise Redeclared(Function(), ast.name.name)
        else:
            try:
                localVar = functools.reduce(lambda env, varDecls: env + [self.visit(varDecls, env)], ast.param, [])
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)

            env = localVar
            hasReturn = False
            for varDecls in ast.body.member:
                if type(varDecls) is VarDecl:
                    env = env + [self.visit(varDecls, env)]
                else:
                    result = self.visit(varDecls, env + c)
                    # Check if it is return statement
                    if type(varDecls) is Return:
                        hasReturn = True
                        # Check mismatch type in return
                        if type(ast.returnType) != type(result.mtype):
                            raise TypeMismatchInStatement(varDecls)

            # Check if function has no return
            if (type(ast.returnType) != VoidType) and (hasReturn == False):
                raise FunctionNotReturn(ast.name.name)

        return Symbol(ast.name.name, ast.returnType)

    def visitVarDecl(self,ast, c):
        print("visitVarDecl: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        found = self.lookup(ast.variable, c, lambda x: x.name)
        if found:
            raise Redeclared(Variable(), ast.variable)
        else:
            return Symbol(ast.variable, ast.varType)

    def visitCallExpr(self, ast, c):
        print("visitCallExpr: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        found = self.lookup(ast.method.name, c, lambda x: x.name)
        if found is None:
            raise Undeclared(Function(), ast.method.name)

    def visitBinaryOp(self, ast, c):
        print("visitBinaryOp: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        leftResult  = self.visit(ast.left, c)
        rightResult = self.visit(ast.right, c)

        if CheckTypeCoercions(leftResult.mtype, rightResult.mtype) == False:
            raise TypeMismatchInExpression(ast)
        else:
            print("OK")
            print(leftResult)
            print(rightResult)
            return Symbol("BinaryOp", leftResult.mtype)

    def visitUnaryOp(self, ast, c):
        result = self.visit(ast.body, ast)
        return Symbol("UnaryOp", result.mtype)

    def visitBlock(self,ast, c):
        print("visitBlock: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        # localDecls = functools.reduce(lambda env, blockMem: env + [self.visit(blockMem, env)], ast.member, [])
        env = []
        for blockMem in ast.member:
            if type(blockMem) is VarDecl:
                env = env + [self.visit(blockMem, env)]
            else:
                self.visit(blockMem, env + c)
        return env

    def visitId(self,ast, c):
        print("visitId: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        found = self.lookup(ast.name, c, lambda x: x.name)
        if found is None:
            raise Undeclared(Variable(), ast.name)
        else:
            return Symbol(found.name, found.mtype)

    def visitIf(self,ast, c):
        print("visitIf: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        result = self.visit(ast.expr, c)
        if type(result.mtype) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            self.visit(ast.thenStmt, c)
            if ast.elseStmt:
                self.visit(ast.elseStmt, c)

    def visitFor(self,ast, c):
        print("visitFor: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        # Check expression1
        if ast.expr1:
            result = self.visit(ast.expr1, c)
            if type(result.mtype) is not IntType:
                raise TypeMismatchInStatement(ast)

        # Check expression2
        if ast.expr2:
            result = self.visit(ast.expr2, c)
            if type(result.mtype) is not BoolType:
                raise TypeMismatchInStatement(ast)

        # Check expression3
        if ast.expr3:
            result = self.visit(ast.expr3, c)
            if type(result.mtype) is not IntType:
                raise TypeMismatchInStatement(ast)

        self.visit(ast.loop, c)

    def visitDowhile(self,ast, c):
        print("visitDowhile: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        result = self.visit(ast.exp, c)
        if type(result.mtype) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            [self.visit(statement, c) for statement in ast.sl]

    def visitContinue(self,ast, c):
        return None

    def visitBreak(self,ast, c):
        return None

    def visitReturn(self,ast, c):
        print("visitReturn: %s, env: %s" % (ast, ','.join(str(i) for i in c)))
        if ast.expr:
            result = self.visit(ast.expr, c)
        else:
            # Used for return without expression
            result = Symbol("Return", VoidType())
        return result

    def visitIntType(self,ast, c):
        return Symbol("Return", IntType())

    def visitFloatType(self,ast, c):
        return Symbol("Return", FloatType())

    def visitBoolType(self,ast, c):
        return Symbol("Return", BoolType())

    def visitStringType(self,ast, c):
        return Symbol("Return", StringType())

    def visitVoidType(self,ast, c):
        return Symbol("Return", VoidType())

    def visitIntLiteral(self,ast, c):
        return Symbol("Return", IntType())

    def visitFloatLiteral(self,ast, c):
        return Symbol("Return", FloatType())

    def visitBooleanLiteral(self,ast, c):
        return Symbol("Return", BooleanType())

    def visitStringLiteral(self,ast, c):
        return Symbol("Return", StringType())


