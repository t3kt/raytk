from raytkUtil import RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	parent.guide = COMP()

class Navigator:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def buildNavItemTable(dat: 'DAT'):
		dat.clear()
		dat.appendRow(['path', 'relPath', 'label', 'level', 'indentedLabel'])
		for guide in parent.guide.findChildren(tags=[RaytkTags.guide.name], depth=1, maxDepth=1):
			title = str(guide.par['Title'] or guide.name)
			dat.appendRow([
				guide.path,
				parent.guide.relativePath(guide).replace('./', ''),
				title,
				'guide',
				f'Guide: {title}',
			])
			headers = guide.findChildren(tags=[RaytkTags.guideHeader.name], depth=1, maxDepth=1)
			headers.sort(key=lambda o: -o.nodeY)
			for header in headers:
				title = str(header.par.Text)
				level = tdu.digits(header.par.Headerlevel)
				dat.appendRow([
					header.path,
					parent.guide.relativePath(header).replace('./', ''),
					title,
					f'h{level}',
					('  ' * level) + ' ' + title,
				])
