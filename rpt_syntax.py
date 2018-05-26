from ply import lex, yacc

INIT_VALUE = 0
REGISTER_SIZE = 256

# register initialization 
register = []
for i in range(REGISTER_SIZE):
    register.append(INIT_VALUE)

# tokens
tokens = ('REG', 'MOVE', 'INC', 'ID', 'REPEAT', 'DEF', 'INT', 'END')

t_MOVE = '<-'
t_INC = 'inc'
t_ID = r'[_a-zA-Z][_a-zA-Z0-9]'
t_DEF= 'DEFINE-MACRO'
t_REPEAT = 'repeat'
t_END = 'end'

def t_REG(t):
    r'r\d+'
    t.value = int(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# YACC parse
def p_prog(p):
    '''prog : instr | intr prog'''
    if len(p) == 3:
        p[0] = ('expr', p[1], p[2]) 
    else:
        p[0] = ('expr', p[1])

def p_instr(p):
    '''instr : cmd | mac'''
    p[0] = p[1]

def p_cmd(p):
    '''cmd : incr | mv | rpt | mac'''
    p[0] = p[1]

def p_incr(p):
    ''' incr : INC REG'''
    p[0] = ('incr', p[2])
    register[p[2]] = register[p[2]] + 1

def p_mv(p):
    '''mv : REG MOVE REG | REG MOVE INT'''
    p[0] = ('move', p[1], p[2])
    register[p[1]] = register[p[2]]

def p_rpt(p):
    '''rpt : REPEAT REG body'''
    p[0] = ('repeat', p[2], p[3])

def p_body(p):
    '''body : innerbody END'''
    p[0] =('body', p[1], p[2])

def p_innerbody(p):
    '''innerbody : cmd | cmd innerbody'''
    if len(p) == 1:
        p[0] = p[1]
    else: 
        p[0] = (p[1], p[2])



# should it be replaced by a first pass of the file where macros are replaced ?
def p_mac(p):
    '''mac : REG MOVE ID reglist'''
    p[0] = ('replace', p[1], p[3], p[4])
    # p3 should be the macdef with good 

def p_macdef(p):
    '''macdef : DEF ID reglist body'''
    p[0] = ("def", p[2], p[3], p]4)

def p_reglist(p):
    '''reglist : REG | REG reglist'''
    if len(p) == 1:
        p[0] = p[1]
    else: 
        p[0] = ('list', p[1], p[2])

