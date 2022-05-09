if (THIS_Enable$ > 0.5) {
  THIS_exposeIndex($);
  #ifdef THIS_Enabletranslate
  p1 = p - THIS_asCoordT(THIS_Translate$);
  #endif
  THIS_merge(res1, inputOp$(p1, ctx), r, n, o);
}
