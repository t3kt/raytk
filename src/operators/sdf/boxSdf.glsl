ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_Scale * THIS_Uniformscale;
	#ifdef THIS_HAS_INPUT_scaleField
	scale *= fillToVec3(inputOp_scaleField(p, ctx));
	#endif
	p -= THIS_Translate;
	Sdf res;
	int infAxis = int(THIS_Infiniteaxis);
	if (infAxis == 0) {
		res = createSdf(fBox(p, scale));
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
		vec3 uv = vec3(0.);
		switch (infAxis - 1) {
			case 0:
				q = p.yz;
				s = scale.yz;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.yz = map01(q, -s/2., s/2.);
					uv.x = p.x;
				} else if (THIS_Uvmode == THISTYPE_Uvmode_faces) {
					vec2 pNorm = q / s;
					vec2 edge = nearestEdge(pNorm);
					uv.y = p.x;
					if (edge.x != 0.)  uv.x = pNorm.y * edge.x;
					else uv.x = pNorm.x * edge.y;
				}
			break;
			case 1:
				q = p.zx;
				s = scale.zx;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.zx = map01(q, -s/2., s/2.);
					uv.y = p.y;
				} else if (THIS_Uvmode == THISTYPE_Uvmode_faces) {
					vec2 pNorm = q / s;
					vec2 edge = nearestEdge(pNorm);
					uv.y = p.y;
					if (edge.x != 0.)  uv.x = pNorm.y * edge.x;
					else uv.x = pNorm.x * edge.y;
				}
			break;
			case 2:
				q = p.xy;
				s = scale.xy;
				if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
					uv.xy = map01(q, -s/2., s/2.);
					uv.z = p.z;
				} else if (THIS_Uvmode == THISTYPE_Uvmode_faces) {
					vec2 pNorm = q / s;
					vec2 edge = nearestEdge(pNorm);
					uv.y = p.z;
					if (edge.x != 0.)  uv.x = pNorm.y * edge.x;
					else uv.x = pNorm.x * edge.y;
				}
			break;
		}
		res = createSdf(fBox2(q, s));
		switch (THIS_Uvmode) {
			case THISTYPE_Uvmode_bounds:
			case THISTYPE_Uvmode_faces:
				assignUV(res, uv);
				break;
		}
	}
	return res;
}