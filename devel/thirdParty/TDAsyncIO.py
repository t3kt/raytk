"""
TDAsyncIO - Utilities for asyncio library with TouchDesigner

Copyright (C) 2021 Motoki Sonoda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

import asyncio
# from TDStoreTools import StorageManager
# TDF = op.TDModules.mod.TDFunctions
import sys

class TDAsyncIO:
	"""
	TDAsyncIO description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# Get the current event loop.
		self.loop = asyncio.get_event_loop()
		
		# If the current event loop was closed, then create a new event loop.
		if self.loop.is_closed():
			self.loop = asyncio.new_event_loop()
			asyncio.set_event_loop(self.loop)

	def __del__(self):
		# Check this component is global OP or not.
		if me.parent() == op.TDAsyncIO:
			# Close the event loop. The loop must not be running.
			# Pending callbacks will be lost.
			self.loop.close()
	
	def Run(self, coroutines):
		for coroutine in coroutines:
			self.loop.create_task(coroutine)
	
	def Update(self):
		self.loop.call_soon(self.loop.stop)
		self.loop.run_forever()

	def Cancel(self):
		if sys.version_info[0] >= 3 and sys.version_info[1] >=7:
			for task in asyncio.all_tasks(self.loop):
				task.cancel()
		else:
			for task in asyncio.Task.all_tasks(self.loop):
				task.cancel()
