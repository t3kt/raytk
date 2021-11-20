vec3 THIS_nc;
vec3 THIS_p;
const vec3 THIS_pab=vec3(0.,0.,1.);
vec3 THIS_pbc;
vec3 THIS_pca;

void THIS_init() {
	float cospin=cos(PI/float(THIS_Type)), scospin=sqrt(0.75-cospin*cospin);
	THIS_nc=vec3(-0.5,-cospin,scospin);//3rd folding plane. The two others are xz and yz planes
	//	THIS_pab=vec3(0.,0.,1.);
	THIS_pbc=vec3(scospin,0.,0.5);//No normalization in order to have 'barycentric' coordinates work evenly
	THIS_pca=vec3(0.,scospin,cospin);
	THIS_p=normalize((THIS_U*THIS_pab+THIS_V*THIS_pbc+THIS_W*THIS_pca));//U,V and W are the 'barycentric' coordinates (coted barycentric word because I'm not sure if they are really barycentric... have to check)
	THIS_pbc=normalize(THIS_pbc);	THIS_pca=normalize(THIS_pca);//for slightly better DE. In reality it's not necesary to apply normalization :)
}