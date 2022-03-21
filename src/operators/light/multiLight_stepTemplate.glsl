#ifdef THIS_HAS_INPUT_$
if ((i+1) == $ && THIS_Enable$ > 0.5) {
  res = inputOp$(p, ctx);
  res.absent = false;
  res.color *= THIS_Level$;
  return res;
}
#endif