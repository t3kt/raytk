Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = createSdf(
		sdMengerSponge(p - THIS_Translate, int(THIS_Steps), THIS_Scale, THIS_Crossscale, THIS_Boxscale));
	return res;
}