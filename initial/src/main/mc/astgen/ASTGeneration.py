from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
     # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visit(ctx.manyDecls())


    # Visit a parse tree produced by MCParser#manyDecls.
    def visitManyDecls(self, ctx:MCParser.ManyDeclsContext):
        return None


    # Visit a parse tree produced by MCParser#varDeclare.
    def visitVarDeclare(self, ctx:MCParser.VarDeclareContext):
        return None


    # Visit a parse tree produced by MCParser#varType.
    def visitVarType(self, ctx:MCParser.VarTypeContext):
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType();

    # Visit a parse tree produced by MCParser#manyVar.
    def visitManyVar(self, ctx:MCParser.ManyVarContext):
        return None


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return None


    # Visit a parse tree produced by MCParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MCParser.FuncDeclareContext):
        return None


    # Visit a parse tree produced by MCParser#returnType.
    def visitReturnType(self, ctx:MCParser.ReturnTypeContext):
        return None


    # Visit a parse tree produced by MCParser#paramDeclare.
    def visitParamDeclare(self, ctx:MCParser.ParamDeclareContext):
        return None


    # Visit a parse tree produced by MCParser#manyParam.
    def visitManyParam(self, ctx:MCParser.ManyParamContext):
        return None


    # Visit a parse tree produced by MCParser#param.
    def visitParam(self, ctx:MCParser.ParamContext):
        return None


    # Visit a parse tree produced by MCParser#blockStatement.
    def visitBlockStatement(self, ctx:MCParser.BlockStatementContext):
        return None


    # Visit a parse tree produced by MCParser#contentBlockStatement.
    def visitContentBlockStatement(self, ctx:MCParser.ContentBlockStatementContext):
        return None


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return None


    # Visit a parse tree produced by MCParser#assignment.
    def visitAssignment(self, ctx:MCParser.AssignmentContext):
        return None


    # Visit a parse tree produced by MCParser#callStatement.
    def visitCallStatement(self, ctx:MCParser.CallStatementContext):
        return None


    # Visit a parse tree produced by MCParser#listExpr.
    def visitListExpr(self, ctx:MCParser.ListExprContext):
        return None


    # Visit a parse tree produced by MCParser#returnFunc.
    def visitReturnFunc(self, ctx:MCParser.ReturnFuncContext):
        return None


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return None


    # Visit a parse tree produced by MCParser#condBlock.
    def visitCondBlock(self, ctx:MCParser.CondBlockContext):
        return None


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        return None


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return None


    # Visit a parse tree produced by MCParser#forExpr1.
    def visitForExpr1(self, ctx:MCParser.ForExpr1Context):
        return None


    # Visit a parse tree produced by MCParser#forExpr2.
    def visitForExpr2(self, ctx:MCParser.ForExpr2Context):
        return None


    # Visit a parse tree produced by MCParser#forExpr3.
    def visitForExpr3(self, ctx:MCParser.ForExpr3Context):
        return None


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return None


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return None


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return None


    # Visit a parse tree produced by MCParser#floatExpr.
    def visitFloatExpr(self, ctx:MCParser.FloatExprContext):
        return None


    # Visit a parse tree produced by MCParser#intExpr.
    def visitIntExpr(self, ctx:MCParser.IntExprContext):
        return None


    # Visit a parse tree produced by MCParser#boolExpr.
    def visitBoolExpr(self, ctx:MCParser.BoolExprContext):
        return None

