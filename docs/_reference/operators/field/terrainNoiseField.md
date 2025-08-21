---
layout: operator
title: terrainNoiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/terrainNoiseField
redirect_from:
  - /reference/opType/raytk.operators.field.terrainNoiseField/
op:
  category: field
  detail: 'Based on [Musgrave''s Noises Collection](https://www.shadertoy.com/view/4sXXW2)
    by xbe.


    See also http://www.classes.cs.uchicago.edu/archive/2014/winter/23700-1/project_4_and_5/MusgraveTerrain00.pdf.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Fractal Increment Field
    name: incrementField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Lacunarity Field
    name: lacunarityField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Frequency Field
    name: frequencyField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Octaves Field
    name: octavesField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Step Offset Field
    name: stepOffsetField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Gain Field
    name: gainField
    returnTypes:
    - float
    - vec4
  keywords:
  - fbm
  - landscape
  name: terrainNoiseField
  opType: raytk.operators.field.terrainNoiseField
  parameters:
  - label: Noise Type
    menuOptions:
    - label: fBm
      name: fBm
    - label: Multi Fractal
      name: multifractal
    - label: Heterogeneous Terrain
      name: heteroTerrain
    - label: Hybrid Multi Fractal
      name: hybridMultiFractal
    - label: Ridged Multi Fractal
      name: ridgedMultiFractal
    name: Noisetype
    readOnlyHandling: baked
    regularHandling: baked
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: When the `Noisetype` uses 2D coordinates but `Coordtype` is 3D, this
      is used to choose which plane of the coordinates are used.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Fractal Increment
    name: Increment
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Lacunarity
    name: Lacunarity
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Gap between successive frequencies.
  - label: Frequency
    name: Frequency
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Density of the pattern (basically another Scale).
  - label: Octaves
    name: Octaves
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of layers of detail (frequencies used in the fBm). Larger values
      produce more detail. Avoid values below 1.
  - label: Step Offset
    name: Stepoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Gain
    name: Gain
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Amplitude
    name: Amplitude
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Multiplies the amount produced by the noise.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets (adds to) the amount produced by the noise.
  summary: Noise that uses fBm (fractal brownian motion), which can work well for
    surface offsetting for terrain.
  thumb: assets/images/reference/operators/field/terrainNoiseField_thumb.png

---


Noise that uses fBm (fractal brownian motion), which can work well for surface offsetting for terrain.

Based on [Musgrave's Noises Collection](https://www.shadertoy.com/view/4sXXW2) by xbe.

See also http://www.classes.cs.uchicago.edu/archive/2014/winter/23700-1/project_4_and_5/MusgraveTerrain00.pdf.