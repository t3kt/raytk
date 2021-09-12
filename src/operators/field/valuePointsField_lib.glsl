int findMin(vec2 vals, out float minVal) {
	if (vals.x < vals.y) {
		minVal = vals.x;
		return 0;
	} else {
		minVal = vals.y;
		return 1;
	}
}

int findMin(vec3 vals, out float minVal) {
	int i = findMin(vals.xy, minVal);
	if (minVal < vals.z) {
		return i;
	} else {
		minVal = vals.z;
		return 2;
	}
}

int findMin(vec4 vals, out float minVal) {
	int i = findMin(vals.xyz, minVal);
	if (minVal < vals.w) {
		return i;
	} else {
		minVal = vals.w;
		return 3;
	}
}
