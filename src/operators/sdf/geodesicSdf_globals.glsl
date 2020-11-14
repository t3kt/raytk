#ifndef GEODESIC_GLOBALS
#define GEODESIC_GLOBALS
vec3 GEODESIC_nc,GEODESIC_pab,GEODESIC_pbc,GEODESIC_pca;
void GEODESIC_init() {//setup folding planes and vertex
	const int Type=5;
    float cospin=cos(PI/float(Type)), scospin=sqrt(0.75-cospin*cospin);
	GEODESIC_nc=vec3(-0.5,-cospin,scospin);//3rd folding plane. The two others are xz and yz planes
	GEODESIC_pab=vec3(0.,0.,1.);
	GEODESIC_pbc=vec3(scospin,0.,0.5);//No normalization in order to have 'barycentric' coordinates work evenly
	GEODESIC_pca=vec3(0.,scospin,cospin);
	GEODESIC_pbc=normalize(GEODESIC_pbc);	GEODESIC_pca=normalize(GEODESIC_pca);//for slightly better DE. In reality it's not necesary to apply normalization :)
}
#endif
