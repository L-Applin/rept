import re

REG_SIZE = 256
INIT_VALUE = 0
DEBUG = True
REPEAT_STACK = []

# Inititating registers
reg = []
for i in range(REG_SIZE):
    reg.append(INIT_VALUE)

# file handling
code = open('test.rpt', mode='r')


# commands

# increment
def inc(n):
    reg[int(n)] = reg[int(n)] + 1


# move
def mv_register(from_reg, dest_reg):
    reg[int(dest_reg)] = reg[int(from_reg)]


def mv_int(value, dest_reg):
    reg[int(dest_reg)] = int(value)


# execute a basic command on a line
def execute(l):
    if line.startswith("inc"):  # increase register
        n = line[5:]
        inc(n)
        print("inc reg " + n)
    elif line.startswith("r"):  # set value
        r1 = re.search('(\d+)', line).groups()[0]
        if re.search('(r)', line[6:]) is not None:  #mv_register
             r2 = re.search('(\d+)', line[6:]).groups()[0]
             mv_register(r2, r1)
             print("move reg "  + r2 +" into reg " + r1)
        else:   # move int into register
             n = re.search('(\d+)', line[6:]).groups()[0]
             print("move " + n +" into reg " + r1)
             mv_int(n, r1)
    elif line.startswith("repeat"):
        n = re.search('(\d+)', line).groups()[0]
        cmd = []
        while l != "end":
            cmd += l.readLine();
        print(cmd)


# repeat statement
def repeat(n, statements):
    for i in range(n):
        for line in statements:
            execute(line)


# parsing the document
for l in code:
    line = l.strip()
    if line.startswith("--") or line.startswith("#"): # comments
        pass
    else:
        execute(line)


if(DEBUG):
    print(reg)
