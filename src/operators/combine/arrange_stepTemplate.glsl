if (THIS_Enable$ > 0.5) {
  THIS_exposeIndex($);
  #ifdef THIS_Enabletranslate
  p1 = p - THIS_asCoordT(THIS_Translate$);
  #endif
  res2 = inputOp$(p1, ctx);
  if (initialized) {
    THIS_merge(res1, res2, r, n, o);
  } else {
    res1 = res2;
    initialized = true;
  }
}
