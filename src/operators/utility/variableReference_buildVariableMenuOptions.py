import json

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	source = parent().par.Source.eval()
	if not source:
		dat.appendRow(['', ''])
		return
	stateTextDat = source.op('opDefinition/opState')
	stateText = stateTextDat and stateTextDat.text
	stateObj = stateText and json.loads(stateText)
	variableObjs = stateObj and stateObj.get('variables')
	if not variableObjs:
		dat.appendRow(['', ''])
		return
	for variableObj in variableObjs:
		name = variableObj['localName']
		label = variableObj['label']
		dataType = variableObj['dataType']
		dat.appendRow([name, f'{label} ({dataType})'])
