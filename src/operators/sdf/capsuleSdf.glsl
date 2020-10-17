Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(fCapsule(p - THIS_Translate, THIS_Endpoint1, THIS_Endpoint2, THIS_Radius));
}