from dataclasses import dataclass, field
import json
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.TreeListerExt import TreeListerExt
	from _typeAliases import *

	class _Par(ParCollection):
		Thumbsize: IntParamT
		Thumbroot: OPParamT
	class _COMP(panelCOMP):
		par: _Par

	class _UIStatePar(ParCollection):
		Showalpha: BoolParamT
		Showbeta: BoolParamT
		Showdeprecated: BoolParamT
		Showhelp: BoolParamT
		Showthumbs: BoolParamT
		Showstatuschips: BoolParamT
		Usedisplaycategories: BoolParamT
		Pinopen: BoolParamT

	ipar.uiState = _UIStatePar()
	from _stubs.TDCallbacksExt import CallbacksExt
	ext.callbacks = CallbacksExt(None)

class OpPicker2:
	def __init__(self, ownerComp: COMP):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.opTable = ownerComp.op('opTable')  # type: DAT

	def buildTreeTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'path', 'compPath', 'type', 'category', 'opType', 'status', 'thumb'])
		categoriesByName: dict[str, _CategoryItem] = {}
		useDisplayCategories = ipar.uiState.Usedisplaycategories
		showAlpha = ipar.uiState.Showalpha
		showBeta = ipar.uiState.Showbeta
		showDeprecated = ipar.uiState.Showdeprecated
		for row in range(1, self.opTable.numRows):
			opItem = _OpItem(
				shortName=self.opTable[row, 'name'].val,
				opType=self.opTable[row, 'opType'].val,
				compPath=self.opTable[row, 'path'].val,
				category=self.opTable[row, 'category'].val,
				displayCategory=self.opTable[row, 'displayCategory'].val or None,
				isAlpha=self.opTable[row, 'status'] == 'alpha',
				isBeta=self.opTable[row, 'status'] == 'beta',
				isDeprecated=self.opTable[row, 'status'] == 'deprecated',
			)
			thumb = self.opTable[row, 'thumb'].val
			if thumb:
				opItem.thumbPath = op.raytk.op(thumb).path
			if opItem.isAlpha:
				opItem.status = 'alpha'
				if not showAlpha:
					continue
			elif opItem.isBeta:
				opItem.status = 'beta'
				if not showBeta:
					continue
			elif opItem.isDeprecated:
				opItem.status = 'deprecated'
				if not showDeprecated:
					continue
			else:
				opItem.status = ''
			if useDisplayCategories:
				catName = opItem.displayCategory or opItem.category
			else:
				catName = opItem.category
			if catName not in categoriesByName:
				categoriesByName[catName] = _CategoryItem(name=catName)
			categoriesByName[catName].ops.append(opItem)
		for catName in sorted(categoriesByName.keys()):
			catItem = categoriesByName[catName]
			dat.appendRow([catItem.name, catItem.name, '', 'category', '', '', ''])
			for opItem in sorted(catItem.ops, key=lambda x: x.shortName):
				dat.appendRow([
					opItem.shortName,
					f"{catItem.name}/{opItem.shortName}",
					opItem.compPath,
					'op',
					catItem.name,
					opItem.opType,
					opItem.status,
					opItem.thumbPath,
				])

@dataclass
class _OpItem:
	shortName: str
	opType: str
	compPath: str
	category: str
	displayCategory: str | None
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	status: str = ''
	thumbPath: str | None = None

@dataclass
class _CategoryItem:
	name: str
	ops: list[_OpItem] = field(default_factory=list)
