from ply import lex, yacc

INIT_VALUE = 0
REGISTER_SIZE = 256

# register initialization 
register = []
for i in range(REGISTER_SIZE):
    register.append(INIT_VALUE)

# tokens
tokens = ('REG', 'MOVE', 'INC', 'ID', 'REPEAT', 'DEF', 'INT')

t_MOVE = '<-'
t_INC = 'inc'
t_ID = r'[_a-zA-Z][_a-zA-Z0-9]'
t_DEF= 'DEFINE-MACRO'
t_REPEAT = 'repeat'


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

def p_mac(p):
    '''mac : REG MOVE ID reglist'''
    p[0] = ('replace', p[1], p[3], p[4])

def p_macdef(p):
    '''macdef : ID reglist'''
    
def p_body(p):
