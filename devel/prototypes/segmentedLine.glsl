// @Count {"default":1, "normMin":0, "normMax":5, "style": "Int"}
// @Radius {"default": 0.1}

ReturnT thismap(CoordT p, Context ctx) {
	float r = THIS_Radius;
	vec3 pt1 = THIS_pos[0].xyz;
	vec3 pt2 = THIS_pos[1].xyz;
	float d = fCapsule(p, pt1, pt2, r);
	int n = int(THIS_Count);
	for (int i = 2; i < n; i++) {
		pt1 = pt2;
		pt2 = THIS_pos[i].xyz;
		d = opSimpleUnion(d, fCapsule(p, pt1, pt2, r));
	}
	return createSdf(d);
}