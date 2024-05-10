ReturnT thismap(CoordT p, ContextT ctx) {
	float totalWeight = THIS_Defaultlevel;
	ReturnT totalValue = THIS_asReturnT(THIS_Defaultvalue) * totalWeight;
	AGGREGATE_BODY();
	ReturnT res = totalValue;
	COMBINE_BODY();
	return res;
}