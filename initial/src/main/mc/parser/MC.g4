// Name: Nguyen Thanh Hoang - ID: 1870172

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}

/***************************************/
/************ Parser *******************/
/***************************************/
program:        declInProgram+ EOF;
declInProgram:  varDeclare | funcDeclare;

// Variable declearation
varDeclare:     varType manyVar SM;
varType:        BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
manyVar:        var (CM var)* ;
var:            IDENTIFIER (LQB INTLIT RQB)? ;

// Function declearation
funcDeclare:    returnType IDENTIFIER LB paramList? RB blockStatement;
returnType:     (BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE | VOIDTYPE) (LQB RQB)?;
paramList:      paramDeclare (CM paramDeclare)*;
paramDeclare:   varType paramName;
paramName:      IDENTIFIER (LQB RQB)?;
blockStatement: LP contentBlockStatement? RP;
contentBlockStatement: declInFunc+;
declInFunc:     varDeclare | statement;

statement:      assignStatement
              | ifStatement
              | doWhileStatement
              | forStatement
              | blockStatement
              | callStatement
              | returnFunc
              | varDeclare
              ;

assignStatement: (IDENTIFIER ASSOP) expr SM;
callStatement:   IDENTIFIER LB listExpr? RB SM;
listExpr:        expr (CM expr)*;
returnFunc:      KEYWORD_RETURN  (expr)? SM;

// If statement
ifStatement:    KEYWORD_IF (LB boolExpr RB) statement (KEYWORD_ELSE statement)?;

// do-while statement
doWhileStatement: KEYWORD_DO blockStatement KEYWORD_WHILE (LB boolExpr RB) SM;

// for statement
forStatement:   KEYWORD_FOR (LB expr? SM boolExpr? SM expr? RB) statement;

// break statement
breakStatement: KEYWORD_BREAK SM;

// continue statement:
continueStatement: KEYWORD_CONTINUE SM;

expr:        intExpr
           | boolExpr
           | stringExpr
           | indexExpr
           | floatExpr
           ;

floatExpr:              LB floatExpr RB
           | <assoc=right> floatExpr ( DIVOP | MULOP | MODOP ) floatExpr
           | <assoc=right> floatExpr ( ADDOP | SUBOP ) floatExpr
           |               floatExpr ( LTHOP | LEQOP | GTHOP | GTHOP ) floatExpr
           |               floatExpr ( EQOP  | NEQOP ) floatExpr
           | <assoc=right> floatExpr ( ANDOP ) floatExpr
           | <assoc=right> floatExpr ( OROP  ) floatExpr
           | <assoc=left>  floatExpr ( ASSOP ) floatExpr
           | FLOATLIT
           | IDENTIFIER
           | intExpr
           ;

intExpr:                LB intExpr RB
           | <assoc=right> intExpr ( DIVOP | MULOP | MODOP ) intExpr
           | <assoc=right> intExpr ( ADDOP | SUBOP ) intExpr
           |               intExpr ( LTHOP | LEQOP | GTHOP | GTHOP ) intExpr
           |               intExpr ( EQOP  | NEQOP ) intExpr
           | <assoc=right> intExpr ( ANDOP ) intExpr
           | <assoc=right> intExpr ( OROP  ) intExpr
           | <assoc=left>  intExpr ( ASSOP ) intExpr
           | INTLIT
           | IDENTIFIER
           ;

boolExpr:               LB boolExpr RB
           | <assoc=left>           ( NOTOP ) boolExpr
           |               boolExpr ( LTHOP | LEQOP | GTHOP | GEQOP ) boolExpr
           |               boolExpr ( EQOP  | NEQOP ) boolExpr
           | <assoc=right> boolExpr ( ANDOP ) boolExpr
           | <assoc=right> boolExpr ( OROP  ) boolExpr
           | <assoc=left>  boolExpr ( ASSOP ) boolExpr
           | BOOLLIT
           | IDENTIFIER
           | intExpr
           ;

stringExpr:   IDENTIFIER ( ASSOP ) STRLIT;
indexExpr :   IDENTIFIER LQB intExpr RQB
            | intExpr
            ;

/***************************************/
/************ Lexer  *******************/
/***************************************/
// Define comment
LINE_COMMENT:  '//' ~[\r\n]* -> skip ; // Skip line comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip ; // Skip block comment fragment

// Define keywords
// KEYWORD_BOOL:     'boolean'   ;
KEYWORD_BREAK:    'break'      ;
KEYWORD_CONTINUE: 'continue'   ;
KEYWORD_ELSE:     'else'       ;
KEYWORD_FOR:      'for'        ;
KEYWORD_IF:       'if'         ;
KEYWORD_RETURN:   'return'     ;
KEYWORD_DO:       'do'         ;
KEYWORD_WHILE:    'while'      ;

// Int Literals
INTLIT: [0-9]+  ;

// Float Literals
fragment DOT:            '.'   ;
fragment DIGIT_NONZERO:  [1-9] ;
fragment EXPONENT:       (DIGIT+)([eE])('-'?)(DIGIT+); // Consider case: 0E0
FLOATLIT:                (DIGIT+)*(DOT)(DIGIT+|EXPONENT)
                       | (DIGIT+) (DOT)
                       | (EXPONENT)
                       ;

// Boolean Literals
BOOLLIT: 'true' | 'false';

// String Literals
STRLIT:  '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* '"' ;

// Define datatype
BOOLTYPE:   'boolean' ;
INTTYPE:    'int'     ;
FLOATTYPE:  'float'   ;
STRINGTYPE: 'string'  ;
VOIDTYPE:   'void'    ;

// Define operators
ADDOP:   '+'    ;
SUBOP:   '-'    ;
MULOP:   '*'    ;
DIVOP:   '/'    ;
MODOP:   '%'    ;
NOTOP:   '!'    ;
OROP :   '||'   ;
ANDOP:   '&&'   ;
NEQOP:   '!='   ;
EQOP:    '=='   ;
LTHOP:   '<'    ;
GTHOP:   '>'    ;
LEQOP:   '<='   ;
GEQOP:   '>='   ;
ASSOP:   '='    ;

// Define separators
LB:      '('    ;
RB:      ')'    ;
LQB:     '['    ;
RQB:     ']'    ;
LP:      '{'    ;
RP:      '}'    ;
SM:      ';'    ;
CM:      ','    ;

// Define IDENTIFIER
fragment DIGIT:       [0-9]      ;
fragment LETTER:      [a-zA-Z]   ;
fragment UNDERSCORE:  [_]        ;
IDENTIFIER:           (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*; // Please consider case: ___ -> indentifier???

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* ;
ILLEGAL_ESCAPE
    : '"' ('\\' [bfrnt'"\\] | ~["\\])*? ([\\] ~[bfrnt'"\\])
        {

             raise IllegalEscape(self.text[1:])
        }
        //(ESC | ~[\r\n] )*  '"'
    ;
ERROR_CHAR: .;
