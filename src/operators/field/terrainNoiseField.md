Noise that uses fBm (fractal brownian motion), which can work well for surface offsetting for terrain.

Based on [Musgrave's Noises Collection](https://www.shadertoy.com/view/4sXXW2) by xbe.

See also http://www.classes.cs.uchicago.edu/archive/2014/winter/23700-1/project_4_and_5/MusgraveTerrain00.pdf.

## Parameters

* `Noisetype`
  * `fBm`
  * `multifractal`
  * `heteroTerrain`
  * `hybridMultiFractal`
  * `ridgedMultiFractal`
* `Axis`: When the `Noisetype` uses 2D coordinates but `Coordtype` is 3D, this is used to choose which plane of the coordinates are used.
  * `x`
  * `y`
  * `z`
* `Translate`
* `Scale`
* `Increment`
* `Lacunarity`: Gap between successive frequencies.
* `Frequency`: Density of the pattern (basically another Scale).
* `Octaves`: Number of layers of detail (frequencies used in the fBm). Larger values produce more detail. Avoid values below 1.
* `Stepoffset`
* `Gain`
* `Amplitude`: Multiplies the amount produced by the noise.
* `Offset`: Offsets (adds to) the amount produced by the noise.

## Inputs

* `coordField`: 
* `incrementField`: 
* `lacunarityField`: 
* `frequencyField`: 
* `octavesField`: 
* `stepOffsetField`: 
* `gainField`: 