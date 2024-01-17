from raytkUtil import isROP, RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from .inspectorExt import Inspector
	from _stubs import *

context = args[0]  # type: BuildTaskContext

context.log('Processing inspector')

inspector = parent()  # type: COMP | Inspector
inspector.Reset()

subComps = inspector.findChildren(type=COMP, tags=[RaytkTags.raytkOP.name, RaytkTags.raytkComp.name], maxDepth=1)
subComps += ops(
	'fieldVisualizer',
	'inspectorCore',
	'bufferInspector',
	'opBasicInfoPanel',
	'shaderBuilderConfig',
	'shaderPanel',
	'*Camera',
	'functionGraphRender',
	'render2D',
	'raymarchRender3D',
)
context.log(f'Found {len(subComps)} child components in inspector')

for comp in subComps:
	context.log(f'Processing inspector child: {comp}')
	context.updateOrReclone(comp)
	context.disableCloning(comp)
	context.detachTox(comp)
	context.log(f'Processing sub-components in {comp}')
	for c in comp.findChildren(type=COMP):
		context.disableCloning(c)
		context.detachTox(c)
		if isROP(c):
			context.updateROPInstance(c)
		else:
			# reclone?
			pass
	context.log(f'Finished processing inspector child {comp}')
context.log('Finished processing inspector child components')

context.detachTox(inspector)
context.log('Finished processing inspector')
context.finishTask()
