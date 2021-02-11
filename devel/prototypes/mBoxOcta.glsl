// @Iterations {"style":"Int", "normMin": 2, "normMax": 100, "default": 11}
// @Coloriterations {"style":"Int", "normMin": 2, "normMax":  100, "default": 8}
// @Coloringtype {"style":"Int", "normMin": 0, "normMax":  4, "default": 0}
// @Colorscale {"style":"Float", "normMin": 0.0, "normMax":  2.0, "default": 1.0}
// @Coloroffset {"style":"Float", "normMin": -8.0, "normMax":  8.0, "default": 0}
// @Scale {"style":"Float", "normMin": -3, "normMax":  3, "default": 2}
// @Fatness {"style":"Float", "normMin": 0, "normMax":  5, "default": 0}
// @Fold {"style":"XYZ", "normMin": -5, "normMax":  5, "default": 0.0}
// @Julia {"style":"XYZ", "normMin": -5, "normMax":  5, "default": -1}
// @Rotate {"style":"XYZ", "normMin": -360, "normMax":  360, "default": 0}
// @Rotminmax {"style":"XY", "normMin": 0, "normMax":  60, "default": 4}
// @Minrad2 {"style":"Float", "normMin": 0, "normMax":  2, "default": 0.25}
// @Octajulia {"style":"XYZ", "normMin": -5, "normMax":  5, "default": 0}
// @Octafold {"style":"XYZ", "normMin": -5, "normMax":  5, "default": 0}
// @Boxiter {"style":"Int", "normMin": 1, "normMax":  9, "default": 1}
// @Ifsiter {"style":"Int", "normMin": 1, "normMax":  9, "default": 1}
// @Ifold {"style":"XYZ", "normMin": -5, "normMax":  5, "default": 0}
// @Ifolditer {"style":"XY", "normMin": 0, "normMax":  30, "default": 0}

ReturnT thismap(CoordT p, Context ctx) {
	vec4 scale = vec4(vec3(THIS_Scale), abs(THIS_Scale)) / THIS_Minrad2;
	float absScalem1 = abs(THIS_Scale - 1.0);
	float absScaleRaisedTo1mIters = pow(abs(THIS_Scale), float(1-THIS_Iterations));
	float r;
	int n;
	mat3 rot;
	rot = rotateMatrix(radians(THIS_Rotate));

	vec4 mp = vec4(p,1.0);
	vec4 mp0 = vec4(THIS_Julia,1.0);
	n = 0;

	int iterations = int(THIS_Iterations);
	int coloringType = int(THIS_Coloringtype);
	int colorIterations = int(THIS_Coloriterations);
	vec3 fold = THIS_Fold;
	int ifsIter = int(THIS_Ifsiter);
	int boxIter = int(THIS_Boxiter);
	vec3 octaJulia = THIS_Octajulia;
	vec3 octaFold = THIS_Octafold;
	float colorOffset = THIS_Coloroffset;
	vec2 iFoldIter = THIS_Ifolditer;
	vec3 iFold = THIS_Ifold;
	vec2 rotMinMax = THIS_Rotminmax;

	float l=0;
	float prevl=0;

	vec4 orbitTrap = vec4(100);

	while (n < iterations)
	{
		prevl=l;

		if (mod(n,boxIter)==0.0)
		{
			mp.xyz=abs(mp.xyz)+fold;
			float r2 = dot(mp.xyz, mp.xyz);
			if (n< colorIterations && coloringType == 0) orbitTrap = min(orbitTrap, abs(vec4(mp.xyz,r2)));
			mp *= clamp(max(THIS_Minrad2/r2, THIS_Minrad2), 0.0, 1.0);  // dp3,div,max.sat,mul
			mp = mp*scale + mp0;
			//mp.xyz *= rot;
		}

		if (mod(n,ifsIter)==0.0)
		{
			//octahedron
			//if (mp.x+mp.y<0.0) mp.xy = -mp.yx;
			//if (mp.x+mp.z<0.0) mp.xz = -mp.zx;
			//if (mp.x-mp.y<0.0) mp.xy = mp.yx;
			//if (mp.x-mp.z<0.0) mp.xz = mp.zx;
			//menger
			if (mp.x<mp.y) mp.xy = mp.yx;
			if (mp.x<mp.z) mp.xz = mp.zx;
			if (mp.y<mp.z) mp.yz = mp.zy;
			//dodecahedron
			//mp.xyz-= 2.0 * min(0.0, dot(mp.xyz, vec3(-0.5, 0.309017, 0.809017))) * vec3(-0.5, 0.309017, 0.809017);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.309017, 0.809017, -0.5))) * vec3(0.309017, 0.809017, -0.5);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.809017, -0.5, 0.309017))) * vec3(0.809017, -0.5, 0.309017);
			//mp.xyz-= 2.0 * min(0.0, dot(mp.xyz, vec3(-0.5, 0.309017, 0.809017))) * vec3(-0.5, 0.309017, 0.809017);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.309017, 0.809017, -0.5))) * vec3(0.309017, 0.809017, -0.5);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.809017, -0.5, 0.309017))) * vec3(0.809017, -0.5, 0.309017);
			//mp.xyz-= 2.0 * min(0.0, dot(mp.xyz, vec3(-0.5, 0.309017, 0.809017))) * vec3(-0.5, 0.309017, 0.809017);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.309017, 0.809017, -0.5))) * vec3(0.309017, 0.809017, -0.5);
			//mp.xyz-=	2.0 * min(0.0, dot(mp.xyz, vec3(0.809017, -0.5, 0.309017))) * vec3(0.809017, -0.5, 0.309017);

			if (n >= iFoldIter.x && n <= iFoldIter.y) mp.xyz -= iFold;
			mp.xyz -= octaJulia;
			mp.xyz = abs(mp.xyz+octaFold)-octaFold;
			if (n >= rotMinMax.x && n <= rotMinMax.y) mp.xyz *= rot;

			l = length(mp.xyz);
			if (n<colorIterations)
			{
				if (coloringType==2) orbitTrap+=exp(-1/abs(l-prevl+THIS_Coloroffset));
				if (coloringType==3) orbitTrap+=abs(l-prevl+THIS_Coloroffset);
				if (coloringType==1) orbitTrap = min(orbitTrap, abs(vec4(mp.xyz,0)));
			}
		}

		n++;

	}

	if (coloringType==3) orbitTrap/=colorIterations;
	//orbitTrap*=ColorScale;
	orbitTrap = orbitTrap * THIS_Colorscale + THIS_Coloroffset;

	float d = ((length(mp.xyz) - absScalem1) / mp.w - absScaleRaisedTo1mIters)-(THIS_Fatness * 0.01);
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orbitTrap;
	#endif
	return res;
}