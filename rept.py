REG_SIZE = 255
INIT_VALUE = 0

# Inititating registers
reg = [];
for i in range(REG_SIZE):
    reg[i] = INIT_VALUE

# file handling
code = open('test.rpt', mode='r')

# parsing the document


# commands

# increment
def inc(n):
    ren[n] = reng[n] + 1

# move
def mv(from_reg, dest_reg):
    ren[dest_reg] = reg[from_reg]

#
