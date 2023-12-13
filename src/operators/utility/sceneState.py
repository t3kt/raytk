# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def updateLockStates(locked: bool):
	sceneRoot = parent().par.Sceneroot.eval()   # type: COMP
	if not sceneRoot:
		return
	tags = tdu.split(parent().par.Searchtags.eval())
	if parent().par.Includeallrops:
		tags.append('raytkOP')
	for o in sceneRoot.findChildren(type=COMP, depth=1, maxDepth=1, tags=tags):
		_updateLockState(o, locked)

# structure of state data:
# 'raytkState': {'lockPars': ['Foo', 'Xyz']}

def _updateLockState(o: 'OP', locked: bool):
	state = o.fetch('raytkState', None, search=False, storeDefault=False) or {}
	if locked:
		lockPars = state.get('lockPars') or []
		for tuplet in o.customTuplets:
			if _ignorePar(tuplet[0]):
				continue
			if tuplet[0].tupletName in lockPars:
				tuplet[0].readOnly = True
	else:
		lockPars = []
		for tuplet in o.customTuplets:
			if _ignorePar(tuplet[0]):
				continue
			if tuplet[0].readOnly:
				lockPars.append(tuplet[0].tupletName)
				tuplet[0].readOnly = False
		lockPars.sort()
		state['lockPars'] = lockPars
		o.store('raytkState', state)

def _ignorePar(par: Par):
	return par.isOP or par.page.name == 'Info'
