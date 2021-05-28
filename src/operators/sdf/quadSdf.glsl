ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	Sdf res;
	#if defined(THIS_Plane_xy) || defined(THIS_Plane_yz) || defined(THIS_Plane_zx)
	{
		vec3 size = vec3(THIS_Thickness);
		size.THIS_Plane = THIS_Size;
		float d = fBox(p, size);
		res = createSdf(d);
		#ifdef RAYTK_USE_UV
		vec3 bound = vec3(THIS_Size/2, THIS_Thickness);
		assignUV(res,
			map01(
				vec3(p.THIS_Plane, p.THIS_Axis),
				-bound, bound));
		#endif
	}
	#elif defined(THIS_Plane_custom)
	// https://www.shadertoy.com/view/Md2BWW
	{
		vec3 v1 = THIS_Point1;
		vec3 v2 = THIS_Point2;
		vec3 v3 = THIS_Point3;
		vec3 v4 = THIS_Point4;
		#if 1
		// handle ill formed quads
		if( dot( cross( v2-v1, v4-v1 ), cross( v4-v3, v2-v3 )) < 0.0 )
		{
			vec3 tmp = v3;
			v3 = v4;
			v4 = tmp;
		}
			#endif


		vec3 v21 = v2 - v1; vec3 p1 = p - v1;
		vec3 v32 = v3 - v2; vec3 p2 = p - v2;
		vec3 v43 = v4 - v3; vec3 p3 = p - v3;
		vec3 v14 = v1 - v4; vec3 p4 = p - v4;
		vec3 nor = cross( v21, v14 );

		float d = sqrt( (sign(dot(cross(v21,nor),p1)) +
		sign(dot(cross(v32,nor),p2)) +
		sign(dot(cross(v43,nor),p3)) +
		sign(dot(cross(v14,nor),p4))<3.0)
		?
		min( min( dot2(v21*clamp(dot(v21,p1)/dot2(v21),0.0,1.0)-p1),
		dot2(v32*clamp(dot(v32,p2)/dot2(v32),0.0,1.0)-p2) ),
		min( dot2(v43*clamp(dot(v43,p3)/dot2(v43),0.0,1.0)-p3),
		dot2(v14*clamp(dot(v14,p4)/dot2(v14),0.0,1.0)-p4) ))
		:
		dot(nor,p1)*dot(nor,p1)/dot2(nor) );
		res = createSdf(d - THIS_Thickness);

		// TODO: UV SUPPORT!
	}
	#else
	#error invalidPlane
	#endif
	return res;
}