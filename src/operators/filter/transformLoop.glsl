ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Iterations);
	#pragma r:if THIS_EXPOSE_index
	THIS_index = 0;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normindex
	THIS_normindex = 0;
	#pragma r:endif

	vec4 q = adaptAsVec4(p);
	for (int i = 0; i < n; i++) {
		#pragma r:if THIS_EXPOSE_index
		THIS_index = i;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normindex
		THIS_normindex = float(i) / float(n - 1);
		#pragma r:endif

		BODY();
	}


	return inputOp1(THIS_asCoordT(q), ctx);
}