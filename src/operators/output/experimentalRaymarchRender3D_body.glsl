Sdf map(vec3 p) {
	Context ctx = createDefaultContext();
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = q;
	#endif
	Sdf res = thismap(q, ctx);
	res.x *= THIS_Distfactor;
	return res;
}

void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	pushStage(RAYTK_STAGE_PRIMARY);

	#if THIS_Antialias > 1
	vec2 shiftStart = vec2(-float(THIS_Antialias) / 2.0);
	vec2 shiftStep = vec2(1.0 / float(THIS_Antialias));
	for (int j=0; j < THIS_Antialias; j++)
	for (int i=0; i < THIS_Antialias; i++)
	{
		vec2 shift = shiftStart + shiftStep * vec2(i, j);
		bool isMainPass = j == 0 && i == 0;
	#else
		vec2 shift = vec2(0);
		bool isMainPass = true;
	#endif
		float renderDepth = IS_TRUE(THIS_Userenderdepth) ?
			min(texture(sTD2DInputs[0], vUV.st).r, RAYTK_MAX_DIST) :
			RAYTK_MAX_DIST;

		// Camera
		Ray ray = getViewRay(shift);
		#ifdef OUTPUT_RAYDIR
		rayDirOut += vec4(ray.dir, 0);
		#endif
		#ifdef OUTPUT_RAYORIGIN
		rayOriginOut += vec4(ray.pos, 0);
		#endif

		// Raymarch
		Sdf res = castRay(ray, renderDepth);
		#ifdef OUTPUT_DEPTH
		depthOut += vec4(vec3(min(res.x, renderDepth)), 1);
		#endif

		// Render
		if (res.x >= renderDepth && renderDepth == RAYTK_MAX_DIST) {
			// If result exceeded render depth and we aren't using a depth input..
			// TODO: background / non-hit stuff
		} else if (res.x > 0.0 && res.x < renderDepth) {
			// If result was a hit and didn't exceed render depth...
			MaterialContext matCtx = createMaterialContext();
			vec3 p = ray.pos + ray.dir * res.x;
			#ifdef OUTPUT_WORLDPOS
			worldPosOut += vec4(p, 1);
			#endif
			#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			matCtx.globalPos = p;
			#endif

			// TODO: SDF output

			// Calculate normal if it's needed
			#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL) || (defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection))
			matCtx.normal = calcNormal(p);
			#endif
			#ifdef OUTPUT_NORMAL
			normalOut += vec4(matCtx.normal, 0);
			#endif
		}


	#if THIS_Antialias > 1
	}
	#endif
}
