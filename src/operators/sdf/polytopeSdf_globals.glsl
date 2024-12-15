vec4 THIS_nc;
vec4 THIS_nd;
vec4 THIS_p;

void THIS_init() {
	float T = 0.01;

	int type = int(THIS_Type);
	float cospin=cos(PI/float(type)), isinpin=1./sin(PI/float(type));
	float scospin=sqrt(2./3.-cospin*cospin), issinpin=1./sqrt(3.-4.*cospin*cospin);
	THIS_nc=0.5*vec4(0,-1,sqrt(3.),0.);
	THIS_nd=vec4(-cospin,-0.5,-0.5/sqrt(3.),scospin);

	vec4 pabc,pbdc,pcda,pdba;
	pabc=vec4(0.,0.,0.,1.);
	pbdc=0.5*sqrt(3.)*vec4(scospin,0.,0.,cospin);
	pcda=isinpin*vec4(0.,0.5*sqrt(3.)*scospin,0.5*scospin,1./sqrt(3.));
	pdba=issinpin*vec4(0.,0.,2.*scospin,1./sqrt(3.));

	THIS_p=normalize(THIS_U*pabc+THIS_V*pbdc+THIS_W*pcda+T*pdba);
}
