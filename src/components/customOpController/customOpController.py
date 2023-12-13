import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	import _stubs.TDJSON as TDJSON
	from typing import Any, Dict, List, Optional, Set, Type

# noinspection PyRedeclaration
TDJSON = op.TDModules.mod.TDJSON

class CustomOp:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	def host(self) -> COMP | None:
		host = self.ownerComp.par.Hostop.eval()
		if not host:
			raise Exception('No host attached to custom op controller')
		return host

	def opDef(self) -> COMP | None:
		return self.ownerComp.par.Opdef.eval()

	def paramsOp(self) -> COMP | None:
		host = self.host()
		return host and op(host.par['Paramsop'])

	def Installinhost(self, _=None):
		host = self.host()
		page = host.appendCustomPage('Tools')
		for par in self.ownerComp.pars(
				'Create*', 'Removeunusedparams'):
			page.appendPulse(par.name, label=par.label)

	def Createopglobals(self, _=None):
		self._createDat(
			textDAT, self.ownerComp.par.Defaultopglobals.eval(),
			'_globals', -320, -150, 'Opglobals')

	def Createinit(self, _=None):
		self._createDat(
			textDAT, self.ownerComp.par.Defaultinit.eval(),
			'_init', -120, -150, 'Initcode')

	def Createfunction(self, _=None):
		self._createDat(
			textDAT,
			self.ownerComp.par.Defaultfunction.eval() or self.ownerComp.op('defaultFunctionTemplate'),
			'_function', 0, -150, 'Function')

	def Creatematerial(self, _=None):
		self._createDat(
			textDAT, self.ownerComp.par.Defaultmaterial.eval(),
			'_material', 120, -150, 'Materialcode')

	def Createbuffertable(self, _=None):
		self._createDat(
			tableDAT, self.ownerComp.op('bufferTableTemplate'),
			'_buffers', -120, -250, 'Buffertable')

	def Createmacrotable(self, _=None):
		self._createDat(
			tableDAT, self.ownerComp.op('macroTableTemplate'),
			'_macros', 0, -250, 'Macrotable')

	def Createtexturetable(self, _=None):
		self._createDat(
			tableDAT, self.ownerComp.op('textureTableTemplate'),
			'_textures', 120, -250, 'Texturetable')

	def Createvariabletable(self, _=None):
		self._createDat(
			tableDAT, self.ownerComp.op('variableTableTemplate'),
			'_variables', 240, -250, 'Variabletable')

	def Createmissingparams(self, _=None):
		self._updateParams(removeUnused=False, createMissing=True)

	def Removeunusedparams(self, _=None):
		self._updateParams(removeUnused=True, createMissing=False)

	def Createparamsop(self, _=None):
		host = self.host()
		parOp = self.paramsOp()
		if parOp:
			return
		parOp = host.parent().create(baseCOMP, host.name + '_params')
		parOp.nodeX = host.nodeX
		parOp.nodeY = host.nodeY + 175
		parOp.dock = host
		host.showDocked = True
		parOp.appendCustomPage('Parameters')
		host.par.Paramsop = parOp
		return parOp

	def _updateParams(self, removeUnused: bool, createMissing: bool):
		host = self.host()
		paramsOp = self.paramsOp()
		if not paramsOp:
			paramsOp = self.Createparamsop()
		print(f'Updating params for {host} using {paramsOp}')
		referencedNames = self._allReferencedParamNames()
		specs = self._paramSpecsFromCode()

		TDJSON.addParametersFromJSONDict(
			paramsOp,
			specs,
			replace=True,
			setValues=False,
			ignoreAttrErrors=True,
			fixParNames=False,
		)

		if createMissing and referencedNames:
			page = paramsOp.appendCustomPage('Parameters')
			knownTupletNames = [
				parTuplet[0].tupletName
				for parTuplet in paramsOp.customTuplets
			]
			for name in referencedNames:
				# attempting to check host.par[tupletName] throws an exception instead of just returning none,
				# so avoid doing that
				if name in knownTupletNames:
					continue
				if host.par[name] is None:
					page.appendFloat(name)

		if removeUnused:
			namesToKeep = list(referencedNames) + list(specs.keys())
			for parTuplet in list(self._hostParamTuplets()):
				if not parTuplet[0].valid:
					continue
				if parTuplet[0].tupletName in namesToKeep:
					continue
				if any(p.name in namesToKeep for p in parTuplet):
					continue
				parTuplet[0].destroy()

	def buildParamTable(self, dat: DAT):
		dat.clear()
		referencedNames = self._allReferencedParamNames()
		names = []
		tupletNames = {
			parTuplet[0].tupletName: [p.name for p in parTuplet]
			for parTuplet in self._hostParamTuplets()
		}
		for name in list(referencedNames):
			if name not in tupletNames:
				if name not in names:
					names.append(name)
			else:
				for partName in tupletNames[name]:
					if partName not in names:
						names.append(partName)
		dat.appendRow([' '.join(names)])

	def _allCodeBlocks(self) -> 'list[str]':
		return [
			dat.text
			for dat in self.codeDats()
		]

	def codeDats(self) -> 'List[DAT]':
		return [
			par.eval()
			for par in self.host().pars('Opglobals', 'Initcode', 'Function', 'Materialcode')
			if par.eval()
		]

	def _allReferencedParamNames(self) -> 'Set[str]':
		return {
			name
			for code in self._allCodeBlocks()
			for name in _paramPattern.findall(code)
		}

	def _paramSpecsFromCode(self):
		specs = {}
		for code in self._allCodeBlocks():
			specs.update(_extractParamSpecs(code))
		return specs

	def _hostParamTuplets(self) -> 'List[ParTupletT]':
		paramsOp = self.paramsOp()
		return paramsOp.customTuplets if paramsOp else []

	def _createDat(
			self, opType: 'Type[DAT]',
			template: 'Optional[DAT]', nameSuffix: str,
			offsetX: int, offsetY: int,
			hostParName: str
	):
		host = self.host()
		name = host.name + nameSuffix
		hostPar = host.par[hostParName]

		def createOrUndo(isUndo: bool, _: dict):
			dest = host.parent()
			if isUndo:
				print(self.ownerComp, f'undoing create OP: {name}')
				newOp = dest.op(name)
				if newOp and newOp.valid:
					try:
						newOp.destroy()
					except:
						pass
				hostPar.val = ''
			else:
				dat = dest.create(opType, name)
				if template:
					dat.copy(template)
				elif dat.isText:
					dat.text = ''
				else:
					dat.clear()
				dat.par.language = 'glsl' if dat.isText else 'txt'
				dat.par.extension = dat.par.language
				dat.nodeX = host.nodeX + offsetX
				dat.nodeY = host.nodeY + offsetY
				dat.dock = host
				host.showDocked = True
				dat.viewer = True
				dat.activeViewer = True
				hostPar.val = dat
		ui.undo.startBlock(f'Create DAT {name}')
		createOrUndo(False, {})
		ui.undo.addCallback(createOrUndo, {})
		ui.undo.endBlock()

_paramPattern = re.compile(r'\bTHIS_([A-Z][a-z0-9]*)\b')
# param spec format:
# // @Translate {"style":"XYZ", "default":1.0, "min":0.1, "max":3.0}
# // @Radius {"default":2.1, "label":"Thing Radius"}
_paramSpecPattern = re.compile(r'@([A-Z][a-z0-9]*)\s*({.*})')

def _extractParamSpecs(code: str) -> 'Dict[str, Dict[str, Any]]':
	if not code:
		return {}
	matches = _paramSpecPattern.findall(code)
	if not matches:
		return {}
	specs = {}
	for name, specJson in matches:
		spec = TDJSON.textToJSON(specJson, showErrors=True)
		if 'name' not in spec:
			spec['name'] = name
		if 'style' not in spec:
			spec['style'] = 'Float'
		if 'page' not in spec:
			spec['page'] = 'Parameters'
		specs[name] = spec
	return specs
