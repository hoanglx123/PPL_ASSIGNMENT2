from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
     # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        declList = []
        for declNode in ctx.declInProgram(): 
            declList += self.visit(declNode)
        # return Program(declList)
        return Program(declList)


    # Visit a parse tree produced by MCParser#declInProgram.
    def visitDeclInProgram(self, ctx:MCParser.DeclInProgramContext):
        if ctx.varDeclare(): 
            return self.visit(ctx.varDeclare())
        else: 
            return self.visit(ctx.funcDeclare())

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
        # paramList = []
        # for paramDeclareNode in self.visit(ctx.paramList()): 
        #     Array pointer type 
        #     if self.visit(paramDeclareNode)[1] == True: 
        #         paramList.append(VarDecl(self.visit(paramDeclareNode)[0], ArrayPointerType(self.visit(ctx.varType()))))
        #     # Basic type 
        #     else:
        #         paramList.append(VarDecl(self.visit(paramDeclareNode)[0], self.visit(ctx.varType())))

        FuncDeclObj = FuncDecl( Id(ctx.IDENTIFIER().getText()), 
                                self.visit(ctx.paramList()) if ctx.paramList() else [],  
                                self.visit(ctx.returnType()), 
                                self.visit(ctx.blockStatement()))
        return [FuncDeclObj]


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
            return ArrayPointerType(self.visit(ctx.varType()))

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
        return Block([])


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

