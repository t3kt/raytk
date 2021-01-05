ReturnT thismap(CoordT p, ContextT ctx) {
	float t = THIS_Thickness;
	#ifdef THIS_THICK_FIELD
		#if defined(THIS_THICK_COORD_TYPE_float)
			t *= THIS_THICK_FIELD(atan(p.z, p.x) / TAU, ctx);
		#elif defined(THIS_THICK_COORD_TYPE_vec3)
			t *= THIS_THICK_FIELD(p, ctx);
		#else
			#error invalidRadiusCoordType
		#endif
	#endif
	return createSdf(sdMobiusRing(p - THIS_Translate, THIS_Radius, t, THIS_Rounding, THIS_Twist, THIS_Twistphase));
}