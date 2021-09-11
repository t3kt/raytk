ReturnT thismap(CoordT p, ContextT ctx) {
	p = mod(p, THIS_Spacing) - THIS_Spacing/2.;
	int s1 = int(THIS_Shape);
	int s2 = int(mod(THIS_Shape + 1., 7.));
	float d1 = lattice_shape(p, s1, THIS_Blendradius);
	float d2 = lattice_shape(p, s2, THIS_Blendradius);
	float u = smoothstep(0.0,1.0,pow(fract(THIS_Shape),3.0));
	float d = mix(d1, d2, u);
	return createSdf(d - THIS_Thickness);
}