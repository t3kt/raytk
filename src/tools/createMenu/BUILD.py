# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext

context = args[0]  # type: BuildTaskContext

createMenu = parent()
createMenu.ClearFilter()
createMenu.par.Devel.expr = ''
createMenu.par.Devel = False
createMenu.par.Devel.readOnly = True
context.resetCustomPars(iop.createMenuState)

context.detachTox(createMenu)

context.finishTask()
