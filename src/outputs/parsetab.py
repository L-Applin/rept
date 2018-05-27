
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DEF END ID INC INT MOVE REG REPEATprog : instr \n            | instr proginstr : cmd \n             | macdefcmd : incr \n           | mv \n           | rpt \n           | macincr : INC REGmv : REG MOVE REG \n          | REG MOVE INTrpt : REPEAT REG bodybody : innerbody ENDinnerbody : cmd \n                 | cmd innerbodymac : REG MOVE ID reglistmacdef : DEF ID reglist bodyreglist : REG \n               | REG reglist'
    
_lr_action_items = {'DEF':([0,1,3,6,7,9,10,11,13,19,22,24,25,27,28,29,30,],[8,-6,-3,-4,-7,8,-8,-5,-9,-12,-18,-11,-10,-13,-17,-19,-16,]),'ID':([8,17,],[15,23,]),'INT':([17,],[24,]),'END':([1,7,10,11,13,18,19,20,22,24,25,26,27,29,30,],[-6,-7,-8,-5,-9,-14,-12,27,-18,-11,-10,-15,-13,-19,-16,]),'INC':([0,1,3,6,7,9,10,11,13,14,18,19,21,22,24,25,27,28,29,30,],[4,-6,-3,-4,-7,4,-8,-5,-9,4,4,-12,4,-18,-11,-10,-13,-17,-19,-16,]),'MOVE':([12,],[17,]),'REPEAT':([0,1,3,6,7,9,10,11,13,14,18,19,21,22,24,25,27,28,29,30,],[5,-6,-3,-4,-7,5,-8,-5,-9,5,5,-12,5,-18,-11,-10,-13,-17,-19,-16,]),'$end':([1,2,3,6,7,9,10,11,13,16,19,22,24,25,27,28,29,30,],[-6,0,-3,-4,-7,-1,-8,-5,-9,-2,-12,-18,-11,-10,-13,-17,-19,-16,]),'REG':([0,1,3,4,5,6,7,9,10,11,13,14,15,17,18,19,21,22,23,24,25,27,28,29,30,],[12,-6,-3,13,14,-4,-7,12,-8,-5,-9,12,22,25,12,-12,12,22,22,-11,-10,-13,-17,-19,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instr':([0,9,],[9,9,]),'mac':([0,9,14,18,21,],[10,10,10,10,10,]),'prog':([0,9,],[2,16,]),'cmd':([0,9,14,18,21,],[3,3,18,18,18,]),'body':([14,21,],[19,28,]),'innerbody':([14,18,21,],[20,26,20,]),'reglist':([15,22,23,],[21,29,30,]),'macdef':([0,9,],[6,6,]),'mv':([0,9,14,18,21,],[1,1,1,1,1,]),'incr':([0,9,14,18,21,],[11,11,11,11,11,]),'rpt':([0,9,14,18,21,],[7,7,7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> instr','prog',1,'p_prog','rpt_syntax.py',93),
  ('prog -> instr prog','prog',2,'p_prog','rpt_syntax.py',94),
  ('instr -> cmd','instr',1,'p_instr','rpt_syntax.py',101),
  ('instr -> macdef','instr',1,'p_instr','rpt_syntax.py',102),
  ('cmd -> incr','cmd',1,'p_cmd','rpt_syntax.py',106),
  ('cmd -> mv','cmd',1,'p_cmd','rpt_syntax.py',107),
  ('cmd -> rpt','cmd',1,'p_cmd','rpt_syntax.py',108),
  ('cmd -> mac','cmd',1,'p_cmd','rpt_syntax.py',109),
  ('incr -> INC REG','incr',2,'p_incr','rpt_syntax.py',113),
  ('mv -> REG MOVE REG','mv',3,'p_mv','rpt_syntax.py',117),
  ('mv -> REG MOVE INT','mv',3,'p_mv','rpt_syntax.py',118),
  ('rpt -> REPEAT REG body','rpt',3,'p_rpt','rpt_syntax.py',122),
  ('body -> innerbody END','body',2,'p_body','rpt_syntax.py',126),
  ('innerbody -> cmd','innerbody',1,'p_innerbody','rpt_syntax.py',130),
  ('innerbody -> cmd innerbody','innerbody',2,'p_innerbody','rpt_syntax.py',131),
  ('mac -> REG MOVE ID reglist','mac',4,'p_mac','rpt_syntax.py',139),
  ('macdef -> DEF ID reglist body','macdef',4,'p_macdef','rpt_syntax.py',144),
  ('reglist -> REG','reglist',1,'p_reglist','rpt_syntax.py',148),
  ('reglist -> REG reglist','reglist',2,'p_reglist','rpt_syntax.py',149),
]
