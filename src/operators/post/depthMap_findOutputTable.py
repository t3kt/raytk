def onCook(dat):
	dat.clear()
	dat.appendRow([''])
	o = parent().par.Outputop.eval()
	if not o:
		return
	if o.isDAT:
		dat[0,0] = o.path
		return
	if o.isCOMP:
		info = o.op('renderInfo')
		p = info.par['Outputtable']
		if p and p.eval():
			dat[0,0] = op(p).path
			return
	raise Exception(f'Invalid Output OP: {o}')
