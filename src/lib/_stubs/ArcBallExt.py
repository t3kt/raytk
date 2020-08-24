class ArcBallExt():
	"""
	The ArcBallExt Class helps with interactively controlling a Camera COMP
	given a Container COMP with the Mouse UV Buttons Parameters for left, 
	middle and right enabled.

	Attributes
	----------
		ownerComp : OP
			Reference to the COMP this Class is initiated by.

	Methods
	-------
		StartTransform(btn=None, u=0, v=0)
			Will begin a transform depending on the mouse button pressed.
		Transform(btn=None, u=0, v=0, scaler=1)
			Applies a transform to the ArcBall depending on the mouse button pressed.
		Reset()
			Resets the ArcBall.
		LoadTransform(dat=None,matrix=None)
			Given a tableDAT or a tdu.Matrix() it can be used to recall a saved transformation.
		SaveTransform(dat=op('newMat'))
			Will save out the current ArcBall's transformation matrix to a tableDAT. If no
			TableDAT is given, the internal newMat TableDAT is being used.
		fillMat()
			Utility function used by the ArcBall.
	"""
	def __init__(self, ownerComp : OP):
		#The component to which this extension is attached
		self.ownerComp = ownerComp
		self.arcInst = tdu.ArcBall(forCamera=True)
		self.matrix = tdu.Matrix()

		# initialize ArcBall to saved out transformation matrix
		matrixDAT = op('newMat')
		for i in range(4):
			for j in range(4):
				self.matrix[i,j] = float(matrixDAT[i,j])

		matCopy = tdu.Matrix(self.matrix)
		self.arcInst.setTransform(matCopy)

	def StartTransform(self, btn : str = None, u : float = 0, v : float = 0) -> None:
		"""

		Parameters
		----------
			btn : str
				The mouse btn pressed. Can be one of 'lselect', 'rselect' or 'mselect' corrseponding to 'rotate', 'pan' and 'zoom'.
			u : float
				The horizontal mouse position on the control panel.
			v : float
				The vertical mouse position on the control panel.
		"""

		if btn == 'lselect':
			#if lselect ==> rotate
			self.arcInst.beginRotate(u,v)
		elif btn == 'rselect':
			#if rselect ==> pan
			self.arcInst.beginPan(u,v)
		elif btn == 'mselect':
			#if mselect ==> zoom
			self.arcInst.beginDolly(u,v)

		return
		
	def Transform(self, btn : str = None, u : float = 0, v : float = 0, scaler : float = 1) -> None:
		"""

		Parameters
		----------
			btn : str
				The mouse btn pressed. Can be one of 'lselect', 'rselect' or 'mselect' corrseponding to 'rotate', 'pan' and 'zoom'.
			u : float
				The horizontal mouse position on the control panel.
			v : float
				The vertical mouse position on the control panel.
			scaler : float
				A multiplier to increase or decrease the transformation.
		"""

		if btn == 'lselect':
			#if lselect ==> rotate
			self.arcInst.rotateTo(u,v,scale=scaler)
		elif btn == 'rselect':
			#if rselect ==> pan
			self.arcInst.panTo(u,v,scale=scaler)
		elif btn == 'mselect':
			#if mselect ==> zoom
			self.arcInst.dollyTo(u,v,scale=scaler)

		self.fillMat()
		return
		
	def Reset(self) -> None:
		op('autoRotate/hold1').par.pulse.pulse()
		op('autoRotate/hold2').par.pulse.pulse()
		op('autoRotate/hold3').par.pulse.pulse()
		self.arcInst.identity()
		self.fillMat()
		return
	
	def LoadTransform(self, dat : tableDAT = None, matrix : tdu.Matrix = None) -> None:
		"""
		Parameters
		----------
			dat : tableDAT
				An tableDAT operator reference to the tableDAT that holds the matrix to be loaded.
			matrix : tdu.MAtrix
				A tdu.Matrix object that holds the matrix to be loaded.
		"""

		if dat and dat.numRows == 4 and dat.numCols == 4:
			matrix = tdu.Matrix()
			for i in range(4):
				for j in range(4):
					matrix[i,j] = float(dat[i,j])

		self.arcInst.setTransform(matrix)
		self.fillMat()
		return

	def SaveTransform(self, dat : tableDAT = op('newMat')) -> None:
		"""
		Parameters
		----------
			dat : tableDAT
				A tableDAT operator reference to the tableDAT where to write the current transform matrix into. 
		"""

		if dat.OPType == 'tableDAT':
			self.matrix.fillTable(dat)

	def fillMat(self):
		newMat = self.arcInst.transform()
		self.matrix = newMat
		self.ownerComp.cook(force=True)
		newMat.fillTable(op('newMat'))
		return