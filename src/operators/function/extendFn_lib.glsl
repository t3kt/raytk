// There are definitely much more efficient ways to do this..

bool allInRange(float val, float low, float high) {
	return val >= low && val <= high;
}

bool allInRange(vec2 val, vec2 low, vec2 high) {
	return val.x >= low.x && val.x <= high.x &&
	val.y >= low.y && val.y <= high.y;
}

bool allInRange(vec3 val, vec3 low, vec3 high) {
	return val.x >= low.x && val.x <= high.x &&
	val.y >= low.y && val.y <= high.y &&
	val.z >= low.z && val.z <= high.z;
}

bool allInRange(vec4 val, vec4 low, vec4 high) {
	return val.x >= low.x && val.x <= high.x &&
	val.y >= low.y && val.y <= high.y &&
	val.z >= low.z && val.z <= high.z &&
	val.w >= low.w && val.w <= high.w;
}
