
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DEF END ID INC INT MOVE REG REPEATprog : instr \n            | instr proginstr : cmd \n             | macdefcmd : incr \n           | mv \n           | rpt \n           | macincr : INC REGmv : REG MOVE REG \n          | REG MOVE INTrpt : REPEAT REG bodybody : innerbody ENDinnerbody : cmd \n                 | cmd innerbodymac : REG MOVE ID reglistmacdef : DEF ID reglist bodyreglist : REG \n               | REG reglist'
    
_lr_action_items = {'MOVE':([2,],[13,]),'$end':([1,4,7,8,9,10,11,12,15,17,18,20,23,25,26,28,29,30,],[-4,-1,-3,-6,-8,0,-5,-7,-2,-9,-11,-10,-12,-18,-16,-13,-17,-19,]),'END':([8,9,11,12,17,18,20,21,22,23,25,26,27,28,30,],[-6,-8,-5,-7,-9,-11,-10,-14,28,-12,-18,-16,-15,-13,-19,]),'ID':([5,13,],[16,19,]),'REG':([0,1,3,4,6,7,8,9,11,12,13,14,16,17,18,19,20,21,23,24,25,26,28,29,30,],[2,-4,14,2,17,-3,-6,-8,-5,-7,20,2,25,-9,-11,25,-10,2,-12,2,25,-16,-13,-17,-19,]),'REPEAT':([0,1,4,7,8,9,11,12,14,17,18,20,21,23,24,25,26,28,29,30,],[3,-4,3,-3,-6,-8,-5,-7,3,-9,-11,-10,3,-12,3,-18,-16,-13,-17,-19,]),'INT':([13,],[18,]),'DEF':([0,1,4,7,8,9,11,12,17,18,20,23,25,26,28,29,30,],[5,-4,5,-3,-6,-8,-5,-7,-9,-11,-10,-12,-18,-16,-13,-17,-19,]),'INC':([0,1,4,7,8,9,11,12,14,17,18,20,21,23,24,25,26,28,29,30,],[6,-4,6,-3,-6,-8,-5,-7,6,-9,-11,-10,6,-12,6,-18,-16,-13,-17,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cmd':([0,4,14,21,24,],[7,7,21,21,21,]),'macdef':([0,4,],[1,1,]),'mac':([0,4,14,21,24,],[9,9,9,9,9,]),'prog':([0,4,],[10,15,]),'reglist':([16,19,25,],[24,26,30,]),'incr':([0,4,14,21,24,],[11,11,11,11,11,]),'instr':([0,4,],[4,4,]),'rpt':([0,4,14,21,24,],[12,12,12,12,12,]),'body':([14,24,],[23,29,]),'mv':([0,4,14,21,24,],[8,8,8,8,8,]),'innerbody':([14,21,24,],[22,27,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> instr','prog',1,'p_prog','rpt_syntax.py',94),
  ('prog -> instr prog','prog',2,'p_prog','rpt_syntax.py',95),
  ('instr -> cmd','instr',1,'p_instr','rpt_syntax.py',102),
  ('instr -> macdef','instr',1,'p_instr','rpt_syntax.py',103),
  ('cmd -> incr','cmd',1,'p_cmd','rpt_syntax.py',107),
  ('cmd -> mv','cmd',1,'p_cmd','rpt_syntax.py',108),
  ('cmd -> rpt','cmd',1,'p_cmd','rpt_syntax.py',109),
  ('cmd -> mac','cmd',1,'p_cmd','rpt_syntax.py',110),
  ('incr -> INC REG','incr',2,'p_incr','rpt_syntax.py',114),
  ('mv -> REG MOVE REG','mv',3,'p_mv','rpt_syntax.py',118),
  ('mv -> REG MOVE INT','mv',3,'p_mv','rpt_syntax.py',119),
  ('rpt -> REPEAT REG body','rpt',3,'p_rpt','rpt_syntax.py',123),
  ('body -> innerbody END','body',2,'p_body','rpt_syntax.py',127),
  ('innerbody -> cmd','innerbody',1,'p_innerbody','rpt_syntax.py',131),
  ('innerbody -> cmd innerbody','innerbody',2,'p_innerbody','rpt_syntax.py',132),
  ('mac -> REG MOVE ID reglist','mac',4,'p_mac','rpt_syntax.py',140),
  ('macdef -> DEF ID reglist body','macdef',4,'p_macdef','rpt_syntax.py',145),
  ('reglist -> REG','reglist',1,'p_reglist','rpt_syntax.py',149),
  ('reglist -> REG reglist','reglist',2,'p_reglist','rpt_syntax.py',150),
]