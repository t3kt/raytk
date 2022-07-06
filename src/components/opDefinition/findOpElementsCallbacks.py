# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List

def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	page.appendStr('Elements')

def onCook(dat: 'DAT'):
	dat.clear()
	dat.appendRow([
		'relPath',
		'paramGroupTable', 'macroTable',
		'placeholder1', 'code1', 'placeholder2', 'code2', 'placeholder3', 'code3', 'placeholder4', 'code4',
	])
	elements = dat.par.Elements.evalOPs()  # type: List[OP]
	for element in elements:
		dat.appendRow([
			dat.relativePath(element),
			element.par['Paramgrouptable'] or '',
			element.par['Macrotable'] or '',
			element.par['Placeholder1'] or '',
			element.par['Code1'] or '',
			element.par['Placeholder2'] or '',
			element.par['Code2'] or '',
			element.par['Placeholder3'] or '',
			element.par['Code3'] or '',
			element.par['Placeholder4'] or '',
			element.par['Code4'] or '',
		])
