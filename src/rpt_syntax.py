# lib import
import ply.lex as lex
import ply.yacc as yacc
import sys
import copy

# project's classes
from Debug import Debug
from Macro import Macro
from Program import Program

# general parameters
INIT_VALUE = 0
REGISTER_SIZE = 64
TEST = 'programs/test.repeat'
TIMES = 'programs/times.repeat'
MACROS_TEST = 'programs/macros.repeat' 
CURRENT_TEST = TEST
line ="=========================="

logger = Debug(True)

# register and macro initialization 
register = []
for i in range(REGISTER_SIZE):
    register.append(INIT_VALUE)

macros= {}

# =======================
#    LEX tokenization
# =======================

# This is where the langage syntax is defined.

# tokens
tokens = ('REG', 'INC', 'MOVE', 'REPEAT', 'DEF', 'INT', 'END', 'ID', 'RP', 'LP')

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

def t_DEF(t):
    r'MACRO'
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
t_LP = r'\('
t_RP = r'\)'

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

# Build the lexerpip3 install PyLint
lexer = lex.lex()


# =================
#    YACC parse
# =================

def p_prog(p):
    '''prog : instr 
            | instr prog'''
    if len(p) == 3:
        p[0] = [ 'exp', p[1], p[2] ]
    else:
        p[0] = [ 'exp', p[1] ]

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
    p[0] = [ p[1], p[2] ]

def p_mv(p):
    '''mv : REG MOVE REG 
          | REG MOVE INT'''
    p[0] = [ p[2], p[1], p[3] ]

def p_rpt(p):
    '''rpt : REPEAT REG body'''
    p[0] = [ 'repeat', p[2], p[3] ]

def p_body(p):
    '''body : innerbody END'''
    p[0] =[ 'body', p[1], p[2] ]

def p_innerbody(p):
    '''innerbody : cmd 
                 | cmd innerbody'''
    if len(p) == 2:
        p[0] = [ p[1], 'nil' ]
    elif len(p) == 3: 
        p[0] = [ p[1], p[2] ]

# macros definitions are at first placed within the tree
def p_mac(p):
    '''mac : REG MOVE ID reglist'''
    p[0] = [ 'macro', p[1], p[3], p[4] ]
    # p3 should be the macdef with good 

def p_macdef(p):
    '''macdef : DEF ID reglist body'''
    p[0] = [ "def", p[2], p[3], p[4] ]

def p_innerreglist(p):
    '''innerreglist : REG 
                    | REG innerreglist'''
    if len(p) == 2:
        p[0] = [ p[1], 'nil']
    elif len(p) == 3: 
        p[0] = [ p[1], p[2] ]
   
def p_reglist(p):
    '''reglist : LP innerreglist RP '''
    p[0] = p[2]

# ========================
#    MACRO replacement
# ========================

# A first pass thru the AST where macro expressions branches are
# replaced by their corresping macro definition tree. This is done
# in two time : First we traverse the tree to find all macro definition
# and add them to the python "macros" dict. Then, we traverse the Tree again 
# to replace each branch that is a macro call by the right macro definition Tree.

def find_macro_def(exp):
    
    if exp[0] == 'exp':
        if len(exp) == 3: # continue on exp1 and exp2
            find_macro_def(exp[1])
            find_macro_def(exp[2])
        elif len(exp) == 2: # continue on exp1 only
            find_macro_def(exp[1])

    elif exp[0] == 'def':
        '''
        exp[1] = ID
        exp[2] = reglist
        exp[3] = body
        '''
        m = Macro(exp[1], exp[2], exp[3])
        macros[exp[1]] = m

def macro_expand(tree, parent):

    #print(tree)

    if tree == 'end' or tree == 'nil' or tree == 'def' or tree == '<-' or tree == 'inc':
        pass
    elif tree[0] == 'end' or tree[0] == 'nil' or tree[0] == 'def' or tree[0] == '<-' or tree[0] == 'inc':
        pass
    elif tree[0] == 'exp':
        if len(tree) == 3: # continue on exp1 and exp2
            macro_expand(tree[1], tree)
            macro_expand(tree[2], tree)
        elif len(tree) == 2: # continue on exp1 only
            macro_expand(tree[1], tree)
    elif tree[0] == 'repeat':
        macro_expand(tree[2], tree)
    elif tree[0] =='body':
        #print('body : ',tree[1])
        macro_expand(tree[1], tree)
    elif tree[0] == 'macro':
        '''
        tree[1] = return register
        tree[2] = macro id
        tree[3] = reg list
        '''
        # find corresping macro def body within macros map
        ident = macros[tree[2]].ID
        for k,v in macros.items():
            if k == ident:
                current_macro = v
        
        reg_to_replace = exp_to_list(current_macro.reglist)
        macro_reg = exp_to_list(tree[3])
        
        # replace register in macro def
        branch = copy.deepcopy(current_macro.body)
        replace_register(branch, reg_to_replace, macro_reg)
        macro_expand(branch, None)
        # print('prarent :', parent)
        # replace macro call branch by macro definition branch
        # first, add the "return" register command to the new branch
        reg = {'type':'reg', 'val':0}
        move = ['<-', tree[1], reg]
        reset = ['<-', {'type':'reg', 'val':0} , {'type':'num', 'val':0}]
        branch = ['exp', branch, ['exp', move, reset]]
        parent[1] = branch
    elif len(tree) == 2:
        # print(tree[0])
        # print(tree[1])
        macro_expand(tree[0], parent)
        macro_expand(tree[1], parent)
    
    
def exp_to_list(list):
    if list[1] == 'nil':
        return [list[0]['val']]
    else:
        return [list[0]["val"]] + exp_to_list(list[1])

def replace_register(tree, old_reg, new_reg):
    
    if type(tree) is dict:
        for i in range(len(old_reg)):
            if tree['val'] == old_reg[i]:
                tree['val'] = new_reg[i]

    elif type(tree[0]) is dict:
        for i in range(len(old_reg)):
            if tree[0]['val'] == old_reg[i]:
                tree[0]['val'] = new_reg[i]
        replace_register(tree[1], old_reg, new_reg)
    
    elif tree == 'nil' or tree == 'end':
        pass
    elif tree[0] == 'exp':
        replace_register(tree[1], old_reg, new_reg)
    elif tree[0] == '<-' or tree[0] == 'repeat':
        replace_register(tree[1], old_reg, new_reg)
        replace_register(tree[2], old_reg, new_reg)
    elif tree[0] == 'inc':
        replace_register(tree[1], old_reg, new_reg)
    elif tree[0] == 'macro':
        replace_register(tree[1], old_reg, new_reg)
        replace_register(tree[3], old_reg, new_reg)
    elif tree[0] == 'body':
        replace_register(tree[1], old_reg, new_reg)
    else:
        replace_register(tree[0], old_reg, new_reg)
        replace_register(tree[1], old_reg, new_reg)

        

# ======================
#    AST evaluation
# ======================

# The syntax tree is represented as a list of expressions where 
# the left branch is the expression to evaluate and the right brand 
# is the next expression to evaluate. The function takes a regular Pyhton
# tuples which is how the interpreter represent the AST with the first element
# being an identifier for the node type, and all other elements are the
# children of that node. Expressions nodes only have two childre but
# other node types may have more.

# specific actions fonctions
def eval_exp(exp):
    """     
    exp[0] = first expression to evaluate
    exp[1] = rest of the tree, may be there or not (absent at the end of the Tree)
    """    
    if logger.log_eval:
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
    if logger.log_eval:
        print('EVAL_INC : ' + str(exp))
        if logger.verbose:
            print("before : r" + str(exp[0]['val']) + ' = ' + str(register[exp[0]['val']]))
    register[exp[0]['val']] = register[exp[0]['val']] + 1
    if logger.verbose and logger.log_eval:
        print("after  : r" + str(exp[0]['val']) + ' = ' + str(register[exp[0]['val']]))

def eval_move(exp):
    """     
    exp[0] = register to move value to
    exp[1] = maybe a register to move value from or an Int 
    """    
    if logger.log_eval:
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
    if logger.log_eval:
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
    if logger.log_eval:
        print('EVAL_REPEAT : ' + str(register[exp[0]["val"]]))
    for n in range(register[exp[0]["val"]]):
        print('reg :', exp[0])
        print('repeat body :', exp[1][1])
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

    if exp[0] == 'end' or exp[0] == 'nil' or exp[0] == 'def':
        pass


# ======================
#    Program launch
# ======================

# file handling
testFile = open(CURRENT_TEST, mode="r")
testData = ""
for l in testFile:
    testData += l

file_name = CURRENT_TEST[9:]

if logger.debug:
    print('\nrunning file : '+ file_name+'\n')

if logger.debug:
    print(line + '\n     Lex Tokens\n' + line + '\n')

# Give the lexer some input
lexer.input(testData)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

# parse the file
parser = yacc.yacc(outputdir="outputs")

# create the AST
abstract_syntax_tree = parser.parse(testData)

print(abstract_syntax_tree)
# handle macros
find_macro_def(abstract_syntax_tree)
macro_expand(abstract_syntax_tree, None)


# evaluate the result
eval(abstract_syntax_tree)

# logging
if logger.debug:
    print('\n' + line + '\n     register content\n' + line )
    print(register)
    print('\n' + line + '\n     Final parsed tree\n' + line)
    print(abstract_syntax_tree)

