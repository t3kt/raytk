from dataclasses import dataclass, field
from typing import Callable, List
from raytkUtil import getToolkit, ROPInfo, RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Updater:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def getSelectedOps() -> 'List[COMP]':
		return RaytkContext.currentROPs()

	def runMigration(self, validate=True, perform=False):
		rops = self.getSelectedOps()
		if not rops:
			return
		migration = Migration(
			getToolkit(), rops,
			validate=validate, perform=perform,
		)
		valid = True
		if validate:
			for o in rops:
				if not self.checkOp(o, migration):
					valid = False
		if perform and (valid or not validate):
			for o in rops:
				self.updateOp(o, migration)

	def checkOp(self, o: 'OP', migration: 'Migration') -> bool:
		pass

	def updateOp(self, o: 'OP', migration: 'Migration'):
		pass

@dataclass
class Migration:
	toolkit: 'COMP'
	rops: 'List[COMP]' = field(default_factory=list)
	errors: 'List[str]' = field(default_factory=list)
	warnings: 'List[str]' = field(default_factory=list)
	validate: bool = True
	perform: bool = False

MigrationHandler = Callable[['COMP', Migration], bool]
