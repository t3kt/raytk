#if defined(THIS_EXPOSE_res1f) || defined(THIS_EXPOSE_res1v)
inputOp1_ReturnT res1 = inputOp1(p, ctx);

#ifdef THIS_EXPOSE_res1f
THIS_res1f = adaptAsFloat(res1);
#endif

#ifdef THIS_EXPOSE_res1v
THIS_res1v = fillToVec4(res1);
#endif

#endif
