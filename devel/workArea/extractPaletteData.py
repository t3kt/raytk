from raytkUtil import RaytkContext, cleanDict
import json

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.opPicker.opPicker import OpPicker, PickerCategoryItem, PickerOpItem

def onCook(dat: 'DAT'):
	dat.clear()

	picker = op.raytk.op('tools/palette/opPicker').ext.opPicker  # type: OpPicker
	library = picker.impl.itemLibrary
	ctx = RaytkContext()
	categories = [
		categoryToObj(catItem) for catItem in library.categories
	]
	data = {
		'toolkitVersion': str(ctx.toolkitVersion()),
		'categories': categories
	}
	text = json.dumps(data, indent='  ')
	dat.write(text)

def categoryToObj(catItem: 'PickerCategoryItem'):
	return cleanDict({
		'shortName': catItem.shortName,
		'helpSummary': catItem.helpSummary,
		'operators': [
			operatorToObj(opItem) for opItem in catItem.ops]
	})

def operatorToObj(opItem: 'PickerOpItem'):
	return cleanDict({
		'shortName': opItem.shortName,
		'helpSummary': opItem.helpSummary,
		'status': opItem.status,
		'opType': opItem.opType,
		'keywords': opItem.keywords,
		'shortcuts': opItem.shortcuts,
		'thumbPath': opItem.thumbPath,
	})
