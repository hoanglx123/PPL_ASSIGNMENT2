# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declInProgram.
    def visitDeclInProgram(self, ctx:MCParser.DeclInProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDeclare.
    def visitVarDeclare(self, ctx:MCParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varType.
    def visitVarType(self, ctx:MCParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manyVar.
    def visitManyVar(self, ctx:MCParser.ManyVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MCParser.FuncDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnType.
    def visitReturnType(self, ctx:MCParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramList.
    def visitParamList(self, ctx:MCParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramDeclare.
    def visitParamDeclare(self, ctx:MCParser.ParamDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramName.
    def visitParamName(self, ctx:MCParser.ParamNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockStatement.
    def visitBlockStatement(self, ctx:MCParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#contentBlockStatement.
    def visitContentBlockStatement(self, ctx:MCParser.ContentBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declInFunc.
    def visitDeclInFunc(self, ctx:MCParser.DeclInFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assignStatement.
    def visitAssignStatement(self, ctx:MCParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#callStatement.
    def visitCallStatement(self, ctx:MCParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listExpr.
    def visitListExpr(self, ctx:MCParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnFunc.
    def visitReturnFunc(self, ctx:MCParser.ReturnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStatement.
    def visitIfStatement(self, ctx:MCParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MCParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStatement.
    def visitForStatement(self, ctx:MCParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStatement.
    def visitBreakStatement(self, ctx:MCParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continueStatement.
    def visitContinueStatement(self, ctx:MCParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#floatExpr.
    def visitFloatExpr(self, ctx:MCParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#intExpr.
    def visitIntExpr(self, ctx:MCParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#boolExpr.
    def visitBoolExpr(self, ctx:MCParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stringExpr.
    def visitStringExpr(self, ctx:MCParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#indexExpr.
    def visitIndexExpr(self, ctx:MCParser.IndexExprContext):
        return self.visitChildren(ctx)



del MCParser