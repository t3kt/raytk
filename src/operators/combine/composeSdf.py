from dataclasses import dataclass

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional, Tuple

@dataclass
class Stage:
	src: str
	cmb: str
	tra: 'Tuple[Par, Par, Par]'
	rad: 'Optional[Par]'
	num: 'Optional[Par]'
	off: 'Optional[Par]'

	def _hasTranslate(self):
		if self.tra[0].mode != ParMode.CONSTANT or self.tra[1].mode != ParMode.CONSTANT or self.tra[2].mode != ParMode.CONSTANT:
			return True
		return self.tra[0] != 0 or self.tra[1] != 0 or self.tra[2] != 0

	def inputCall(self):
		if not self._hasTranslate():
			return f'{self.src}(p, ctx)'
		return f'{self.src}(p - THIS_asCoordT(vec3({parCode(self.tra[0])}, {parCode(self.tra[1])}, {parCode(self.tra[2])})), ctx)'

def loadStages() -> 'List[Stage]':
	p = parent().par
	stages = []
	for i in range(1, 9):
		suffix = str(i)
		if not p['Enable' + suffix]:
			continue
		cmb = p['Combine' + suffix].eval()
		if cmb.startswith('simple'):
			rad = None
		else:
			rad = p['Blendradius' + suffix]
		if cmb.startswith('stair') or cmb.startswith('column'):
			num = p['Blendnumber' + suffix]
			off = p['Blendoffset' + suffix]
		else:
			num = None
			off = None
		stages.append(Stage(
			src='inputOp' + p['Input' + suffix].eval()[-1],
			cmb=cmb,
			tra=(p[f'Translate{suffix}x'], p[f'Translate{suffix}y'], p[f'Translate{suffix}z']),
			rad=rad, num=num, off=off
		))
	return stages

def parCode(par: 'Par'):
	if par.mode == ParMode.CONSTANT:
		return par.eval()
	return 'THIS_' + par.name
