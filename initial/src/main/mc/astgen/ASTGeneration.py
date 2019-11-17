#  Name: Nguyen Thanh Hoang - ID: 1870172
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
     # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        declList = []
        for declNode in ctx.declInProgram(): 
            declList += self.visit(declNode)
        return Program(declList)


    # Visit a parse tree produced by MCParser#declInProgram.
    def visitDeclInProgram(self, ctx:MCParser.DeclInProgramContext):
        declInProgram = []
        if ctx.varDeclare(): 
            declInProgram += self.visit(ctx.varDeclare())
        else: 
            declInProgram.append(self.visit(ctx.funcDeclare()))
        return declInProgram

    # Visit a parse tree produced by MCParser#varDeclare.
    def visitVarDeclare(self, ctx:MCParser.VarDeclareContext):
        result = []
        for varNode in self.visit(ctx.manyVar()):
            # Basic type 
            if self.visit(varNode)[1] == -1: 
                result.append(VarDecl(self.visit(varNode)[0], self.visit(ctx.varType())))   
            # Array type
            else: 
                result.append(VarDecl(self.visit(varNode)[0], ArrayType(self.visit(varNode)[1], self.visit(ctx.varType()))))
        return result 


    # Visit a parse tree produced by MCParser#varType.
    def visitVarType(self, ctx:MCParser.VarTypeContext):
        if ctx.BOOLTYPE():
            varType = BoolType()
        elif ctx.INTTYPE():
            varType = IntType()
        elif ctx.FLOATTYPE():
            varType = FloatType()
        elif ctx.STRINGTYPE():
            varType = StringType()
        else:
            varType = "UNKNOWN"
        return varType
     

    # Visit a parse tree produced by MCParser#manyVar.
    def visitManyVar(self, ctx:MCParser.ManyVarContext):
        return ctx.var()


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        """Return var with format: [varName, index] 
                where: 
                    + index = -1: var belongs to basic type (int, float, string, ...)
                    + index > 0 : var belongs to array type"""
        if ctx.getChildCount() > 1:
            return [ctx.IDENTIFIER().getText(), int(ctx.INTLIT().getText())]
        else: 
            return [ctx.IDENTIFIER().getText(), -1]


    # Visit a parse tree produced by MCParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MCParser.FuncDeclareContext):
        return FuncDecl( Id(ctx.IDENTIFIER().getText()), 
                            self.visit(ctx.paramList()) if ctx.paramList() else [],  
                            self.visit(ctx.returnType()), 
                            self.visit(ctx.blockStatement()))


    # Visit a parse tree produced by MCParser#returnType.
    def visitReturnType(self, ctx:MCParser.ReturnTypeContext):
        if ctx.BOOLTYPE():
            returnType = BoolType()
        elif ctx.INTTYPE():
            returnType = IntType()
        elif ctx.FLOATTYPE():
            returnType = FloatType()
        elif ctx.STRINGTYPE():
            returnType = StringType()
        elif ctx.VOIDTYPE(): 
            returnType = VoidType()
        else:
            raise ValueError("Not implemented yet.")

        # Check if return type is array pointer type 
        if ctx.LQB():
            returnType = ArrayPointerType(returnType)

        return returnType

    # Visit a parse tree produced by MCParser#paramList.
    def visitParamList(self, ctx:MCParser.ParamListContext):
        paramList = []
        for paramDeclareNode in ctx.paramDeclare():
            paramList.append(self.visit(paramDeclareNode))
        return paramList

    # Visit a parse tree produced by MCParser#paramDeclare.
    def visitParamDeclare(self, ctx:MCParser.ParamDeclareContext):
        # Basic type 
        if self.visit(ctx.paramName())[1] == False: 
            return VarDecl(self.visit(ctx.paramName())[0], self.visit(ctx.varType()))
        # Array type 
        else:
            return VarDecl(self.visit(ctx.paramName())[0], ArrayPointerType(self.visit(ctx.varType())))

    # Visit a parse tree produced by MCParser#paramName.
    def visitParamName(self, ctx:MCParser.ParamNameContext):
        # Array type 
        if ctx.getChildCount() > 1:
            return [ctx.IDENTIFIER().getText(), True]
        # Basic type 
        else: 
            return [ctx.IDENTIFIER().getText(), False]


    # Visit a parse tree produced by MCParser#blockStatement.
    def visitBlockStatement(self, ctx:MCParser.BlockStatementContext):
        return Block(self.visit(ctx.contentBlockStatement())) if ctx.contentBlockStatement() else Block([])


    # Visit a parse tree produced by MCParser#contentBlockStatement.
    def visitContentBlockStatement(self, ctx:MCParser.ContentBlockStatementContext):
        blockMemberList = []
        for declNode in ctx.declInFunc():
            blockMemberList += self.visit(declNode)
        return blockMemberList

    # Visit a parse tree produced by MCParser#declInFunc.
    def visitDeclInFunc(self, ctx:MCParser.DeclInFuncContext):
        # Var declare 
        if ctx.varDeclare(): 
            return self.visit(ctx.varDeclare())
        # Statement declare
        else:  
            return [self.visit(ctx.statement())]


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        if ctx.assignStatement(): 
            return self.visit(ctx.assignStatement())
        elif ctx.ifStatement(): 
            return self.visit(ctx.ifStatement())
        elif ctx.doWhileStatement(): 
            return self.visit(ctx.doWhileStatement())
        elif ctx.forStatement(): 
            return self.visit(ctx.forStatement())
        elif ctx.blockStatement(): 
            return self.visit(ctx.blockStatement())
        elif ctx.callStatement(): 
            return self.visit(ctx.callStatement())
        elif ctx.returnFunc(): 
            return self.visit(ctx.returnFunc())
        else: 
            return "UNKOWN_STATEMENT" 


    # Visit a parse tree produced by MCParser#assignment.
    def visitAssignStatement(self, ctx:MCParser.AssignStatementContext):
        leftExpr  = Id(ctx.IDENTIFIER().getText())
        rightExpr = self.visit(ctx.expr())
        return BinaryOp(ctx.ASSOP().getText(), leftExpr, rightExpr)


    # Visit a parse tree produced by MCParser#callStatement.
    def visitCallStatement(self, ctx:MCParser.CallStatementContext):
        method    = Id(ctx.IDENTIFIER().getText())
        paramList = self.visit(ctx.listExpr()) if ctx.listExpr() else []
        return CallExpr(method, paramList)


    # Visit a parse tree produced by MCParser#listExpr.
    def visitListExpr(self, ctx:MCParser.ListExprContext):
        listExpr = []
        for exprNode in ctx.expr(): 
            listExpr.append(self.visit(exprNode))
        return listExpr


    # Visit a parse tree produced by MCParser#returnFunc.
    def visitReturnFunc(self, ctx:MCParser.ReturnFuncContext):
        return Return(self.visit(ctx.expr()))


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIfStatement(self, ctx:MCParser.IfStatementContext):
        expr     = self.visit(ctx.boolExpr())
        thenStmt = self.visit(ctx.statement(0))
        if ctx.KEYWORD_ELSE(): 
            elseStmt = self.visit(ctx.statement(1))
        else:
            elseStmt = None
        return If(expr, thenStmt, elseStmt)


    # Visit a parse tree produced by MCParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MCParser.DoWhileStatementContext):
        stmList = [self.visit(ctx.blockStatement())]
        expr    = self.visit(ctx.boolExpr())
        return Dowhile(stmList, expr)


    # Visit a parse tree produced by MCParser#forStatement.
    def visitForStatement(self, ctx:MCParser.ForStatementContext):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.boolExpr())
        expr3 = self.visit(ctx.expr(1))
        loop  = self.visit(ctx.statement()) 
        return For(expr1, expr2, expr3, loop)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreakStatement(self, ctx:MCParser.BreakStatementContext):
        return Break()


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinueStatement(self, ctx:MCParser.ContinueStatementContext):
        return Continue()


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        if ctx.floatExpr():
            return self.visit(ctx.floatExpr())
        elif ctx.intExpr():
            return self.visit(ctx.intExpr())
        elif ctx.boolExpr():
            return self.visit(ctx.boolExpr())
        elif ctx.stringExpr():
            return self.visit(ctx.stringExpr())
        elif ctx.indexExpr():
            return self.visit(ctx.indexExpr())
        else:
            return "UNKNOWN_EXPR"


    # Visit a parse tree produced by MCParser#floatExpr.
    def visitFloatExpr(self, ctx:MCParser.FloatExprContext):
        if ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.intExpr():
            return self.visit(ctx.intExpr())
        else: 
            # Expression in "(" and ")"
            if ctx.LB():
                return self.visit(ctx.getChild(1))
            # Binary Oprand
            elif ctx.getChildCount() == 3: 
                op        = ctx.getChild(1).getText()
                leftExpr  = self.visit(ctx.getChild(0))
                rightExpr = self.visit(ctx.getChild(2))
                return BinaryOp(op, leftExpr, rightExpr)
            else:
                return "UNDEFINED_EXPR"


    # Visit a parse tree produced by MCParser#intExpr.
    def visitIntExpr(self, ctx:MCParser.IntExprContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else: 
            # Expression in "(" and ")"
            if ctx.LB():
                # return self.visit(ctx.intExpr())
                return self.visit(ctx.getChild(1))
            # Binary Oprand
            elif ctx.getChildCount() == 3: 
                op        = ctx.getChild(1).getText()
                leftExpr  = self.visit(ctx.getChild(0))
                rightExpr = self.visit(ctx.getChild(2))
                return BinaryOp(op, leftExpr, rightExpr)
            else:
                return "UNDEFINED_EXPR"

    # Visit a parse tree produced by MCParser#boolExpr.
    def visitBoolExpr(self, ctx:MCParser.BoolExprContext):
        if ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.intExpr():
            return self.visit(ctx.intExpr())
        else: 
            # Expression in "(" and ")"
            if ctx.LB():
                return self.visit(ctx.getChild(1))
            # Binary Oprand
            elif ctx.getChildCount() == 3: 
                op        = ctx.getChild(1).getText()
                leftExpr  = self.visit(ctx.getChild(0))
                rightExpr = self.visit(ctx.getChild(2))
                return BinaryOp(op, leftExpr, rightExpr)
            else: 
                return "UNDEFINED_EXPR"


    # Visit a parse tree produced by MCParser#stringExpr.
    def visitStringExpr(self, ctx:MCParser.StringExprContext):
        leftExpr  = Id(ctx.IDENTIFIER().getText())
        rightExpr = StringLiteral(ctx.STRLIT().getText())
        return BinaryOp("=", leftExpr, rightExpr)


    # Visit a parse tree produced by MCParser#indexExpr.
    def visitIndexExpr(self, ctx:MCParser.IndexExprContext):
        if ctx.getChildCount() > 1:  
            idxExpr = "INDEX_BY_ARRAY_TYPE"
        else:
            idxExpr = self.visit(ctx.intExpr()) 
        return idxExpr
