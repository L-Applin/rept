# PYTHON Interpreter for "REPEAT" langage

Note : this is a personal project that I'm doing for fun and learning. Don't expect any commitement from my part or regular updates or anything of such. If you would like more information about the project, contact me personnaly.

## Description

*Repeat* is a pseudo-programing languge invented by [Alain Tapp][alain tapp] for our 
[Introduction à l'informatique théorique][info theo] (Introduction to Theoretical computer science) at [University of Montreal][udem]]. As a challenge I decided I would try to implement an interpreter of the langage by myself using Python.

### The langage
*Repeat* is a very simple, very contrived and very limited "programming langage". I made some very slight modification to the syntax Mr Tapp used in his class but everything else is exactly the same. Firts, it has an infinitly large amount of register that can each store an integer as large as needed. Second, it has only a few operations that can be made on those register : 

1. Increment the value stored in a register : `inc r<sub>i<\sub>`
2. Move the value from one register to another : `r<sub>i<\sub> <- r<sub>j<\sub>` 
3. Repeat a block of commands by the amount of a register : `repeat r<sub>i<\sub> <list of commands to repeat>`
4. It also has the ability to define *non-rucursive* macro to make the code more readable

### Grammar
Here is the grammar I came up with for the *Repeat* langage






[info theo]: https://sites.google.com/site/dirotappift2105/
[alain tapp]: http://diro.umontreal.ca/repertoire-departement/vue/tapp-alain/
[udem]: http://www.umontreal.ca/