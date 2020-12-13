from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Tuple

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
	label: Optional[str] = None
	summary: Optional[str] = None

	def formatMarkdownListItem(self):
		text = f'* {self.label} (`{self.name}`)'
		if self.summary:
			text += f': {self.summary}'
		return text

	@classmethod
	def extractFromPar(cls, par: 'Par'):
		return cls(
			par.tupletName,
			par.label,
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
		ropHelp = cls(
			name=info.shortName,
			opType=info.opType,
			category=info.categoryName,
			isAlpha=info.isAlpha,
			isBeta=info.isBeta,
			parameters=[
				ROPParamHelp.extractFromPar(pt[0])
				for pt in parTuples
			],
		)
		ropHelp.summary, ropHelp.detail = _extractHelpSummaryAndDetail(info.helpDAT)
		return ropHelp

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
		catHelp.summary, catHelp.detail = _extractHelpSummaryAndDetail(info.helpDAT)
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

def _extractHelpSummaryAndDetail(dat: 'DAT') -> 'Tuple[str, str]':
	docText = (dat.text if dat else '').strip()
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
