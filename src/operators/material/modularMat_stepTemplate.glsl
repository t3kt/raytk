#ifdef THIS_HAS_INPUT_shading$
if (false) {}
#if !defined(inputOp_shading$_HAS_TAG_uselight) && !defined(inputOp_shading$_HAS_TAG_useshadow)
else if (light.absent && lightIndex > 0) {}
#endif
else {
	col += fillToVec3(inputOp_shading$(p, matCtx));
}
#endif