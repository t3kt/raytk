from typing import List
from pathlib import Path

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	op.raytk = COMP()

class AutoLoader:
	def __init__(self, folderComp: 'COMP'):
		self.folderComp = folderComp

	def setUpParameters(self):
		if not self.folderComp.par.externaltox:
			ui.status = f'Component does not have a tox, so auto-load does not apply: {self.folderComp}'
			return
		ui.undo.startBlock(f'Add auto-load parameters to {self.folderComp}')
		page = self.folderComp.appendCustomPage('Auto Load')
		if not self.folderComp.par['Autoloadfolder']:
			p = page.appendFolder('Autoloadfolder', label='Auto Load Folder')[0]
			toxPath = self.folderComp.par.externaltox.eval()
			if toxPath:
				p.val = Path(toxPath).parent.as_posix() + '/'
		if self.folderComp.par['Autoloaddeletemissing'] is None:
			page.appendToggle('Autoloaddeletemissing', label='Delete Missing Components')
		if self.folderComp.par['Autoloadalwaysreloadall'] is None:
			page.appendToggle('Autoloadalwaysreloadall', label='Always Reload All')
		ui.undo.endBlock()

	def applyAutoLoad(self):
		print(f'Applying auto load to {self.folderComp}')
		if not self.folderComp.par['Autoloadfolder']:
			return
		folder = self.folderComp.par.Autoloadfolder.eval()
		folderPath = Path(folder)
		if not folderPath.exists() or not folderPath.is_dir():
			raise Exception(f'Invalid auto-load folder: {folder!r}')
		parentToxPath = Path(self.folderComp.par.externaltox.eval()).as_posix()
		deleteMissing = bool(self.folderComp.par['Autoloaddeletemissing'])
		alwaysReload = bool(self.folderComp.par['Autoloadalwaysreloadall'])

		currentCompsByTox = {
			Path(c.par.externaltox.eval()).as_posix(): c
			for c in self.folderComp.findChildren(type=COMP, maxDepth=1)
			if c.par.externaltox
		}

		toxPaths = [
			p.as_posix()
			for p in sorted(folderPath.glob('*.tox'))
			if p.as_posix() != parentToxPath
		]
		print(f'Auto load found current comps:')
		for t, c in currentCompsByTox.items():
			print(f'   {c} : {t}')
		print(f'Auto load found toxes:')
		for t in toxPaths:
			print(f'   {t}')

		toDelete = []  # type: List[COMP]
		toxsToLoad = []  # type: List[str]

		if alwaysReload:
			toDelete = list(currentCompsByTox.values())
			toxsToLoad = list(toxPaths)
		else:
			if deleteMissing:
				toDelete = [
					comp
					for tox, comp in currentCompsByTox.items()
					if tox not in toxPaths
				]
			toxsToLoad = [
				tox
				for tox in toxPaths
				if tox not in currentCompsByTox
			]

		# print(f'Auto load for {self.folderComp} will destroy:')
		# print('\n'.join([c.name for c in toDelete]))
		# print('and will load:')
		# print('\n'.join(toxsToLoad))

		ui.undo.startBlock(f'Applying auto load in {self.folderComp}')

		for child in toDelete:
			print(f'Auto load is removing {child}')
			try:
				child.destroy()
			except:
				pass

		for i, tox in enumerate(toxsToLoad):
			print(f'Auto load is loading {tox}')
			comp = self.folderComp.loadTox(tox)
			comp.nodeY = 500 - i * 150

		ui.undo.endBlock()

