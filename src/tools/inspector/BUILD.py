from raytkUtil import RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from .inspectorExt import Inspector
	from typing import Union
	from _stubs import *

context = args[0]  # type: BuildTaskContext

inspector = parent()  # type: Union[COMP, Inspector]
inspector.Reset()

subComps = inspector.findChildren(type=COMP, tags=[RaytkTags.raytkOP.name], maxDepth=1)
subComps += ops('fieldVisualizer', 'inspectorCore', 'bufferInspector', 'axisHelper')

for comp in subComps:
	context.reclone(comp)
	context.disableCloning(comp)

context.detachTox(inspector)
context.finishTask()
