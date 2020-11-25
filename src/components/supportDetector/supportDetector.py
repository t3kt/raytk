# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildSupportTable(
		support: 'scriptDAT',
		top: 'glslTOP'):
	support.clear()
	support.appendRow(['include', 0])
	result = top.compileResult
	if not result:
		return
	if not _hasIncludeError(result):
		support['include', 1] = 1

_includeErrorTags = [
	'error C7529',
	'OpenGL does not allow #include directives',
	'#include statements are not supported',
]

def _hasIncludeError(result: str):
	for tag in _includeErrorTags:
		if tag in result:
			return True
	return False
