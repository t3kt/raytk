ReturnT THIS_getColor(int i) {
	if (i < 0) return THIS_Color1;
	switch (i) {
		case 0: return THIS_Color1;
		case 1: return THIS_Color2;
		case 2: return THIS_Color3;
		case 3: return THIS_Color4;
		case 4: return THIS_Color5;
		case 5: return THIS_Color6;
		case 6: return THIS_Color7;
		case 7: return THIS_Color8;
	}
	return THIS_Color8;
}

float THIS_applyExtend(float i, float n) {
	EXTEND();
	return i;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float n = THIS_Count;
	ReturnT res;
	float i = inputOp_indexField(p, ctx);
	if (THIS_Blendindices > 0.) {
		i += THIS_Offset;
		i = THIS_applyExtend(i, n);
		int iA = int(floor(i));
		int iB = int(ceil(i));
		ReturnT colA = THIS_getColor(iA);
		ReturnT colB = THIS_getColor(iB);
		res = mix(colA, colB, i - float(iA));
	} else {
		i += round(THIS_Offset);
		i = THIS_applyExtend(i, n);
		int index = int(floor(i));
		res = THIS_getColor(index);
	}
	return res;
}