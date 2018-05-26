import ply.lex as lex
import ply.yacc as yacc
import sys
from Debug import Debug

INIT_VALUE = 0
REGISTER_SIZE = 64
DEBUG = False
FILE_URL = 'programs/test.repeat'

# register initialization 
register = []
for i in range(REGISTER_SIZE):
    register.append(INIT_VALUE)

# =======================
#    LEX tokenization
# =======================

# tokens
tokens = ('REG', 'INC', 'MOVE', 'REPEAT', 'DEF', 'INT', 'END', 'ID')

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

def t_REG(t):
    r'r\d+'
    t.value = {'type' : 'reg', 'val' : int(t.value[1:])}
    return t

def t_INC(t):
    r'inc'
    return t

def t_END(t):
    r'end'
    return t

def t_EF(t):
    r'DEFINE-MACRO'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_INT(t):
    r'\d+'
    t.value = {'type' : 'num', 'val' : int(t.value)}    
    return t

t_MOVE = r'<-'
t_ID = r'[_a-zA-Z][_a-zA-Z0-9]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# =================
#    YACC parse
# =================

def p_prog(p):
    '''prog : instr 
            | instr prog'''
    if len(p) == 3:
        p[0] = ('exp', p[1], p[2]) 
    else:
        p[0] = ('exp', p[1])

def p_instr(p):
    '''instr : cmd 
             | macdef'''
    p[0] = p[1]

def p_cmd(p):
    '''cmd : incr 
           | mv 
           | rpt 
           | mac'''
    p[0] = p[1]

def p_incr(p):
    '''incr : INC REG'''
    p[0] = (p[1], p[2])

def p_mv(p):
    '''mv : REG MOVE REG 
          | REG MOVE INT'''
    p[0] = (p[2], p[1], p[3])

# repeat the BODY for mem[REG[]] amount of time 
def p_rpt(p):
    '''rpt : REPEAT REG body'''
    p[0] = ('repeat', p[2], p[3])

def p_body(p):
    '''body : innerbody END'''
    p[0] =('body', p[1], p[2])

def p_innerbody(p):
    '''innerbody : cmd 
                 | cmd innerbody'''
    if len(p) == 2:
        p[0] = (p[1], 'nil')
    elif len(p) == 3: 
        p[0] = (p[1], p[2])



# should it be replaced by a first pass of the file where macros are replaced ?
def p_mac(p):
    '''mac : REG MOVE ID reglist'''
    p[0] = ('replace', p[1], p[3], p[4])
    # p3 should be the macdef with good 

def p_macdef(p):
    '''macdef : DEF ID reglist body'''
    p[0] = ("def", p[2], p[3], p[4])

def p_reglist(p):
    '''reglist : REG 
               | REG reglist'''
    if len(p) == 1:
        p[0] = p[1]
    else: 
        p[0] = ('list', p[1], p[2])


# ======================
#    AST evaluation
# ======================

# The syntax tree is represented as a list of expression where 
# the left branch is the expression to evaluate and the right brand 
# is the next expression to evaluate. The function takes a regular Pyhton
# tuples which is how the interpreter represent the AST with the first element
# being an identifier for the node type, and all other elements are the
# children of that node.


# specific actions fonctions

def eval_exp(exp):
    """     
    exp[0] = first expression to evaluate
    exp[1] = rest of the tree, may be there or not (absent at the end of the Tree)
    """    
    if DEBUG:
        print('EVAL_EXP')
    if len(exp) == 2: # deux expression à évaluer
        eval(exp[0])
        eval(exp[1])
    elif len(exp) == 1: # une seule expression à évaluer
        eval(exp[0])
    else:
        print('ERROR : malformed expression')


def eval_inc(exp):
    """     
    # exp[0] = register to increment
    """    
    if DEBUG:
        print('EVAL_INC : ' + str(exp))
        print("before : r" + str(exp[0]['val']) + ' = ' + str(register[exp[0]['val']]))
    register[exp[0]['val']] = register[exp[0]['val']] + 1
    if DEBUG:
        print("after  : r" + str(exp[0]['val']) + ' = ' + str(register[exp[0]['val']]))



def eval_move(exp):
    """     
    exp[0] = register to move value to
    exp[1] = maybe a register to move value from or an Int 
    """    
    if DEBUG:
        print('EVAL_MOVE : ' + str(exp[0]) + " <- " + str(exp[1]))
    # moving register value
    if exp[1]['type'] == 'reg':
        register[exp[0]['val']] = register[exp[1]['val']]
    # sugar : putting int inside register
    if exp[1]['type'] == 'num':
        register[exp[0]['val']] = [exp[1]['val']][0]    

def eval_body(body):
    """ 
    body[0] = (exp1, ((exp2, ((exp3, (( expN, "nil" )))))))
    """
    if DEBUG:
        print('EVAL_BODY : ' + str(body))
    if body[1] == 'nil':
        eval(body[0])
    else:
        eval(body[0])
        eval_body(body[1])

def eval_repeat(exp):
    """ 
    exp[0] = register to use
    exp[1] = body
    """
    if DEBUG:
        print('EVAL_REPEAT : ' + str(register[exp[0]["val"]]))
    for n in range(register[exp[0]["val"]]):
        eval_body(exp[1][1])



# main eval function
def eval(exp):
    
    # expressions
    if exp[0] == 'exp':
        eval_exp(exp[1:])
    
    # increments
    if exp[0] == 'inc':
        eval_inc(exp[1:])

    # move
    if exp[0] == '<-':
        eval_move(exp[1:])

    # repeat
    if exp[0] == 'repeat':
        eval_repeat(exp[1:])

    if exp[0] == 'body':
        eval_body(exp[1])

    if exp[0] == 'end' or exp[0] == 'nil':
        pass

    
    
# file handling
testFile = open(FILE_URL, mode="r")
testData = ""
for line in testFile:
    testData += line

# Give the lexer some input
lexer.input(testData)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

parser = yacc.yacc()

abstract_syntax_tree = parser.parse(testData)

eval(abstract_syntax_tree)
logger = Debug(True)
line ="=========================="
if logger.debug:
    print('\n' + line + '\n     register content\n' + line )
    print(register)
    print('\n' + line + '\n        Parsed tree\n' + line)
    print(abstract_syntax_tree)


