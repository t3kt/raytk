{
	TDTexInfo info = THIS_texture_info;
	#ifdef THIS_EXPOSE_res
	THIS_res = info.res.zw;
	#endif
	#ifdef THIS_EXPOSE_aspect
	THIS_aspect = info.res.z / info.res.w;
	#endif
}