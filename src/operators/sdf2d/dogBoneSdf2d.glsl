// "DogBone SDF" by Martijn Steinrucken aka BigWings/CountFrolic - 2019
// https://www.shadertoy.com/view/wld3D4

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 pt1;
	vec2 pt2;

	#ifdef THIS_HAS_INPUT_lengthField
	float w = inputOp_lengthField(p, ctx) * 0.5;
	#else
	float w = THIS_Length * 0.5;
	#endif

	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x:
			pt1 = vec2(-w, 0);
			pt2 = vec2(w, 0);
			break;
		case THISTYPE_Axis_y:
			pt1 = vec2(0, -w);
			pt2 = vec2(0, w);
			break;
		case THISTYPE_Axis_custom:
			#ifdef THIS_HAS_INPUT_point1Field
			pt1 = inputOp_point1Field(p, ctx).xy;
			#else
		  pt1 = THIS_Pointa;
			#endif
			#ifdef THIS_HAS_INPUT_point2Field
			pt2 = inputOp_point2Field(p, ctx).xy;
			#else
			pt2 = THIS_Pointb;
			#endif
			break;
	}

	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_bulgeField
	float b = -inputOp_bulgeField(p, ctx);
	#else
	float b = -THIS_Bulge;
	#endif

	p -= THIS_Translate;

	float d = sdOrientedUnevenDogbone(p, pt1, pt2, r, r, b);

	return createSdf(d);
}
