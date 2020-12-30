from dataclasses import dataclass
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from _stubs.TDCallbacksExt import CallbacksExt

	ext.callbacks = CallbacksExt(COMP())

	class _Pars(ParCollection):
		Targetop: 'OPParamT'
		Selecteditem: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class DatEditorPanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	@property
	def _currentItemPar(self) -> 'Optional[Par]':
		o = self.ownerComp.par.Targetop.eval()
		if not o:
			return
		name = self.ownerComp.par.Selecteditem.eval()
		if name:
			return o.par[name]

	@property
	def currentSourceDat(self) -> 'Optional[DAT]':
		graph = self._currentItemGraph
		return graph and graph.sourceDat

	def _callbackInfo(self, **kwargs):
		info = {
			'parName': self.ownerComp.par.Selecteditem.eval(),
			'endDat': '',
		}
		pass

	@property
	def _currentItemGraph(self) -> 'Optional[_ItemGraph]':
		par = self._currentItemPar
		if par is None:
			return
		graph = _ItemGraph.fromPar(par)
		if graph.supported:
			return graph

	@property
	def _currentItemFilePar(self) -> 'Optional[Par]':
		graph = self._currentItemGraph
		return graph and graph.file

	def buildItemGraphInfo(self, dat: 'DAT'):
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
		graph = self._currentItemGraph
		if not graph:
			return
		dat['endDat', 1] = graph.endDat or ''
		dat['sourceDat', 1] = graph.sourceDat or ''
		dat['hasEval', 1] = int(graph.hasEval)
		dat['hasMerge', 1] = int(graph.hasMerge)
		dat['supported', 1] = 1
		dat['file', 1] = graph.file or ''



@dataclass
class _ItemGraph:
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
		if isinstance(endDat, (tableDAT, textDAT)):
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
		if isinstance(dat, (tableDAT, textDAT)):
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
