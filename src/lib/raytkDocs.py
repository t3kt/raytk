"""
Tools for extracting and processing documentation for the toolkit and the operators within it.

This should only be used within development tools.
"""

from dataclasses import dataclass, field
import json
from pathlib import Path
import re
import yaml

from raytkUtil import ROPInfo, CategoryInfo, RaytkTags, InputInfo, cleanDict, mergeDicts

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
else:
	# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
	TDJSON = op.TDModules.mod.TDJSON

_defaultParamHelp = 'Help not available.'

@dataclass
class MenuOptionHelp:
	name: str | None = None
	label: str | None = None
	description: str | None = None

	def formatMarkdownListItem(self, includeLabel=False):
		text = f'* `{self.name}`'
		if self.label and includeLabel:
			text += f' *{self.label}*'
		if self.description:
			text += ': ' + self.description
		return text

	def toFrontMatterData(self):
		return cleanDict({
			'name': self.name,
			'label': self.label,
			'description': self.description,
		})

@dataclass
class ROPParamHelp:
	name: str | None = None
	label: str | None = None
	summary: str | None = None
	regularHandling: str | None = None
	readOnlyHandling: str | None = None
	menuOptions: list[MenuOptionHelp] = field(default_factory=list)

	def formatMarkdownListItem(self, includeLabel=False):
		text = f'* `{self.name}`'
		if includeLabel and self.label:
			text += f' *{self.label}*'
		if self.summary:
			text += f': {self.summary}'
		if self.menuOptions:
			text += '\n'.join([''] + [
				'  ' + option.formatMarkdownListItem(includeLabel)
				for option in self.menuOptions
			])
		return text

	def pullOptionsFromPar(self, par: Par):
		if not par.isMenu:
			return
		descriptions = {
			o.name: o.description
			for o in self.menuOptions
		}
		self.menuOptions = [
			MenuOptionHelp(
				name,
				label,
				descriptions.get(name)
			)
			for name, label in zip(par.menuNames, par.menuLabels)
		]

	@classmethod
	def extractFromPar(cls, par: Par):
		parHelp = cls(
			name=par.tupletName,
			label=par.label,
			summary=par.help if par.help != _defaultParamHelp else None,
		)
		if par.isMenu:
			parHelp.pullOptionsFromPar(par)
		return parHelp

	def toFrontMatterData(self):
		return cleanDict({
			'name': self.name,
			'label': self.label,
			'summary': self.summary,
			'regularHandling': self.regularHandling,
			'readOnlyHandling': self.readOnlyHandling,
			'menuOptions': [
				opt.toFrontMatterData()
				for opt in self.menuOptions
			],
		})

@dataclass
class VariableHelp:
	name: str | None = None
	label: str | None = None
	summary: str | None = None

	def formatMarkdownListItem(self, forBuild=False):
		text = f'* `{self.name}`'
		if forBuild and self.label:
			text += f' *{self.label}*'
		text += ': '
		if self.summary:
			text += f' {self.summary}'
		return text

	@classmethod
	def extractFromTable(cls, variableTable: DAT):
		if not variableTable:
			return []
		varHelps = []
		for i in range(1, variableTable.numRows):
			name = str(variableTable[i, 'localName'])
			varHelps.append(cls(
				name=name,
				label=str(variableTable[i, 'label'] or name),
			))
		return varHelps

	@classmethod
	def extractFromOpStateDict(cls, ropStateObj: dict):
		if not ropStateObj:
			return []
		variableObjs = ropStateObj.get('variables')
		if not variableObjs:
			return []
		return [
			cls(variableObj['localName'], variableObj['label'])
			for variableObj in variableObjs
		]

	def mergeFrom(self, other: 'VariableHelp'):
		if self.name != other.name:
			self.name = other.name
		if other.label and not self.label:
			self.label = other.label
		if other.summary and not self.summary:
			self.summary = other.summary

	def toFrontMatterData(self):
		return cleanDict({
			'name': self.name,
			'label': self.label or self.name,
			'summary': self.summary,
		})

@dataclass
class InputHelp:
	name: str | None = None
	label: str | None = None
	summary: str | None = None
	required: bool = False
	coordTypes: list[str] = field(default_factory=list)
	contextTypes: list[str] = field(default_factory=list)
	returnTypes: list[str] = field(default_factory=list)
	supportedVariables: list[str] = field(default_factory=list)
	supportedVariableInputs: list[str] = field(default_factory=list)
	inputHandler: COMP | None = None

	def formatMarkdownListItem(self, forBuild=False):
		text = f'* `{self.name}`'
		if forBuild and self.label:
			text += f' *{self.label}*'
		text += ': '
		if forBuild and self.required:
			text += ' **(Required)**'
		if self.summary:
			text += f' {self.summary}'
		return text

	@classmethod
	def extractFromInputHandler(cls, inputHandler: COMP, varHelps: list[VariableHelp]):
		info = InputInfo(inputHandler)
		varNames = info.supportedVariables
		if '*' in varNames:
			varNames = [varHelp.name for varHelp in varHelps]
		return cls(
			name=info.name,
			label=info.label,
			required=info.required,
			coordTypes=info.supportedCoordTypes,
			contextTypes=info.supportedContextTypes,
			returnTypes=info.supportedReturnTypes,
			supportedVariables=varNames,
			supportedVariableInputs=info.supportedVariableInputs,
			inputHandler=inputHandler,
		)

	def updateSupportedVariableInputs(self, inputHelps: list['InputHelp']):
		if '*' in self.supportedVariableInputs:
			self.supportedVariableInputs = [
				inHelp.name
				for inHelp in inputHelps
				if inHelp.name != self.name
			]

	def mergeFrom(self, other: 'InputHelp'):
		if self.name != other.name:
			self.name = other.name
		if other.label and not self.label:
			self.label = other.label
		self.required = other.required
		self.coordTypes = other.coordTypes
		self.contextTypes = other.contextTypes
		self.returnTypes = other.returnTypes
		self.inputHandler = self.inputHandler or other.inputHandler
		self.supportedVariables = other.supportedVariables
		self.supportedVariableInputs = other.supportedVariableInputs

	def toFrontMatterData(self):
		return cleanDict({
			'name': self.name,
			'label': self.label or self.name,
			'required': self.required or None,
			'coordTypes': self.coordTypes,
			'contextTypes': self.contextTypes,
			'returnTypes': self.returnTypes,
			'supportedVariables': self.supportedVariables,
			'supportedVariableInputs': self.supportedVariableInputs,
			'summary': self.summary,
		})

_ignorePars = 'Help', 'Inspect', 'Updateop'

def _shouldIgnorePar(par: Par):
	if par.name in _ignorePars:
		return True
	return par.style == 'Header' or par.readOnly

@dataclass
class ROPHelp:
	name: str | None = None
	summary: str | None = None
	detail: str | None = None
	opType: str | None = None
	category: str | None = None
	parameters: list[ROPParamHelp] = field(default_factory=list)
	inputs: list[InputHelp] = field(default_factory=list)
	variables: list[VariableHelp] = field(default_factory=list)
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	keywords: list[str] = field(default_factory=list)
	shortcuts: list[str] = field(default_factory=list)
	images: list[str] = field(default_factory=list)
	thumb: str | None = None

	@classmethod
	def extractFromROP(cls, rop: COMP):
		info = ROPInfo(rop)
		parTuples = [
			pt
			for pt in rop.customTuplets
			if not _shouldIgnorePar(pt[0])
		]
		parTuples.sort(key=lambda pt: (pt[0].page.index * 1000) + pt[0].order)
		ropHelp = cls.fromInfoOnly(info)
		ropHelp.parameters = [
			ROPParamHelp.extractFromPar(pt[0])
			for pt in parTuples
		]
		dat = info.helpDAT
		if dat:
			docText = dat.text
			ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(docText)
		return ropHelp

	@classmethod
	def fromInfoOnly(cls, info: ROPInfo):
		return cls(
			name=info.shortName,
			opType=info.opType,
			category=info.categoryName,
			isAlpha=info.isAlpha,
			isBeta=info.isBeta,
			isDeprecated=info.isDeprecated,
			keywords=list(sorted(info.keywords)),
			shortcuts=list(sorted(info.shortcuts)),
		)

	def formatMainText(self):
		parts = [
			self.summary,
			self.detail,
		]
		if self.parameters:
			parts += [
				'## Parameters',
				'\n'.join([
					parHelp.formatMarkdownListItem()
					for parHelp in self.parameters
					if parHelp.name not in _ignorePars
				])
			]
		if self.inputs:
			parts += [
				'## Inputs',
				'\n'.join([
					inHelp.formatMarkdownListItem()
					for inHelp in self.inputs
				])
			]
		if self.variables:
			parts += [
				'## Variables',
				'\n'.join([
					varHelp.formatMarkdownListItem()
					for varHelp in self.variables
				])
			]
		return _mergeMarkdownChunks(parts)

	def formatAsFullPage(self, ropInfo: ROPInfo):
		frontMatterData = _dumpYaml(cleanDict(self.toFrontMatterData(full=True)))
		header = f'''---
layout: operator
title: {ropInfo.shortName}
parent: {ropInfo.categoryName.capitalize()} Operators
grand_parent: Operators
permalink: /reference/operators/{ropInfo.categoryName}/{ropInfo.shortName}
redirect_from:
  - /reference/opType/{ropInfo.opType}/
{frontMatterData}
---
'''
		parts = [
			header,
			self.summary,
			self.detail,
		]
		return _mergeMarkdownChunks(parts)

	def toFrontMatterData(self, full: bool):
		if self.isDeprecated:
			status = 'deprecated'
		elif self.isAlpha:
			status = 'alpha'
		elif self.isBeta:
			status = 'beta'
		else:
			status = None
		summary = self.summary
		# this is a hacky workaround since the doc processing
		# in build is sort of a tangled mess
		if summary and summary.startswith('## '):
			summary = None
		obj = cleanDict(mergeDicts(
			{
				'name': self.name,
				'summary': summary,
			},
			{
				'detail': self.detail,
				'opType': self.opType,
				'category': self.category,
			} if full else None,
			{
				'status': status,
				'keywords': list(sorted(self.keywords)),
				'shortcuts': list(sorted(self.shortcuts)),
				'thumb': self.thumb,
			},
			{
				'inputs': [
					inHelp.toFrontMatterData()
					for inHelp in self.inputs
				],
				'parameters': [
					parHelp.toFrontMatterData()
					for parHelp in self.parameters
					if parHelp.name not in _ignorePars
				],
				'variables': [
					varHelp.toFrontMatterData()
					for varHelp in self.variables
				],
				'images': self.images or [],
			} if full else None,
		))
		if full:
			return {'op': obj}
		return obj

	def formatAsListItem(self):
		text = f'* [`{self.name}`]({self.name}/) - {self.summary or ""}'
		if self.isAlpha:
			text += ' *alpha*{: .label .status-alpha }'
		elif self.isBeta:
			text += ' *beta*{: .label .status-beta }'
		elif self.isDeprecated:
			text += ' *deprecated*{: .label .status-deprecated }'
		return text

	def replaceOrAddParam(self, name: str, paramHelp: 'ROPParamHelp | None'):
		for i in range(len(self.parameters)):
			if self.parameters[i].name == name:
				if paramHelp:
					self.parameters[i] = paramHelp
				else:
					del self.parameters[i]
				return
		self.parameters.append(paramHelp)

@dataclass
class CategoryHelp:
	name: str | None = None
	summary: str | None = None
	detail: str | None = None
	operators: list[ROPHelp] = field(default_factory=list)

	@classmethod
	def extractFromComp(cls, comp: COMP):
		info = CategoryInfo(comp)
		catHelp = cls(
			name=info.categoryName,
		)
		dat = info.helpDAT
		if dat:
			docText = dat.text
			catHelp.summary, catHelp.detail = _extractHelpSummaryAndDetail(docText)
		for rop in info.operators:
			catHelp.operators.append(ROPHelp.extractFromROP(rop))
		return catHelp

	def formatAsList(self):
		parts = [
			f'# {self.name.capitalize()} Operators',
			self.summary,
			self.detail,
			'\n'.join([
				ropHelp.formatAsListItem()
				for ropHelp in self.operators
			])
		]
		return _mergeMarkdownChunks(parts)

	def formatAsListPage(self):
		frontMatterData = _dumpYaml(self.toFrontMatterData())
		parts = [
			f'''---
layout: operatorCategory
title: {self.name.capitalize()} Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/{self.name}/
{frontMatterData}
---''',
			f'# {self.name.capitalize()} Operators',
			self.summary,
			self.detail,
		]
		return _mergeMarkdownChunks(parts) + '\n'

	def toFrontMatterData(self):
		return {
			'cat': cleanDict({
				'name': self.name,
				'summary': self.summary,
				'detail': self.detail,
				'operators': [
					opHelp.toFrontMatterData(full=False)
					for opHelp in self.operators
				],
			})
		}

@dataclass
class ToolkitInfo:
	toolkitVersion: str

	def toData(self):
		return {
			'toolkitVersion': self.toolkitVersion,
		}

	def formatAsDataFile(self):
		return _dumpYaml(self.toData())

def _extractHelpSummaryAndDetail(docText: str) -> tuple[str, str]:
	if not docText:
		return '', ''
	docText = docText.strip()
	docText = _stripFrontMatter(docText).strip()
	docText = _stripFirstMarkdownHeader(docText)
	if not docText:
		return '', ''
	parts = docText.split('\n\n', maxsplit=1)
	summary = parts[0]
	detail = ''
	if len(parts) > 1:
		detail = parts[1]
		if '## Parameters' in detail:
			detail = detail.split('## Parameters', maxsplit=1)[0]
		elif '## Inputs' in detail:
			detail = detail.split('## Inputs', maxsplit=1)[0]
		elif '## Variables' in detail:
			detail = detail.split('## variables', maxsplit=1)[0]
	return summary, detail

def _mergeMarkdownChunks(parts: list[str]):
	return '\n\n'.join([p for p in parts if p])

class OpDocManager:
	def __init__(self, rop: ROPInfo | OP | str):
		if isinstance(rop, str):
			rop = op(rop)
		if isinstance(rop, ROPInfo):
			self.rop = rop.rop
			self.info = rop
		else:
			self.info = ROPInfo(rop)
			self.rop = self.info.rop

	def _parseDAT(self):
		ropHelp = ROPHelp.fromInfoOnly(self.info)
		dat = self.info.helpDAT
		if not dat:
			return ropHelp
		docText = dat.text
		docText = docText.strip()
		docText = _stripFrontMatter(docText).strip()
		docText = _stripFirstMarkdownHeader(docText)
		sections = _parseMarkdownSections(docText, sectionNames=['Parameters', 'Inputs', 'Variables'])
		if '' in sections:
			ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(sections[''])
		if 'Parameters' in sections:
			self._parseParamListInto(ropHelp, sections['Parameters'])
		if 'Inputs' in sections:
			self._parseInputListInto(ropHelp, sections['Inputs'])
		if 'Variables' in sections:
			self._parseVariableListInto(ropHelp, sections['Variables'])
		return ropHelp

	def _writeToDAT(self, ropHelp: ROPHelp):
		text = ropHelp.formatMainText()
		dat = self.info.helpDAT
		if not dat:
			dat = self.rop.create(textDAT, 'help')
			dat.nodeY = self.info.opDef.nodeY + 500
			dat.nodeWidth = 350
			dat.nodeHeight = 175
			dat.par.language = 'text'
			dat.par.extension = 'md'
			self.info.helpDAT = dat
			if not dat.par.file and self.rop.par.externaltox:
				dat.par.file = self.rop.par.externaltox.eval().replace('.tox', '.md')
			RaytkTags.fileSync.apply(dat, True)
			dat.viewer = True
		dat.text = text

	@staticmethod
	def _formatMainText(ropHelp: ROPHelp):
		parts = [
			ropHelp.summary,
			ropHelp.detail,
		]
		if ropHelp.parameters:
			parts += [
				'## Parameters',
				'\n'.join([
					parHelp.formatMarkdownListItem()
					for parHelp in ropHelp.parameters
				])
			]
		if ropHelp.variables:
			parts += [
				'## Variables',
				'\n'.join([
					varHelp.formatMarkdownListItem()
					for varHelp in ropHelp.variables
				])
			]
		return _mergeMarkdownChunks(parts)

	@staticmethod
	def _parseParamListInto(ropHelp: ROPHelp, text: str):
		text = text.strip()
		if not text:
			return
		if '*' not in text:
			raise Exception('Invalid params section')
		items = _parseMarkdownListItems(text)
		for item in items:
			name, label, desc = _parseNamedListItem(item)
			if not name:
				raise Exception(f'Invalid param list item: {item!r}')
			if ' ' in name:
				name = name.replace(' ', '').capitalize()
			menuOpts = []
			if '\n  * ' in desc:
				desc, optionsText = desc.split('\n  * ', maxsplit=1)
				optionsText = '* ' + optionsText.replace('\n  * ', '\n* ')
				subItems = _parseMarkdownListItems(optionsText)
				for subItem in subItems:
					optName, optLabel, optDesc = _parseNamedListItem(subItem)
					menuOpts.append(
						MenuOptionHelp(
							optName,
							optLabel,
							optDesc,
						)
					)
			paramHelp = ROPParamHelp(
				name=name,
				label=label,
				summary=desc,
				menuOptions=menuOpts,
			)
			ropHelp.replaceOrAddParam(name, paramHelp)

	@staticmethod
	def _parseInputListInto(ropHelp: ROPHelp, text: str):
		text = text.strip()
		ropHelp.inputs.clear()
		if not text:
			return
		if '*' not in text:
			raise Exception('Invalid inputs section')
		items = _parseMarkdownListItems(text)
		for item in items:
			name, label, desc = _parseNamedListItem(item)
			if not name:
				raise Exception(f'Invalid input list item: {item!r}')
			if ' ' in name:
				name = name.replace(' ', '').capitalize()
			ropHelp.inputs.append(InputHelp(
				name,
				label,
				desc,
			))

	@staticmethod
	def _parseVariableListInto(ropHelp: ROPHelp, text: str):
		ropHelp.variables.clear()
		text = text.strip()
		if not text:
			return
		if '*' not in text:
			raise Exception('Invalid variables section')
		items = _parseMarkdownListItems(text)
		for item in items:
			name, label, desc = _parseNamedListItem(item)
			if not name:
				raise Exception(f'Invalid variable list item: {item!r}')
			ropHelp.variables.append(VariableHelp(name, label, desc))

	def _pullFromMissingParamsInto(self, ropHelp: ROPHelp):
		paramHelps = {
			paramHelp.name: paramHelp
			for paramHelp in ropHelp.parameters
		}
		for parTuplet in self.rop.customTuplets:
			if parTuplet[0].readOnly or parTuplet[0].name.startswith('Createref') or parTuplet[0].name.startswith('Creatersel'):
				continue
			name = parTuplet[0].tupletName
			helpText = parTuplet[0].help
			if helpText == _defaultParamHelp:
				helpText = ''
			paramHelp = paramHelps.get(name) or ROPParamHelp(name)
			paramHelp.label = parTuplet[0].label
			if helpText and not paramHelp.summary:
				paramHelp.summary = helpText
			if parTuplet[0].isMenu:
				paramHelp.pullOptionsFromPar(parTuplet[0])
			paramHelps[name] = paramHelp
		ropHelp.parameters = list(paramHelps.values())

	def _pullParamHandlingInto(self, ropHelp: ROPHelp):
		paramHelps = {
			paramHelp.name: paramHelp
			for paramHelp in ropHelp.parameters
		}
		paramTable = self.info.opDefPar.Paramgrouptable.eval()
		if not paramTable:
			return
		if paramTable.inputs:
			paramTable = paramTable.inputs[0]
		if not isinstance(paramTable, tableDAT):
			return
		tupletNamesByPartName = {
			par.name: par.tupletName
			for par in self.rop.customPars
		}
		processedTupletNames = set()
		for i in range(1, paramTable.numRows):
			names = tdu.expand(paramTable[i, 'names'].val)
			regularVal = str(paramTable[i, 'handling'] or '')
			readOnlyVal = str(paramTable[i, 'readOnlyHandling'] or '') or regularVal
			for name in names:
				tupletName = tupletNamesByPartName.get(name)
				if not tupletName or tupletName in processedTupletNames:
					continue
				processedTupletNames.add(tupletName)
				paramHelp = paramHelps.get(tupletName)
				if not paramHelp:
					continue
				paramHelp.regularHandling = regularVal
				paramHelp.readOnlyHandling = readOnlyVal

	def _pullFromMissingInputsInto(self, ropHelp: ROPHelp):
		inHelps = ropHelp.inputs
		for i, handler in enumerate(self.info.inputHandlers):
			extractedHelp = InputHelp.extractFromInputHandler(handler, ropHelp.variables)
			extractedHelp.updateSupportedVariableInputs(inHelps)
			if i < len(inHelps):
				inHelps[i].mergeFrom(extractedHelp)
			else:
				inHelps.append(extractedHelp)

	def _pullFromMissingVariablesInto(self, ropHelp: ROPHelp):
		if not self.info.isROP:
			return
		varHelps = {
			varHelp.name: varHelp
			for varHelp in ropHelp.variables
		}  # type: dict[str, VariableHelp]
		stateText = self.info.opStateText
		stateObj = json.loads(stateText)
		extractedVars = VariableHelp.extractFromOpStateDict(stateObj)
		debug('known vars: ', varHelps)
		debug('extracted vars: ', extractedVars)
		for extractedVar in extractedVars:
			if extractedVar.name in varHelps:
				varHelps[extractedVar.name].mergeFrom(extractedVar)
			else:
				varHelps[extractedVar.name] = extractedVar
		ropHelp.variables = list(varHelps.values())

	def setUpMissingParts(self):
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		self._pullParamHandlingInto(ropHelp)
		self._pullFromMissingVariablesInto(ropHelp)
		self._pullFromMissingInputsInto(ropHelp)
		self._writeToDAT(ropHelp)

	def _getRopParByTupletName(self, tupletName: str) -> Par | None:
		for parTuple in self.rop.customTuplets:
			if parTuple[0].tupletName == tupletName:
				return parTuple[0]

	def pushToParams(self):
		ropHelp = self._parseDAT()
		for parHelp in ropHelp.parameters:
			if not parHelp.summary:
				continue
			# Some TD builds don't yet support op.parTuple
			if hasattr(self.rop, 'parTuple'):
				parTuple = self.rop.parTuple[parHelp.name]
				if parTuple is not None:
					parTuple.help = parHelp.summary
			else:
				par = self._getRopParByTupletName(parHelp.name)
				if par is not None:
					par.help = parHelp.summary

	def _gatherImages(self, ropHelp: ROPHelp, imagesFolder: Path):
		folder = imagesFolder / f'reference/operators/{self.info.categoryName}'
		debug(f'checking images in {folder.absolute()}')
		images = list(folder.glob(self.info.shortName + '_*.png'))
		debug(f'for {self.rop}, found images: {images!r}')
		ropHelp.images = []
		for img in images:
			img = img.as_posix()
			if img.startswith('docs/'):
				img = img.replace('docs/', '', 1)
			if img.endswith('_thumb.png'):
				ropHelp.thumb = img
			else:
				ropHelp.images.append(img)

	def extractForBuild(self, imagesFolder: Path | None) -> ROPHelp:
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		self._pullParamHandlingInto(ropHelp)
		self._pullFromMissingInputsInto(ropHelp)
		# this is always present except in debug code
		if imagesFolder:
			self._gatherImages(ropHelp, imagesFolder)
		return ropHelp

	def formatForBuild(self, imagesFolder: Path | None) -> str:
		ropHelp = self.extractForBuild(imagesFolder)
		return ropHelp.formatAsFullPage(self.info)

def _parseMarkdownSections(text: str, sectionNames: list[str]) -> dict[str, str]:
	"""
	Splits apart markdown into blocks with titles using level 2 headers (`## Foo`)
	:return: dict of title -> body. There may be an empty title for the first section.
	"""
	text = text and text.strip()
	if not text:
		return {}
	if '## ' not in text:
		return {'': text}
	sections = []
	title = ''
	body = ''
	for line in text.splitlines(keepends=True):
		if line.startswith('## ') and line[3:].strip() in sectionNames:
			if body:
				sections.append((title, body.strip()))
			title = line[3:].strip()
			body = ''
		else:
			body += line
	if body:
		sections.append((title, body.strip()))
	return {
		section[0]: section[1]
		for section in sections
	}

# https://stackoverflow.com/questions/59515074/z-pcre-equivalent-in-javascript-regex-to-match-all-markdown-list-items
_listItemsPattern = re.compile(r'^(?:\d+\.|[*+-]) .*(?:\r?\n(?!(?:\d+\.|[*+-]) ).*)*', re.MULTILINE)
def _parseMarkdownListItems(text: str) -> list[str]:
	if not text:
		return []
	return _listItemsPattern.findall(text)

_namedListItemPattern = re.compile(
	r'^\s*\* `(?P<name>[\w ]+)`\s*(\*(?P<label>[\w\s]+)\*)?\s*([:-]\s+(?P<desc>.*)?)?', re.DOTALL)
def _parseNamedListItem(itemText: str) -> tuple[str, str, str]:
	match = _namedListItemPattern.match(itemText)
	if not match:
		return '', '', itemText.lstrip('* ')
	return match.group('name'), match.group('label') or '', match.group('desc') or ''

def _stripFirstMarkdownHeader(text: str):
	if not text:
		return ''
	if not text.startswith('# '):
		return text
	return text.split('\n', 1)[1].strip()

def _stripFrontMatter(text: str):
	if not text or not text.startswith('---'):
		return text or ''
	return text.split('---\n', maxsplit=2)[-1]

def _dumpYaml(obj):
	return yaml.dump(obj)
	# return mod.json.dumps(obj, indent='  ')
