vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
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
	CoordT mp = THIS_asCoordT(getPosForMaterial(adaptAsVec3(p), matCtx));
	#ifdef THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#endif
	#ifdef THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#ifdef RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = matCtx.shadedLevel;
		}
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = matCtx.light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = matCtx.light.pos;
	#endif
	#ifdef THIS_EXPOSE_surfacecolor
	{
		#ifdef RAYTK_USE_SURFACE_COLOR
		THIS_surfacecolor = matCtx.result.color;
		#else
		THIS_surfacecolor = vec4(1., 1., 1., 0.);
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_surfaceuv
	{
		#ifdef RAYTK_USE_UV
		THIS_surfaceuv = matCtx.uv;
		#else
		THIS_surfaceuv = vec4(0.);
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_sdf
		THIS_sdf = matCtx.result;
	#endif
	vec3 col = vec3(0.);
	float d = matCtx.result.x - THIS_Offset;
	if (IS_TRUE(THIS_Enablefill)) {
		vec3 fillColor = THIS_Fillcolor;
		#ifdef THIS_HAS_INPUT_fillColorField
		{
			#if defined(inputOp_fillColorField_COORD_TYPE_float)
			float q = -d;
			#else
			inputOp_fillColorField_CoordT q = inputOp_fillColorField_asCoordT(mp);
			#endif
			fillColor *= fillToVec3(inputOp_fillColorField(q, matCtx));
		}
			#endif
		col += fillColor * (1.0 - smoothstep(0, THIS_Blending, max(d, 0.)));
	}
	if (IS_TRUE(THIS_Enableedge)) {
		vec3 edgeColor = THIS_Edgecolor;
		#ifdef THIS_HAS_INPUT_edgeColorField
		{
			#if defined(inputOp_edgeColorField_COORD_TYPE_float)
			float q = -d;
			#else
			inputOp_edgeColorField_CoordT q = inputOp_edgeColorField_asCoordT(mp);
			#endif
			edgeColor *= fillToVec3(inputOp_edgeColorField(q, matCtx));
		}
		#endif
		col += edgeColor * (1.0 - smoothstep(THIS_Edgethickness - THIS_Blending / 2., THIS_Edgethickness + THIS_Blending/2., abs(d)));
	}
	return col;
}