from typing import List, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def simplifyNames(fullNames: List[Union[str, 'Cell']], sep='_'):
	"""
	Removes prefixes shared by all the provided names.

	For example, ["FOO_x", "FOO_abc", "FOO_asdf"] would produce ["x", "abc", "asdf"]
	"""
	if not fullNames:
		return []
	fullNames = [str(n) for n in fullNames]
	if len(fullNames) != 1 and not any(sep not in n for n in fullNames):
		prefixes = [
			n.rsplit(sep, maxsplit=1)[0] + sep
			for n in fullNames
		]
		commonPrefix = _longestCommonPrefix(prefixes)
		if commonPrefix and not commonPrefix.endswith(sep):
			commonPrefix = commonPrefix.rsplit(sep, maxsplit=1)[0] + sep
		if commonPrefix:
			prefixLen = len(commonPrefix)
			return [
				n[prefixLen:]
				for n in fullNames
			]
	return fullNames

def _longestCommonPrefix(strs):
	if not strs:
		return []
	for i, letter_group in enumerate(zip(*strs)):
		if len(set(letter_group)) > 1:
			return strs[0][:i]
	else:
		return min(strs)
