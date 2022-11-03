ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT result;

	#if THIS_INPUT_COUNT == 1
	result = THIS_INPUT_1(p, ctx);
	#else
	{
		vec4 ival = extractIteration(ctx);
		float i;
		switch (THIS_Iterationpart) {
			case THISTYPE_Iterationpart_x: i = ival.x; break;
			case THISTYPE_Iterationpart_y: i = ival.y; break;
			case THISTYPE_Iterationpart_z: i = ival.z; break;
			case THISTYPE_Iterationpart_w: i = ival.w; break;
		}
		switch (THIS_Extend) {
			case THISTYPE_Extend_clamp:
				i = clamp(i, 0., THIS_INPUT_COUNT - 1);
				break;
			case THISTYPE_Extend_loop:
				i = mod(i, THIS_INPUT_COUNT);
				break;
			case THISTYPE_Extend_zigzag:
				i = modZigZag(i / float(THIS_INPUT_COUNT - 1)) * float(THIS_INPUT_COUNT - 1);
				break;
		}
		int index = int(round(i));

		switch (index) {
			#if THIS_INPUT_COUNT >= 2
			case 1:
				result = THIS_INPUT_2(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT >= 3
			case 2:
				result = THIS_INPUT_3(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT >= 4
			case 3:
				result = THIS_INPUT_4(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT >= 5
				case 4:
				result = THIS_INPUT_5(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT >= 6
				case 5:
				result = THIS_INPUT_6(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT >= 7
				case 6:
				result = THIS_INPUT_7(p, ctx);
				break;
			#endif
			#if THIS_INPUT_COUNT == 8
				case 7:
				result = THIS_INPUT_8(p, ctx);
				break;
			#endif
			default:
				result = THIS_INPUT_1(p, ctx);
				break;
		}

		return result;
	}
	#endif
}