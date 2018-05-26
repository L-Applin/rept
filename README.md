# PYTHON Interpreter for "REPEAT" langage

Note : this is a personal project that I'm doing for fun and learning. Don't expect any commitement from my part or regular updates or anything of such. If you would like more information about the project, contact me personnaly.

## Description

*Repeat* is a pseudo-programing languge invented by [Alain Tapp][alain tapp] for our 
[Introduction à l'informatique théorique][info theo] (Introduction to Theoretical computer science) at [University of Montreal][udem]. As a challenge I decided I would try to implement an interpreter of the langage by myself using Python.

### The langage
*Repeat* is a very simple, very contrived and very limited "programming langage". I made some very slight modification to the syntax Mr Tapp used in his class but everything else is exactly the same. First, the langage has an infinit amount of registers that it canuse to store an integer, as large as needed. Second, it has a few operations that can be made on those register : 

1. Increment the value stored in a register : `inc r0`
2. Move the value from one register to another : `r1 <- r2`. It is also possible to directly put a value inside a register : `r0 <- 1024`
3. Repeat a block of commands by the amount of a register : `repeat r4 <list of commands to repeat>`
4. It also has the ability to define *non-recursive* macro to make the code more readable :
``` text
DEFINE-MACRO macro_id <list of identifiers> 
    <block of commands for the macro>
end

r0 <- macro_id <list of registers to use for the macro>
    <that line will execute all commands writen within the macro block with the specified registers>

```
That's it.


### Grammar
Here is the grammar I came up with for the *Repeat* langage

```
GRAMMAR                                            ACTION
---------------------------------------------      -------------------------------------------
<prog>      ::=    <instr> | <instr> <prog>        none           
<instr>     ::=    <cmd> | <mac>                   none          
<cmd>       ::=    <incr>                          none
                    | <mv>                         
                    | <rpt> 
                    | <mac>              

<incr>      ::=    INC REG                         reg[<register>] = reg[<register>] + 1
<mv>        ::=    REG MOVE (REG | INT)            reg[<register1>] = reg[<register2>]
<rpt>       ::=    REPEAT REG <body>               repeats all commands in body <register> amount of time

<mac>       ::=    REG MOVE ID <reglist>           execute all commands within matchin f macro definition
<macdef>    ::=    DEF ID <reglist> <body>         define all actions to be done upon calling macro

<body>      ::=    <inner-body> END                none        
<innerbody> ::=    <cmd> | <cmd> <inner-body>      none      
<reglist>   ::=    REG | REG <reglist>             none
<register>  ::=    REG                             none


tokens : 
    REG   : r\d+
    MOVE  : <- 
    INC   : inc rn
    INT   : \d+
    ID    : ([_a-zA-Z])([_a-zA-Z0-9]+)
```

### Parsing
For parsing the .repeat file, I choose to go with the pyhton library [PLY][ply]. This is a robust a classic library to work easily with BNF Grammar syntax. [Documentation][ply doc] for the library can be found by following the link.


[info theo]: https://sites.google.com/site/dirotappift2105/
[alain tapp]: http://diro.umontreal.ca/repertoire-departement/vue/tapp-alain/
[udem]: http://www.umontreal.ca/
[ply]: http://www.dabeaz.com/ply/
[ply doc]: http://www.dabeaz.com/ply/ply.html