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

	float r1, r2;

	#if !defined(THIS_HAS_INPUT_radiusField)
	r1 = THIS_Rad1 * THIS_Radius;
	r2 = THIS_Rad2 * THIS_Radius;
	#elif defined(inputOp_radiusField_RETURN_TYPE_vec4)
	vec2 rad = inputOp_radiusField(p, ctx).xy;
	r1 = rad.x * THIS_Radius;
	r2 = rad.y * THIS_Radius;
	#elif defined(inputOp_radiusField_RETURN_TYPE_float)
	float rMult = inputOp_radiusField(p, ctx);
	r1 = rMult * THIS_Rad1;
	r2 = rMult * THIS_Rad2;
	#endif

	#ifdef THIS_HAS_INPUT_bulgeField
	float b = -inputOp_bulgeField(p, ctx);
	#else
	float b = -THIS_Bulge;
	#endif

	p -= THIS_Translate;

	float d = sdOrientedUnevenDogbone(p, pt1, pt2, r1, r2, b);

	return createSdf(d);
}
