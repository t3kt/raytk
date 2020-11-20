import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	import _stubs.TDJSON as TDJSON
	from typing import Any, Dict, List, Optional, Set

# noinspection PyRedeclaration
TDJSON = op.TDModules.mod.TDJSON

class CustomOp:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def host(self) -> 'Optional[COMP]':
		host = self.ownerComp.par.Hostop.eval()
		if not host:
			raise Exception('No host attached to custom op controller')
		return host

	def opDef(self) -> 'Optional[COMP]':
		return self.ownerComp.par.Opdef.eval()

	def Installinhost(self, _=None):
		host = self.host()
		page = host.appendCustomPage('Actions')
		for par in self.ownerComp.pars(
				'Create*', 'Removeunusedparams'):
			page.appendPulse(par.name, par.label)

	def Createopglobals(self, _=None):
		host = self.host()
		dat = _createCodeDat(
			host,
			self.ownerComp.par.Defaultopglobals.eval(),
			'_globals',
			-320
		)
		host.par.Opglobals = dat

	def Createinit(self, _=None):
		host = self.host()
		dat = _createCodeDat(
			host,
			self.ownerComp.par.Defaultinit.eval(),
			'_init',
			-120)
		host.par.Initcode = dat

	def Createfunction(self, _=None):
		host = self.host()
		dat = _createCodeDat(
			host,
			self.ownerComp.par.Defaultfunction.eval() or self.ownerComp.op('defaultFunctionTemplate'),
			'_function',
			0)
		host.par.Functemplate = dat

	def Creatematerial(self, _=None):
		host = self.host()
		dat = _createCodeDat(
			host,
			self.ownerComp.par.Defaultmaterial.eval(),
			'_material',
			120
		)
		host.par.Materialcode = dat

	def Createmissingparams(self, _=None):
		self._updateParams(removeUnused=False, createMissing=True)
		pass

	def Removeunusedparams(self, _=None):
		self._updateParams(removeUnused=True, createMissing=False)

	def _updateParams(self, removeUnused: bool, createMissing: bool):
		host = self.host()
		referencedNames = self._allReferencedParamNames()
		specs = self._paramSpecsFromCode()

		TDJSON.addParametersFromJSONDict(
			host,
			specs,
			replace=True,
			setValues=False,
			ignoreAttrErrors=True,
			fixParNames=False,
		)

		if createMissing:
			for name in referencedNames:
				if host.par[name] is None:
					page = host.appendCustomPage('Parameters')
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

		opDef = self.opDef()
		if opDef:
			par = opDef.par.Params
			if par.mode == ParMode.CONSTANT:
				names = set(referencedNames)
				names.update({
					spec['name']
					for spec in specs.values()
					if spec.get('name')
				})
				par.val = ' '.join(names)

	def _allCodeBlocks(self) -> 'List[str]':
		return [
			par.eval().text
			for par in self.host().pars('Opglobals', 'Initcode', 'Functemplate', 'Materialcode')
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
		host = self.host()
		for page in host.customPages:
			if page.name == 'Parameters':
				return page.parTuplets
		return []

def _createCodeDat(host: 'COMP', template: 'Optional[DAT]', nameSuffix: str, offsetX: int) -> 'DAT':
	dat = host.parent().create(textDAT, host.name + nameSuffix)
	dat.text = template.text if template else ''
	dat.par.extension = 'glsl'
	dat.nodeX = host.nodeX + offsetX
	dat.nodeY = host.nodeY - host.nodeHeight - 120
	dat.dock = host
	host.showDocked = True
	return dat

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
