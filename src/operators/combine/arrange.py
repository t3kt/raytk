from dataclasses import dataclass

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional, Tuple

@dataclass
class Stage:
	i: int
	tra: 'Optional[Tuple[Par, Par, Par]]'

	def hasTranslate(self):
		if self.tra is None:
			return False
		if not _isConst(self.tra[0]) or not _isConst(self.tra[1]) or not _isConst(self.tra[2]):
			return True
		return self.tra[0] != 0 or self.tra[1] != 0 or self.tra[2] != 0

	def inputCall(self):
		if not self.hasTranslate():
			return f'inputOp{self.i}(p, ctx)'
		return f'inputOp{self.i}(p - THIS_asCoordT(vec3({parCode(self.tra[0])}, {parCode(self.tra[1])}, {parCode(self.tra[2])})), ctx)'

def _isConst(par: 'Par'):
	return par.mode == ParMode.CONSTANT

def _parOrConst(par: 'Par'):
	return par.eval() if _isConst(par) else par

@dataclass
class State:
	cmb: str
	swap: bool
	stages: 'List[Stage]'
	rad: 'Optional[Par]' = None
	num: 'Optional[Par]' = None
	off: 'Optional[Par]' = None

def loadState() -> 'State':
	p = parent().par
	cmb = p.Combine.eval()
	state = State(cmb, p.Swapinputs.eval(), [])
	useTranslate = p.Enabletranslate.eval()
	if not cmb.startswith('simple'):
		state.rad = p.Radius
	if cmb.startswith('stair') or cmb.startswith('column'):
		state.num = p.Number
		state.off = p.Offset
	for i in range(1, 9):
		suffix = str(i)
		if op('definition_' + suffix).numRows < 2:
			continue
		if not p['Enable' + suffix]:
			continue
		state.stages.append(Stage(
			i,
			tra=(p[f'Translate{suffix}x'], p[f'Translate{suffix}y'], p[f'Translate{suffix}z']) if useTranslate else None,
		))
	return state

def parCode(par: 'Par'):
	if _isConst(par):
		return str(par.eval())
	return 'THIS_' + par.name
