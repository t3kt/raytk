import re
from typing import Dict, List, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildName():
	host = parent().par.Hostop.eval()
	if not host:
		return ''
	pathParts = host.path[1:].split('/')
	for i in range(len(pathParts)):
		if pathParts[i].startswith('_'):
			pathParts[i] = 'U' + pathParts[i][1:]
	name = '_'.join(pathParts)
	name = re.sub('_+', '_', name)
	if name.startswith('_'):
		name = 'o_' + name
	return name

def evaluateTypeProperty(par: 'Par', fieldName: str):
	if par != 'useinput':
		return str(par)
	raise NotImplementedError()

def extractInputNames(dat: 'DAT', inDats: List['DAT']):
	dat.clear()
	for inDat in inDats:
		name = str(inDat[1, 'name'] or '')
		dat.appendRow([f'inputName{inDat.digits}', name])

def mergeInputDefs(dat: 'DAT', inDats: List['DAT']):
	dat.clear()
	for inDat in inDats:
		if inDat.numRows < 2:
			continue
		if dat.numRows == 0:
			dat.appendRow(inDat.row(0))
		for row in range(1, inDat.numRows):
			# skip rows already added in an earlier input
			if dat[inDat[row, 0], 0] is None:
				dat.appendRow(inDat.row(row))
