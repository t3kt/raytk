from dataclasses import dataclass, field
import re
from typing import Dict, Iterable, List, Optional, Tuple
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
	name: Optional[str] = None
	label: Optional[str] = None
	description: Optional[str] = None

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
	name: Optional[str] = None
	label: Optional[str] = None
	summary: Optional[str] = None
	menuOptions: List[MenuOptionHelp] = field(default_factory=list)

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

	def pullOptionsFromPar(self, par: 'Par'):
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
	def extractFromPar(cls, par: 'Par'):
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
			'menuOptions': [
				opt.toFrontMatterData()
				for opt in self.menuOptions
			],
		})

@dataclass
class InputHelp:
	name: Optional[str] = None
	label: Optional[str] = None
	summary: Optional[str] = None
	required: bool = False
	coordTypes: List[str] = field(default_factory=list)
	contextTypes: List[str] = field(default_factory=list)
	returnTypes: List[str] = field(default_factory=list)

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
	def extractFromInputHandler(cls, inputHandler: 'COMP'):
		info = InputInfo(inputHandler)
		return cls(
			name=info.name,
			label=info.label,
			summary=info.helpText,
			required=info.required,
			coordTypes=info.supportedCoordTypes,
			contextTypes=info.supportedContextTypes,
			returnTypes=info.supportedReturnTypes,
		)

	def mergeFrom(self, other: 'InputHelp'):
		if self.name != other.name:
			self.name = other.name
		if other.label and not self.label:
			self.label = other.label
		self.required = other.required
		self.coordTypes = other.coordTypes
		self.contextTypes = other.contextTypes
		self.returnTypes = other.returnTypes

	def toFrontMatterData(self):
		return cleanDict({
			'name': self.name,
			'label': self.label or self.name,
			'required': self.required or None,
			'coordTypes': self.coordTypes,
			'contextTypes': self.contextTypes,
			'returnTypes': self.returnTypes,
			'summary': self.summary,
		})

_ignorePars = 'Help', 'Inspect', 'Updateop'

@dataclass
class ROPHelp:
	name: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None
	opType: Optional[str] = None
	category: Optional[str] = None
	parameters: List[ROPParamHelp] = field(default_factory=list)
	inputs: List[InputHelp] = field(default_factory=list)
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	keywords: List[str] = field(default_factory=list)

	@classmethod
	def extractFromROP(cls, rop: 'COMP'):
		info = ROPInfo(rop)
		parTuples = [
			pt
			for pt in rop.customTuplets
			if not pt[0].readOnly
		]
		parTuples.sort(key=lambda pt: (pt[0].page.index * 1000) + pt[0].order)
		ropHelp = cls.fromInfoOnly(info)
		ropHelp.parameters = [
			ROPParamHelp.extractFromPar(pt[0])
			for pt in parTuples
			if pt[0].name not in _ignorePars
		]
		dat = info.helpDAT
		if dat:
			docText = dat.text
			ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(docText)
		return ropHelp

	@classmethod
	def fromInfoOnly(cls, info: 'ROPInfo'):
		return cls(
			name=info.shortName,
			opType=info.opType,
			category=info.categoryName,
			isAlpha=info.isAlpha,
			isBeta=info.isBeta,
			isDeprecated=info.isDeprecated,
			keywords=list(sorted(info.keywords)),
		)

	def formatAsMarkdown(self, headerOffset: int = 0):
		headerPrefix = '#' * headerOffset
		parts = [
			f'{headerPrefix}# {self.name}',
		]
		if self.isAlpha:
			parts.append('alpha\n{: .label .status-alpha }')
		elif self.isBeta:
			parts.append('beta\n{: .label .status-beta }')
		elif self.isDeprecated:
			parts.append('deprecated\n{: .label .status-deprecated }')
		parts += [
			self.summary,
			self.detail,
		]
		if self.parameters:
			parts += [
				'## Parameters',
				'\n'.join([
					parHelp.formatMarkdownListItem()
					for parHelp in self.parameters
				])
			]
		return _mergeMarkdownChunks(parts)

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
		return _mergeMarkdownChunks(parts)

	def formatAsFullPage(self, ropInfo: 'ROPInfo'):
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
		obj = cleanDict(mergeDicts(
			{
				'name': self.name,
				'summary': self.summary,
			},
			{
				'detail': self.detail,
				'opType': self.opType,
				'category': self.category,
			} if full else None,
			{
				'status': status,
				'keywords': list(sorted(self.keywords)),
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

	def replaceOrAddParam(self, name: str, paramHelp: 'Optional[ROPParamHelp]'):
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
	name: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None
	operators: List[ROPHelp] = field(default_factory=list)

	@classmethod
	def extractFromComp(cls, comp: 'COMP'):
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

def _extractHelpSummaryAndDetail(docText: str) -> 'Tuple[str, str]':
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
	return summary, detail

def _mergeMarkdownChunks(parts: Iterable[str]):
	return '\n\n'.join([p for p in parts if p])

class OpDocManager:
	def __init__(self, rop: 'Union[ROPInfo, OP, str]'):
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
		sections = _parseMarkdownSections(docText, sectionNames=['Parameters', 'Inputs'])
		if '' in sections:
			ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(sections[''])
		if 'Parameters' in sections:
			self._parseParamListInto(ropHelp, sections['Parameters'])
			pass
		if 'Inputs' in sections:
			self._parseInputListInto(ropHelp, sections['Inputs'])
		return ropHelp

	def _writeToDAT(self, ropHelp: 'ROPHelp'):
		text = ropHelp.formatMainText()
		dat = self.info.helpDAT
		if not dat:
			dat = self.rop.create(textDAT, 'help')
			dat.nodeY = self.info.opDef.nodeY + 500
			dat.nodeWidth = 350
			dat.nodeHeight = 175
			self.info.helpDAT = dat
			if not dat.par.file and self.rop.par.externaltox:
				dat.par.file = self.rop.par.externaltox.eval().replace('.tox', '.md')
			RaytkTags.fileSync.apply(dat, True)
			dat.viewer = True
		dat.text = text

	@staticmethod
	def _formatMainText(ropHelp: 'ROPHelp'):
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
		return _mergeMarkdownChunks(parts)

	@staticmethod
	def _parseParamListInto(ropHelp: 'ROPHelp', text: str):
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
	def _parseInputListInto(ropHelp: 'ROPHelp', text: str):
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
				raise Exception(f'Invalid param list item: {item!r}')
			if ' ' in name:
				name = name.replace(' ', '').capitalize()
			ropHelp.inputs.append(InputHelp(
				name,
				label,
				desc,
			))

	def _pullFromMissingParamsInto(self, ropHelp: 'ROPHelp'):
		paramHelps = {
			paramHelp.name: paramHelp
			for paramHelp in ropHelp.parameters
		}
		for parTuplet in self.rop.customTuplets:
			if parTuplet[0].readOnly:
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

	def _pullFromMissingInputsInto(self, ropHelp: 'ROPHelp'):
		inHelps = ropHelp.inputs
		for i, handler in enumerate(self.info.inputHandlers):
			extractedHelp = InputHelp.extractFromInputHandler(handler)
			if i < len(inHelps):
				inHelps[i].mergeFrom(extractedHelp)
			else:
				inHelps.append(extractedHelp)

	def setUpMissingParts(self):
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		self._pullFromMissingInputsInto(ropHelp)
		self._writeToDAT(ropHelp)

	def _getRopParByTupletName(self, tupletName: str) -> 'Optional[Par]':
		for parTuple in self.rop.customTuplets:
			if parTuple[0].tupletName == tupletName:
				return parTuple[0]

	def pushToParamsAndInputs(self):
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
		for inHelp in ropHelp.inputs:
			if not inHelp.label:
				continue
			inOp = self.rop.op(inHelp.name)
			if inOp:
				inOp.par.label = inHelp.label

	def formatForBuild(self) -> str:
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		self._pullFromMissingInputsInto(ropHelp)
		return ropHelp.formatAsFullPage(self.info)

def _parseMarkdownSections(text: str, sectionNames: List[str]) -> 'Dict[str, str]':
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
def _parseMarkdownListItems(text: str) -> 'List[str]':
	if not text:
		return []
	return _listItemsPattern.findall(text)

_namedListItemPattern = re.compile(
	r'^\s*\* `(?P<name>[\w ]+)`\s*(\*(?P<label>[\w\s]+)\*)?\s*([:-]\s+(?P<desc>.*)?)?', re.DOTALL)
def _parseNamedListItem(itemText: str) -> 'Tuple[str, str, str]':
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
