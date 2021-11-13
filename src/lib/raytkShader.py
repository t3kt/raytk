import re
from dataclasses import dataclass
from typing import List, Set, Iterable, Union

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

class CodeFilter:
	@staticmethod
	def processCodeBlock(code: str) -> str:
		return code

	@classmethod
	def macroizer(cls):
		return _CodeMacroizerFilter()

	@classmethod
	def reducer(cls, macros: 'Iterable[str]'):
		return _CodeReducerFilter(macros)

_filterLinePattern = re.compile(r'^\s*#pragma r:(if|elif|else|endif)([ \t]+(.+))?$', re.MULTILINE)

class _CodeMacroizerFilter(CodeFilter):
	def processCodeBlock(self, code: str) -> str:
		if not code:
			return ''
		return _filterLinePattern.sub(self._replacement, code)

	@staticmethod
	def _replacement(m: 're.Match'):
		command = m.group(1)
		condition = _ReducerCondition.parse(m.group(3))
		if command == 'if':
			return f'#if {condition.asExpr()}'
		elif command == 'elif':
			return f'#elif {condition.asExpr()}'
		elif command == 'else':
			return '#else'
		elif command == 'endif':
			return '#endif'
		else:
			return m.group()

class _CodeReducerFilter(CodeFilter):
	def __init__(self, macros: 'Iterable[str]'):
		self.macros = set(macros or [])  # type: Set[str]

	def processCodeBlock(self, code: str) -> str:
		if not code:
			return ''
		if not self.macros:
			return code
		lines = []
		state = _ReducerState()
		for line in code.splitlines():
			cleaned = line.lstrip()
			if cleaned.startswith('#pragma r:'):
				cleaned = cleaned[10:]
				parts = cleaned.split(' ', maxsplit=1)
				command = parts[0]
				conditionExpr = parts[1] if len(parts) > 1 else None
				condition = _ReducerCondition.parse(conditionExpr)
				if command == 'endif':
					if condition:
						raise AssertionError(f'Invalid endif: {line}')
					state.handleEndif()
					continue
				elif command == 'if':
					if not condition:
						raise AssertionError(f'Missing condition: {line}')
					state.handleIf(condition.eval(self.macros))
					continue
				elif command == 'elif':
					if not condition:
						raise AssertionError(f'Missing condition: {line}')
					state.handleElif(condition.eval(self.macros))
					continue
				elif command == 'else':
					if condition:
						raise AssertionError('Invalid else')
					state.handleElse()
					continue
				else:
					raise AssertionError(f'Invalid pragma: {line}')
			if state.matching:
				lines.append(line)
		if state.hasOpenBlock():
			raise AssertionError('Unmatched if block, missing endif')
		return '\n'.join(lines)

class _ReducerCondition:
	def eval(self, macros: 'Set[str]') -> bool: pass
	def asExpr(self) -> str: pass

	@classmethod
	def parse(cls, expr: str):
		expr = expr.strip() if expr else None
		if not expr:
			return None

		posSyms = set()
		negSyms = set()
		isOr = False
		isAnd = False

		for token in expr.split():
			if token == '||':
				if isAnd:
					raise AssertionError(f'Invalid expression (multiple operators): {expr!r}')
				isOr = True
			elif token == '&&':
				if isOr:
					raise AssertionError(f'Invalid expression (multiple operators): {expr!r}')
				isAnd = True
			else:
				neg = token.startswith('!')
				if neg:
					token = token[1:]
				# if not re.fullmatch(r'\w+', token):
				# 	raise AssertionError(f'Invalid expression (bad token): {expr!r}')
				# else:
				if neg:
					negSyms.add(token)
				else:
					posSyms.add(token)
		if not posSyms and not negSyms:
			if isOr or isAnd:
				raise AssertionError(f'Invalid expression (operator but no symbols): {expr!r}')
			return None
		if isOr:
			return _ReducerConditionOr(posSyms, negSyms)
		elif isAnd:
			return _ReducerConditionAnd(posSyms, negSyms)
		else:
			if (len(posSyms) + len(negSyms)) > 1:
				raise AssertionError(f'Invalid expression (missing operator): {expr!r}')
			else:
				if posSyms:
					return _ReducerConditionSingle(posSyms.pop(), neg=False)
				else:
					return _ReducerConditionSingle(negSyms.pop(), neg=True)

class _ReducerConditionOr(_ReducerCondition):
	def __init__(self, posSyms: 'Set[str]', negSyms: 'Set[str]'):
		self.posSyms = posSyms
		self.negSyms = negSyms

	def eval(self, macros: 'Set[str]') -> bool:
		if self.posSyms and _anyIn(self.posSyms, macros):
			return True
		if self.negSyms and not _allIn(self.negSyms, macros):
			return True
		return False

	def asExpr(self) -> str:
		return ' || '.join([f'defined({s})' for s in self.posSyms] + [f'!defined({s})' for s in self.negSyms])

class _ReducerConditionAnd(_ReducerCondition):
	def __init__(self, posSyms: 'Set[str]', negSyms: 'Set[str]'):
		self.posSyms = posSyms
		self.negSyms = negSyms

	def eval(self, macros: 'Set[str]') -> bool:
		if self.posSyms and not _allIn(self.posSyms, macros):
			return False
		if self.negSyms and _anyIn(self.posSyms, macros):
			return False
		return True

	def asExpr(self) -> str:
		return ' && '.join([f'defined({s})' for s in self.posSyms] + [f'!defined({s})' for s in self.negSyms])

class _ReducerConditionSingle(_ReducerCondition):
	def __init__(self, sym: str, neg: bool):
		self.sym = sym
		self.neg = neg

	def eval(self, macros: 'Set[str]') -> bool:
		if self.neg:
			return self.sym not in macros
		else:
			return self.sym in macros

	def asExpr(self) -> str:
		if self.neg:
			return f'!defined({self.sym})'
		else:
			return f'defined({self.sym})'

def _anyIn(s1: 'Set[str]', s2: 'Set[str]'):
	return s1.intersection(s2)
def _allIn(s1: 'Set[str]', s2: 'Set[str]'):
	return s1.issubset(s2)

@dataclass
class _ReducerFrame:
	nowMatching: bool
	hasMatched: bool = False

class _ReducerState:
	def __init__(self):
		self._stack = []  # type: List[_ReducerFrame]
		self.matching = True

	def handleIf(self, matching: bool):
		self._stack.append(_ReducerFrame(nowMatching=matching, hasMatched=matching))
		self._updateState()

	def handleElif(self, matching: bool):
		if not self._stack:
			raise AssertionError('Invalid elif without if')
		frame = self._stack[-1]
		if matching:
			if not frame.hasMatched:
				frame.nowMatching = True
				frame.hasMatched = True
		else:
			frame.nowMatching = False
		self._updateState()

	def handleElse(self):
		if not self._stack:
			raise AssertionError('Invalid else without if')
		frame = self._stack[-1]
		if frame.hasMatched:
			frame.nowMatching = False
		else:
			frame.nowMatching = True
			frame.hasMatched = True
		self._updateState()

	def handleEndif(self):
		if not self._stack:
			raise AssertionError('Invalid endif without if')
		self._stack.pop()
		self._updateState()

	def _updateState(self):
		if not self._stack:
			self.matching = True
		else:
			self.matching = all(f.nowMatching for f in self._stack)

	def hasOpenBlock(self):
		return bool(self._stack)
