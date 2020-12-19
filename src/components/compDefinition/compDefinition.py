import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Union
	from raytkUtil import CompDefParsT

def parentPar() -> 'Union[ParCollection, CompDefParsT]':
	return parent().par

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
	return 'RTK_' + name

def inspect():
	for o in parentPar().Rops.evalOPs():
		par = o.par['Inspect']
		if par is not None:
			par.pulse()
			return

def _useLocalHelp():
	return hasattr(op, 'raytk') and bool(op.raytk.par['Devel'])

def launchHelp():
	url = parentPar().Helpurl.eval()
	if not url:
		return
	if _useLocalHelp():
		url = url.replace('https://t3kt.github.io/raytk/', 'http://localhost:4000/raytk/')
	if url:
		ui.viewFile(url)
