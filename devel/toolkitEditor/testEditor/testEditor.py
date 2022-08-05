from pathlib import Path
from raytkUtil import showPromptDialog, navigateTo
from raytkTest import processTest
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor.ropEditor import ROPEditor
	from components.testInspectorCore.testInspectorCore import TestInspectorCore
	from editor.componentLoader.componentLoader import ComponentLoader
	ext.ropEditor = ROPEditor(COMP())
	# noinspection PyTypeHints
	iop.loader = ComponentLoader(COMP())
	# noinspection PyTypeChecker
	iop.testInspectorCore = TestInspectorCore(COMP())

	class _Par(ParCollection):
		Selectedrop: 'CompParamT'
		Selectedoptype: 'StrParamT'
		Testcasefolder: 'StrParamT'
		Snapshotsfolder: 'StrParamT'
		Sourcefolder: 'StrParamT'

	class _COMP(COMP):
		par: _Par

class TestEditor:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	@property
	def hostedComponent(self) -> 'Optional[COMP]':
		return iop.loader.Component

	@property
	def currentTestName(self):
		return iop.loader.ComponentName

	@property
	def formattedTestName(self):
		name = self.currentTestName
		if name:
			name = name.replace('_test', '').replace('_', ' ')
		return name

	@property
	def currentTox(self):
		return iop.loader.ComponentTox

	@staticmethod
	def _disableComponentCooking():
		comp = iop.loader.Component  # type: COMP
		if comp:
			comp.allowCooking = False

	def Unload(self):
		try:
			self._disableComponentCooking()
			iop.loader.UnloadComponent()
		except:
			pass
		self._reloadOutputsSoon()

	def Save(self):
		iop.loader.SaveComponent()
		msg = f'Saved to {self.currentTox}'
		print(msg)
		ui.status = msg

	def writeSnapshots(self):
		iop.testInspectorCore.WriteSnapshots(
			caseRootFolder=self.ownerComp.par.Testcasefolder.eval(),
			imagesRootFolder=self.ownerComp.par.Snapshotsfolder.eval(),
			sourceFolder=self.ownerComp.par.Sourcefolder.eval(),
		)

	def processTest(self):
		comp = self.hostedComponent
		if not comp:
			return
		processTest(comp, log=None)
		comp.clearScriptErrors(recurse=True)
		self.reloadOutputs()
		iop.testInspectorCore.GetFindings()

	def _loadTest(self, name: str, toxPath: Path):
		if name:
			name = name.replace(' ', '_')
			if not name.endswith('_test') and not name.endswith('_snippet'):
				name += '_test'
		self._disableComponentCooking()
		iop.loader.LoadComponent(tox=toxPath, name=name)
		self._reloadOutputsSoon()
		self.ownerComp.op('findingsPanel').cook(force=True)

	def createTest(self):
		self._create('test')

	def createSnippet(self):
		self._create('snippet')

	def _create(self, group: str):
		print(self.ownerComp, f'create {group}')
		info = ext.ropEditor.ROPInfo
		if not info:
			print(self.ownerComp, 'there is no rop')
			return
		if group == 'test':
			folder = Path(self.ownerComp.par.Testcasefolder.eval())
		elif group == 'snippet':
			folder = Path(self.ownerComp.par.Snippetfolder.eval())
		else:
			raise Exception(f'Invalid group: {group}')
		showPromptDialog(
			title='Create ' + group,
			text=group.upper() + ' name',
			default=info.shortName + '_' + group,
			textEntry=True,
			ok=lambda name: self._doCreate(name, group, folder),
		)

	def _doCreate(self, name: str, group: str, folder: Path, confirmed=False):
		info = ext.ropEditor.ROPInfo
		if not info:
			return
		name = name.replace(' ', '_')
		if name.endswith('.tox'):
			name = name.replace('.tox', '')
		if not name.endswith('_' + group):
			name += '_' + group
		toxPath = folder / 'operators' / info.categoryName / (name + '.tox')
		print(self.ownerComp, f'name: {name!r} toxPath: {toxPath!r}')
		if toxPath.exists() and not confirmed:
			showPromptDialog(
				title='Overwrite TOX',
				text=f'File {toxPath} exists. Replace it?',
				textEntry=False,
				ok=lambda _: self._doCreate(
					name, group, folder, confirmed=True),
			)
		else:
			iop.loader.CreateNewComponent(
				tox=toxPath,
				name=name,
				autoSave=True,
			)
			self._reloadOutputsSoon()

	def _reloadOutputsSoon(self):
		run('args[0]()', self.reloadOutputs, delayFrames=5, delayRef=root)

	def reloadOutputs(self):
		self.ownerComp.op('layout_test_outputs').cook(force=True)

	def listOnSelectRow(self, info: dict):
		# rowData = info['rowData']
		# print(self.ownerComp, 'listOnSelectRow', mod.json.dumps(rowData, indent='  '))
		pass

	def listOnClick(self, info: dict):
		rowData = info.get('rowData')
		rowObj = rowData and rowData.get('rowObject')
		print(self.ownerComp, 'listOnClick', mod.json.dumps(rowData, indent='  '))
		if not rowObj:
			return
		self.Unload()
		self._loadTest(rowObj['name'], Path(rowObj['path']))

	@staticmethod
	def showInEditor():
		comp = iop.loader.Component
		if not comp:
			return
		navigateTo(comp, goInto=True)
