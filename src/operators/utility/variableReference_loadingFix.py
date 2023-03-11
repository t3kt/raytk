# https://github.com/t3kt/raytk/issues/1020

def onStart():
	o = op('selCurrentField')
	run(f'op("{o.path}").cook(force=True)', delayFrames=1)
