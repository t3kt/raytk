// https://www.shadertoy.com/view/4sXXW2
// Musgrave's noise functions for terrain rendering
// https://engineering.purdue.edu/~ebertd/texture/1stEdition/musgrave/musgrave.c
// Originaly published in "Texturing & Modeling: A Procedural Approach"
// by David S. Ebert, F. Kenton Musgrave, Darwyn Peachey, Ken Perlin, Steven Worley


// K.Musgrave Procedural Noises Collections
// Ashima Port
//

/*
 * Procedural fBm evaluated at point.
 *
 * Parameters:
 * H is the fractal increment parameter
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 437. Third Edition. San Francisco: Morgan Kaufmann.
*/
float fBmA(vec2 point, float H, float lacunarity, float frequency, float octaves) {
  float value = 0.0;
  float remainder = 0.0;
  float pwrHL = pow(lacunarity, -H);
  float pwr = 1.0;

  /* inner loop of fractal construction */
  for (int i=0; i<65535; i++) {
    value += snoise(point * frequency) * pwr;
    pwr *= pwrHL;
    point *= lacunarity;

    if (i==int(octaves)-1) break;
  }

  remainder = octaves - floor(octaves);
  if (remainder != 0.0) {
    value += remainder * snoise(point * frequency) * pwr;
  }

  return value;
}

/*
 * Procedural multifractal evaluated at point.
 *
 * Parameters:
 * H determines the fractal dimension of the roughest areas
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 * offset is the zero offset, which determines multifractality
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 440. Third Edition. San Francisco: Morgan Kaufmann.
*/
float multifractalA(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset) {
  float value = 1.0;
  float rmd = 0.0;
  float pwHL = pow(lacunarity, -H);
  float pwr = 1.0;

  /* inner loop of fractal construction */
  for (int i=0; i<65535; i++) {
    value *= pwr * snoise(point*frequency) + offset;
    pwr *= pwHL;
    point *= lacunarity;

    if (i==int(octaves)-1) break;
  }

  rmd = octaves - floor(octaves);
  if (rmd != 0.0) value += (rmd * snoise(point*frequency) * pwr);

  return value;
}

/*
 * Heterogeneous procedural terrain function: stats by altitude method.
 * Evaluated at point; returns value stored in value.
 *
 * Parameters:
 * H determines the fractal dimension of the roughest areas
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 * offset raises the terrain from sea level
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 500. Third Edition. San Francisco: Morgan Kaufmann.
*/
float heteroTerrainA(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset) {
 float value, increment, remainder;
  float pwrHL = pow(lacunarity, -H);
  float pwr = pwrHL; /* starts with i=1 instead of 0 */

  value = offset + snoise(point * frequency);
  point *= lacunarity;

  for (int i=1; i<65535; i++) {
    increment = (snoise(point * frequency) + offset) * pwr * value;
    // frequency *= lacunarity;
    value += increment;
    point *= lacunarity;

    if (i==int(octaves)) break;
  }

  /* take care of remainder in 'octaves'  */
  remainder = mod(octaves, floor(octaves));

  if (remainder != 0.0) {
    increment = (snoise(point * frequency) + offset) * pwr * value;
    value += remainder * increment;
  }

  return value;
}

///////////////////////////////////////////////////////////////////////////////////////////
// K.Musgrave Procedural Noises Collections
// XBE Port
//

/*
 * Procedural fBm evaluated at point.
 *
 * Parameters:
 * H is the fractal increment parameter
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 437. Third Edition. San Francisco: Morgan Kaufmann.
*/
float fBm(vec2 point, float H, float lacunarity, float frequency, float octaves)
{
	float value = 0.0;
	float rmd = 0.0;
	float pwHL = pow(lacunarity, -H);
	float pwr = pwHL;

	for (int i=0; i<65535; i++)
	{
		value += snoise(point * frequency) * pwr;
		point *= lacunarity;
		pwr *= pwHL;
		if (i==int(octaves)-1) break;
	}

	rmd = octaves - floor(octaves);
	if (rmd != 0.0) value += rmd * snoise(point * frequency) * pwr;

	return value;
}

/*
 * Procedural multifractal evaluated at point.
 *
 * Parameters:
 * H determines the fractal dimension of the roughest areas
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 * offset is the zero offset, which determines multifractality
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 440. Third Edition. San Francisco: Morgan Kaufmann.
*/
float multifractal(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset)
{
	float value = 1.0;
	float rmd = 0.0;
	float pwHL = pow(lacunarity, -H);
	float pwr = pwHL;

	for (int i=0; i<65535; i++)
	{
		value *= pwr*snoise(point*frequency) + offset;
		point *= lacunarity;
		pwr *= pwHL;
		if (i==int(octaves)-1) break;
	}

	rmd = octaves - floor(octaves);
	if (rmd != 0.0) value += (rmd * snoise(point*frequency) * pwr);

	return value;
}

/*
 * Heterogeneous procedural terrain function: stats by altitude method.
 * Evaluated at point; returns value stored in value.
 *
 * Parameters:
 * H determines the fractal dimension of the roughest areas
 * lacunarity is the gap between successive frequencies
 * octaves is the number of frequencies in the fBm
 * offset raises the terrain from sea level
 *
 * Ebert, D., F. K. Musgrave, D. Peachey, K. Perlin, and S. Worley. 2003. Texturing and modeling: A procedural approach, 500. Third Edition. San Francisco: Morgan Kaufmann.
*/
float heteroTerrain(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset)
{
	float value = 1.;
	float increment = 0.;
	float rmd = 0.;
	float pwHL = pow(lacunarity, -H);
	float pwr = pwHL;

	value = pwr*(offset + snoise(point * frequency));
	point *= lacunarity;
	pwr *= pwHL;

	for (int i=1; i<65535; i++)
	{
		increment = (snoise(point * frequency) + offset) * pwr * value;
		value += increment;
		point *= lacunarity;
		pwr *= pwHL;
		if (i==int(octaves)) break;
	}

	rmd = mod(octaves, floor(octaves));
	if (rmd != 0.0) value += rmd * ((snoise(point * frequency) + offset) * pwr * value);

	return value;
}

/* Hybrid additive/multiplicative multifractal terrain model.
 *
 * Copyright 1994 F. Kenton Musgrave
 *
 * Some good parameter values to start with:
 *
 *      H:           0.25
 *      offset:      0.7
 */
float hybridMultiFractal(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset)
{
	float value = 1.0;
	float signal = 0.0;
	float rmd = 0.0;
	float pwHL = pow(lacunarity, -H);
	float pwr = pwHL;
	float weight = 0.;

	/* get first octave of function */
	value = pwr*(snoise(point * frequency)+offset);
	weight = value;
	point *= lacunarity;
	pwr *= pwHL;

	/* spectral construction inner loop, where the fractal is built */
	for (int i=1; i<65535; i++)
	{
		weight = weight>1. ? 1. : weight;
		signal = pwr * (snoise(point*frequency) + offset);
		value += weight*signal;
		weight *= signal;
		pwr *= pwHL;
		point *= lacunarity;
		if (i==int(octaves)-1) break;
	}

	/* take care of remainder in ``octaves''  */
	rmd = octaves - floor(octaves);
	if (rmd != 0.0) value += (rmd * snoise(point*frequency) * pwr);

	return value;
}

/* Ridged multifractal terrain model.
 *
 * Copyright 1994 F. Kenton Musgrave
 *
 * Some good parameter values to start with:
 *
 *      H:           1.0
 *      offset:      1.0
 *      gain:        2.0
 */
float ridgedMultiFractal(vec2 point, float H, float lacunarity, float frequency, float octaves, float offset, float gain)
{
	float value = 1.0;
	float signal = 0.0;
	float pwHL = pow(lacunarity, -H);
	float pwr = pwHL;
	float weight = 0.;

	/* get first octave of function */
	signal = snoise(point * frequency);
	signal = offset-abs(signal);
	signal *= signal;
	value = signal * pwr;
	weight = 1.0;
	pwr *= pwHL;

	/* spectral construction inner loop, where the fractal is built */
	for (int i=1; i<65535; i++)
	{
		point *= lacunarity;
		weight = clamp(signal*gain, 0.,1.);
		signal = snoise(point * frequency);
		signal = offset-abs(signal);
		signal *= signal;
		signal *= weight;
		value += signal * pwr;
		pwr *= pwHL;
		if (i==int(octaves)-1) break;
	}

	return value;
}
