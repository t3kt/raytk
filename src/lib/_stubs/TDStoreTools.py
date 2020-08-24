# This file and all related intellectual property rights are
# owned by Derivative Inc. ("Derivative").  The use and modification
# of this file is governed by, and only permitted under, the terms
# of the Derivative [End-User License Agreement]
# [https://www.derivative.ca/Agreements/UsageAgreementTouchDesigner.asp]
# (the "License Agreement").  Among other terms, this file can only
# be used, and/or modified for use, with Derivative's TouchDesigner
# software, and only by employees of the organization that has licensed
# Derivative's TouchDesigner software by [accepting] the License Agreement.
# Any redistribution or sharing of this file, with or without modification,
# to or with any other person is strictly prohibited [(except as expressly
# permitted by the License Agreement)].
#
# Version: 099.2017.30440.28Sep
#
# _END_HEADER_

# TDStoreTools

from collections.abc import MutableSet, MutableMapping, MutableSequence
from abc import ABCMeta, abstractmethod
from numbers import Number


class StorageManager(MutableMapping):
	def __init__(self, extension, ownerComp, storedItems=None,
				 restoreAllDefaults=False, sync=True, dictName=None,
				 locked=True):
		"""
		StorageManager manages a TDStoreTools.dependDict for ease of use in
			extensions.
		extension: the extension using this StorageManager
		ownerComp: the comp to manage storage for
		storedItems: a list of dictionaries in the form:
			{'name': itemName, 'default': defaultValue, 'readOnly': T/F,
				'property': T/F, 'dependable':T/F}

			if unspecified, defaultValue will be None.
			property defaults to True and decides whether to add item as a
				property of extension
			readOnly defaults to False and defines whether the created property
				is readOnly
			dependable defaults to False and determines if a container will be
				wrapped in a dependency. These are slower but will cause nodes
				that observe them to cook properly.
			capitalized properties can be promoted in the extension.
		restoreAllDefaults: if True, force all values to their default
		sync: if True, clear old items that are no longer defined and set to
			default value if they are new
		dictName: all stored data will go in this dict in storage. defaults to
			ownerComp.__class__.__name__ + 'Store'
		locked: if True, raise an exception if an attempt is made to add a value
			not defined in storedItems
		"""
		self._items = {}  # will be set up in setItems...
		# {'attrName': provided dict}
		# this is an internal list of item info and should
		# not be messed with lightly

		self.locked = False
		if isinstance(ownerComp, COMP):
			self.ownerComp = ownerComp
		else:
			raise TypeError('Invalid owner for StorageManager', ownerComp)
		self.extension = extension
		if dictName is None:
			dictName = extension.__class__.__name__ + 'Stored'
		if dictName in ownerComp.storage:
			self.storageDict = ownerComp.storage[dictName]
		else:
			self.storageDict = ownerComp.store(dictName, DependDict())
		setattr(extension, '_storageDict', self.storageDict)
		if storedItems is None:
			storedItems = []
		self._setItems(storedItems, sync=sync)
		if restoreAllDefaults:
			self.restoreAllDefaults()
		self.locked = locked

	def restoreAllDefaults(self):
		"""
		Restore all storage items to the default value defined during init.
		If no default value was defined, item will be set to None
		"""
		for item, info in self._items.items():
			self.storageDict[item] = info['default']

	def restoreDefault(self, storageItem):
		if storageItem in self._items:
			self.storageDict[storageItem] = self._items[storageItem]['default']

	def _sync(self, deleteOld=True):
		"""
		Create items in storage, make properties, and set to default if
		necessary. If deleteOld is True, delete stored items that aren't in item
		list.
		Should really only be done during initialization.
		"""
		if deleteOld:
			oldKeys = []
			for key in self.storageDict:
				if key not in self._items:
					oldKeys.append(key)
			for key in [key for key in self.storageDict
						if key not in self._items]:
				del self.storageDict[key]
		for key, info in self._items.items():
			if key not in self.storageDict:
				try:
					self[key] = info['default']
				except:
					import traceback;
					traceback.print_exc()
					print('Unable to create ' + info['name'],
						  'on', self.ownerComp, info['default'])
					raise
			else:
				# check to make sure 'dependable' flag hasn't changed:
				if info['dependable'] and not isinstance(self[key],
														 DependMixin):
					# re-setting causes dependability to be updated
					self.storageDict[key] = self.storageDict[key]
				elif not info['dependable'] and isinstance(self[key],
														   DependMixin):
					try:
						self[key] = self[key].getRaw()  # attempt to update
					except:
						print('Unable to update ' + info['name'],
							  'on', self.ownerComp, self[key])
						raise
			if info['property']:
				self._makeProperty(key, info['readOnly'])

	def _makeProperty(self, key, readOnly=False):
		"""
		Creates a property on ownerComp. Really should only be done during
		initialization.
		"""
		if not isinstance(key, str) or not key.isidentifier():
			raise ValueError('Invalid identifier in stored items', key,
							 self.ownerComp)
		# def getter(s):
		# 	return s.storage[self.dictName]
		# 	debug(id(self.storageDict),
		# 		  id(self.ownerComp.storage[self.dictName]))

		if readOnly:
			def setter(s, val):
				raise AttributeError("Can't set attribute", key, val,
									 self.ownerComp)
		else:
			def setter(s, val):
				s._storageDict[key] = val
		prop = property(lambda s: s._storageDict[key], setter)
		try:
			setattr(self.extension.__class__, key, prop)
		except:
			print('Unable to create', key, 'property on', self.extension)
			raise

	def _setItems(self, storedItems, sync=True):
		"""
		Create values in dictionary and set up item values if necessary.
		items is a list of lists or dicts just like in __init__
		If sync is True, perform a sync as well.
		"""
		oldItems = self._items.copy()
		self._items = {}
		for item in storedItems:
			self._addItem(item)
		for name, info in oldItems.items():
			if name not in self._items and info['property'] is False:
				# Watch out for this! Changing the ownerComp's class!
				delattr(self.ownerComp.__class__, name)
		if sync:
			self._sync()

	def _addItem(self, storageItem):
		"""
		Add an item to StorageManager. WARNING: all instances of an extension
		class will share the properties of that class!
		"""
		if isinstance(storageItem, dict) and storageItem.get('name', None):
			storageItem.setdefault('default', None)
			storageItem.setdefault('readOnly', False)
			storageItem.setdefault('property', True)
			storageItem.setdefault('dependable', False)
			self._items[storageItem['name']] = storageItem
		else:
			raise ValueError("StorageItems must be a list of dictionaries. See "
							 "StorageManager docs.", self.ownerComp)

	def _removeItem(self, itemName):
		"""
		Remove an item from StorageManager. WARNING: all instances of an
		extension class will share the properties of that class!
		"""
		if itemName in self._items:
			propertyType = self._items[itemName][1]
			if propertyType:
				delattr(self.ownerComp.__class__, itemName)
			del self._items[itemName]

	# Fake operation as dictionary

	def __getitem__(self, key):
		return self.storageDict[key]

	def __setitem__(self, key, val):
		if self.locked and key not in self.storageDict:
			raise KeyError("Can't create key in locked storage dictionary",
						   key, self.ownerComp)
		if self._items[key]['dependable']:
			self.storageDict[key] = val
		else:
			# allow dict, list, set to go in raw
			self.storageDict.setItem(key, val,
									 raw=isinstance(val, (dict, list, set)))

	def __delitem__(self, key):
		del self.storageDict[key]

	def __iter__(self):
		return iter(self.storageDict)

	def __len__(self):
		return len(self.storageDict)


# some basic functionalities in all our Depend collections
class DependMixin:
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		self.myMainDep = tdu.Dependency()
		self.parentDep = None

	@abstractmethod
	def getRaw(self):
		"""
		returns dependable with dependency wrappers removed
		"""
		self.myMainDep.val  # this has to be in your method definition

	def getDependencies(self):
		"""
		returns object with dependency wrappers intact
		"""
		return self.myItems

	def __len__(self):
		# try:
		# 	debug(self.myItems)
		# except:
		# 	pass
		self.myMainDep.val  # dummy for dependency
		return len(self.myItems)

	def __str__(self):
		self.myMainDep.val  # dummy for dependency
		# return str(self.myItems)
		return str(self.getRaw())

	def __repr__(self):
		self.myMainDep.val  # dummy for dependency
		return 'type: ' + self.__class__.__name__ + ' val: ' + str(self.myItems)

	def __iter__(self):
		self.myMainDep.val  # dummy for dependency
		return iter(self.myItems)

	def __contains__(self, item):
		self.myMainDep.val  # dummy for dependency
		return item in self.myItems

	def __del__(self):
		self.myMainDep.modified()

	def copy(self):
		return self.__class__(self.myItems)


class DependDict(DependMixin, MutableMapping):
	def __init__(self, *args, **kwargs):
		DependMixin.__init__(self)
		self.myItems = dict()
		self.update(dict(*args, **kwargs))  # use the free update to set keys

	@property
	def val(self):
		return self

	@val.setter
	def val(self, value):
		self.clear()
		try:
			self.clear()
			self.update(value)
			self.myMainDep.modified()
		except:
			print("DependDict.val can only be set to a dict")

	def getRaw(self, key=None):
		self.myMainDep.val
		if key is None:
			return {key: item.val.getRaw()
			if isinstance(item.val, DependMixin) else item.val
					for key, item in self.myItems.items()}
		if isinstance(self.myItems[key], DependMixin):
			return self.myItems[key].getRaw()
		else:
			return self.myItems[key].val

	def __getitem__(self, key):
		try:
			item = self.myItems[key]
			return item.val
		except:
			self.myMainDep.val  # dummy for dependency
			raise

	def getDependency(self, key):
		return self.myItems[key]

	def __setitem__(self, key, item):
		self.setItem(key, item)

	def setItem(self, key, item, raw=False):
		if key in self.myItems:
			if raw or isImmutable(item):
				self.myItems[key].val = item
				return
			else:
				self.myItems[key].modified()
		self.myMainDep.modified()
		newv = makeDependable(self, item, raw)
		self.myItems[key] = newv

	def clear(self):
		try:
			for i in self.myItems:
				i.modified()
		except:
			pass
		self.myMainDep.modified()
		self.myItems.clear()

	# def update(self, *args, **kwargs):
	# 	self.myItems.update(*args, **kwargs)

	def __delitem__(self, key):
		self.myMainDep.modified()
		self.myItems[key].modified()
		del self.myItems[key]


class DependList(DependMixin, MutableSequence):
	def __init__(self, arg=None):
		if arg is None:
			arg = []
		DependMixin.__init__(self)
		self.myItems = []
		for i in arg:
			self.append(i)

	@property
	def val(self):
		return self

	@val.setter
	def val(self, value):
		if isinstance(value, list):
			self.clear()
			for i in value:
				self.append(i)
			self.myMainDep.modified()
		else:
			raise TypeError("DependDict.val can only be set to a dict")

	def getRaw(self, index=None):
		self.myMainDep.val
		if index is None:
			return [item.val.getRaw() if isinstance(item.val, DependMixin)
					else item.val for item in self.myItems]
		if isinstance(self.myItems[index].val, DependMixin):
			return self.myItems[index].val.getRaw()
		else:
			return self.myItems[index].val

	def append(self, value, raw=False):
		self.insert(len(self.myItems), value, raw)

	def insert(self, index, item, raw=False):
		for i in range(index, len(self.myItems)):
			self.myItems[i].modified()
		self.myMainDep.modified()
		newitem = makeDependable(self, item, raw)
		self.myItems.insert(index, newitem)

	def __getitem__(self, index):
		try:
			item = self.myItems[index]
			return item.val
		except:
			self.myMainDep.val  # dummy for dependency
			raise

	def __setitem__(self, index, item):
		self.setItem(index, item)

	def setItem(self, index, item, raw=False):
		if 0 <= index < len(self.myItems):
			if raw or isImmutable(item):
				self.myItems[index].val = item
				return
			else:
				self.myItems[index].modified()
		self.myMainDep.modified()
		newv = makeDependable(self, item, raw)
		self.myItems[index] = newv

	def getDependency(self, index):
		return self.myItems[index]

	def __iter__(self):
		self.myMainDep.val  # dummy for dependency
		return iter([i.val for i in self.myItems])

	def clear(self):
		self.myMainDep.modified()
		self.myItems.clear()

	def __delitem__(self, index):
		for i in range(index, len(self.myItems)):
			self.myItems[i].modified()
		self.myMainDep.modified()
		del self.myItems[index]

	# def pop(self, *args, **kwargs):
	# 	self.myMainDep.modified()
	# 	return self.myItems.pop(*args, **kwargs)

class DependSet(DependMixin, MutableSet):
	"""
	DependSet is a bit different in that we don't need to convert items inside
	to dependencies.
	"""

	def __init__(self, *args, **kwargs):
		DependMixin.__init__(self)
		self.myItems = set(*args, **kwargs)

	@property
	def val(self):
		return self

	@val.setter
	def val(self, value):
		try:
			self.clear()
			self.myItems = value
			self.myMainDep.modified()
		except:
			print("DependSet.val set to bad value")

	def getRaw(self):
		self.myMainDep.val
		return self.myItems

	def add(self, item):
		if item in self.myItems:
			return
		self.myMainDep.modified()
		self.myItems.add(item)

	def discard(self, item):
		if item not in self.myItems:
			return
		self.myMainDep.modified()
		self.myItems.discard(item)

	def update(self, *args, **kwargs):
		self.myMainDep.modified()
		self.myItems.update(*args, **kwargs)

	def clear(self):
		self.myItems.clear()
		self.myMainDep.modified()


def isImmutable(item):
	if item is None:
		return True
	if isinstance(item, Number):
		return True
	if type(item) in (str, tuple, frozenset):
		return True
	return False


def makeDependable(parentDep, value, raw=False):
	if isImmutable(value):
		newv = value
	elif isinstance(value, (tdu.Vector, tdu.Matrix, tdu.Position)):
		newv = value
	elif raw and isinstance(value, (dict, list, set)):
		newv = value
	elif isinstance(value, dict):
		newv = DependDict(value)
		newv.parentDep = parentDep
	elif isinstance(value, list):
		newv = DependList(value)
		newv.parentDep = parentDep
	elif isinstance(value, set):
		newv = DependSet(value)
		newv.parentDep = parentDep
	elif isinstance(value, DependMixin):
		value.parentDep = parentDep
		newv = value
	elif type(value).__name__ in ['DependDict', 'DependList', 'DependSet']:
		value.parentDep = parentDep
		newv = value
	elif isinstance(value, tdu.Dependency):
		if isinstance(value.val, DependMixin):
			value.val.parentDep = parentDep
		elif type(value.val).__name__ in \
				['DependDict', 'DependList', 'DependSet']:
			value.val.parentDep = parentDep
		return value
	else:
		raise TypeError('Value can not be made dependable', value, type(value))
	return tdu.Dependency(newv)


def isImmutable(item):
	if item is None:
		return True
	if isinstance(item, Number):
		return True
	if type(item) in (str, tuple, frozenset):
		return True
	return False
