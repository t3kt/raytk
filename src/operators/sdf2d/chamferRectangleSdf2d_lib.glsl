// Chamfered Box SDF by TheTurk
// https://www.shadertoy.com/view/ftG3Dw
float sdChamferRect(vec2 position, vec2 halfSize, vec2 chamferRadius) {
   position = abs(position) - halfSize;
   vec2 d1 = vec2(max(position.x + chamferRadius.x, 0.0), position.y);
   vec2 d2 = vec2(position.x, max(position.y + chamferRadius.y, 0.0));
   position.x += chamferRadius.x; 
   vec2 end = vec2(chamferRadius.x, -chamferRadius.y);
   vec2 d3 = position - end * clamp(dot(position, end) / dot(end, end), 0.0, 1.0);
   float s = sign(max(d3.x, d1.y));
   return sqrt(min(min(dot(d1, d1), dot(d2, d2)), dot(d3, d3))) * s;
}