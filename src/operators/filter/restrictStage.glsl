bool THIS_check() {
	#if !defined(THIS_Includeprimary) || !defined(THIS_Includeshadow) || !defined(THIS_Includereflect) || !defined(THIS_Includematerial) || !defined(THIS_Includeocclusion)
	int s = getStage();
	return false ||
	#ifdef THIS_Includeprimary
	(s == RAYTK_STAGE_PRIMARY) ||
	#endif
	#ifdef THIS_Includeshadow
	(s == RAYTK_STAGE_SHADOW) ||
	#endif
	#ifdef THIS_Includereflect
	(s == RAYTK_STAGE_REFLECT) ||
	#endif
	#ifdef THIS_Includematerial
	(s == RAYTK_STAGE_MATERIAL) ||
	#endif
	#ifdef THIS_Includeocclusion
	(s == RAYTK_STAGE_OCCLUSION) ||
	#endif
	false
	;
	#else
	return true;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (THIS_check()) {
		res = inputOp1(p, ctx);
	} else {
		#ifdef THIS_HAS_INPUT_2
		res = inputOp2(p, ctx);
		#else
		initDefVal(res);
		#endif
	}
	return res;
}