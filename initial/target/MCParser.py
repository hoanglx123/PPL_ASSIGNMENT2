# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0138\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\3\2\3\3\3\3\5\3F\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6Q\n\6\f\6\16\6T\13\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7Z\n\7\3\b\3\b\3\b\3\b\5\b`\n\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\5\th\n\t\3\n\3\n\3\n\7\nm\n\n\f\n\16")
        buf.write("\np\13\n\3\13\3\13\3\13\3\f\3\f\3\f\5\fx\n\f\3\r\3\r\5")
        buf.write("\r|\n\r\3\r\3\r\3\16\3\16\5\16\u0082\n\16\3\16\3\16\7")
        buf.write("\16\u0086\n\16\f\16\16\16\u0089\13\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u0092\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\5\21\u009c\n\21\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\7\22\u00a4\n\22\f\22\16\22\u00a7\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00b2")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\5\27\u00c1\n\27\3\27\3\27\5\27\u00c5\n")
        buf.write("\27\3\27\3\27\5\27\u00c9\n\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\5\35\u00dd\n\35\3\36\3\36\3\36\3\36\5\36\u00e3")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\7\36\u00fa\n\36\f\36\16\36\u00fd\13\36\3\37\3\37\3\37")
        buf.write("\5\37\u0102\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\7\37\u0119\n\37\f\37\16\37\u011c\13\37")
        buf.write("\3 \3 \5 \u0120\n \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \7 \u0133\n \f \16 \u0136\13 \3 \2\5:")
        buf.write("<>!\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>\2\t\3\2\21\24\3\2\21\25\3\2\30\32\3\2\26")
        buf.write("\27\3\2 \"\3\2\36\37\5\2\r\r\17\17--\2\u0148\2@\3\2\2")
        buf.write("\2\4E\3\2\2\2\6G\3\2\2\2\bK\3\2\2\2\nM\3\2\2\2\fU\3\2")
        buf.write("\2\2\16[\3\2\2\2\20d\3\2\2\2\22i\3\2\2\2\24q\3\2\2\2\26")
        buf.write("t\3\2\2\2\30y\3\2\2\2\32\u0081\3\2\2\2\34\u0091\3\2\2")
        buf.write("\2\36\u0093\3\2\2\2 \u0098\3\2\2\2\"\u00a0\3\2\2\2$\u00a8")
        buf.write("\3\2\2\2&\u00ac\3\2\2\2(\u00b3\3\2\2\2*\u00b7\3\2\2\2")
        buf.write(",\u00bd\3\2\2\2.\u00cd\3\2\2\2\60\u00cf\3\2\2\2\62\u00d1")
        buf.write("\3\2\2\2\64\u00d3\3\2\2\2\66\u00d6\3\2\2\28\u00dc\3\2")
        buf.write("\2\2:\u00e2\3\2\2\2<\u0101\3\2\2\2>\u011d\3\2\2\2@A\5")
        buf.write("\4\3\2AB\7\2\2\3B\3\3\2\2\2CF\5\6\4\2DF\5\16\b\2EC\3\2")
        buf.write("\2\2ED\3\2\2\2F\5\3\2\2\2GH\5\b\5\2HI\5\n\6\2IJ\7+\2\2")
        buf.write("J\7\3\2\2\2KL\t\2\2\2L\t\3\2\2\2MR\5\f\7\2NO\7,\2\2OQ")
        buf.write("\5\f\7\2PN\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\13\3")
        buf.write("\2\2\2TR\3\2\2\2UY\7-\2\2VW\7\'\2\2WX\7\r\2\2XZ\7(\2\2")
        buf.write("YV\3\2\2\2YZ\3\2\2\2Z\r\3\2\2\2[\\\5\20\t\2\\]\7-\2\2")
        buf.write("]_\7%\2\2^`\5\22\n\2_^\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7")
        buf.write("&\2\2bc\5\30\r\2c\17\3\2\2\2dg\t\3\2\2ef\7\'\2\2fh\7(")
        buf.write("\2\2ge\3\2\2\2gh\3\2\2\2h\21\3\2\2\2in\5\24\13\2jk\7,")
        buf.write("\2\2km\5\24\13\2lj\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2")
        buf.write("\2o\23\3\2\2\2pn\3\2\2\2qr\5\b\5\2rs\5\26\f\2s\25\3\2")
        buf.write("\2\2tw\7-\2\2uv\7\'\2\2vx\7(\2\2wu\3\2\2\2wx\3\2\2\2x")
        buf.write("\27\3\2\2\2y{\7)\2\2z|\5\32\16\2{z\3\2\2\2{|\3\2\2\2|")
        buf.write("}\3\2\2\2}~\7*\2\2~\31\3\2\2\2\177\u0082\5\6\4\2\u0080")
        buf.write("\u0082\5\34\17\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\u0087\3\2\2\2\u0083\u0086\5\6\4\2\u0084\u0086\5")
        buf.write("\34\17\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\33\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u0092\5\36")
        buf.write("\20\2\u008b\u0092\5&\24\2\u008c\u0092\5*\26\2\u008d\u0092")
        buf.write("\5,\27\2\u008e\u0092\5\30\r\2\u008f\u0092\5 \21\2\u0090")
        buf.write("\u0092\5$\23\2\u0091\u008a\3\2\2\2\u0091\u008b\3\2\2\2")
        buf.write("\u0091\u008c\3\2\2\2\u0091\u008d\3\2\2\2\u0091\u008e\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\35")
        buf.write("\3\2\2\2\u0093\u0094\7-\2\2\u0094\u0095\7$\2\2\u0095\u0096")
        buf.write("\58\35\2\u0096\u0097\7+\2\2\u0097\37\3\2\2\2\u0098\u0099")
        buf.write("\7-\2\2\u0099\u009b\7%\2\2\u009a\u009c\5\"\22\2\u009b")
        buf.write("\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u009e\7&\2\2\u009e\u009f\7+\2\2\u009f!\3\2\2\2")
        buf.write("\u00a0\u00a5\58\35\2\u00a1\u00a2\7,\2\2\u00a2\u00a4\5")
        buf.write("8\35\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6#\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00a9\7\n\2\2\u00a9\u00aa\58\35\2\u00aa")
        buf.write("\u00ab\7+\2\2\u00ab%\3\2\2\2\u00ac\u00ad\7\t\2\2\u00ad")
        buf.write("\u00ae\5(\25\2\u00ae\u00b1\5\30\r\2\u00af\u00b0\7\7\2")
        buf.write("\2\u00b0\u00b2\5\30\r\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\'\3\2\2\2\u00b3\u00b4\7%\2\2\u00b4\u00b5")
        buf.write("\5> \2\u00b5\u00b6\7&\2\2\u00b6)\3\2\2\2\u00b7\u00b8\7")
        buf.write("\13\2\2\u00b8\u00b9\5\30\r\2\u00b9\u00ba\7\f\2\2\u00ba")
        buf.write("\u00bb\5(\25\2\u00bb\u00bc\7+\2\2\u00bc+\3\2\2\2\u00bd")
        buf.write("\u00be\7\b\2\2\u00be\u00c0\7%\2\2\u00bf\u00c1\5.\30\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c4\7+\2\2\u00c3\u00c5\5\60\31\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c8\7+\2\2\u00c7\u00c9\5\62\32\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\7&\2\2\u00cb\u00cc\5\30\r\2\u00cc-\3\2\2\2\u00cd")
        buf.write("\u00ce\58\35\2\u00ce/\3\2\2\2\u00cf\u00d0\5> \2\u00d0")
        buf.write("\61\3\2\2\2\u00d1\u00d2\58\35\2\u00d2\63\3\2\2\2\u00d3")
        buf.write("\u00d4\7\5\2\2\u00d4\u00d5\7+\2\2\u00d5\65\3\2\2\2\u00d6")
        buf.write("\u00d7\7\6\2\2\u00d7\u00d8\7+\2\2\u00d8\67\3\2\2\2\u00d9")
        buf.write("\u00dd\5:\36\2\u00da\u00dd\5<\37\2\u00db\u00dd\5> \2\u00dc")
        buf.write("\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2")
        buf.write("\u00dd9\3\2\2\2\u00de\u00df\b\36\1\2\u00df\u00e3\7\16")
        buf.write("\2\2\u00e0\u00e3\5> \2\u00e1\u00e3\5<\37\2\u00e2\u00de")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("\u00fb\3\2\2\2\u00e4\u00e5\f\f\2\2\u00e5\u00e6\t\4\2\2")
        buf.write("\u00e6\u00fa\5:\36\f\u00e7\u00e8\f\13\2\2\u00e8\u00e9")
        buf.write("\t\5\2\2\u00e9\u00fa\5:\36\13\u00ea\u00eb\f\n\2\2\u00eb")
        buf.write("\u00ec\t\6\2\2\u00ec\u00fa\5:\36\13\u00ed\u00ee\f\t\2")
        buf.write("\2\u00ee\u00ef\t\7\2\2\u00ef\u00fa\5:\36\n\u00f0\u00f1")
        buf.write("\f\b\2\2\u00f1\u00f2\7\35\2\2\u00f2\u00fa\5:\36\b\u00f3")
        buf.write("\u00f4\f\7\2\2\u00f4\u00f5\7\34\2\2\u00f5\u00fa\5:\36")
        buf.write("\7\u00f6\u00f7\f\6\2\2\u00f7\u00f8\7$\2\2\u00f8\u00fa")
        buf.write("\5:\36\7\u00f9\u00e4\3\2\2\2\u00f9\u00e7\3\2\2\2\u00f9")
        buf.write("\u00ea\3\2\2\2\u00f9\u00ed\3\2\2\2\u00f9\u00f0\3\2\2\2")
        buf.write("\u00f9\u00f3\3\2\2\2\u00f9\u00f6\3\2\2\2\u00fa\u00fd\3")
        buf.write("\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc;")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\b\37\1\2\u00ff")
        buf.write("\u0102\7\r\2\2\u0100\u0102\5> \2\u0101\u00fe\3\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u011a\3\2\2\2\u0103\u0104\f\13\2")
        buf.write("\2\u0104\u0105\t\4\2\2\u0105\u0119\5<\37\13\u0106\u0107")
        buf.write("\f\n\2\2\u0107\u0108\t\5\2\2\u0108\u0119\5<\37\n\u0109")
        buf.write("\u010a\f\t\2\2\u010a\u010b\t\6\2\2\u010b\u0119\5<\37\n")
        buf.write("\u010c\u010d\f\b\2\2\u010d\u010e\t\7\2\2\u010e\u0119\5")
        buf.write("<\37\t\u010f\u0110\f\7\2\2\u0110\u0111\7\35\2\2\u0111")
        buf.write("\u0119\5<\37\7\u0112\u0113\f\6\2\2\u0113\u0114\7\34\2")
        buf.write("\2\u0114\u0119\5<\37\6\u0115\u0116\f\5\2\2\u0116\u0117")
        buf.write("\7$\2\2\u0117\u0119\5<\37\6\u0118\u0103\3\2\2\2\u0118")
        buf.write("\u0106\3\2\2\2\u0118\u0109\3\2\2\2\u0118\u010c\3\2\2\2")
        buf.write("\u0118\u010f\3\2\2\2\u0118\u0112\3\2\2\2\u0118\u0115\3")
        buf.write("\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b=\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011f")
        buf.write("\b \1\2\u011e\u0120\7\33\2\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\t\b\2\2")
        buf.write("\u0122\u0134\3\2\2\2\u0123\u0124\f\b\2\2\u0124\u0125\t")
        buf.write("\6\2\2\u0125\u0133\5> \t\u0126\u0127\f\7\2\2\u0127\u0128")
        buf.write("\t\7\2\2\u0128\u0133\5> \b\u0129\u012a\f\6\2\2\u012a\u012b")
        buf.write("\7\35\2\2\u012b\u0133\5> \6\u012c\u012d\f\5\2\2\u012d")
        buf.write("\u012e\7\34\2\2\u012e\u0133\5> \5\u012f\u0130\f\4\2\2")
        buf.write("\u0130\u0131\7$\2\2\u0131\u0133\5> \5\u0132\u0123\3\2")
        buf.write("\2\2\u0132\u0126\3\2\2\2\u0132\u0129\3\2\2\2\u0132\u012c")
        buf.write("\3\2\2\2\u0132\u012f\3\2\2\2\u0133\u0136\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135?\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\36ERY_gnw{\u0081\u0085\u0087\u0091\u009b")
        buf.write("\u00a5\u00b1\u00c0\u00c4\u00c8\u00dc\u00e2\u00f9\u00fb")
        buf.write("\u0101\u0118\u011a\u011f\u0132\u0134")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'else'", "'for'", "'if'", "'return'", "'do'", "'while'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'boolean'", "'int'", "'float'", "'string'", "'void'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", 
                     "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", "KEYWORD_BREAK", 
                      "KEYWORD_CONTINUE", "KEYWORD_ELSE", "KEYWORD_FOR", 
                      "KEYWORD_IF", "KEYWORD_RETURN", "KEYWORD_DO", "KEYWORD_WHILE", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", "BOOLTYPE", 
                      "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", 
                      "OROP", "ANDOP", "NEQOP", "EQOP", "LTHOP", "GTHOP", 
                      "LEQOP", "GEQOP", "ASSOP", "LB", "RB", "LQB", "RQB", 
                      "LP", "RP", "SM", "CM", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declInProgram = 1
    RULE_varDeclare = 2
    RULE_varType = 3
    RULE_manyVar = 4
    RULE_var = 5
    RULE_funcDeclare = 6
    RULE_returnType = 7
    RULE_paramList = 8
    RULE_paramDeclare = 9
    RULE_paramName = 10
    RULE_blockStatement = 11
    RULE_contentBlockStatement = 12
    RULE_statement = 13
    RULE_assignment = 14
    RULE_callStatement = 15
    RULE_listExpr = 16
    RULE_returnFunc = 17
    RULE_if_statement = 18
    RULE_condBlock = 19
    RULE_do_while_statement = 20
    RULE_for_statement = 21
    RULE_forExpr1 = 22
    RULE_forExpr2 = 23
    RULE_forExpr3 = 24
    RULE_break_statement = 25
    RULE_continue_statement = 26
    RULE_expr = 27
    RULE_floatExpr = 28
    RULE_intExpr = 29
    RULE_boolExpr = 30

    ruleNames =  [ "program", "declInProgram", "varDeclare", "varType", 
                   "manyVar", "var", "funcDeclare", "returnType", "paramList", 
                   "paramDeclare", "paramName", "blockStatement", "contentBlockStatement", 
                   "statement", "assignment", "callStatement", "listExpr", 
                   "returnFunc", "if_statement", "condBlock", "do_while_statement", 
                   "for_statement", "forExpr1", "forExpr2", "forExpr3", 
                   "break_statement", "continue_statement", "expr", "floatExpr", 
                   "intExpr", "boolExpr" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    BLOCK_COMMENT=2
    KEYWORD_BREAK=3
    KEYWORD_CONTINUE=4
    KEYWORD_ELSE=5
    KEYWORD_FOR=6
    KEYWORD_IF=7
    KEYWORD_RETURN=8
    KEYWORD_DO=9
    KEYWORD_WHILE=10
    INTLIT=11
    FLOATLIT=12
    BOOLLIT=13
    STRLIT=14
    BOOLTYPE=15
    INTTYPE=16
    FLOATTYPE=17
    STRINGTYPE=18
    VOIDTYPE=19
    ADDOP=20
    SUBOP=21
    MULOP=22
    DIVOP=23
    MODOP=24
    NOTOP=25
    OROP=26
    ANDOP=27
    NEQOP=28
    EQOP=29
    LTHOP=30
    GTHOP=31
    LEQOP=32
    GEQOP=33
    ASSOP=34
    LB=35
    RB=36
    LQB=37
    RQB=38
    LP=39
    RP=40
    SM=41
    CM=42
    IDENTIFIER=43
    WS=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46
    ERROR_CHAR=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declInProgram(self):
            return self.getTypedRuleContext(MCParser.DeclInProgramContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.declInProgram()
            self.state = 63
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclInProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclare(self):
            return self.getTypedRuleContext(MCParser.VarDeclareContext,0)


        def funcDeclare(self):
            return self.getTypedRuleContext(MCParser.FuncDeclareContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declInProgram

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclInProgram" ):
                return visitor.visitDeclInProgram(self)
            else:
                return visitor.visitChildren(self)




    def declInProgram(self):

        localctx = MCParser.DeclInProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declInProgram)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.varDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.funcDeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(MCParser.VarTypeContext,0)


        def manyVar(self):
            return self.getTypedRuleContext(MCParser.ManyVarContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclare" ):
                return visitor.visitVarDeclare(self)
            else:
                return visitor.visitChildren(self)




    def varDeclare(self):

        localctx = MCParser.VarDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.varType()
            self.state = 70
            self.manyVar()
            self.state = 71
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = MCParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_manyVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyVar" ):
                return visitor.visitManyVar(self)
            else:
                return visitor.visitChildren(self)




    def manyVar(self):

        localctx = MCParser.ManyVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_manyVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.var()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 76
                self.match(MCParser.CM)
                self.state = 77
                self.var()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LQB(self):
            return self.getToken(MCParser.LQB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RQB(self):
            return self.getToken(MCParser.RQB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MCParser.IDENTIFIER)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LQB:
                self.state = 84
                self.match(MCParser.LQB)
                self.state = 85
                self.match(MCParser.INTLIT)
                self.state = 86
                self.match(MCParser.RQB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(MCParser.ReturnTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(MCParser.BlockStatementContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MCParser.ParamListContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclare" ):
                return visitor.visitFuncDeclare(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclare(self):

        localctx = MCParser.FuncDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.returnType()
            self.state = 90
            self.match(MCParser.IDENTIFIER)
            self.state = 91
            self.match(MCParser.LB)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 92
                self.paramList()


            self.state = 95
            self.match(MCParser.RB)
            self.state = 96
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def LQB(self):
            return self.getToken(MCParser.LQB, 0)

        def RQB(self):
            return self.getToken(MCParser.RQB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = MCParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LQB:
                self.state = 99
                self.match(MCParser.LQB)
                self.state = 100
                self.match(MCParser.RQB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParamDeclareContext)
            else:
                return self.getTypedRuleContext(MCParser.ParamDeclareContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.paramDeclare()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 104
                self.match(MCParser.CM)
                self.state = 105
                self.paramDeclare()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(MCParser.VarTypeContext,0)


        def paramName(self):
            return self.getTypedRuleContext(MCParser.ParamNameContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paramDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclare" ):
                return visitor.visitParamDeclare(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclare(self):

        localctx = MCParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.varType()
            self.state = 112
            self.paramName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LQB(self):
            return self.getToken(MCParser.LQB, 0)

        def RQB(self):
            return self.getToken(MCParser.RQB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_paramName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamName" ):
                return visitor.visitParamName(self)
            else:
                return visitor.visitChildren(self)




    def paramName(self):

        localctx = MCParser.ParamNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MCParser.IDENTIFIER)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LQB:
                self.state = 115
                self.match(MCParser.LQB)
                self.state = 116
                self.match(MCParser.RQB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def contentBlockStatement(self):
            return self.getTypedRuleContext(MCParser.ContentBlockStatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = MCParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MCParser.LP)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.KEYWORD_FOR) | (1 << MCParser.KEYWORD_IF) | (1 << MCParser.KEYWORD_RETURN) | (1 << MCParser.KEYWORD_DO) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.LP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 120
                self.contentBlockStatement()


            self.state = 123
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentBlockStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarDeclareContext)
            else:
                return self.getTypedRuleContext(MCParser.VarDeclareContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_contentBlockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContentBlockStatement" ):
                return visitor.visitContentBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def contentBlockStatement(self):

        localctx = MCParser.ContentBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_contentBlockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                self.state = 125
                self.varDeclare()
                pass
            elif token in [MCParser.KEYWORD_FOR, MCParser.KEYWORD_IF, MCParser.KEYWORD_RETURN, MCParser.KEYWORD_DO, MCParser.LP, MCParser.IDENTIFIER]:
                self.state = 126
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.KEYWORD_FOR) | (1 << MCParser.KEYWORD_IF) | (1 << MCParser.KEYWORD_RETURN) | (1 << MCParser.KEYWORD_DO) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.LP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 131
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                    self.state = 129
                    self.varDeclare()
                    pass
                elif token in [MCParser.KEYWORD_FOR, MCParser.KEYWORD_IF, MCParser.KEYWORD_RETURN, MCParser.KEYWORD_DO, MCParser.LP, MCParser.IDENTIFIER]:
                    self.state = 130
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MCParser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MCParser.If_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(MCParser.Do_while_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MCParser.For_statementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MCParser.BlockStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MCParser.CallStatementContext,0)


        def returnFunc(self):
            return self.getTypedRuleContext(MCParser.ReturnFuncContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.do_while_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.blockStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.callStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.returnFunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def ASSOP(self):
            return self.getToken(MCParser.ASSOP, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MCParser.IDENTIFIER)
            self.state = 146
            self.match(MCParser.ASSOP)
            self.state = 147
            self.expr()
            self.state = 148
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def listExpr(self):
            return self.getTypedRuleContext(MCParser.ListExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MCParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MCParser.IDENTIFIER)
            self.state = 151
            self.match(MCParser.LB)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 152
                self.listExpr()


            self.state = 155
            self.match(MCParser.RB)
            self.state = 156
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_listExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)




    def listExpr(self):

        localctx = MCParser.ListExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_listExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.expr()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 159
                self.match(MCParser.CM)
                self.state = 160
                self.expr()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_RETURN(self):
            return self.getToken(MCParser.KEYWORD_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_returnFunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnFunc" ):
                return visitor.visitReturnFunc(self)
            else:
                return visitor.visitChildren(self)




    def returnFunc(self):

        localctx = MCParser.ReturnFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MCParser.KEYWORD_RETURN)
            self.state = 167
            self.expr()
            self.state = 168
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_IF(self):
            return self.getToken(MCParser.KEYWORD_IF, 0)

        def condBlock(self):
            return self.getTypedRuleContext(MCParser.CondBlockContext,0)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(MCParser.BlockStatementContext,i)


        def KEYWORD_ELSE(self):
            return self.getToken(MCParser.KEYWORD_ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MCParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MCParser.KEYWORD_IF)
            self.state = 171
            self.condBlock()
            self.state = 172
            self.blockStatement()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.KEYWORD_ELSE:
                self.state = 173
                self.match(MCParser.KEYWORD_ELSE)
                self.state = 174
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(MCParser.BoolExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_condBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondBlock" ):
                return visitor.visitCondBlock(self)
            else:
                return visitor.visitChildren(self)




    def condBlock(self):

        localctx = MCParser.CondBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MCParser.LB)
            self.state = 178
            self.boolExpr(0)
            self.state = 179
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_DO(self):
            return self.getToken(MCParser.KEYWORD_DO, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(MCParser.BlockStatementContext,0)


        def KEYWORD_WHILE(self):
            return self.getToken(MCParser.KEYWORD_WHILE, 0)

        def condBlock(self):
            return self.getTypedRuleContext(MCParser.CondBlockContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = MCParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MCParser.KEYWORD_DO)
            self.state = 182
            self.blockStatement()
            self.state = 183
            self.match(MCParser.KEYWORD_WHILE)
            self.state = 184
            self.condBlock()
            self.state = 185
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_FOR(self):
            return self.getToken(MCParser.KEYWORD_FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SM)
            else:
                return self.getToken(MCParser.SM, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(MCParser.BlockStatementContext,0)


        def forExpr1(self):
            return self.getTypedRuleContext(MCParser.ForExpr1Context,0)


        def forExpr2(self):
            return self.getTypedRuleContext(MCParser.ForExpr2Context,0)


        def forExpr3(self):
            return self.getTypedRuleContext(MCParser.ForExpr3Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MCParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MCParser.KEYWORD_FOR)
            self.state = 188
            self.match(MCParser.LB)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 189
                self.forExpr1()


            self.state = 192
            self.match(MCParser.SM)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 193
                self.forExpr2()


            self.state = 196
            self.match(MCParser.SM)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 197
                self.forExpr3()


            self.state = 200
            self.match(MCParser.RB)
            self.state = 201
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExpr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forExpr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpr1" ):
                return visitor.visitForExpr1(self)
            else:
                return visitor.visitChildren(self)




    def forExpr1(self):

        localctx = MCParser.ForExpr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forExpr1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExpr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpr(self):
            return self.getTypedRuleContext(MCParser.BoolExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forExpr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpr2" ):
                return visitor.visitForExpr2(self)
            else:
                return visitor.visitChildren(self)




    def forExpr2(self):

        localctx = MCParser.ForExpr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forExpr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.boolExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExpr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forExpr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpr3" ):
                return visitor.visitForExpr3(self)
            else:
                return visitor.visitChildren(self)




    def forExpr3(self):

        localctx = MCParser.ForExpr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forExpr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_BREAK(self):
            return self.getToken(MCParser.KEYWORD_BREAK, 0)

        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MCParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MCParser.KEYWORD_BREAK)
            self.state = 210
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_CONTINUE(self):
            return self.getToken(MCParser.KEYWORD_CONTINUE, 0)

        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MCParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MCParser.KEYWORD_CONTINUE)
            self.state = 213
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def floatExpr(self):
            return self.getTypedRuleContext(MCParser.FloatExprContext,0)


        def intExpr(self):
            return self.getTypedRuleContext(MCParser.IntExprContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(MCParser.BoolExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.floatExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.intExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.boolExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(MCParser.BoolExprContext,0)


        def intExpr(self):
            return self.getTypedRuleContext(MCParser.IntExprContext,0)


        def floatExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.FloatExprContext)
            else:
                return self.getTypedRuleContext(MCParser.FloatExprContext,i)


        def DIVOP(self):
            return self.getToken(MCParser.DIVOP, 0)

        def MULOP(self):
            return self.getToken(MCParser.MULOP, 0)

        def MODOP(self):
            return self.getToken(MCParser.MODOP, 0)

        def ADDOP(self):
            return self.getToken(MCParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def LTHOP(self):
            return self.getToken(MCParser.LTHOP, 0)

        def LEQOP(self):
            return self.getToken(MCParser.LEQOP, 0)

        def GTHOP(self):
            return self.getToken(MCParser.GTHOP, 0)

        def EQOP(self):
            return self.getToken(MCParser.EQOP, 0)

        def NEQOP(self):
            return self.getToken(MCParser.NEQOP, 0)

        def ANDOP(self):
            return self.getToken(MCParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MCParser.OROP, 0)

        def ASSOP(self):
            return self.getToken(MCParser.ASSOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_floatExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)



    def floatExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.FloatExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_floatExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 221
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 2:
                self.state = 222
                self.boolExpr(0)
                pass

            elif la_ == 3:
                self.state = 223
                self.intExpr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 247
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 226
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.floatExpr(10)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 229
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 230
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 231
                        self.floatExpr(9)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 232
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 233
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 234
                        self.floatExpr(9)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 235
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 236
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 237
                        self.floatExpr(8)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 238
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 239
                        self.match(MCParser.ANDOP)
                        self.state = 240
                        self.floatExpr(6)
                        pass

                    elif la_ == 6:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 241
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 242
                        self.match(MCParser.OROP)
                        self.state = 243
                        self.floatExpr(5)
                        pass

                    elif la_ == 7:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 244
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 245
                        self.match(MCParser.ASSOP)
                        self.state = 246
                        self.floatExpr(5)
                        pass

             
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IntExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(MCParser.BoolExprContext,0)


        def intExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.IntExprContext)
            else:
                return self.getTypedRuleContext(MCParser.IntExprContext,i)


        def DIVOP(self):
            return self.getToken(MCParser.DIVOP, 0)

        def MULOP(self):
            return self.getToken(MCParser.MULOP, 0)

        def MODOP(self):
            return self.getToken(MCParser.MODOP, 0)

        def ADDOP(self):
            return self.getToken(MCParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def LTHOP(self):
            return self.getToken(MCParser.LTHOP, 0)

        def LEQOP(self):
            return self.getToken(MCParser.LEQOP, 0)

        def GTHOP(self):
            return self.getToken(MCParser.GTHOP, 0)

        def EQOP(self):
            return self.getToken(MCParser.EQOP, 0)

        def NEQOP(self):
            return self.getToken(MCParser.NEQOP, 0)

        def ANDOP(self):
            return self.getToken(MCParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MCParser.OROP, 0)

        def ASSOP(self):
            return self.getToken(MCParser.ASSOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_intExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)



    def intExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.IntExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_intExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.state = 254
                self.boolExpr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 278
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 257
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 258
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 259
                        self.intExpr(9)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 260
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 261
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 262
                        self.intExpr(8)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 263
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 264
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 265
                        self.intExpr(8)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 266
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 267
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 268
                        self.intExpr(7)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 269
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 270
                        self.match(MCParser.ANDOP)
                        self.state = 271
                        self.intExpr(5)
                        pass

                    elif la_ == 6:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 272
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 273
                        self.match(MCParser.OROP)
                        self.state = 274
                        self.intExpr(4)
                        pass

                    elif la_ == 7:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 275
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 276
                        self.match(MCParser.ASSOP)
                        self.state = 277
                        self.intExpr(4)
                        pass

             
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BoolExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def NOTOP(self):
            return self.getToken(MCParser.NOTOP, 0)

        def boolExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.BoolExprContext)
            else:
                return self.getTypedRuleContext(MCParser.BoolExprContext,i)


        def LTHOP(self):
            return self.getToken(MCParser.LTHOP, 0)

        def LEQOP(self):
            return self.getToken(MCParser.LEQOP, 0)

        def GTHOP(self):
            return self.getToken(MCParser.GTHOP, 0)

        def EQOP(self):
            return self.getToken(MCParser.EQOP, 0)

        def NEQOP(self):
            return self.getToken(MCParser.NEQOP, 0)

        def ANDOP(self):
            return self.getToken(MCParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MCParser.OROP, 0)

        def ASSOP(self):
            return self.getToken(MCParser.ASSOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_boolExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.BoolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_boolExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.NOTOP:
                self.state = 284
                self.match(MCParser.NOTOP)


            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.IDENTIFIER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 304
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 289
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 290
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 291
                        self.boolExpr(7)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 292
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 293
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 294
                        self.boolExpr(6)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 295
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 296
                        self.match(MCParser.ANDOP)
                        self.state = 297
                        self.boolExpr(4)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 298
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 299
                        self.match(MCParser.OROP)
                        self.state = 300
                        self.boolExpr(3)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 301
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 302
                        self.match(MCParser.ASSOP)
                        self.state = 303
                        self.boolExpr(3)
                        pass

             
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.floatExpr_sempred
        self._predicates[29] = self.intExpr_sempred
        self._predicates[30] = self.boolExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def floatExpr_sempred(self, localctx:FloatExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

    def intExpr_sempred(self, localctx:IntExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

    def boolExpr_sempred(self, localctx:BoolExprContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         




