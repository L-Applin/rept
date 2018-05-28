
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DEF END ID INC INT LP MOVE REG REPEAT RPprog : instr \n            | instr proginstr : cmd \n             | macdefcmd : incr \n           | mv \n           | rpt \n           | macincr : INC REGmv : REG MOVE REG \n          | REG MOVE INTrpt : REPEAT REG bodybody : innerbody ENDinnerbody : cmd \n                 | cmd innerbodymac : REG MOVE ID reglistmacdef : DEF ID reglist bodyinnerreglist : REG \n                    | REG innerreglistreglist : LP innerreglist RP '
    
_lr_action_items = {'LP':([17,21,],[24,24,]),'ID':([7,15,],[17,21,]),'INC':([0,2,3,6,8,9,10,12,13,14,18,20,22,23,25,27,28,31,33,],[1,-8,-3,1,-6,-4,-7,-5,-9,1,1,-12,-11,-10,1,-13,-16,-17,-20,]),'END':([2,8,10,12,13,18,19,20,22,23,26,27,28,33,],[-8,-6,-7,-5,-9,-14,27,-12,-11,-10,-15,-13,-16,-20,]),'REG':([0,1,2,3,4,6,8,9,10,12,13,14,15,18,20,22,23,24,25,27,28,29,31,33,],[5,13,-8,-3,14,5,-6,-4,-7,-5,-9,5,23,5,-12,-11,-10,29,5,-13,-16,29,-17,-20,]),'INT':([15,],[22,]),'REPEAT':([0,2,3,6,8,9,10,12,13,14,18,20,22,23,25,27,28,31,33,],[4,-8,-3,4,-6,-4,-7,-5,-9,4,4,-12,-11,-10,4,-13,-16,-17,-20,]),'RP':([29,30,32,],[-18,33,-19,]),'$end':([2,3,6,8,9,10,11,12,13,16,20,22,23,27,28,31,33,],[-8,-3,-1,-6,-4,-7,0,-5,-9,-2,-12,-11,-10,-13,-16,-17,-20,]),'MOVE':([5,],[15,]),'DEF':([0,2,3,6,8,9,10,12,13,20,22,23,27,28,31,33,],[7,-8,-3,7,-6,-4,-7,-5,-9,-12,-11,-10,-13,-16,-17,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'macdef':([0,6,],[9,9,]),'mac':([0,6,14,18,25,],[2,2,2,2,2,]),'cmd':([0,6,14,18,25,],[3,3,18,18,18,]),'body':([14,25,],[20,31,]),'instr':([0,6,],[6,6,]),'innerbody':([14,18,25,],[19,26,19,]),'mv':([0,6,14,18,25,],[8,8,8,8,8,]),'rpt':([0,6,14,18,25,],[10,10,10,10,10,]),'prog':([0,6,],[11,16,]),'innerreglist':([24,29,],[30,32,]),'incr':([0,6,14,18,25,],[12,12,12,12,12,]),'reglist':([17,21,],[25,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> instr','prog',1,'p_prog','rpt_syntax.py',97),
  ('prog -> instr prog','prog',2,'p_prog','rpt_syntax.py',98),
  ('instr -> cmd','instr',1,'p_instr','rpt_syntax.py',105),
  ('instr -> macdef','instr',1,'p_instr','rpt_syntax.py',106),
  ('cmd -> incr','cmd',1,'p_cmd','rpt_syntax.py',110),
  ('cmd -> mv','cmd',1,'p_cmd','rpt_syntax.py',111),
  ('cmd -> rpt','cmd',1,'p_cmd','rpt_syntax.py',112),
  ('cmd -> mac','cmd',1,'p_cmd','rpt_syntax.py',113),
  ('incr -> INC REG','incr',2,'p_incr','rpt_syntax.py',117),
  ('mv -> REG MOVE REG','mv',3,'p_mv','rpt_syntax.py',121),
  ('mv -> REG MOVE INT','mv',3,'p_mv','rpt_syntax.py',122),
  ('rpt -> REPEAT REG body','rpt',3,'p_rpt','rpt_syntax.py',126),
  ('body -> innerbody END','body',2,'p_body','rpt_syntax.py',130),
  ('innerbody -> cmd','innerbody',1,'p_innerbody','rpt_syntax.py',134),
  ('innerbody -> cmd innerbody','innerbody',2,'p_innerbody','rpt_syntax.py',135),
  ('mac -> REG MOVE ID reglist','mac',4,'p_mac','rpt_syntax.py',143),
  ('macdef -> DEF ID reglist body','macdef',4,'p_macdef','rpt_syntax.py',148),
  ('innerreglist -> REG','innerreglist',1,'p_innerreglist','rpt_syntax.py',152),
  ('innerreglist -> REG innerreglist','innerreglist',2,'p_innerreglist','rpt_syntax.py',153),
  ('reglist -> LP innerreglist RP','reglist',3,'p_reglist','rpt_syntax.py',160),
]
