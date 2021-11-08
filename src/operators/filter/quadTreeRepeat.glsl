// vec2 to vec2 hash.
vec2 THIS_hash22(vec2 p){
	// Faster, but doesn't disperse things quite as nicely.
	return fract(vec2(262144, 32768)*sin(dot(p, vec2(THIS_Seed, 27))));
}

// https://www.shadertoy.com/view/llcBD7
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	vec2 q = p;

	// Distance file values.
//	vec4 d = vec4(1e5);

	// Initial cell dimension.
	float dim = 1.;

	// Random entries -- One for each layer. The X values represent the chance that
	// a tile for that particular layer will be rendered. For instance, the large
	// tile will have a 35% chance, the middle tiles, 70%, and the remaining smaller
	// tiles will have a 100% chance. I.e., they'll fill in the rest of the squares.
	float rndTiles[3] = float[3](
		THIS_Chance1,
		THIS_Chance2,
		1.
	);

	float div = THIS_Division;

	for(int k=0; k<3; k++) {

		vec2 ip = floor(q*dim);

		vec2 rnd = THIS_hash22(ip);
		if(rnd.x<rndTiles[k]) {

			// Local cell coordinate.
			vec2 locP = q - (ip + .5)/dim; // Equivalent to: mod(oP, 1./dim) - .5/dim;

			// Reusing "rnd" to calculate a new random number. Not absolutely necessary,
			// but I wanted to mix things up a bit more.
			rnd = fract(rnd*27.63 + float(k*THIS_Seed + 1));

			// Using a unique random cell ID to create an offset.
//			vec2 off = (rnd - .5)*.33/dim;

			// An offset disk... or disc, as some people spell it. :)
			// If rendering outside the loop, you'd have to take an overall minimum, and keep
			// some copies, etc.
			// I.e.: d.x = min(d.x, (length(p - off) - .44/1.4/dim));
			//
//			d.x = length(locP - off) - .3/dim;

			// Grid lines.
//			const float lwg = .015;
//			d.y = abs(max(abs(locP.x), abs(locP.y)) - .5/dim) - lwg/2.;

			#ifdef THIS_Iterationtype_cell
			setIterationCell(ctx, vec3(rnd, float(k) / 3.));
			#endif

			CoordT pForIn = locP * dim * div;
			res = inputOp1(pForIn, ctx);
			#ifdef inputOp1_RETURN_TYPE_Sdf
			res = withAdjustedScale(res, 1./dim/div);
			#endif
			return res;
		}

		// Subdividing. I.e., decrease the cell size by doubling the frequency.
		dim *= div;

	}
	initDefVal(res);
	return res;
}