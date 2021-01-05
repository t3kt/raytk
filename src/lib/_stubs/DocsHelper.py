"""
Generic docs help button and pulse par system
"""

class DocsHelper:
	"""
	DocsHelper description
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		if not ownerComp.par.Palettename and ownerComp.par.Palettecomp.eval() != op.TDResources:
			ownerComp.par.Palettename = ownerComp.par.Palettecomp.eval().name

	@property
	def HelpCommand(self):
		if self.ownerComp.par.Mode.eval() == 'Palette':
			return "ui.viewFile('https://docs.derivative.ca/" \
					+ ('Experimental:' if self.ownerComp.par.Experimental
					   												else '') \
					+ "Palette:" + self.ownerComp.par.Palettename \
					+ ("#" + self.ownerComp.par.Section.eval()
					   		if self.ownerComp.par.Section.eval() else '') \
					+ "')"
		elif self.ownerComp.par.Mode.eval() == 'Wiki':
			return "ui.viewFile('https://docs.derivative.ca/" \
					+ ('Experimental:' if self.ownerComp.par.Experimental
					   												else '') \
					+ self.ownerComp.par.Wikipage \
					+ ("#" + self.ownerComp.par.Section.eval()
					   		if self.ownerComp.par.Section.eval() else '') \
					+ "')"
		elif self.ownerComp.par.Mode.eval() == 'URL':
			return "ui.viewFile('" + self.ownerComp.par.Url.eval() + "')"

	def OpenDocs(self):
		exec(self.ownerComp.par.Helpcommand.eval())

	def onParValueChange(self, par, prev):
		pass

	def onParPulse(self, par):
		if par.name in ['Createhelppar', 'Createversionpar']:
			helpComp = self.ownerComp.par.Palettecomp.eval()
			if helpComp is None:
				raise Exception('Invalid Palette COMP ('
								+ par.name + ' ' + self.ownerComp.path +')')
			if par.name == 'Createhelppar':
				newPar = 'Help'
			elif par.name == 'Createversionpar':
				newPar = 'Version'
			if not helpComp.pars(newPar):
				pages = helpComp.customPages
				if not pages:
					helpPage = \
						helpComp.appendCustomPage('Help')
					lowOrder = 0
				else:
					helpPage = pages[0]
					if helpPage.pars:
						lowOrder = helpPage.pars[0].order
					else:
						lowOrder = 0
				if par.name == 'Createhelppar':
					helpPage.appendPulse('Help')
					helpComp.par.Help.order = lowOrder - 2
				elif par.name == 'Createversionpar':
					try:
						if helpPage.pars[0].name == 'Help':
							helpPage.pars[0].order = lowOrder - 1
							lowOrder += 1
					except:
						pass
					helpPage.appendStr('Version')
					helpComp.par.Version.order = lowOrder - 1
					helpComp.par.Version = '0.1.0'
					helpComp.par.Version.readOnly = True
		elif par.name == 'Resetpalettecompname':
			self.ownerComp.par.Palettename = \
									self.ownerComp.par.Palettecomp.eval().name
		elif par.name == 'Testopenhelp':
			self.OpenDocs()

	def onParValueChange(self, par, prev):
		helpComp = self.ownerComp.par.Palettecomp.eval()
		if par.name == 'Mode':
			if par.eval() == 'Palette':
				parList = ['Palettename', 'Experimental', 'Section',
						   'Resetpalettecompname']
			elif par.eval() == 'Wiki':
				parList = ['Wikipage', 'Experimental', 'Section']
			else: # URL
				parList = ['Url']
			for p in ['Palettename', 'Experimental', 'Section',
					  'Resetpalettecompname', 'Wikipage', 'Experimental',
					  'Section', 'Url']:
				getattr(self.ownerComp.par, p).enable = p in parList