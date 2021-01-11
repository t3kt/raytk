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
subComps += ops(
	'fieldVisualizer',
	'inspectorCore',
	'bufferInspector',
	'axisHelper',
	'opBasicInfoPanel',
	'shaderBuilderConfig',
	'shaderPanel',
	'*Camera',
	'functionGraphRender',
	'render2D',
	'raymarchRender3D',
)

for comp in subComps:
	context.reclone(comp)
	context.disableCloning(comp)
	context.detachTox(comp)
	for c in comp.findChildren(type=COMP):
		context.reclone(c)
		context.disableCloning(c)
		context.detachTox(c)

context.detachTox(inspector)
context.finishTask()
