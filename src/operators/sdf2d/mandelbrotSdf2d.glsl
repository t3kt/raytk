ReturnT thismap(CoordT p, ContextT ctx) {
	int nIter = int(pow(2, THIS_Iterations));
	float R = 25. * 25.;
	float d = m_distance(nIter, R, p);
	return createSdf(d);
}