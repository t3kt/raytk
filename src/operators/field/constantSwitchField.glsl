ReturnT THIS_getValue(int i) {
	if (i < 0) return THIS_asReturnT(THIS_Value1);
	switch (i) {
		case 0: return THIS_asReturnT(THIS_Value1);
		case 1: return THIS_asReturnT(THIS_Value2);
		case 2: return THIS_asReturnT(THIS_Value3);
		case 3: return THIS_asReturnT(THIS_Value4);
		case 4: return THIS_asReturnT(THIS_Value5);
		case 5: return THIS_asReturnT(THIS_Value6);
		case 6: return THIS_asReturnT(THIS_Value7);
		case 7: return THIS_asReturnT(THIS_Value8);
	}
	return THIS_asReturnT(THIS_Value8);
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
		ReturnT valA = THIS_getValue(iA);
		ReturnT valB = THIS_getValue(iB);
		res = mix(valA, valB, i - float(iA));
	} else {
		i += round(THIS_Offset);
		i = THIS_applyExtend(i, n);
		int index = int(floor(i));
		res = THIS_getValue(index);
	}
	return res;
}