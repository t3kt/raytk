float level$ = float(THIS_Enable$) * THIS_Level$;
if (level$ != 0.0) {
	ReturnT v = inputOp$(p, ctx);
  totalValue += v * level$;
	totalWeight += level$;
}