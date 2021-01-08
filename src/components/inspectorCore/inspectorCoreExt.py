from typing import Optional, Union
from raytkUtil import InspectorTargetTypes, VisualizerTypes, ReturnTypes, CoordTypes, ContextTypes
from raytkUtil import isROP, isROPDef, ROPInfo, navigateTo
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _state(ParCollection):
		Hastarget: 'BoolParamT'
		Hasownviewer: 'BoolParamT'
		Targettype: 'StrParamT'
		Rawtarget: 'OPParamT'
		Definitiontable: 'DatParamT'
		Targetcomp: 'CompParamT'
		Outputcomp: 'CompParamT'
		Shaderbuilder: 'CompParamT'
		Returntype: 'StrParamT'
		Coordtype: 'StrParamT'
		Contexttype: 'StrParamT'
		Visualizertype: 'StrParamT'

def updateStateMenus():
	p = parent().par.Targettype  # type: Par
	p.menuNames = p.menuLabels = InspectorTargetTypes.values
	p = parent().par.Returntype
	p.menuNames = p.menuLabels = ReturnTypes.values
	p = parent().par.Coordtype
	p.menuNames = p.menuLabels = CoordTypes.values
	p = parent().par.Contexttype
	p.menuNames = p.menuLabels = ContextTypes.values
	p = parent().par.Visualizertype
	p.menuNames = p.menuLabels = VisualizerTypes.values

class InspectorCore:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		# noinspection PyTypeChecker
		self.state = ownerComp.par   # type: _state

	def Reset(self, _=None):
		self.state.Hastarget = False
		self.state.Targettype = InspectorTargetTypes.none
		self.state.Rawtarget = ''
		self.state.Targetcomp = ''
		self.state.Outputcomp = ''
		self.state.Shaderbuilder = ''
		self.state.Definitiontable = ''
		self.state.Visualizertype = VisualizerTypes.none

	def Inspect(self, o: 'Union[OP, DAT, COMP, str]'):
		o = o and op(o)
		if not o:
			self.Reset()
			return
		if isROPDef(o) and o.par['Hostop']:
			o = o.par.Hostop.eval()
		if o.isDAT and o.isTable and o.numRows > 1:
			self.inspectDefinitionTable(o)
		elif isROP(o):
			self.inspectComp(o)
		else:
			# TODO: better error handling
			raise Exception(f'Unsupported OP: {o!r}')

	def inspectDefinitionTable(self, dat: 'DAT'):
		if isROP(dat.parent()) and dat.name == 'definition' and dat[1, 'path'] == dat.parent().path:
			self.inspectComp(dat.parent())
			return
		self.state.Rawtarget = dat
		self.state.Targettype = InspectorTargetTypes.definitionTable
		self.state.Definitiontable = _pathOrEmpty(dat)
		comp = op(dat[1, 'path'])
		self.state.Targetcomp = _pathOrEmpty(comp)
		self.state.Hastarget = True
		self.state.Hasownviewer = False
		ropInfo = ROPInfo(comp)
		self.updateVisualizerType()
		self.AttachOutputComp(comp if ropInfo.isOutput else None)

	def inspectComp(self, comp: 'COMP'):
		self.state.Rawtarget = _pathOrEmpty(comp)
		self.state.Targetcomp = _pathOrEmpty(comp)
		ropInfo = ROPInfo(comp)
		if ropInfo.isOutput:
			self.state.Targettype = InspectorTargetTypes.outputOp
		else:
			self.state.Targettype = InspectorTargetTypes.rop
		self.state.Definitiontable = _pathOrEmpty(comp.op('definition'))
		self.state.Hastarget = True
		self.state.Hasownviewer = ropInfo.isOutput
		self.updateVisualizerType()
		self.AttachOutputComp(comp if ropInfo.isOutput else None)

	def updateVisualizerType(self):
		self.state.Visualizertype = VisualizerTypes.none
		if not self.state.Hastarget:
			return
		if self.state.Coordtype == CoordTypes.float:
			self.state.Visualizertype = VisualizerTypes.functionGraph
		elif self.state.Coordtype == CoordTypes.vec2:
			self.state.Visualizertype = VisualizerTypes.render2d
		elif self.state.Returntype == ReturnTypes.Sdf:
			self.state.Visualizertype = VisualizerTypes.render3d
		elif self.state.Returntype in [ReturnTypes.float, ReturnTypes.vec4]:
			self.state.Visualizertype = VisualizerTypes.field

	def ShowTargetInEditor(self, popup=False):
		navigateTo(self.state.Rawtarget.eval(), popup=popup, goInto=False)

	def AttachOutputComp(self, o: 'COMP'):
		self.state.Outputcomp = _pathOrEmpty(o)
		if o and o.par['Shaderbuilder'] is not None:
			self.state.Shaderbuilder = _pathOrEmpty(o.par.Shaderbuilder.eval())

	@property
	def TargetComp(self) -> 'Optional[COMP]':
		return self.state.Targetcomp.eval()

	@staticmethod
	def buildShaderIncludes(dat: 'DAT', shaderCode: str):
		dat.clear()
		dat.appendRow(['path', 'name'])
		if not shaderCode:
			return
		for match in re.finditer(r'#include\s+<([\w\/_]+)>', shaderCode):
			path = match.group(1)
			o = op(path)
			if o:
				dat.appendRow([
					o.path,
					o.name,
				])


def _pathOrEmpty(o: Optional['OP']):
	return o.path if o else ''
