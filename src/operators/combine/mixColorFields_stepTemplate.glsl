float level$ = float(THIS_Enable$) * THIS_Level$;
if (level$ != 0.0) {
	vec4 v = fillToVec4(inputOp$(p, ctx));
  totalValue += v.rgb * THIS_Color$ * level$;
	totalWeight += level$;
}
