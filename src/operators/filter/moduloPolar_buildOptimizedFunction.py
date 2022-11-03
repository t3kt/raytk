from io import StringIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.write(buildCode())

def buildCode():
	out = StringIO()
	p = parent().par
	mirror = p.Mirrortype == 'mirror'
	out.write('''
void THIS_apply(vec2 p, out float cell) {
	''')
	out.write('''
float repetitions = THIS_Repetitions;
float angle = TAU/repetitions;
float a = atan(q.y, q.x) + angle/2.;
float cell = floor(a/angle);
	''')
	if p.Uselimit:
		out.write('''
float start = THIS_Limitlow;
float stop = THIS_Limithigh;
float a2 = mod(a, TAU)/angle;
if (a2 < start) {
	cell = -1.;
	return;
}
if (a2 > stop) {
	cell = repetitions + 1.;
	return;
}
''')
		if mirror:
			out.write('''
	float a1 = mod(a, angle * 2.);
	if (a1 >= angle) {
		a1 = angle - a1;
	}
	q = mod(a1, angle) - angle/2.;
''')
		else:
			out.write('''
	a = mod(a, angle) - angle/2.;
''')
	else:
		if mirror:
			out.write('''''')
		pass

	out.write('''
}
ReturnT thismap(CoordT p, ContextT ctx) {
vec2 pivot = THIS_Pivot;
float r = THIS_Rotate;
pR(q, r);
	''')
	if op('rotate_field_definition').numRows > 1:
		out.write('r += radians(inputOp_rotateField(p, ctx));\n')
	plane = {'x': 'yz', 'y': 'zx', 'z': 'xy'}[p.Axis.eval()]
	out.write(f'vec2 q = p.{plane} - pivot;\n')

	out.write('return res;\n')
	out.write('}\n')
	return out.getvalue()
