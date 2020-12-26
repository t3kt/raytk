from dataclasses import dataclass
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())

	class _Pars(ParCollection):
		Selectedtable: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class TablePanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp


@dataclass
class _TableGraph:
	par: 'Par'
	endDat: 'Optional[DAT]' = None
	sourceDat: 'Optional[DAT]' = None
	hasEval: bool = False
	hasMerge: bool = False
	supported: bool = False

	@classmethod
	def fromPar(cls, par: 'Par'):
		endDat = par.eval()
		if not endDat:
			return cls(par, supported=True)
		if isinstance(endDat, tableDAT):
			return cls(
				par,
				endDat=endDat,
				sourceDat=endDat,
				hasEval=False,
				hasMerge=False,
				supported=True,
			)
		dat = endDat
		if isinstance(dat, nullDAT):
			if not dat.inputs:
				return cls(par, supported=False)
			dat = dat.inputs[0]
		hasEval = False
		hasMerge = False
		if isinstance(dat, evaluateDAT):
			if not dat.inputs:
				return cls(par, endDat=endDat, supported=False)
			hasEval = True
			dat = dat.inputs[0]

		# TODO: STUFF!

		pass

