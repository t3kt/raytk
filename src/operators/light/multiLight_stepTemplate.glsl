#ifdef THIS_HAS_INPUT_$
if ((i+1) == $ && THIS_Enable$ > 0.5) {
  #ifdef THIS_HAS_INPUT_bounds$
    if (adaptAsFloat(inputOp_bounds$(p, ctx)) > 0.) {
      return res;
    }
  #endif
  res = inputOp$(p, ctx);
  res.absent = false;
  res.color *= THIS_Level$;
  return res;
}
#endif