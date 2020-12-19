Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(sdTetrahedron((p - THIS_Translate) / THIS_Scale) * THIS_Scale);
}