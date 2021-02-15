# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildSupportTable(
		support: 'scriptDAT',
		top: 'glslTOP',
		info: 'infoDAT'):
	support.clear()
	support.appendRow(['include', 0])
	textSources = [
		top.compileResult,
		info.text,
		top.warnings(),
	]
	if not any([_hasIncludeError(text) for text in textSources]):
		support['include', 1] = 1

_includeErrorTags = [
	'error C7529',
	'OpenGL does not allow #include directives',
	'#include statements are not supported',
]

def _hasIncludeError(result: str):
	if not result:
		return False
	for tag in _includeErrorTags:
		if tag in result:
			return True
	return False
