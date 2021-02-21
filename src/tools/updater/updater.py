from dataclasses import dataclass, field
from typing import Dict, List
from raytkUtil import ROPInfo, RaytkContext, Version, showMessageDialog

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Updater:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	# This MUST remain publicly available since OPs reference it for the `Updateop` par handler.
	def UpdateOP(self, o: 'COMP'):
		info = ROPInfo(o)
		if not info:
			self._showError(f'Unable to update {o}, it must be a ROP or RComp')
			return
		master = o.par.clone.eval()
		if not master:
			self._showError(f'Unable to update {o}, no clone master found')
			return
		self._log(f'Updating {o} using master {master}')
		o.par.enablecloningpulse.pulse()
		img = o.op('*Definition/opImage')
		if img:
			o.par.opviewer.val = img
			o.viewer = True

	def _showError(self, msg: str):
		self._log(msg)
		showMessageDialog(
			title='Warning',
			text=msg,
			escOnClickAway=True,
		)

	def _log(self, msg: str):
		print(self.ownerComp, msg)
		ui.status = msg

class _Updater:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.mappings = []   # type: List[Mapping]
		self.currentOpTypes = {}  # type: Dict[str, COMP]

	def loadSettings(self):
		migrations = self.ownerComp.op('opMigrations')
		self.mappings = [
			Mapping(
				str(migrations[i, 'fromOpType']),
				int(migrations[i, 'fromOpVersion']),
				Version(migrations[i, 'fromToolkitVersion']),
				str(migrations[i, 'toOpType']),
				int(migrations[i, 'toOpVersion']),
				Version(migrations[i, 'toToolkitVersion']),
			)
			for i in range(1, migrations.numRows)
		]
		opTypes = self.ownerComp.op('opTable')
		self.currentOpTypes = {
			str(opTypes[i, 'opType']): op(opTypes[i, 'path'])
			for i in range(1, opTypes.numRows)
		}

	@staticmethod
	def getSelectedOps() -> 'List[COMP]':
		return RaytkContext().currentROPs()

	def runMigration(self, validate=True, perform=False):
		self.loadSettings()
		rops = self.getSelectedOps()
		if not rops:
			return
		migration = Migration(
			RaytkContext().toolkit(), rops,
			validate=validate, perform=perform,
		)
		valid = True
		if validate:
			for o in rops:
				if not self.processOp(o, migration, validate=True, update=False):
					valid = False
		if perform and (valid or not validate):
			for o in rops:
				self.processOp(o, migration, validate=False, update=True)

	def processOp(self, o: 'OP', migration: 'Migration', validate: bool, update: bool) -> bool:
		ropInfo = ROPInfo(o)
		t = ropInfo.opType
		v = int(ropInfo.opVersion)
		master = self.currentOpTypes.get(t)
		pass

@dataclass
class Mapping:
	fromOpType: str
	fromOpVersion: int
	fromToolkitVersion: Version
	toOpType: str
	toOpVersion: int
	toToolkitVersion: Version

@dataclass
class Migration:
	toolkit: 'COMP'
	rops: 'List[COMP]' = field(default_factory=list)
	errors: 'List[str]' = field(default_factory=list)
	warnings: 'List[str]' = field(default_factory=list)
	validate: bool = True
	perform: bool = False

class MigrationHandler:
	def check(self, ropInfo: ROPInfo, migration: 'Migration') -> bool:
		pass

	def update(self, ropInfo: ROPInfo, migration: 'Migration'):
		pass
