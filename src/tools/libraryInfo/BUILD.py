# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from raytkBuild import BuildTaskContext
	from .libraryInfoExt import LibraryInfoBuilder
	ext.libraryInfo = LibraryInfoBuilder(COMP())


context = args[0]  # type: BuildTaskContext

context.log('Updating library info')
context.safeDestroyOps(ops('write_*'))
ext.libraryInfo.Forcebuild()
context.lockOps(ops('opTable', 'opCategoryTable', 'versionInfo', 'opHelpTable', 'info_text'))
context.finishTask()
