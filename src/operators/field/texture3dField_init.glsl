{
	TDTexInfo info = THIS_texture_info;
	#ifdef THIS_EXPOSE_res
	THIS_res = info.res.zw;
	#endif
	#ifdef THIS_EXPOSE_aspect
	THIS_aspect = info.res.z / info.res.w;
	#endif
	#ifdef THIS_EXPOSE_depth
	THIS_depth = info.depth.y;
	#endif
	#ifdef THIS_EXPOSE_firstslice
	THIS_firstslice = info.depth.x * 0.5 + info.depth.z;
	#endif
}