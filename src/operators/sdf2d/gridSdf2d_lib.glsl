// GridX6 by Del
// https://www.shadertoy.com/view/7dX3Dj

// All 6 Grid functions return the same:
// ret.x  - distance to border
// ret.y  - distance to center
// ret.zw - cell uv
// id - cell coordinates

// nice hex function from - https://www.shadertoy.com/view/lldfWH
vec4 gr_HexGrid(vec2 uv, out vec2 id)
{
    uv *= mat2(1.1547,0.0,-0.5773503,1.0);
    vec2 f = fract(uv);
    float triid = 1.0;
	if((f.x+f.y) > 1.0)
    {
        f = 1.0 - f;
     	triid = -1.0;
    }
    vec2 co = step(f.yx,f) * step(1.0-f.x-f.y,max(f.x,f.y));
    id = floor(uv) + (triid < 0.0 ? 1.0 - co : co);
    co = (f - co) * triid * mat2(0.866026,0.0,0.5,1.0);    
    uv = abs(co);
    id*=inverse(mat2(1.1547,0.0,-0.5773503,1.0)); // optional unskew IDs
    return vec4(0.5-max(uv.y,abs(dot(vec2(0.866026,0.5),uv))),length(co),co);
}

// Triangle grid using the skewed, split rectangle method (quicker)
// this version based on fabrices excellent hexagonal tiling tutorial (I wish I'd found this earlier!!)
// https://www.shadertoy.com/view/4dKXR3
vec4 gr_TriGrid(vec2 uv, out vec2 id)
{
    uv *= mat2(1,-1./1.73, 0,2./1.73);
    vec3 g = vec3(uv,1.-uv.x-uv.y);
    vec3 _id = floor(g)+0.5;
    g = fract(g);
    float lg = length(g);
    if (lg>1.)
        g = 1.-g;
    vec3 g2 = abs(2.*fract(g)-1.);                  // distance to borders
    vec2 triuv = (g.xy-ceil(1.-g.z)/3.) * mat2(1,.5, 0,1.73/2.);
    float edge = max(max(g2.x,g2.y),g2.z);
    id = _id.xy;
    id*= mat2(1,.5, 0,1.73/2.); // Optional, unskew IDs
    id.xy += sign(lg-1.)*0.1; // Optional tastefully adjust ID's
    return vec4((1.0-edge)*0.43,length(triuv),triuv);
}

// simple square grid equiv
vec4 gr_SquareGrid(vec2 uv, out vec2 id)
{
    uv += 0.5;
    vec2 fs =  fract(uv)-0.5;
    id = floor(uv);
    vec2 d = abs(fs)-0.5;
    float edge = length(max(d,0.0)) + min(max(d.x,d.y),0.0);
    return vec4(abs(edge),length(fs),fs.xy);
}

// simple diamond grid equiv
vec4 gr_DiamondGrid(vec2 uv, out vec2 id)
{
    uv = uv* mat2(1,-1,1,1);
    return(gr_SquareGrid(uv,id));
}

// simple brick grid equiv
vec4 gr_BrickGrid(vec2 uv, out vec2 id)
{
    vec2 pos = uv * vec2(1.0,2.0);
    if(fract(uv.y)>0.5)
        pos.x += 0.5;
    id = floor(pos);
    id.y *= 0.5;
    pos = fract(pos);
    vec2 uv2 = fract (pos)-0.5;
    uv2.y *= 0.5;
    pos=abs(fract (pos + 0.5) - 0.5);
    float d = min(pos.x,pos.y*0.5);
    return vec4(abs(d),length(uv2),uv2);
}

// Shanes octagonal-diamond grid equiv - https://www.shadertoy.com/view/3tGBWV
vec4 gr_OctagonalGrid(vec2 uv, out vec2 id)
{
    vec2 guv;
    vec2 p = uv - .5;
    id = floor(p) + .5;
    p -= id;
    float d = abs(p.x) + abs(p.y) - (1. - sqrt(2.)/2.);
    if(d<.0)
    {
        // inside a diamond
        guv = fract(p-0.5)-0.5;
        id += .5;
    }
    else
    {
        // inside an octagon
        guv = fract(p)-0.5;
        p = uv;
        id = floor(p) + .5;
        p -= id;
        d = max((abs(p.x) + abs(p.y))/sqrt(2.), max(abs(p.x), abs(p.y))) - .5;
    }
    return vec4(abs(d), length(guv), guv);
}