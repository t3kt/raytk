// Based on Klems code https://www.shadertoy.com/view/XljSWm

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	int n = int(THIS_Steps);
	float scale = THIS_Scale;
	float dist = 0.0;
	for (int i = 0; i < n; i++) {
		#pragma r:if THIS_EXPOSE_step
		THIS_step = i;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_crossScaleField
		float crossScale = inputOp_crossScaleField(p, ctx);
		#pragma r:else
		float crossScale = THIS_Crossscale;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_boxScaleField
		float boxScale = inputOp_boxScaleField(p, ctx);
		#pragma r:else
		float boxScale = THIS_Boxscale;
		#pragma r:endif
		dist = max(dist, mengerCrossDist(p, crossScale, boxScale)*scale);
		p = fract((p-1.0)*0.5) * 6.0 - 3.0;
		scale /= 3.0;
		#pragma r:if THIS_HAS_INPUT_stepOffsetField
		p -= fillToVec3(inputOp_stepOffsetField(p, ctx));
		#pragma r:else
		p -= THIS_Stepoffset;
		#pragma r:endif
	}
	return createSdf(dist);
}