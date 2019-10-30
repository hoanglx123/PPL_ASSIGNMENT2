# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u013a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\3\2\3\3\3\3\6\3F\n\3\r\3\16\3")
        buf.write("G\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6S\n\6\f\6\16")
        buf.write("\6V\13\6\3\7\3\7\3\7\3\7\5\7\\\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\5\th\n\t\3\n\3\n\3\n\5\nm\n\n\3\13")
        buf.write("\3\13\3\13\7\13r\n\13\f\13\16\13u\13\13\3\f\3\f\3\f\5")
        buf.write("\fz\n\f\3\r\3\r\5\r~\n\r\3\r\3\r\3\16\3\16\5\16\u0084")
        buf.write("\n\16\3\16\3\16\7\16\u0088\n\16\f\16\16\16\u008b\13\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0094\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u009e\n\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\7\22\u00a6\n\22\f\22\16")
        buf.write("\22\u00a9\13\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00b4\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\5\27\u00c3\n\27\3\27")
        buf.write("\3\27\5\27\u00c7\n\27\3\27\3\27\5\27\u00cb\n\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\5\35\u00df\n\35\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u00e5\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\7\36\u00fc\n\36\f\36\16\36\u00ff")
        buf.write("\13\36\3\37\3\37\3\37\5\37\u0104\n\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u011b\n\37\f")
        buf.write("\37\16\37\u011e\13\37\3 \3 \5 \u0122\n \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0135\n \f \16")
        buf.write(" \u0138\13 \3 \2\5:<>!\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>\2\t\3\2\21\24\3\2\21\25")
        buf.write("\3\2\30\32\3\2\26\27\3\2 \"\3\2\36\37\5\2\r\r\17\17--")
        buf.write("\2\u014b\2@\3\2\2\2\4E\3\2\2\2\6I\3\2\2\2\bM\3\2\2\2\n")
        buf.write("O\3\2\2\2\fW\3\2\2\2\16]\3\2\2\2\20d\3\2\2\2\22l\3\2\2")
        buf.write("\2\24n\3\2\2\2\26v\3\2\2\2\30{\3\2\2\2\32\u0083\3\2\2")
        buf.write("\2\34\u0093\3\2\2\2\36\u0095\3\2\2\2 \u009a\3\2\2\2\"")
        buf.write("\u00a2\3\2\2\2$\u00aa\3\2\2\2&\u00ae\3\2\2\2(\u00b5\3")
        buf.write("\2\2\2*\u00b9\3\2\2\2,\u00bf\3\2\2\2.\u00cf\3\2\2\2\60")
        buf.write("\u00d1\3\2\2\2\62\u00d3\3\2\2\2\64\u00d5\3\2\2\2\66\u00d8")
        buf.write("\3\2\2\28\u00de\3\2\2\2:\u00e4\3\2\2\2<\u0103\3\2\2\2")
        buf.write(">\u011f\3\2\2\2@A\5\4\3\2AB\7\2\2\3B\3\3\2\2\2CF\5\6\4")
        buf.write("\2DF\5\16\b\2EC\3\2\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2")
        buf.write("GH\3\2\2\2H\5\3\2\2\2IJ\5\b\5\2JK\5\n\6\2KL\7+\2\2L\7")
        buf.write("\3\2\2\2MN\t\2\2\2N\t\3\2\2\2OT\5\f\7\2PQ\7,\2\2QS\5\f")
        buf.write("\7\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\13\3\2\2")
        buf.write("\2VT\3\2\2\2W[\7-\2\2XY\7\'\2\2YZ\7\r\2\2Z\\\7(\2\2[X")
        buf.write("\3\2\2\2[\\\3\2\2\2\\\r\3\2\2\2]^\5\20\t\2^_\7-\2\2_`")
        buf.write("\7%\2\2`a\5\22\n\2ab\7&\2\2bc\5\30\r\2c\17\3\2\2\2dg\t")
        buf.write("\3\2\2ef\7\'\2\2fh\7(\2\2ge\3\2\2\2gh\3\2\2\2h\21\3\2")
        buf.write("\2\2ij\5\b\5\2jk\5\24\13\2km\3\2\2\2li\3\2\2\2lm\3\2\2")
        buf.write("\2m\23\3\2\2\2ns\5\26\f\2op\7,\2\2pr\5\26\f\2qo\3\2\2")
        buf.write("\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\25\3\2\2\2us\3\2\2\2")
        buf.write("vy\7-\2\2wx\7\'\2\2xz\7(\2\2yw\3\2\2\2yz\3\2\2\2z\27\3")
        buf.write("\2\2\2{}\7)\2\2|~\5\32\16\2}|\3\2\2\2}~\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0080\7*\2\2\u0080\31\3\2\2\2\u0081\u0084\5")
        buf.write("\6\4\2\u0082\u0084\5\34\17\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0084\u0089\3\2\2\2\u0085\u0088\5\6\4\2")
        buf.write("\u0086\u0088\5\34\17\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\33\3\2\2\2\u008b\u0089\3\2\2\2\u008c")
        buf.write("\u0094\5\36\20\2\u008d\u0094\5&\24\2\u008e\u0094\5*\26")
        buf.write("\2\u008f\u0094\5,\27\2\u0090\u0094\5\30\r\2\u0091\u0094")
        buf.write("\5 \21\2\u0092\u0094\5$\23\2\u0093\u008c\3\2\2\2\u0093")
        buf.write("\u008d\3\2\2\2\u0093\u008e\3\2\2\2\u0093\u008f\3\2\2\2")
        buf.write("\u0093\u0090\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3")
        buf.write("\2\2\2\u0094\35\3\2\2\2\u0095\u0096\7-\2\2\u0096\u0097")
        buf.write("\7$\2\2\u0097\u0098\58\35\2\u0098\u0099\7+\2\2\u0099\37")
        buf.write("\3\2\2\2\u009a\u009b\7-\2\2\u009b\u009d\7%\2\2\u009c\u009e")
        buf.write("\5\"\22\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\7&\2\2\u00a0\u00a1\7+\2\2\u00a1")
        buf.write("!\3\2\2\2\u00a2\u00a7\58\35\2\u00a3\u00a4\7,\2\2\u00a4")
        buf.write("\u00a6\58\35\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8#\3\2\2")
        buf.write("\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7\n\2\2\u00ab\u00ac")
        buf.write("\58\35\2\u00ac\u00ad\7+\2\2\u00ad%\3\2\2\2\u00ae\u00af")
        buf.write("\7\t\2\2\u00af\u00b0\5(\25\2\u00b0\u00b3\5\30\r\2\u00b1")
        buf.write("\u00b2\7\7\2\2\u00b2\u00b4\5\30\r\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b4\3\2\2\2\u00b4\'\3\2\2\2\u00b5\u00b6\7%")
        buf.write("\2\2\u00b6\u00b7\5> \2\u00b7\u00b8\7&\2\2\u00b8)\3\2\2")
        buf.write("\2\u00b9\u00ba\7\13\2\2\u00ba\u00bb\5\30\r\2\u00bb\u00bc")
        buf.write("\7\f\2\2\u00bc\u00bd\5(\25\2\u00bd\u00be\7+\2\2\u00be")
        buf.write("+\3\2\2\2\u00bf\u00c0\7\b\2\2\u00c0\u00c2\7%\2\2\u00c1")
        buf.write("\u00c3\5.\30\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c6\7+\2\2\u00c5\u00c7\5")
        buf.write("\60\31\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8\u00ca\7+\2\2\u00c9\u00cb\5\62\32")
        buf.write("\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00cd\7&\2\2\u00cd\u00ce\5\30\r\2\u00ce")
        buf.write("-\3\2\2\2\u00cf\u00d0\58\35\2\u00d0/\3\2\2\2\u00d1\u00d2")
        buf.write("\5> \2\u00d2\61\3\2\2\2\u00d3\u00d4\58\35\2\u00d4\63\3")
        buf.write("\2\2\2\u00d5\u00d6\7\5\2\2\u00d6\u00d7\7+\2\2\u00d7\65")
        buf.write("\3\2\2\2\u00d8\u00d9\7\6\2\2\u00d9\u00da\7+\2\2\u00da")
        buf.write("\67\3\2\2\2\u00db\u00df\5:\36\2\u00dc\u00df\5<\37\2\u00dd")
        buf.write("\u00df\5> \2\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df9\3\2\2\2\u00e0\u00e1\b\36\1\2\u00e1")
        buf.write("\u00e5\7\16\2\2\u00e2\u00e5\5> \2\u00e3\u00e5\5<\37\2")
        buf.write("\u00e4\u00e0\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3")
        buf.write("\2\2\2\u00e5\u00fd\3\2\2\2\u00e6\u00e7\f\f\2\2\u00e7\u00e8")
        buf.write("\t\4\2\2\u00e8\u00fc\5:\36\f\u00e9\u00ea\f\13\2\2\u00ea")
        buf.write("\u00eb\t\5\2\2\u00eb\u00fc\5:\36\13\u00ec\u00ed\f\n\2")
        buf.write("\2\u00ed\u00ee\t\6\2\2\u00ee\u00fc\5:\36\13\u00ef\u00f0")
        buf.write("\f\t\2\2\u00f0\u00f1\t\7\2\2\u00f1\u00fc\5:\36\n\u00f2")
        buf.write("\u00f3\f\b\2\2\u00f3\u00f4\7\35\2\2\u00f4\u00fc\5:\36")
        buf.write("\b\u00f5\u00f6\f\7\2\2\u00f6\u00f7\7\34\2\2\u00f7\u00fc")
        buf.write("\5:\36\7\u00f8\u00f9\f\6\2\2\u00f9\u00fa\7$\2\2\u00fa")
        buf.write("\u00fc\5:\36\7\u00fb\u00e6\3\2\2\2\u00fb\u00e9\3\2\2\2")
        buf.write("\u00fb\u00ec\3\2\2\2\u00fb\u00ef\3\2\2\2\u00fb\u00f2\3")
        buf.write("\2\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fc\u00ff")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write(";\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\b\37\1\2\u0101")
        buf.write("\u0104\7\r\2\2\u0102\u0104\5> \2\u0103\u0100\3\2\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u011c\3\2\2\2\u0105\u0106\f\13\2")
        buf.write("\2\u0106\u0107\t\4\2\2\u0107\u011b\5<\37\13\u0108\u0109")
        buf.write("\f\n\2\2\u0109\u010a\t\5\2\2\u010a\u011b\5<\37\n\u010b")
        buf.write("\u010c\f\t\2\2\u010c\u010d\t\6\2\2\u010d\u011b\5<\37\n")
        buf.write("\u010e\u010f\f\b\2\2\u010f\u0110\t\7\2\2\u0110\u011b\5")
        buf.write("<\37\t\u0111\u0112\f\7\2\2\u0112\u0113\7\35\2\2\u0113")
        buf.write("\u011b\5<\37\7\u0114\u0115\f\6\2\2\u0115\u0116\7\34\2")
        buf.write("\2\u0116\u011b\5<\37\6\u0117\u0118\f\5\2\2\u0118\u0119")
        buf.write("\7$\2\2\u0119\u011b\5<\37\6\u011a\u0105\3\2\2\2\u011a")
        buf.write("\u0108\3\2\2\2\u011a\u010b\3\2\2\2\u011a\u010e\3\2\2\2")
        buf.write("\u011a\u0111\3\2\2\2\u011a\u0114\3\2\2\2\u011a\u0117\3")
        buf.write("\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d=\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0121")
        buf.write("\b \1\2\u0120\u0122\7\33\2\2\u0121\u0120\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\t\b\2\2")
        buf.write("\u0124\u0136\3\2\2\2\u0125\u0126\f\b\2\2\u0126\u0127\t")
        buf.write("\6\2\2\u0127\u0135\5> \t\u0128\u0129\f\7\2\2\u0129\u012a")
        buf.write("\t\7\2\2\u012a\u0135\5> \b\u012b\u012c\f\6\2\2\u012c\u012d")
        buf.write("\7\35\2\2\u012d\u0135\5> \6\u012e\u012f\f\5\2\2\u012f")
        buf.write("\u0130\7\34\2\2\u0130\u0135\5> \5\u0131\u0132\f\4\2\2")
        buf.write("\u0132\u0133\7$\2\2\u0133\u0135\5> \5\u0134\u0125\3\2")
        buf.write("\2\2\u0134\u0128\3\2\2\2\u0134\u012b\3\2\2\2\u0134\u012e")
        buf.write("\3\2\2\2\u0134\u0131\3\2\2\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137?\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\37EGT[glsy}\u0083\u0087\u0089\u0093\u009d")
        buf.write("\u00a7\u00b3\u00c2\u00c6\u00ca\u00de\u00e4\u00fb\u00fd")
        buf.write("\u0103\u011a\u011c\u0121\u0134\u0136")
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
    RULE_manyDecls = 1
    RULE_varDeclare = 2
    RULE_varType = 3
    RULE_manyVar = 4
    RULE_var = 5
    RULE_funcDeclare = 6
    RULE_returnType = 7
    RULE_paramDeclare = 8
    RULE_manyParam = 9
    RULE_param = 10
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

    ruleNames =  [ "program", "manyDecls", "varDeclare", "varType", "manyVar", 
                   "var", "funcDeclare", "returnType", "paramDeclare", "manyParam", 
                   "param", "blockStatement", "contentBlockStatement", "statement", 
                   "assignment", "callStatement", "listExpr", "returnFunc", 
                   "if_statement", "condBlock", "do_while_statement", "for_statement", 
                   "forExpr1", "forExpr2", "forExpr3", "break_statement", 
                   "continue_statement", "expr", "floatExpr", "intExpr", 
                   "boolExpr" ]

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

        def manyDecls(self):
            return self.getTypedRuleContext(MCParser.ManyDeclsContext,0)


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
            self.manyDecls()
            self.state = 63
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyDeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarDeclareContext)
            else:
                return self.getTypedRuleContext(MCParser.VarDeclareContext,i)


        def funcDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.FuncDeclareContext)
            else:
                return self.getTypedRuleContext(MCParser.FuncDeclareContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_manyDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyDecls" ):
                return visitor.visitManyDecls(self)
            else:
                return visitor.visitChildren(self)




    def manyDecls(self):

        localctx = MCParser.ManyDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manyDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 65
                    self.varDeclare()
                    pass

                elif la_ == 2:
                    self.state = 66
                    self.funcDeclare()
                    pass


                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

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
            self.state = 71
            self.varType()
            self.state = 72
            self.manyVar()
            self.state = 73
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
            self.state = 75
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
            self.state = 77
            self.var()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 78
                self.match(MCParser.CM)
                self.state = 79
                self.var()
                self.state = 84
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
            self.state = 85
            self.match(MCParser.IDENTIFIER)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LQB:
                self.state = 86
                self.match(MCParser.LQB)
                self.state = 87
                self.match(MCParser.INTLIT)
                self.state = 88
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

        def paramDeclare(self):
            return self.getTypedRuleContext(MCParser.ParamDeclareContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(MCParser.BlockStatementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.returnType()
            self.state = 92
            self.match(MCParser.IDENTIFIER)
            self.state = 93
            self.match(MCParser.LB)
            self.state = 94
            self.paramDeclare()
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


    class ParamDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(MCParser.VarTypeContext,0)


        def manyParam(self):
            return self.getTypedRuleContext(MCParser.ManyParamContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paramDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclare" ):
                return visitor.visitParamDeclare(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclare(self):

        localctx = MCParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 103
                self.varType()
                self.state = 104
                self.manyParam()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParamContext)
            else:
                return self.getTypedRuleContext(MCParser.ParamContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_manyParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyParam" ):
                return visitor.visitManyParam(self)
            else:
                return visitor.visitChildren(self)




    def manyParam(self):

        localctx = MCParser.ManyParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_manyParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.param()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 109
                self.match(MCParser.CM)
                self.state = 110
                self.param()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

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
            return MCParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MCParser.IDENTIFIER)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LQB:
                self.state = 117
                self.match(MCParser.LQB)
                self.state = 118
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
            self.state = 121
            self.match(MCParser.LP)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.KEYWORD_FOR) | (1 << MCParser.KEYWORD_IF) | (1 << MCParser.KEYWORD_RETURN) | (1 << MCParser.KEYWORD_DO) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.LP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 122
                self.contentBlockStatement()


            self.state = 125
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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                self.state = 127
                self.varDeclare()
                pass
            elif token in [MCParser.KEYWORD_FOR, MCParser.KEYWORD_IF, MCParser.KEYWORD_RETURN, MCParser.KEYWORD_DO, MCParser.LP, MCParser.IDENTIFIER]:
                self.state = 128
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.KEYWORD_FOR) | (1 << MCParser.KEYWORD_IF) | (1 << MCParser.KEYWORD_RETURN) | (1 << MCParser.KEYWORD_DO) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.LP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 133
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                    self.state = 131
                    self.varDeclare()
                    pass
                elif token in [MCParser.KEYWORD_FOR, MCParser.KEYWORD_IF, MCParser.KEYWORD_RETURN, MCParser.KEYWORD_DO, MCParser.LP, MCParser.IDENTIFIER]:
                    self.state = 132
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 137
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.do_while_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.blockStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.callStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
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
            self.state = 147
            self.match(MCParser.IDENTIFIER)
            self.state = 148
            self.match(MCParser.ASSOP)
            self.state = 149
            self.expr()
            self.state = 150
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
            self.state = 152
            self.match(MCParser.IDENTIFIER)
            self.state = 153
            self.match(MCParser.LB)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 154
                self.listExpr()


            self.state = 157
            self.match(MCParser.RB)
            self.state = 158
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
            self.state = 160
            self.expr()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 161
                self.match(MCParser.CM)
                self.state = 162
                self.expr()
                self.state = 167
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
            self.state = 168
            self.match(MCParser.KEYWORD_RETURN)
            self.state = 169
            self.expr()
            self.state = 170
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
            self.state = 172
            self.match(MCParser.KEYWORD_IF)
            self.state = 173
            self.condBlock()
            self.state = 174
            self.blockStatement()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.KEYWORD_ELSE:
                self.state = 175
                self.match(MCParser.KEYWORD_ELSE)
                self.state = 176
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
            self.state = 179
            self.match(MCParser.LB)
            self.state = 180
            self.boolExpr(0)
            self.state = 181
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
            self.state = 183
            self.match(MCParser.KEYWORD_DO)
            self.state = 184
            self.blockStatement()
            self.state = 185
            self.match(MCParser.KEYWORD_WHILE)
            self.state = 186
            self.condBlock()
            self.state = 187
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
            self.state = 189
            self.match(MCParser.KEYWORD_FOR)
            self.state = 190
            self.match(MCParser.LB)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 191
                self.forExpr1()


            self.state = 194
            self.match(MCParser.SM)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 195
                self.forExpr2()


            self.state = 198
            self.match(MCParser.SM)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.NOTOP) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 199
                self.forExpr3()


            self.state = 202
            self.match(MCParser.RB)
            self.state = 203
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
            self.state = 205
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
            self.state = 207
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
            self.state = 209
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
            self.state = 211
            self.match(MCParser.KEYWORD_BREAK)
            self.state = 212
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
            self.state = 214
            self.match(MCParser.KEYWORD_CONTINUE)
            self.state = 215
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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.floatExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.intExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 2:
                self.state = 224
                self.boolExpr(0)
                pass

            elif la_ == 3:
                self.state = 225
                self.intExpr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 249
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 228
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 229
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.floatExpr(10)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 231
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 232
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.floatExpr(9)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 234
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 235
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 236
                        self.floatExpr(9)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 237
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 238
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 239
                        self.floatExpr(8)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 240
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 241
                        self.match(MCParser.ANDOP)
                        self.state = 242
                        self.floatExpr(6)
                        pass

                    elif la_ == 6:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 243
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 244
                        self.match(MCParser.OROP)
                        self.state = 245
                        self.floatExpr(5)
                        pass

                    elif la_ == 7:
                        localctx = MCParser.FloatExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExpr)
                        self.state = 246
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 247
                        self.match(MCParser.ASSOP)
                        self.state = 248
                        self.floatExpr(5)
                        pass

             
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 255
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.state = 256
                self.boolExpr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 280
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 259
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 260
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 261
                        self.intExpr(9)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 262
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 263
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.intExpr(8)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 265
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 266
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 267
                        self.intExpr(8)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 268
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 269
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 270
                        self.intExpr(7)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 271
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 272
                        self.match(MCParser.ANDOP)
                        self.state = 273
                        self.intExpr(5)
                        pass

                    elif la_ == 6:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 274
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 275
                        self.match(MCParser.OROP)
                        self.state = 276
                        self.intExpr(4)
                        pass

                    elif la_ == 7:
                        localctx = MCParser.IntExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExpr)
                        self.state = 277
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 278
                        self.match(MCParser.ASSOP)
                        self.state = 279
                        self.intExpr(4)
                        pass

             
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.NOTOP:
                self.state = 286
                self.match(MCParser.NOTOP)


            self.state = 289
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.IDENTIFIER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 306
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 291
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 292
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LTHOP) | (1 << MCParser.GTHOP) | (1 << MCParser.LEQOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 293
                        self.boolExpr(7)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 294
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 295
                        _la = self._input.LA(1)
                        if not(_la==MCParser.NEQOP or _la==MCParser.EQOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 296
                        self.boolExpr(6)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 297
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 298
                        self.match(MCParser.ANDOP)
                        self.state = 299
                        self.boolExpr(4)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 300
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 301
                        self.match(MCParser.OROP)
                        self.state = 302
                        self.boolExpr(3)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 303
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 304
                        self.match(MCParser.ASSOP)
                        self.state = 305
                        self.boolExpr(3)
                        pass

             
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
         




