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

	def buildTableGraphInfo(self, dat: 'DAT'):
		dat.clear()
		dat.appendCol([
			'endDat',
			'sourceDat',
			'hasEval',
			'hasMerge',
			'supported',
			'file',
		])
		dat.appendCol([''])
		graph = self._tableGraph
		if not graph:
			return
		dat['endDat', 1] = graph.endDat or ''
		dat['sourceDat', 1] = graph.sourceDat or ''
		dat['hasEval', 1] = int(graph.hasEval)
		dat['hasMerge', 1] = int(graph.hasMerge)
		dat['supported', 1] = 1
		dat['file', 1] = graph.file or ''

	@property
	def _tableGraph(self) -> 'Optional[_TableGraph]':
		info = ext.ropEditor.ROPInfo
		if not info or not info.isROP:
			return
		name = self.ownerComp.par.Selectedtable.eval()
		par = info.opDefPar[name]
		if par is None:
			return
		graph = _TableGraph.fromPar(par)
		if not graph.supported:
			return
		return graph

	@property
	def tableFilePar(self) -> 'Optional[Par]':
		graph = self._tableGraph
		if graph:
			return graph.file

@dataclass
class _TableGraph:
	par: 'Par'
	endDat: 'Optional[DAT]' = None
	sourceDat: 'Optional[DAT]' = None
	hasEval: bool = False
	hasMerge: bool = False
	supported: bool = False
	file: 'Optional[Par]' = None

	@classmethod
	def fromPar(cls, par: 'Par'):
		endDat = par.eval()  # type: Optional[DAT]
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
				file=endDat.par['file'],
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
		if isinstance(dat, tableDAT):
			return cls(
				par,
				endDat=endDat,
				sourceDat=dat,
				hasMerge=hasMerge,
				hasEval=hasEval,
				supported=True,
				file=dat.par['file'],
			)
		return cls(par, supported=False)

