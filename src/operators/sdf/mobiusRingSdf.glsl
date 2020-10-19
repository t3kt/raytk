ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdMobiusRing(p - THIS_Translate, THIS_Radius, THIS_Thickness, THIS_Rounding, THIS_Twist, THIS_Twistphase));
}