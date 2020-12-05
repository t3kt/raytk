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

"""TDCodeGen

Helpers for automatically generated Python code. Heavily based on the ast 
Python library
"""

import ast
script = op('script1_callbacks')

def datFunctionInfo(dat):
	"""
	Get info about all the top level functions in a DAT

	Args:
		dat: the dat to analyze

	Returns:
		{'functionName': {'docString': docString, 'lines': line range}, ...}
	"""
	ast = datAst(dat)
	functions = nodeFunctions(ast)
	return {functionName: 
					{'docString': nodeDocString(node), 
					'lines': nodeLines(node)}
				for functionName, node in functions.items()}

def datRemoveFunction(dat, functionName):
	"""
	Remove a function from a dat

	Args:
		dat: the DAT
		functionName: name of function to remove
	"""
	info = datFunctionInfo(dat)
	if functionName in info:
		functionInfo = info[functionName]
		lines = functionInfo['lines']
		lines[0] -= 1 # 1 based
		lines[1] -= 1 # 1 based
		datLines = dat.text.splitlines()
		# remove a blank line if surrounded on both sides
		if len(datLines) > lines[1] and not datLines[lines[0] - 1].strip() \
									and not datLines[lines[1]].strip():
			lines[1] += 1
		newLines = datLines[:lines[0]] + datLines[lines[1]:]
		dat.text = '\n'.join(newLines)

def datInsertText(dat, text, insertLine=None):
	"""
	Insert text into a dat. 

	Args:
		dat: the DAT
		text: the text to be inserted. 
		insertLine: the line at which to insert text. If None (default), insert
			text after last non-pblank line in file.
	"""
	insertLines = text.splitlines()
	datLines = dat.text.splitlines()
	if insertLine is None:
		insertLine = len(datLines)
		while not datLines[insertLine-1].strip() and insertLine > 1:
			insertLine -= 1
	else:
		insertLine -= 1 # 1 based
	newText = datLines[:insertLine] + insertLines + datLines[insertLine:]
	dat.text = '\n'.join(newText)

def datAst(dat):
	"""
	Get the ast node of a DAT holding Python code

	Args:
		dat: the dat to analyze

	Returns:
		ast node of the DAT's text. Will be ast.Module at top
	"""
	return ast.parse(dat.text)

def nodeFunctions(node):
	"""
	Get info about functions at the top level of node

	Args:
		node: the ast node to search

	Returns:
		{<function name>: ast node of function}
	"""
	functionDict = {}
	for item in node.body:
		if isinstance(item, ast.FunctionDef):
			functionDict[item.name] = item
	return functionDict

def nodeDocString(node):
	"""
	Get the docstring of a node

	Args:
		node: ast node

	Returns:
		docstring or none
	"""
	try:
		item = node.body[0]
		if isinstance(item, ast.Expr) and isinstance(item.value, ast.Str):
			return item.value.s
	except:
		return None
		
def nodeLines(node):
	"""
	Get the line number range of a node

	Args:
		node: an ast node

	Returns:
		(start line #, end line # + 1)
	"""
	
	min_lineno = node.lineno
	max_lineno = node.lineno
	for node in ast.walk(node):
		if hasattr(node, "lineno"):
			min_lineno = min(min_lineno, node.lineno)
			max_lineno = max(max_lineno, node.lineno)
	return [min_lineno, max_lineno + 1]