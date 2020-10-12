from dataclasses import dataclass, field
import re
from typing import Dict, List

@dataclass
class ROPInputSpec:
	name: str = None
	inputDAT: str = None
	returnTypes: List[str] = field(default_factory=list)
	coordTypes: List[str] = field(default_factory=list)
	contextTypes: List[str] = field(default_factory=list)

	@classmethod
	def fromJsDict(cls, obj: dict):
		return cls(
			returnTypes=obj['returnTypes'].split(' ') if obj['returnTypes'] else [],
			coordTypes=obj['coordTypes'].split(' ') if obj['coordTypes'] else [],
			contextTypes=obj['contextTypes'].split(' ') if obj['contextTypes'] else [],
		)

	def toJsDict(self):
		return cleanDict({
			'name': self.name,
			'inputDAT': self.inputDAT,
			'returnTypes': ' '.join(self.returnTypes),
			'coordTypes': ' '.join(self.coordTypes),
			'contextTypes': ' '.join(self.contextTypes),
		})

	@classmethod
	def parseFromText(cls, text: str):
		obj = _parseTextObject(text)
		return cls(
			name=_getSingleString(obj.get('input')),
			inputDAT=_getSingleString(obj.get('inputDAT')),
			returnTypes=obj.get('return') or [],
			coordTypes=obj.get('coord') or [],
			contextTypes=obj.get('context') or [],
		)

def _getSingleString(vals: List[str]):
	if not vals:
		return None
	if len(vals) > 1:
		return ' '.join(vals)
	return vals[0]

def _parseTextObject(text: str) -> Dict[str, List[str]]:
	obj = {}
	for line in text.splitlines():
		line = line.strip()
		if not line.startswith('@'):
			continue
		parts = re.split(r'\W+', line[1:])
		key = parts[0]
		vals = parts[1:]
		if not vals:
			continue
		if key not in obj:
			obj[key] = []
		obj[key] += vals
	return obj

def cleanDict(d):
	if not d:
		return None
	return {
		key: val
		for key, val in d.items()
		if not (val is None or (isinstance(val, (str, list, dict, tuple)) and len(val) == 0))
	}

def mergeDicts(*parts):
	x = {}
	for part in parts:
		if part:
			x.update(part)
	return x
