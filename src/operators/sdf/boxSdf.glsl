ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_Scale * THIS_Uniformscale;
	#ifdef THIS_HAS_INPUT_scaleField
	scale *= fillToVec3(inputOp_scaleField(p, ctx));
	#endif
	p -= THIS_Translate;
	Sdf res;
	int infAxis = int(THIS_Infiniteaxis);
	if (infAxis == 0) {
		res = createSdf(THIS_BOX_FUNC_3D(p, scale));
		switch (int(THIS_Uvmode)) {
			case THISTYPE_Uvmode_bounds:
				assignUV(res, map01(p, -scale/2., scale/2.));
				break;
			case THISTYPE_Uvmode_faces:
				vec3 pNorm = p / scale;
				vec3 boxFaces = nearestFace(pNorm);
				if (boxFaces.x != 0.) {
					assignUV(res, vec3(pNorm.y * boxFaces.x, pNorm.z, 0.));
				} else if(boxFaces.y != 0.) {
					assignUV(res, vec3(pNorm.z * boxFaces.y, pNorm.x, 0.));
				} else if (boxFaces.z != 0.) {
					assignUV(res, vec3(pNorm.x * boxFaces.z, pNorm.y, 0.));
				}
				break;
		}
	} else {
		vec2 q;
		vec2 s;
		vec3 uv;
		switch (infAxis - 1) {
			case 0:
				q = p.yz;
				s = scale.yz;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.yz = map01(q, -s/2., s/2.);
					uv.x = p.x;
				}
			break;
			case 1:
				q = p.zx;
				s = scale.zx;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.zx = map01(q, -s/2., s/2.);
					uv.y = p.y;
				}
			break;
			case 2:
				q = p.xy;
				s = scale.xy;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.xy = map01(q, -s/2., s/2.);
					uv.z = p.z;
				}
			break;
		}
		res = createSdf(THIS_BOX_FUNC_2D(q, s));
		if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
			assignUV(res, uv);
		}
	}
	return res;
}