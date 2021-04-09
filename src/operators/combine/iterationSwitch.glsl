ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT result;

	#if THIS_INPUT_COUNT == 1
	result = THIS_INPUT_1(p, ctx);
	#else
	{
		vec4 ival = extractIteration(ctx);
		float i = ival.THIS_Iterationpart;
		#if defined(THIS_Extend_clamp)
		i = clamp(i, 0., THIS_INPUT_COUNT - 1);
		#elif defined(THIS_Extend_loop)
		i = mod(i, THIS_INPUT_COUNT);
		#elif defined(THIS_Extend_zigzag)
		i = modZigZag(i / float(THIS_INPUT_COUNT - 1)) * float(THIS_INPUT_COUNT - 1);
		#else
		#error invalidExtend
		#endif
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