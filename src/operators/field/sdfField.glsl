ReturnT thismap(CoordT p, ContextT ctx) {
	float d = adaptAsFloat(inputOp1(p, ctx)) - THIS_Offset;
	#ifndef THIS_Fieldtype_dist
	{
		float t = THIS_Thickness/2.;
		float b = THIS_Blending;
		#if defined(THIS_Fieldtype_inside)
		d = smoothstep(0., b, -d);
		#elif defined(THIS_Fieldtype_outside)
		d = smoothstep(0., b, d);
		#elif defined(THIS_Fieldtype_surface)
		d = 1.0-smoothstep(0., b, abs(d) - t);
		#elif defined(THIS_Fieldtype_surfaceinside)
		d = (1.0 - smoothstep(0., b, abs(d) - t)) * (1.0-step(0., d));
		#elif defined(THIS_Fieldtype_surfaceoutside)
		d = (1.0 - smoothstep(0., b, abs(d) - t)) * (1.0-step(0., -d));
		#else
		#error invalidFieldType
		#endif
	}
	#endif

	return d;
}