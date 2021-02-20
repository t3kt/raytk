# This really shouldn't be necessary but for some reason the connection
# change doesn't trigger the switch DAT to cook automatically.

def onWireChange(changeOp):
	op('default_camera_switch').cook(force=True)
	