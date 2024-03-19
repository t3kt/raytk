# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from raytkBuild import BuildContext
	from libraryInfoExt import LibraryInfoBuilder
	ext.libraryInfo = LibraryInfoBuilder(COMP())

async def build(context: 'BuildContext'):
	context.log('Updating library info')
	context.safeDestroyOps(ops('write_*'))
	ext.libraryInfo.Forcebuild()
	context.lockOps(ops('opTable', 'opCategoryTable', 'versionInfo', 'opHelpTable', 'info_text'))
