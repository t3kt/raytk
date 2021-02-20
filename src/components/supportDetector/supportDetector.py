# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildSupportTable(
		support: 'scriptDAT',
		top: 'glslTOP'):
	support.clear()
	support.appendRow([
		'include',
		int(_supportsInclude(top)),
	])

def _supportsInclude(top: 'glslTOP'):
	# See issue #34.
	# It's hard to predict what wording every GPU driver is going to use to indicate the error
	# so instead of looking for anything specific, just consider any warning on that op as an
	# indication that includes aren't supported.
	if top.warnings():
		return False
	return True
