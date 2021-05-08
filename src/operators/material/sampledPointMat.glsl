vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	vec3 col = vec3(0.);
	#ifdef THIS_Enablefill
	{
		vec3 fillColor = THIS_Fillcolor;
		#ifdef THIS_HAS_INPUT_2
		{
			#if defined(inputOp2_COORD_TYPE_float)
			float q = -matCtx.result.x;
			#else
			inputOp2_CoordT q = inputOp2_asCoordT(mp);
			#endif
			fillColor *= fillToVec3(inputOp2(q, matCtx));
		}
			#endif
		col += fillColor * (1.0 - smoothstep(0, THIS_Blending, max(matCtx.result.x, 0.)));
	}
	#endif
	#ifdef THIS_Enableedge
	{
		vec3 edgeColor = THIS_Edgecolor;
		#ifdef THIS_HAS_INPUT_3
		{
			#if defined(inputOp3_COORD_TYPE_float)
			float q = -matCtx.result.x;
			#else
			inputOp3_CoordT q = inputOp3_asCoordT(mp);
			#endif
			edgeColor *= fillToVec3(inputOp3(q, matCtx));
		}
		#endif
		col += edgeColor * (1.0 - smoothstep(THIS_Edgethickness - THIS_Blending / 2., THIS_Edgethickness + THIS_Blending/2., abs(matCtx.result.x)));
	}
	#endif
	return col;
}