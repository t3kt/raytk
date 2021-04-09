ReturnT thismap(CoordT p, ContextT ctx) {
	return vec4(cosPalette(p, THIS_Color1, THIS_Color2, THIS_Color3, THIS_Color4), 1.0);
}