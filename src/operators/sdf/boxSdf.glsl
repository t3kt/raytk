ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_Scale * THIS_Uniformscale;
	#pragma r:if THIS_HAS_INPUT_scaleField
	scale *= fillToVec3(inputOp_scaleField(p, ctx));
	#pragma r:endif
	p -= THIS_Translate;
	Sdf res;
	int infAxis = int(THIS_Infiniteaxis);
	if (infAxis == 0) {
		res = createSdf(THIS_BOX_FUNC_3D(p, scale));
		#pragma r:if THIS_Uvmode_bounds
		assignUV(res, map01(p, -scale/2., scale/2.));
		#pragma r:endif
	} else {
		vec2 q;
		vec2 s;
		vec3 uv;
		switch (infAxis - 1) {
			case 0:
				q = p.yz;
				s = scale.yz;
				#pragma r:if THIS_Uvmode_bounds
				uv.yz = map01(q, -s/2., s/2.);
				uv.x = p.x;
				#pragma r:endif
			break;
			case 1:
				q = p.zx;
				s = scale.zx;
				#pragma r:if THIS_Uvmode_bounds
				uv.zx = map01(q, -s/2., s/2.);
				uv.y = p.y;
				#pragma r:endif
			break;
			case 2:
				q = p.xy;
				s = scale.xy;
				#pragma r:if THIS_Uvmode_bounds
				uv.xy = map01(q, -s/2., s/2.);
				uv.z = p.z;
				#pragma r:endif
			break;
		}
		res = createSdf(THIS_BOX_FUNC_2D(q, s));
		#pragma r:if THIS_Uvmode_bounds
		assignUV(res, uv);
		#pragma r:endif
	}
	return res;
}