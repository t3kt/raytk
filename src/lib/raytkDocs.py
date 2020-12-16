from dataclasses import dataclass, field
import re
from typing import Dict, Iterable, List, Optional, Tuple

from raytkUtil import ROPInfo, stripFirstMarkdownHeader, stripFrontMatter, \
	CategoryInfo

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
class ROPParamHelp:
	name: Optional[str] = None
	summary: Optional[str] = None

	def formatMarkdownListItem(self):
		text = f'* `{self.name}`'
		if self.summary:
			text += f': {self.summary}'
		return text

	@classmethod
	def extractFromPar(cls, par: 'Par'):
		return cls(
			par.tupletName,
			par.help if par.help != _defaultParamHelp else None,
		)

@dataclass
class ROPHelp:
	name: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None
	opType: Optional[str] = None
	category: Optional[str] = None
	parameters: List[ROPParamHelp] = field(default_factory=list)
	isAlpha: bool = False
	isBeta: bool = False

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
		)

	def formatAsMarkdown(self, headerOffset: int = 0):
		headerPrefix = '#' * headerOffset
		parts = [
			f'{headerPrefix}# {self.name}',
		]
		if self.isAlpha:
			parts.append('Alpha\n{: .label .label-purple }')
		elif self.isBeta:
			parts.append('Beta\n{: .label .label-yellow }')
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

	def formatAsFullPage(self, ropInfo: 'ROPInfo'):
		docText = self.formatAsMarkdown()
		docText = f'''---
layout: page
title: {ropInfo.shortName}
parent: {ropInfo.categoryName.capitalize()} Operators
grand_parent: Operators
permalink: /reference/operators/{ropInfo.categoryName}/{ropInfo.shortName}
---

{docText}
'''
		return docText

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

	def formatAsMarkdown(self):
		parts = [
			f'# {self.name}',
			self.summary,
			self.detail,
		]
		parts += [
			opHelp.formatAsMarkdown(headerOffset=1)
			for opHelp in self.operators
		]
		return _mergeMarkdownChunks(parts)

	def formatAsList(self):
		parts = [
			f'# {self.name.capitalize()} Operators',
			self.summary,
			self.detail,
			'\n'.join([
				f'* [`{ropHelp.name}`]({ropHelp.name}/) - {ropHelp.summary or ""}'
				for ropHelp in self.operators
			])
		]
		return _mergeMarkdownChunks(parts)

	def formatAsListPage(self):
		parts = [
			f'''---
layout: page
title: {self.name.capitalize()} Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/{self.name}/
---''',
			self.formatAsList(),
		]
		return _mergeMarkdownChunks(parts) + '\n'

def _extractHelpSummaryAndDetail(docText: str) -> 'Tuple[str, str]':
	if not docText:
		return '', ''
	docText = docText.strip()
	docText = stripFrontMatter(docText).strip()
	docText = stripFirstMarkdownHeader(docText)
	if not docText:
		return '', ''
	parts = docText.split('\n\n', maxsplit=1)
	summary = parts[0]
	detail = ''
	if len(parts) > 1:
		detail = parts[1]
		if '## Parameters' in detail:
			detail = detail.split('## Parameters', maxsplit=1)[0]
	return summary, detail

def _mergeMarkdownChunks(parts: Iterable[str]):
	return '\n\n'.join([p for p in parts if p])

class OpDocManager:
	def __init__(self, rop: 'COMP'):
		self.rop = rop
		self.info = ROPInfo(rop)

	def _parseDAT(self):
		ropHelp = ROPHelp.fromInfoOnly(self.info)
		dat = self.info.helpDAT
		if not dat:
			return ropHelp
		docText = dat.text
		docText = docText.strip()
		docText = stripFrontMatter(docText).strip()
		docText = stripFirstMarkdownHeader(docText)
		sections = _parseMarkdownSections(docText)
		if '' in sections:
			ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(sections[''])
		if 'Parameters' in sections:
			self._parseParamListInto(ropHelp, sections['Parameters'])
			pass
		if 'Inputs' in sections:
			raise NotImplementedError('Inputs section not yet supported')
		return ropHelp

	def _writeToDAT(self, ropHelp: 'ROPHelp'):
		dat = self.info.helpDAT
		if not dat:
			dat = self.rop.create(textDAT, 'help')
			self.info.helpDAT = dat
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
		dat.text = _mergeMarkdownChunks(parts)

	@staticmethod
	def _parseParamListInto(ropHelp: 'ROPHelp', paramsText: str):
		paramsText = paramsText.strip()
		if not paramsText:
			return
		if '*' not in paramsText:
			raise Exception('Invalid params section')
		items = _parseMarkdownListItems(paramsText)
		for item in items:
			name, desc = _extractNameAndDescriptionFromListItem(item)
			if not name:
				raise Exception(f'Invalid param list item: {item!r}')
			paramHelp = ROPParamHelp(
				name=name,
				summary=desc,
			)
			ropHelp.replaceOrAddParam(name, paramHelp)

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
			if helpText and not paramHelp.summary:
				paramHelp.summary = helpText

	def loadMissingParts(self):
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		self._writeToDAT(ropHelp)

	def pushToParams(self):
		ropHelp = self._parseDAT()
		for parHelp in ropHelp.parameters:
			if not parHelp.summary:
				continue
			parTuple = self.rop.parTuple[parHelp.name]
			if parTuple is not None:
				parTuple.help = parHelp.summary

	def formatForBuild(self) -> str:
		ropHelp = self._parseDAT()
		self._pullFromMissingParamsInto(ropHelp)
		return ropHelp.formatAsFullPage(self.info)

def _parseMarkdownSections(text: str) -> 'Dict[str, str]':
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
		if line.startswith('## '):
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

_namedListItemPattern = re.compile(r'^\* `(?P<name>\w+)`(:\s+(?P<desc>.*))?', re.DOTALL)
def _extractNameAndDescriptionFromListItem(itemText: str):
	match = _namedListItemPattern.match(itemText)
	if not match:
		return '', itemText.lstrip('* ')
	return match.group('name'), match.group('desc') or ''
